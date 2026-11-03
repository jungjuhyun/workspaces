"""Inspect the completed S006 guide trial; no generation or source separation.

Pitch tracks and separated activity are diagnostics, not listening judgments.
The reference reader stops at 222 seconds, before the playlist's next song.
"""
from pathlib import Path
import hashlib
import json
import sys

import librosa
import numpy as np
import pyloudnorm as pyln
import scipy.signal as sig
import soundfile as sf

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / 'local/deep-house/generation_R01S006_20261103'
SR = 11025
HOP = 128


def load(path, limit=None, interval=None):
    with sf.SoundFile(path) as f:
        sr = f.samplerate
        if interval is not None:
            f.seek(round(interval[0] * sr))
            frames = round(interval[1] * sr) - round(interval[0] * sr)
        else:
            frames = -1 if limit is None else round(limit * sr)
        x = f.read(frames=frames, dtype='float32', always_2d=True)
        if frames >= 0 and len(x) != frames:
            raise ValueError(f'Incomplete input: {path}')
    return x, sr


def db(x):
    return 20 * np.log10(np.maximum(x, 1e-12))


def mono(x, sr):
    return librosa.resample(x.mean(axis=1), orig_sr=sr, target_sr=SR)


def pitch_detail(path, limit=None):
    x, sr = load(path, limit)
    y = mono(x, sr)
    f0 = librosa.yin(y, sr=SR, fmin=30, fmax=150,
                     frame_length=2048, hop_length=HOP)
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=HOP)[0]
    midi = librosa.hz_to_midi(f0)
    times = np.arange(len(f0)) * HOP / SR
    # Relative gate excludes near-silence; semitone tolerance rejects ambiguous
    # estimates. Neither is a music-quality acceptance threshold.
    gate = float(np.percentile(db(rms), 95) - 24)
    valid = (db(rms) > gate) & (abs(midi - np.round(midi)) < .35)
    cells = []
    for a in np.arange(0, len(y) / SR, .1):
        mask = valid & (times >= a) & (times < a + .1)
        labels = np.round(midi[mask]).astype(int)
        weights = rms[mask] ** 2
        totals = {int(n): float(weights[labels == n].sum())
                  for n in np.unique(labels)}
        n = max(totals, key=totals.get) if totals else None
        cells.append({'start_s': round(float(a), 3), 'midi': n,
                      'winning_energy_fraction': None if n is None else
                      totals[n] / sum(totals.values())})
    # Keep holes and brief alternate estimates; do not bridge or force the
    # requested three notes into the estimated contour.
    runs = []
    start = 0
    for end in range(1, len(cells) + 1):
        if end == len(cells) or cells[end]['midi'] != cells[start]['midi']:
            n = cells[start]['midi']
            if n is not None and end - start >= 2:
                runs.append({'start_s': round(start * .1, 3),
                             'end_s': round(end * .1, 3), 'midi': n,
                             'hz_equal_tempered': float(librosa.midi_to_hz(n))})
            start = end
    return {'source': str(path), 'relative_gate_dbfs': gate,
            'cell_s': .1, 'frame_length': 2048, 'hop': HOP,
            'minimum_reported_run_s': .2, 'cells': cells, 'runs': runs}


def spectral_peaks(path, a, b):
    x, sr = load(path, interval=(a, b))
    y = x.mean(axis=1).astype('float64')
    y = (y - y.mean()) * np.hanning(len(y))
    nfft = 2 ** int(np.ceil(np.log2(len(y) * 8)))
    magnitude = abs(np.fft.rfft(y, n=nfft))
    frequencies = np.fft.rfftfreq(nfft, 1 / sr)
    peaks, _ = sig.find_peaks(magnitude)
    peaks = [i for i in peaks if 28 <= frequencies[i] <= 180]
    selected = sorted(peaks, key=lambda i: -magnitude[i])[:10]
    maximum = max((magnitude[i] for i in selected), default=1)
    return {'interval_s': [a, b], 'window_s': b-a,
            'window': 'Hann', 'zero_padding_factor_at_least': 8,
            'note': 'Padding interpolates the spectrum; it does not improve its physical resolution.',
            'peaks': [{'hz': float(frequencies[i]),
                       'db_relative_strongest_28_180hz_peak': float(db(magnitude[i]/maximum))}
                      for i in selected]}


