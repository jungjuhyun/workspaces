"""Prepare S007 full-mix listening review and fixed-window signal diagnostics.

No direct AI listening, Suno action, EQ, reverb, or stem replacement.
"""
from pathlib import Path
import json
import hashlib
import sys
import numpy as np
import pyloudnorm as pyln
import soundfile as sf
from g12_sw_diagnostics import read, summary, activity, FS, PARTS
from guide_trial_detail import pitch_detail, spectral_peaks

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'local/deep-house'
RUN = BASE/'generation_R01S007_20261103'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8*1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    execution = json.loads((RUN/'execution_record.json').read_text(encoding='utf-8'))
    masters = {'REF': BASE/'first_track_20261102/track01_original_0_222.wav',
               'G12': BASE/'generation_R01S006_20261103/R01-S006_G12_e83d79e1.wav',
               **{r['label']:Path(r['file']) for r in execution['outputs']}}
    windows = {'body': {'REF':(39.33,57.616), 'G13':(36.7,54.986), 'G14':(36.7,54.986)},
               'voice': {'REF':(92,110), 'G13':(81,99), 'G14':(81,99)},
               'break': {'REF':(149,167), 'G13':(149,167), 'G14':(149,167)}}
    result = {'reference_limit_s':222, 'ai_direct_listening':False, 'windows':windows,
              'analysis_gain_basis':'Each fixed body mix at -20 LUFS; same gain retained in other windows and stems.',
              'limits':['Stem estimates include leakage and tails; activity is not dry phoneme duration.',
                        'Historical REF SW is CPU; new generated SW uses CUDA autocast and excerpt context.',
                        'Fixed windows are reused from G12; they do not prove matching arrangement positions.',
                        'No automatic acceptance score; full-mix user listening remains pending.'],
              'signals':{}, 'review':{}, 'bass_pitch_candidates':{}}
    for label in ['G13','G14']:
        detail = pitch_detail(RUN/f'stems/{label}/bass.wav', limit=60)
        spectra = []
        for midi in [30,34,25]:
            candidates = [r for r in detail['runs'] if r['midi']==midi and r['start_s']>=16]
            if candidates:
                run = max(candidates,key=lambda r:r['end_s']-r['start_s'])
                a = run['start_s']
                b = min(run['end_s'],a+.8)
                spectra.append({'midi_candidate':midi,**spectral_peaks(masters[label],a,b)})
        detail['raw_mix_spectra'] = spectra
        result['bass_pitch_candidates'][label] = detail
        print('PITCH_RUNS_16_60',label,json.dumps([r for r in detail['runs'] if r['end_s']>16]),flush=True)
    for label in ['REF','G13','G14']:
        gain = 10**((-20-pyln.Meter(FS).integrated_loudness(read(masters[label],*windows['body'][label])))/20)
        sep = None if label == 'REF' else json.loads((RUN/f'sw_review_20261103/{label}/sw_separation_record.json').read_text(encoding='utf-8'))
        if sep:
            assert sep['status'] == 'all_three_contextual_excerpts_separated_and_headers_verified'
            assert sha(masters[label]) == sep['source_sha256']
        result['signals'][label] = {'gain':float(gain), 'sections':{}}
        for section in windows:
            a,b = windows[section][label]
            master = read(masters[label],a,b)
            stems = {}
            for part in PARTS:
                if label == 'REF':
                    path = BASE/f'reference/stems_sw/R01_Lost in the Echoes/R01_Lost in the Echoes_({part})_BS-Roformer-SW.wav'
                    stems[part] = read(path,a,b)
                else:
                    entry = sep['excerpts'][section]
                    path = Path(next(r['file'] for r in entry['outputs'] if r['part']==part))
                    offset = entry['source_interval_s'][0]
                    stems[part] = read(path,a-offset,b-offset)
            n = min(len(master),*(len(x) for x in stems.values()))
            master = master[:n]
            stems = {p:x[:n] for p,x in stems.items()}
            stems['background'] = stems['other']+stems['piano']+stems['guitar']
            row = {p:summary(x,gain) for p,x in {'master':master,**stems}.items()}
            estimate = sum(stems[p] for p in PARTS)
            row['stem_sum_correlation'] = float(np.corrcoef(master.ravel(),estimate.ravel())[0,1])
            if section == 'voice':
                row['SW_activity'] = activity(stems['vocals'],gain)
                demucs_path = BASE/'reference/stems/htdemucs_6s/R01_Lost in the Echoes/vocals.wav' if label=='REF' else RUN/f'stems/{label}/vocals.wav'
                row['Demucs_activity'] = activity(read(demucs_path,a,b),gain)
            result['signals'][label]['sections'][section] = row
        print('SIGNALS',label,json.dumps({
            'vocal_SW_fraction':result['signals'][label]['sections']['voice']['SW_activity']['results'][0]['active_fraction'],
            'vocal_Demucs_fraction':result['signals'][label]['sections']['voice']['Demucs_activity']['results'][0]['active_fraction'],
            'break_minus_body_db':{p:round(result['signals'][label]['sections']['break'][p]['rms_dbfs']-result['signals'][label]['sections']['body'][p]['rms_dbfs'],2) for p in ['bass','drums']},
            'mid_side_db':result['signals'][label]['sections']['body']['master']['bands']['500_2000']['side_mid_db']}),flush=True)

    order = ['REF','G12','G13','G14']
    review_windows = {'REF':(92,110), **{label:(81,99) for label in order[1:]}}
    pieces, rows = [], []
    for i,label in enumerate(order):
        a,b = review_windows[label]
        assert label != 'REF' or b <= 222
        x = read(masters[label],a,b)
        level = float(pyln.Meter(FS).integrated_loudness(x))
        x *= 10**((-20-level)/20)
        peak = float(np.max(abs(x)))
        assert peak < 1 and np.isfinite(x).all()
        if pieces:
            pieces.append(np.zeros((FS,2),dtype='float32'))
        pieces.append(x)
        rows.append({'label':label,'source':str(masters[label]),'source_sha256':sha(masters[label]),
                     'source_window_s':[a,b],'review_window_s':[i*19,i*19+18],
                     'source_lufs':level,'rendered_lufs':float(pyln.Meter(FS).integrated_loudness(x)),
                     'sample_peak_dbfs':float(20*np.log10(peak))})
    dest = RUN/'REF_G12_G13_G14_fullmix_review75s.wav'
    sf.write(dest,np.concatenate(pieces),FS,subtype='PCM_16')
    assert sf.info(dest).frames == 75*FS
    decoded = sf.read(dest,dtype='float32',always_2d=True)[0]
    for i in range(4):
        lufs = float(pyln.Meter(FS).integrated_loudness(decoded[i*19*FS:(i*19+18)*FS]))
        assert abs(lufs+20) < .01
        rows[i]['decoded_lufs'] = lufs
    result['review'] = {'file':str(dest),'sha256':sha(dest),'seconds':75,'order':order,'clips':rows,
                        'processing':'Whole mix excerpts, gain only to -20 LUFS each; no stem solo, EQ or reverb.'}
    (RUN/'s007_review_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('S007_FULL_MIX_REVIEW_COMPLETE',flush=True)


if __name__ == '__main__':
    main()
