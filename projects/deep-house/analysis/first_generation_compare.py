"""Compare two authorized generated songs with only reference track 01.

Demucs outputs, activity thresholds and pitch estimates are diagnostic evidence,
not listening judgments, true MIDI, or automatic vocal identification.
"""
from pathlib import Path
import argparse
import json
import hashlib
import time
import numpy as np
import soundfile as sf
import scipy.signal as sig
from scipy.ndimage import gaussian_filter1d, binary_closing, binary_opening
from scipy.optimize import minimize
import librosa
import pyloudnorm as pyln
import torch
from demucs.pretrained import get_model
from demucs.apply import apply_model
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
REF = ROOT / 'local/deep-house/first_track_20261102'
OUT = ROOT / 'local/deep-house/generation_R01S001_20261103'
FS = 11025
PARTS = ['bass', 'drums', 'other', 'vocals']


def db(x):
    return 20 * np.log10(np.maximum(x, 1e-12))


def read(path, limit=222):
    with sf.SoundFile(path) as f:
        sr = f.samplerate
        x = f.read(frames=-1 if limit is None else round(sr * limit), dtype='float32', always_2d=True)
    return x, sr


def mono(x, sr):
    return librosa.resample(x.mean(axis=1), orig_sr=sr, target_sr=FS)


def band(x, lo, hi, sr=FS):
    return sig.sosfiltfilt(sig.butter(4, [lo, hi], btype='bandpass', fs=sr, output='sos'), x, axis=0)


def frames_rms(y, step=.25):
    starts = np.arange(0, len(y) / FS, step)
    return np.asarray([np.sqrt(np.mean(y[int(t*FS):min(len(y),int((t+step)*FS))] ** 2)) for t in starts])


def regions(mask, step=.25, minimum=3):
    d = np.diff(np.r_[False, mask, False].astype(int))
    return [{'start_s':float(a*step), 'end_s':float(b*step)}
            for a, b in zip(np.flatnonzero(d == 1),np.flatnonzero(d == -1)) if (b-a)*step >= minimum]