def prepare_review(tracks):
    """Equal-loudness original-mix excerpts, not isolated or classified vocals."""
    prior = json.loads((ROOT/'local/deep-house/generation_R01S003_20261103/execution_record.json')
                       .read_text(encoding='utf-8'))
    g05 = next(r for r in prior['outputs'] if r['label'] == 'G05')
    if hashlib.sha256(Path(g05['file']).read_bytes()).hexdigest() != g05['sha256']:
        raise RuntimeError('G05 source hash mismatch')
    sources = {**tracks, 'G05': {'master': Path(g05['file'])}}
    # Reference and G05 windows contain previously human-confirmed chop events.
    # New windows were selected using assigned-stem activity; their semantic
    # identity remains for human listening. No claim of identical arrangement.
    windows = {'REF': (92, 110), 'G05': (61.5, 79.5),
               'G11': (88, 106), 'G12': (81, 99)}
    chunks, records = [], []
    for index, label in enumerate(['REF', 'G05', 'G11', 'G12']):
        a, b = windows[label]
        if label == 'REF' and b > 222:
            raise RuntimeError('Reference would exceed first song')
        x, source_sr = load(sources[label]['master'], interval=(a, b))
        x = librosa.resample(x.T, orig_sr=source_sr, target_sr=48000).T
        source_lufs = float(pyln.Meter(48000).integrated_loudness(x))
        x *= 10 ** ((-20-source_lufs)/20)
        if np.max(abs(x)) >= 1:
            raise RuntimeError('Comparison excerpt would clip')
        dest = RUN/f'{label}_review18s_minus20LUFS.wav'
        sf.write(dest, x, 48000, subtype='PCM_16')
        written, sr = load(dest)
        measured = float(pyln.Meter(sr).integrated_loudness(written))
        if abs(measured+20) > .02:
            raise RuntimeError('Comparison loudness validation failed')
        records.append({'label': label, 'file': str(dest),
                        'source_file': str(sources[label]['master']),
                        'source_interval_s': [a, b], 'target_lufs': -20,
                        'written_lufs': measured,
                        'written_peak_dbfs': float(db(np.max(abs(written)))),
                        'combined_interval_s': [index*19, index*19+18]})
        if chunks:
            chunks.append(np.zeros((48000, 2), dtype='float32'))
        chunks.append(written)
    combined = RUN/'REF_G05_G11_G12_review75s.wav'
    sf.write(combined, np.concatenate(chunks), 48000, subtype='PCM_16')
    return {'clips': records, 'combined_file': str(combined),
            'combined_order': ['REF', 'G05', 'G11', 'G12'],
            'silence_between_s': 1, 'combined_duration_s': sf.info(combined).duration,
            'note': 'Original mixes; gain matching only. No EQ, reverb, stem solo, pitch correction or AI direct listening. Arrangement positions differ.'}


