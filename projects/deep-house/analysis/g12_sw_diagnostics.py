"""Compare contextual G12 SW estimates with only reference track 01.

Numbers describe assigned stems, never verified instrument truth or AI hearing.
"""
from pathlib import Path
import json
import sys

import librosa
import numpy as np
import pyloudnorm as pyln
import scipy.signal as sig
import soundfile as sf

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'local/deep-house'
RUN = BASE/'generation_R01S006_20261103'
OUT = RUN/'sw_review_20261103'
FS = 44100
PARTS = ['bass', 'drums', 'other', 'vocals', 'guitar', 'piano']


def db(x):
    return 20*np.log10(np.maximum(x, 1e-12))


def read(path, a, b):
    with sf.SoundFile(path) as f:
        sr = f.samplerate
        f.seek(round(a*sr))
        x = f.read(round(b*sr)-round(a*sr), dtype='float32', always_2d=True)
    if len(x) != round(b*sr)-round(a*sr):
        raise ValueError(f'Incomplete audio interval: {path}, {a}, {b}')
    if sr != FS:
        x = librosa.resample(x.T, orig_sr=sr, target_sr=FS).T
    return x


def band(x, lo, hi):
    return sig.sosfiltfilt(sig.butter(4,[lo,hi],btype='bandpass',fs=FS,output='sos'),x,axis=0)


def summary(x, gain):
    x = x*gain
    bands = {}
    for lo,hi in [(25,160),(160,500),(500,2000),(2000,6000),(6000,16000)]:
        z = band(x,lo,hi)
        mid = z.mean(axis=1)
        side = (z[:,0]-z[:,1])/2
        bands[f'{lo}_{hi}'] = {'rms_dbfs':float(db(np.sqrt(np.mean(z*z)))),
                               'side_mid_db':float(db(np.sqrt(np.mean(side*side))/max(np.sqrt(np.mean(mid*mid)),1e-12)))}
    return {'rms_dbfs':float(db(np.sqrt(np.mean(x*x)))),
            'peak_dbfs':float(db(np.max(abs(x)))), 'bands':bands}