def separate(label, path, model):
    dest = OUT / 'stems' / label
    expected_frames = round(sf.info(path).duration * model.samplerate)
    complete = (dest / 'separation_record.json').exists()
    for part in PARTS:
        try:
            info = sf.info(dest / f'{part}.wav')
            complete = complete and info.samplerate == model.samplerate and info.channels == 2 and abs(info.frames-expected_frames) <= 1
        except (OSError, sf.LibsndfileError):
            complete = False
    if complete:
        print('REUSE_COMPLETED_STEMS',label,flush=True)
        return
    start = time.time()
    x, sr = read(path, limit=None)
    x = librosa.resample(x.T, orig_sr=sr, target_sr=model.samplerate)
    wav = torch.from_numpy(x)
    ref = wav.mean(0)
    mean, std = ref.mean(), ref.std()
    normalized = (wav - mean) / max(float(std), 1e-8)
    torch.manual_seed(0)
    with torch.inference_mode():
        sources = apply_model(model, normalized[None], device='cuda', shifts=0,
                              split=True, overlap=.25, progress=False, num_workers=0)[0]
        sources = sources.cpu() * std + mean
    dest.mkdir(parents=True,exist_ok=True)
    for part in PARTS:
        sf.write(dest / f'{part}.wav', sources[model.sources.index(part)].T.numpy(),
                 model.samplerate, subtype='FLOAT')
    record = {'label':label,'input':str(path),'model':'htdemucs_6s','shifts':0,
              'overlap':.25,'device':'cuda','sample_rate':model.samplerate,
              'seconds':x.shape[-1]/model.samplerate,'elapsed_s':time.time()-start,
              'normalization':'global mono mean/std, inverse applied per output',
              'note':'Analysis aid; not the original instrument tracks; reference used existing htdemucs_6s outputs.'}
    (dest/'separation_record.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    print('SEPARATED',json.dumps(record),flush=True)


def rhythm(drums):
    z = band(drums,30,160)
    e = np.sqrt(np.maximum(gaussian_filter1d(sig.resample_poly(z*z,200,FS),1.2),0))
    ix,_ = sig.find_peaks(e,distance=.25*200,prominence=np.percentile(e,90)*.18)
    t = ix/200
    good = (t>35)&(t<200)&(e[ix]>np.percentile(e[ix],35))
    t = t[good]
    intervals = np.diff(t)
    intervals = intervals[(intervals>.36)&(intervals<.85)]
    hist, edges = np.histogram(intervals,bins=np.arange(.36,.855,.005))
    initial = float((edges[np.argmax(hist)]+edges[np.argmax(hist)+1])/2)
    def loss(v):
        per, phase = v
        residual = ((t-phase+per/2)%per)-per/2
        return float(np.mean(np.minimum(residual**2,.07**2)))
    fits = []
    for ph in np.linspace(0,initial,20,endpoint=False):
        fit = minimize(loss,[initial,ph],method='Nelder-Mead',options={'maxiter':400})
        if abs(fit.x[0]-initial)<.04:
            fits.append((float(fit.fun),float(fit.x[0]),float(fit.x[1]%fit.x[0])))
    _,per,phase=min(fits)
    residual=((t-phase+per/2)%per)-per/2
    windows=[]
    for a in [40,80,112,168]:
        b=min(a+32,len(drums)/FS)
        if b-a<8:
            continue
        y=drums[int(a*FS):int(b*FS)]
        onset=librosa.onset.onset_strength(y=y,sr=FS,hop_length=128)
        tempo=librosa.feature.tempo(onset_envelope=onset,sr=FS,hop_length=128,start_bpm=110,max_tempo=180)
        windows.append({'start_s':a,'end_s':b,'bpm':float(tempo[0])})
    return {'bpm_fit':60/per,'period_s':per,'phase_s':phase,'low_pulse_candidates':len(t),
            'median_absolute_peak_grid_residual_ms':float(np.median(abs(residual))*1000),
            'onset_tempo_windows':windows}


def analyze(label,path):
    stereo,sr=read(path, limit=222 if label=='REF' else None)
    full = mono(stereo,sr)
    if label=='REF':
        folder=ROOT/'local/deep-house/reference/stems/htdemucs_6s/R01_Lost in the Echoes'
    else:
        folder=OUT/'stems'/label
    stems={}
    for part in PARTS:
        x,s=read(folder/f'{part}.wav', limit=222 if label=='REF' else None)
        stems[part]=mono(x,s)
    levels={p:db(frames_rms(y)) for p,y in stems.items()}
    length=min(map(len,levels.values()))
    active=(levels['bass'][:length]>np.percentile(levels['bass'],95)-12)&(levels['drums'][:length]>np.percentile(levels['drums'],95)-12)
    active=binary_opening(binary_closing(active,structure=np.ones(3)),structure=np.ones(5))
    body_regions=regions(active,minimum=8)
    candidates=[r for r in body_regions if r['end_s']-r['start_s']>=32]
    if candidates:
        body_start=min(candidates[0]['start_s']+1,candidates[0]['end_s']-32)
    else:
        pair=levels['bass'][:length]+levels['drums'][:length]
        w=128
        body_start=float(np.argmax(np.convolve(pair,np.ones(w)/w,mode='valid'))*.25)
    body_end=body_start+32
    sl=slice(int(body_start*FS),int(body_end*FS))
    r={'label':label,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'seconds':len(stereo)/sr,'sample_rate':sr,'lufs':float(pyln.Meter(sr).integrated_loudness(stereo)),
       'peak_dbfs':float(db(np.max(abs(stereo)))),'rhythm':rhythm(stems['drums']),
       'paired_stem_activity_regions':body_regions,'selected_body_window_s':[body_start,body_end],
       'activity_method':{'step_s':.25,'threshold_each_stem_db_relative_p95':-12,
                          'closing_cells':3,'opening_cells':5,'min_region_s':8,
                          'note':'Operational joint bass/drum activity; not verified arrangement labels.'}}
    spatial=[]
    for name,lo,hi in [('low',25,160),('mid',160,2000),('high',2000,16000)]:
        z=band(stereo,lo,hi,sr)
        for section,a,b in [('selected_body',body_start,body_end),('intro',0,18),('middle_target',112,144),('break_target',149,167),('return_target',168,200)]:
            b=min(b,len(stereo)/sr)
            if b<=a:
                continue
            q=z[int(a*sr):int(b*sr)]
            mid=q.mean(axis=1);side=(q[:,0]-q[:,1])/2
            spatial.append({'section':section,'band':name,'interval_s':[a,b],
                            'side_mid_db':float(db(np.sqrt(np.mean(side**2))/max(np.sqrt(np.mean(mid**2)),1e-12))),
                            'lr_correlation':float(np.corrcoef(q.T)[0,1])})
    r['spatial']=spatial
    energy={}
    for source in ['master','drums','bass','other','vocals']:
        y=full if source=='master' else stems[source]
        energy[source]={}
        for lo,hi in [(25,160),(160,2000),(2000,6000),(6000,16000)]:
            if hi>=FS/2:continue
            q=band(y,lo,hi)[sl]
            energy[source][f'{lo}_{hi}']=float(db(np.sqrt(np.mean(q*q))))
    # High-band power uses 44.1/48 kHz stereo rather than the 11 kHz analysis signal.
    for source in ['master','drums']:
        x,s=read(path if source=='master' else folder/'drums.wav', limit=222 if label=='REF' else None)
        for lo,hi in [(2000,6000),(6000,16000)]:
            z=band(x,lo,hi,s)[int(body_start*s):int(body_end*s)]
            energy[source][f'{lo}_{hi}']=float(db(np.sqrt(np.mean(z*z))))
    r['body_band_rms_dbfs']=energy
    bass=stems['bass'];hop=256
    f0=librosa.yin(bass,sr=FS,fmin=30,fmax=200,frame_length=2048,hop_length=hop)
    rms=librosa.feature.rms(y=bass,frame_length=2048,hop_length=hop)[0]
    midi=librosa.hz_to_midi(f0);tt=np.arange(len(midi))*hop/FS
    valid=(db(rms)>np.percentile(db(rms),95)-24)&(abs(midi-np.round(midi))<.35)
    r['bass_pitch_candidates']=[]
    for a in np.arange(0,len(bass)/FS,4):
        m=valid&(tt>=a)&(tt<a+4);ns=np.round(midi[m]).astype(int);weights=rms[m]**2
        totals={int(n):float(weights[ns==n].sum()) for n in np.unique(ns)}
        top=sorted(totals,key=lambda n:-totals[n])[:3]
        r['bass_pitch_candidates'].append({'start_s':float(a),'top':[{'midi':n,'note':librosa.midi_to_note(n),'energy_weight':totals[n]/max(sum(totals.values()),1e-12)} for n in top]})
    r['stem_rms_timeline']={p:levels[p].tolist() for p in PARTS}
    r['stem_body_rms_dbfs']={p:float(db(np.sqrt(np.mean(y[sl]**2)))) for p,y in stems.items()}
    # Comparison copies only: no EQ/reverb, identical target loudness, no original overwritten.
    normalized=stereo*10**((-20-r['lufs'])/20)
    peak=float(np.max(abs(normalized)))
    if peak>=1:
        raise RuntimeError('Loudness copy would clip; use a lower shared target.')
    sf.write(OUT/f'{label}_full_minus20LUFS.wav',normalized,sr,subtype='PCM_16')
    clip=stereo[int(body_start*sr):int((body_start+24)*sr)]
    clip_lufs=float(pyln.Meter(sr).integrated_loudness(clip))
    clip=clip*10**((-20-clip_lufs)/20)
    assert np.max(abs(clip))<1
    sf.write(OUT/f'{label}_body24s_minus20LUFS.wav',clip,sr,subtype='PCM_16')
    r['comparison_audio']={'full_target_lufs':-20,'full_gain_db':-20-r['lufs'],
                           'body_clip_interval_s':[body_start,body_start+24],
                           'body_clip_original_lufs':clip_lufs,'body_clip_gain_db':-20-clip_lufs}
    print('ANALYZED',label,json.dumps({k:v for k,v in r.items() if k in ['lufs','selected_body_window_s','rhythm','paired_stem_activity_regions','stem_body_rms_dbfs']}),flush=True)
    return r


def main():
    global OUT
    parser=argparse.ArgumentParser()
    parser.add_argument('--run-dir',type=Path,default=OUT)
    args=parser.parse_args()
    OUT=args.run_dir.resolve()
    torch.set_num_threads(4)
    model=get_model('htdemucs_6s').eval()
    manifest=json.loads((OUT/'execution_record.json').read_text(encoding='utf-8'))
    for row in manifest['outputs']:
        separate(row['label'],Path(row['file']),model)
    del model
    torch.cuda.empty_cache()
    tracks=[('REF',REF/'track01_original_0_222.wav')]+[(r['label'],Path(r['file'])) for r in manifest['outputs']]
    results=[analyze(label,path) for label,path in tracks]
    (OUT/'comparison_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
    fig,axes=plt.subplots(4,1,figsize=(15,12),sharex=True)
    colors={r['label']:color for r,color in zip(results,['black','#246bb2','#d4701e'])}
    for r in results:
        for i,p in enumerate(PARTS):
            y=np.asarray(r['stem_rms_timeline'][p]);axes[i].plot(np.arange(len(y))*.25,y-r['lufs']-20,label=r['label'],color=colors[r['label']],lw=.8)
            axes[i].set(ylim=(-65,-10),ylabel=f'{p} RMS dBFS\nfull track at -20 LUFS')
    for ax in axes:
        ax.legend(ncol=3)
        for a in [39,73,112,149,167,203]:ax.axvline(a,color='gray',alpha=.2)
    axes[-1].set(xlim=(0,max(r['seconds'] for r in results)),xlabel='Track time (s); reference landmarks are gray, not assumed generated section boundaries')
    fig.tight_layout();fig.savefig(OUT/'first_generation_structure.png',dpi=140);plt.close(fig)
    print('FIRST_GENERATION_COMPARISON_COMPLETE',flush=True)


if __name__=='__main__':
    main()