def arrangement_check():
    rows = json.loads((RUN/'comparison_results.json').read_text(encoding='utf-8'))
    checks = []
    for row in rows:
        for part in ['bass', 'drums']:
            power = 10 ** (np.asarray(row['stem_rms_timeline'][part])/10)
            def level(a, b):
                return float(10*np.log10(np.mean(power[round(a*4):round(b*4)])))
            baseline = level(*row['selected_body_window_s'])
            for a, b in [(149, 167), (150, 158)]:
                checks.append({'label': row['label'], 'assigned_stem': part,
                               'interval_s': [a, b],
                               'body_interval_s': row['selected_body_window_s'],
                               'window_vs_body_db': level(a, b)-baseline})
    return {'source': str(RUN/'comparison_results.json'),
            'method': 'Mean linear power of existing 0.25s RMS cells, converted back to dB; within-track comparison against previously selected body window.',
            'note': 'Assigned-stem levels, not listening or exact arrangement boundaries. Different body windows and separation leakage limit interpretation.',
            'checks': checks}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if RUN.is_symlink() or str(RUN.resolve()).lower() != str(RUN).lower():
        raise RuntimeError('S006 must be physically stored at the C path.')
    manifest = json.loads((RUN/'execution_record.json').read_text(encoding='utf-8-sig'))
    reference = ROOT/'local/deep-house/first_track_20261102/track01_original_0_222.wav'
    reference_stems = ROOT/'local/deep-house/reference/stems/htdemucs_6s/R01_Lost in the Echoes'
    tracks = {'REF': {'master': reference, 'bass': reference_stems/'bass.wav', 'limit': 222}}
    for row in manifest['outputs']:
        source = Path(row['file'])
        if hashlib.sha256(source.read_bytes()).hexdigest() != row['sha256']:
            raise RuntimeError(f"Original WAV hash mismatch: {row['label']}")
        folder = RUN/'stems'/row['label']
        if not (folder/'separation_record.json').is_file():
            raise RuntimeError('Missing completed separation record')
        for part in ['bass', 'drums', 'other', 'vocals']:
            info = sf.info(folder/f'{part}.wav')
            if info.samplerate != 44100 or info.channels != 2 or abs(info.duration-row['seconds']) > 1/44100:
                raise RuntimeError(f'Incomplete stem: {folder}/{part}')
        tracks[row['label']] = {'master': source, 'bass': folder/'bass.wav', 'limit': None}
    result = {'reference_limit_s': 222, 'ai_direct_listening': False,
              'physical_run_directory': str(RUN.resolve()),
              'method': 'YIN candidates at 0.1s aggregation, raw-mix spectral checks; no pitch correction or EQ.',
              'tracks': {}}
    for label, source in tracks.items():
        detail = pitch_detail(source['bass'], source['limit'])
        # Check one stable Gb, one Bb, and a possible Db-to-Gb turnaround in
        # each measured contour; these windows are explicit, not hidden scoring.
        windows = {'REF': [(43, 43.8), (51, 51.8), (56.8, 57.4), (58, 58.8)],
                   'G11': [(21, 21.8), (29, 29.8), (35.8, 36.25), (37, 37.8), (54.1, 54.55)],
                   'G12': [(21, 21.8), (29, 29.8), (35.8, 36.25), (37, 37.8), (54.1, 54.55)]}[label]
        detail['raw_mix_spectra'] = [spectral_peaks(source['master'], *w) for w in windows]
        result['tracks'][label] = detail
        print(label, 'PITCH_RUNS_16_60', json.dumps([r for r in detail['runs']
              if r['end_s'] > 16 and r['start_s'] < 60]), flush=True)
        print(label, 'RAW_MIX_PEAKS', json.dumps(detail['raw_mix_spectra']), flush=True)
    result['listening_review'] = prepare_review(tracks)
    result['arrangement_window_check'] = arrangement_check()
    (RUN/'guide_detail_results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    manifest['status'] = 'resumed_on_C_signal_detail_complete_listening_pending'
    manifest['physical_storage_root'] = RUN.as_posix()
    manifest['legacy_path_is_junction'] = False
    manifest['pause_reason'] = None
    manifest['resume_authorization'] = '여기 D드라이브로 옮기지 말고 C드라이브에서 다시 시작해 이어서'
    manifest['storage_history'] = [
        'Originally generated/downloaded on C.',
        'Moved to D after C ran out of space; C path temporarily a Junction.',
        '2026-11-03: copied all 34 files back to physical C, SHA256 verified. Old D copy and renamed old_D_link retained; no longer used for analysis.'
    ]
    (RUN/'execution_record.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
    print('S006_DETAIL_COMPLETE', flush=True)


if __name__ == '__main__':
    main()