def activity(x, gain):
    y = (x*gain).mean(axis=1)
    n = round(FS*.05)
    y = y[:len(y)//n*n].reshape(-1,n)
    levels = db(np.sqrt(np.mean(y*y,axis=1)))
    results = []
    for threshold in [-40.,float(np.percentile(levels,95)-12)]:
        mask = levels > threshold
        changes = np.diff(np.r_[False,mask,False].astype(int))
        spans = [(a*.05,b*.05) for a,b in zip(np.flatnonzero(changes==1),np.flatnonzero(changes==-1))]
        results.append({'threshold_dbfs':threshold,'active_fraction':float(mask.mean()),
                        'longest_contiguous_active_s':max((b-a for a,b in spans),default=0),
                        'note':'Assigned-stem activity including tails/leakage. Not dry-syllable boundaries or an acceptance threshold.'})
    return {'step_s':.05,'results':results,'levels_dbfs':levels.tolist()}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sep = json.loads((OUT/'sw_separation_record.json').read_text(encoding='utf-8'))
    if sep['status'] != 'all_three_contextual_excerpts_separated_and_headers_verified':
        raise RuntimeError('Complete SW separation is required')
    ref_master = BASE/'first_track_20261102/track01_original_0_222.wav'
    ref_sw = BASE/'reference/stems_sw/R01_Lost in the Echoes'
    ref_demucs = BASE/'reference/stems/htdemucs_6s/R01_Lost in the Echoes'
    g12_master = Path(sep['source'])

    def get(label, model, part, a, b, context='body'):
        if label == 'REF':
            if b > 222:
                raise ValueError('Reference extends beyond first song')
            path = ref_master if part=='master' else (
                ref_sw/f'R01_Lost in the Echoes_({part})_BS-Roformer-SW.wav'
                if model=='SW' else ref_demucs/f'{part}.wav')
        elif part == 'master':
            path = g12_master
        elif model == 'Demucs':
            path = RUN/'stems/G12'/f'{part}.wav'
        else:
            section = sep['excerpts'][context]
            row = next(r for r in section['outputs'] if r['part']==part)
            path = Path(row['file'])
            offset = section['source_interval_s'][0]
            a,b = a-offset,b-offset
        return read(path,a,b)

    windows = {'body':{'REF':(39.33,57.616),'G12':(36.7,54.986)},
               'voice':{'REF':(92,110),'G12':(81,99)},
               'break':{'REF':(149,167),'G12':(149,167)}}
    data = {}
    master_gain = {}
    for label in ['REF','G12']:
        x = get(label,'SW','master',*windows['body'][label])
        level = float(pyln.Meter(FS).integrated_loudness(x))
        master_gain[label] = 10**((-20-level)/20)
    result = {'reference_limit_s':222,'ai_direct_listening':False,
              'windows':windows,'analysis_gain_basis':'Each body mix at -20 LUFS; same gain retained for its other windows and stems.',
              'analysis_gains':master_gain,'SW':{},'vocal_model_crosscheck':{},
              'limits':['Separated stems are estimates; labels do not prove an instrument.',
                        'Background is the sum of other+piano+guitar; other alone is not all harmony.',
                        'Reference CPU historical SW output and new CUDA-autocast G12 output differ in precision/context.',
                        'Only user listening can establish phoneme/voice identity; activity includes reverb tails.']}
    for section, by_label in windows.items():
        result['SW'][section] = {}
        for label,(a,b) in by_label.items():
            stems = {part:get(label,'SW',part,a,b,section) for part in PARTS}
            master = get(label,'SW','master',a,b,section)
            n = min(len(master),*(len(x) for x in stems.values()))
            master = master[:n]
            stems = {p:x[:n] for p,x in stems.items()}
            stems['background'] = stems['other']+stems['piano']+stems['guitar']
            data[(section,label)] = {'master':master,**stems}
            rows = {part:summary(x,master_gain[label]) for part,x in {'master':master,**stems}.items()}
            estimate = sum(stems[p] for p in PARTS)
            gain = float(np.sum(master*estimate)/max(np.sum(estimate*estimate),1e-20))
            rows['sum_check'] = {'correlation':float(np.corrcoef(master.ravel(),estimate.ravel())[0,1]),
                                 'best_fit_gain':gain,
                                 'residual_vs_mix_db':float(db(np.sqrt(np.mean((master-estimate*gain)**2))/max(np.sqrt(np.mean(master*master)),1e-12))),
                                 'note':'Input/level alignment aid, not stem purity.'}
            rows['vocal_activity'] = activity(stems['vocals'],master_gain[label])
            result['SW'][section][label] = rows
    for label in ['REF','G12']:
        a,b = windows['voice'][label]
        d = get(label,'Demucs','vocals',a,b,context='voice')
        result['vocal_model_crosscheck'][label] = {'Demucs':activity(d,master_gain[label]),
                                                  'SW':result['SW']['voice'][label]['vocal_activity']}

    # A/B files use one mix-derived gain per excerpt, shared by all its stems.
    # They deliberately preserve vocal/background level rather than normalizing
    # each solo to -20 LUFS, which would hide a foreground/background difference.
    clips = []
    for part,section,duration in [('master','body',12),('vocals','voice',18),
                                  ('background','body',12),('drums','body',12)]:
        pieces = []
        levels = {}
        peaks = {}
        for label in ['REF','G12']:
            source = data[(section,label)]
            mix = source['master'][:round(duration*FS)]
            level = float(pyln.Meter(FS).integrated_loudness(mix))
            gain = 10**((-20-level)/20)
            x = source[part][:len(mix)]*gain
            if np.max(abs(x)) >= 1:
                raise RuntimeError('Comparison stem would clip')
            levels[label] = {'source_mix_lufs':level,'applied_gain_db':-20-level}
            peaks[label] = float(db(np.max(abs(x))))
            if pieces:
                pieces.append(np.zeros((FS,2),dtype='float32'))
            pieces.append(x)
        dest = OUT/f'AB_REF_G12_{part}_{2*duration+1}s.wav'
        sf.write(dest,np.concatenate(pieces),FS,subtype='PCM_16')
        clips.append({'part':part,'file':str(dest),'seconds':sf.info(dest).duration,
                      'order':['REF','G12'],'source_windows':windows[section],
                      'seconds_used_from_each_window':duration,'silence_s':1,
                      'mix_derived_gain':levels,'peak_dbfs':peaks,
                      'note':'Solo estimates inherit their corresponding mix loudness gain; solos are not independently leveled.'})
    result['review_clips'] = clips
    (OUT/'sw_comparison_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    for section in windows:
        for label in ['REF','G12']:
            row = result['SW'][section][label]
            print(section,label,'LEVELS',json.dumps({p:round(row[p]['rms_dbfs'],2) for p in ['master','bass','drums','vocals','background']}),flush=True)
            if section=='body':
                print('BODY_BACKGROUND_BANDS',label,json.dumps(row['background']['bands']),flush=True)
            if section=='voice':
                print('VOICE_ACTIVITY',label,json.dumps(row['vocal_activity']['results']),flush=True)
            print('SUM_CHECK',section,label,json.dumps(row['sum_check']),flush=True)
    print('G12_SW_DIAGNOSTICS_COMPLETE',flush=True)


if __name__=='__main__':
    main()
