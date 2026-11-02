"""First-track diagnostics: event timing, pitch candidates, section and stereo details."""
from pathlib import Path
import json,csv
import numpy as np
import scipy.signal as ss
from scipy.ndimage import gaussian_filter1d
import soundfile as sf
import librosa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'local/deep-house/first_track_20261102'
END=222
def db(v):return 20*np.log10(np.maximum(np.asarray(v),1e-12))
def load(part,model='sw',sr=11025):
    if part=='original':p=OUT/'track01_original_0_222.wav'
    elif model=='sw':p=ROOT/f'local/deep-house/reference/stems_sw/R01_Lost in the Echoes/R01_Lost in the Echoes_({part})_BS-Roformer-SW.wav'
    else:p=ROOT/f'local/deep-house/reference/stems/htdemucs_6s/R01_Lost in the Echoes/{part}.wav'
    x,s=sf.read(p,frames=44100*END,dtype='float32',always_2d=True)
    return librosa.resample(x.mean(axis=1),orig_sr=s,target_sr=sr)
def main():
    base=json.loads((OUT/'signal_results.json').read_text());sr=11025;hop=256;res={}
    # Time-local pitch, with an energy mask; note names are hypotheses.
    f0s={};valids={}
    for model in ['sw','demucs']:
        x=load('bass',model,sr)
        f0=librosa.yin(x,sr=sr,fmin=30,fmax=250,frame_length=2048,hop_length=hop)
        rms=librosa.feature.rms(y=x,frame_length=2048,hop_length=hop)[0]
        midi=librosa.hz_to_midi(f0);valid=(db(rms)>-42)&(np.abs(midi-np.round(midi))<.35)
        f0s[model]=midi;valids[model]=valid
        counts={librosa.midi_to_note(int(n)):int(np.sum(valid&(np.round(midi)==n))) for n in np.unique(np.round(midi[valid]))}
        res[model+'_bass_yin']={'strongest_notes':dict(sorted(counts.items(),key=lambda x:x[1],reverse=True)[:15]),'frames_total':len(valid),'frames_energy_and_pitch_mask':int(valid.sum()),'params':{'sr':sr,'fmin':30,'fmax':250,'frame_length':2048,'hop':hop,'minimum_rms_dbfs':-42,'nearest_note_tolerance_semitones':.35}}
    same=valids['sw']&valids['demucs'];delta=np.abs(f0s['sw'][same]-f0s['demucs'][same])
    res['bass_cross_model_pitch_diagnostics']={'compared_frames':int(same.sum()),'median_absolute_semitones':float(np.median(delta)),'within_half_semitone_fraction':float(np.mean(delta<.5))}
    # Chroma in 4-beat windows. CQT and pitch-class energy are not chord truth.
    per=base['rhythm']['sw']['period_s'];phase=base['rhythm']['sw']['phase_s']
    x=load('other',sr=sr);C=abs(librosa.cqt(x,sr=sr,hop_length=hop,fmin=librosa.note_to_hz('C2'),n_bins=72))
    chroma=np.stack([C[i::12].sum(axis=0) for i in range(12)])
    times=np.arange(C.shape[1])*hop/sr
    rows=[]
    for t in np.arange(phase,END-4*per,4*per):
        m=(times>=t)&(times<t+4*per);p=chroma[:,m].mean(axis=1);p=p/(p.sum()+1e-12)
        rows.append({'start_s':round(float(t),3),'top_pitch_classes':[{'note':librosa.midi_to_note(int(i)+60,octave=False),'relative_weight':round(float(p[i]),3)} for i in np.argsort(p)[-5:][::-1]]})
    res['other_pitchclass_4beat_candidates']=rows
    # RMS over 0.25-second windows, for approximate entry/exit times.
    timelines={};step=.25
    for p in ['bass','drums','other','vocals']:
        x=load(p,sr=sr);edges=np.arange(0,END+1e-6,step)
        timelines[p]=np.array([float(db(np.sqrt(np.mean(x[int(a*sr):int(b*sr)]**2)))) for a,b in zip(edges[:-1],edges[1:])])
    res['section_markers']={}
    for p in ['bass','drums']:
        active=timelines[p]>({'bass':-32,'drums':-29}[p])
        # Heuristic activity threshold only; report it instead of claiming exact musical boundaries.
        changes=np.where(np.diff(active.astype(int))!=0)[0]+1
        res['section_markers'][p]={'threshold_dbfs':{'bass':-32,'drums':-29}[p],'changes_s':(changes*step).tolist()}
    # Detail diagnostics for kick, backbeat, hats in a stable 32 s window.
    drum=load('drums',sr=22050);fs=22050
    event_data={};beat_grid=np.arange(phase,END,per)
    for label,lo,hi in [('kick',30,160),('backbeat',180,2000),('hat',3000,10000)]:
        filt=ss.sosfiltfilt(ss.butter(4,[lo,hi],btype='bandpass',fs=fs,output='sos'),drum)
        env=np.sqrt(np.maximum(ss.resample_poly(filt*filt,1000,fs),0));env=gaussian_filter1d(env,2)
        idx,_=ss.find_peaks(env,distance=int(per*.25*1000),prominence=np.percentile(env,90)*.20)
        ts=idx/1000
        mask=(ts>=40)&(ts<140);ts=ts[mask];amp=env[idx[mask]]
        if label=='kick':keep=np.abs(((ts-phase+per/2)%per)-per/2)<.09
        elif label=='hat':keep=np.abs(((ts-phase+per/2)%per)-per/2)>per*.25
        else:keep=np.ones(len(ts),dtype=bool)
        ts=ts[keep];amp=amp[keep]
        phase_beats=((ts-phase)/per)%1
        event_data[label]={'event_count_40_140s':len(ts),'phase_quantiles':np.percentile(phase_beats,[10,50,90]).tolist() if len(ts) else [],'events':[{'time_s':round(float(t),3),'beat_phase':round(float(q),3),'strength':round(float(a),6)} for t,q,a in zip(ts,phase_beats,amp)]}
    res['band_event_candidates']=event_data
    # Spatial separation of low-end and pad-like midrange in comparable sections.
    st,s=sf.read(OUT/'track01_original_0_222.wav',dtype='float32',always_2d=True)
    spatial=[]
    for name,lo,hi in [('low',25,160),('mid',160,2000),('high',2000,16000)]:
        z=ss.sosfiltfilt(ss.butter(4,[lo,hi],btype='bandpass',fs=s,output='sos'),st,axis=0)
        for a,b in [(0,18),(40,72),(112,144),(151,156),(168,200),(216,220)]:
            q=z[int(a*s):int(b*s)];m=q.mean(axis=1);side=(q[:,0]-q[:,1])/2
            spatial.append({'band':name,'start_s':a,'end_s':b,'lr_correlation':float(np.corrcoef(q.T)[0,1]),'side_mid_db':float(db(np.sqrt(np.mean(side**2))/max(np.sqrt(np.mean(m*m)),1e-12)))})
    res['spatial_sections']=spatial
    # Pitch/repetition summaries across representative 4-second cells.
    pitch_cells=[]
    tt=np.arange(len(f0s['sw']))*hop/sr
    for a in range(0,END,4):
        mask=valids['sw']&(tt>=a)&(tt<a+4);n=np.round(f0s['sw'][mask]).astype(int)
        top=[{'note':librosa.midi_to_note(int(k)),'frames':int((n==k).sum())} for k in sorted(set(n),key=lambda k:-(n==k).sum())[:4]]
        pitch_cells.append({'start_s':a,'bass_note_candidates':top})
    res['bass_pitch_4s']=pitch_cells
    (OUT/'detail_results.json').write_text(json.dumps(res,indent=2,ensure_ascii=False),encoding='utf-8')
    print('PITCH',json.dumps({k:v for k,v in res.items() if 'yin' in k or 'diagnostics' in k},ensure_ascii=False),flush=True)
    print('MARKERS',json.dumps(res['section_markers']),flush=True)
    fig,ax=plt.subplots(3,1,figsize=(15,11))
    for model,color in [('sw','#265c9f'),('demucs','#e29a21')]:
        mask=valids[model];ax[0].scatter(tt[mask],f0s[model][mask],s=2,alpha=.5,c=color,label=model)
    ax[0].set_xlim(0,222);ax[0].set_ylim(20,64);ax[0].set_ylabel('Bass MIDI pitch candidate');ax[0].legend()
    ax[1].imshow(chroma,aspect='auto',origin='lower',extent=[0,222,0,12],cmap='magma');ax[1].set_yticks(np.arange(12)+.5,[librosa.midi_to_note(i+60,octave=False) for i in range(12)]);ax[1].set_ylabel('Other stem pitch-class energy')
    for p in ['bass','drums','other','vocals']:ax[2].plot(edges[:-1],timelines[p],label=p,lw=.7)
    ax[2].set_ylim(-65,-12);ax[2].set_xlim(0,222);ax[2].legend(ncol=4);ax[2].set_ylabel('0.25 s RMS dBFS');ax[2].set_xlabel('First-track time (s)')
    fig.tight_layout();fig.savefig(OUT/'track01_pitch_sections.png',dpi=150)
    print('DETAIL_COMPLETE',OUT,flush=True)
if __name__=='__main__':main()
