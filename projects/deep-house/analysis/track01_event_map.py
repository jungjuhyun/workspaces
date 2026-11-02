"""Map first-track pitch spans, pumping and recurrence; never read past 222 s.

Outputs are diagnostics, not a ground-truth score, MIDI or instrument classifier.
"""
from pathlib import Path
import json
import numpy as np
import scipy.signal as sig
from scipy.ndimage import gaussian_filter1d, binary_closing
import soundfile as sf
import librosa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'local/deep-house/first_track_20261102'
OUT = BASE / 'refinement'
SR = 11025
END = 222


def load(part, model='sw'):
    if part == 'original':
        path = BASE / 'track01_original_0_222.wav'
    elif model == 'sw':
        path = ROOT / f'local/deep-house/reference/stems_sw/R01_Lost in the Echoes/R01_Lost in the Echoes_({part})_BS-Roformer-SW.wav'
    else:
        path = ROOT / f'local/deep-house/reference/stems/htdemucs_6s/R01_Lost in the Echoes/{part}.wav'
    with sf.SoundFile(path) as f:
        source_sr = f.samplerate
        x = f.read(frames=source_sr * END, dtype='float32', always_2d=True)
    assert len(x) == source_sr * END
    return librosa.resample(x.mean(axis=1), orig_sr=source_sr, target_sr=SR)


def db(x):
    return 20 * np.log10(np.maximum(x, 1e-12))


def envelope(x, lo, hi):
    z = sig.sosfiltfilt(sig.butter(4, [lo, hi], btype='bandpass', fs=SR, output='sos'), x)
    return gaussian_filter1d(np.abs(sig.hilbert(z)), SR * .01)


def similarity_features(y):
    hop = 220
    m = librosa.feature.melspectrogram(y=y, sr=SR, n_fft=2048, hop_length=hop,
                                      n_mels=24, fmin=150, fmax=2500, power=2)
    # Positive features and rolling cosine similarity preserve spectral shape.
    return np.sqrt(m).astype('float64'), hop / SR


def activity_regions(y, threshold_dbfs=-45.0):
    """Thresholded assigned-stem activity, including tails; not vocal note bounds."""
    edges = np.arange(0, END, .1)
    levels = np.asarray([float(db(np.sqrt(np.mean(y[int(t * SR):int(min(t + .1, END) * SR)] ** 2))))
                         for t in edges])
    active = binary_closing(levels > threshold_dbfs, structure=np.ones(3))
    changes = np.diff(np.r_[False, active, False].astype(int))
    rows = []
    for a, b in zip(np.flatnonzero(changes == 1), np.flatnonzero(changes == -1)):
        if b - a >= 3:
            rows.append({'start_s': round(a * .1, 2), 'end_s': round(b * .1, 2),
                         'peak_0p1s_rms_dbfs': float(levels[a:b].max())})
    return {'threshold_dbfs': threshold_dbfs, 'time_step_s': .1, 'closing_window_s': .3,
            'minimum_region_s': .3, 'note': 'assigned-stem signal plus tails; not a semantic vocal detector',
            'regions': rows}


def recurrence(features, step, a, b):
    i, j = round(a / step), round(b / step)
    template = features[:, i:j]
    width = template.shape[1]
    numerator = sum(sig.correlate(row, target, mode='valid', method='direct')
                    for row, target in zip(features, template))
    energy = sig.convolve(np.sum(features ** 2, axis=0), np.ones(width), mode='valid', method='direct')
    denom = np.sqrt(np.maximum(energy, 0) * np.sum(template ** 2))
    valid = energy > max(float(energy.max()) * 1e-8, 1e-20)
    score = np.full_like(numerator, -1.0)
    score[valid] = numerator[valid] / np.maximum(denom[valid], 1e-20)
    assert np.max(score) <= 1 + 1e-6, 'Cosine similarity exceeded its numerical bound.'
    score = np.minimum(score, 1.0)
    peaks, _ = sig.find_peaks(score, distance=round(3 / step))
    ranked = sorted(peaks, key=lambda k: -score[k])[:20]
    return [{'start_s': float(k * step), 'end_s': float(k * step + b - a),
             'similarity': float(score[k])} for k in ranked]


def main():
    OUT.mkdir(exist_ok=True)
    base = json.loads((BASE / 'signal_results.json').read_text(encoding='utf-8'))
    period = base['rhythm']['sw']['period_s']
    phase = base['rhythm']['sw']['phase_s']
    # This local bar origin follows a root-cycle entry, not a verified global bar 1.
    anchor = phase + round((39.31 - phase) / period) * period
    result = {'seconds': END, 'sr': SR, 'beat_period_s': period,
              'local_eight_bar_anchor_s': anchor,
              'recurrence_method': {'mel_bands': 24, 'band_hz': [150, 2500],
                                    'window_s': 3, 'energy_floor_relative_to_max': 1e-8,
                                    'normalization': 'rolling cosine; direct summation; upper bound asserted',
                                    'interpretation': 'candidate only; quiet-window spectral similarity is not vocal evidence'},
              'limitations': ['Candidate pitch spans include masked/gated frames; they are not note gates.',
                             'A repeated envelope alone cannot identify oscillator retriggers or a compressor.',
                             'Template similarity identifies candidates, not semantic vocal confirmation.']}
    original = load('original')
    bass_rows = []
    pitch_traces = []
    for model in ['sw', 'demucs']:
        y = load('bass', model)
        hop = 128
        f0 = librosa.yin(y, sr=SR, fmin=30, fmax=150, frame_length=2048, hop_length=hop)
        rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=hop)[0]
        midi = librosa.hz_to_midi(f0)
        valid = (db(rms) > -42) & (np.abs(midi - np.round(midi)) < .35)
        times = np.arange(len(midi)) * hop / SR
        pitch_traces.append((model, times, midi, valid))
        for k in range(32):
            a = anchor + k * period
            b = a + period
            mask = valid & (times >= a) & (times < b)
            labels = np.round(midi[mask]).astype(int)
            weights = rms[mask] ** 2
            totals = {int(n): float(weights[labels == n].sum()) for n in np.unique(labels)}
            notes = sorted(totals, key=lambda n: -totals[n])
            bass_rows.append({'model': model, 'local_bar': k // 4 + 1, 'beat': k % 4 + 1,
                              'start_s': a, 'end_s': b, 'valid_frame_count': int(mask.sum()),
                              'pitch_candidates': [{'midi': n, 'note': librosa.midi_to_note(n),
                                                    'within_cell_energy_weight': totals[n] / max(sum(totals.values()), 1e-12)}
                                                   for n in notes[:3]]})
    result['representative_eight_bars_bass'] = bass_rows
    print('EIGHT_BAR_BASS', json.dumps(bass_rows, ensure_ascii=True), flush=True)

    # Keep same-pitch support and beat-synchronous amplitude as separate observations.
    pump_rows = []
    folded = []
    for label, a, b, center in [('Gb', 40, 48, 92.5), ('Bb', 49, 56, 116.54)]:
        for source in ['original', 'sw', 'demucs']:
            y = original if source == 'original' else load('bass', source)
            e = envelope(y, center - 9, center + 9)
            curves = []
            for t in np.arange(phase, END, period):
                if a <= t and t + period < b:
                    c = np.interp(t + np.linspace(0, period, 100, endpoint=False), np.arange(len(e)) / SR, e)
                    curves.append(c / max(np.percentile(c, 95), 1e-12))
            curve = np.median(curves, axis=0)
            folded.append((label, source, curve))
            low, high = np.argmin(curve), np.argmax(curve)
            pump_rows.append({'root_region': label, 'source': source, 'interval_s': [a, b],
                              'band_hz': [center - 9, center + 9], 'beats': len(curves),
                              'minimum_beat_fraction': float(low / 100), 'maximum_beat_fraction': float(high / 100),
                              'maximum_minimum_db': float(db(curve[high] / max(curve[low], 1e-12)))})
    result['representative_harmonic_envelope'] = pump_rows
    print('PUMP_TIMING', json.dumps(pump_rows), flush=True)

    # Track spectral/pitch content at intro events instead of declaring every peak a new note.
    intro_events = json.loads((OUT / 'refinement_signal_results.json').read_text(encoding='utf-8'))['intro_other_spectral_onsets_s']
    intro_rows = []
    other_features = {}
    for model in ['sw', 'demucs']:
        y = load('other', model)
        hop = 128
        c = np.abs(librosa.cqt(y, sr=SR, hop_length=hop, fmin=librosa.note_to_hz('C2'), n_bins=72))
        other_features[model] = c
        for t in intro_events:
            if not 3 < t < 18:
                continue
            # Observe just after a candidate spectral change; CQT kernels blur boundaries.
            i, j = int((t + .03) * SR / hop), int((t + .17) * SR / hop)
            v = np.mean(c[:, i:j], axis=1)
            peaks, _ = sig.find_peaks(v)
            strongest = sorted(peaks, key=lambda n: -v[n])[:4]
            intro_rows.append({'model': model, 'event_candidate_s': t,
                               'spectral_note_candidates': [{'midi': int(k + 36), 'note': librosa.midi_to_note(k + 36),
                                                             'relative_cqt_amplitude': float(v[k] / max(v.max(), 1e-12))}
                                                            for k in strongest]})
    result['intro_event_spectral_candidates'] = intro_rows
    print('INTRO_EVENT_PITCH', json.dumps(intro_rows[:32], ensure_ascii=True), flush=True)

    rec = {}
    for source in ['original', 'sw', 'demucs']:
        y = original if source == 'original' else load('vocals', source)
        features, step = similarity_features(y)
        rec[source] = {'A_20_23': recurrence(features, step, 20, 23),
                       'B_93_96': recurrence(features, step, 93, 96)}
    result['vocal_template_candidate_recurrence'] = rec
    print('VOCAL_RECURRENCE', json.dumps(rec), flush=True)
    activity = {model: activity_regions(load('vocals', model)) for model in ['sw', 'demucs']}
    result['assigned_vocal_activity_regions'] = activity
    (OUT / 'assigned_vocal_activity_regions.json').write_text(json.dumps(activity, indent=2), encoding='utf-8')

    fig, axes = plt.subplots(4, 1, figsize=(14, 12))
    for model, times, midi, valid in pitch_traces:
        m = valid & (times > anchor) & (times < anchor + 32 * period)
        axes[0].scatter(times[m], midi[m], s=3, label=model, alpha=.5)
    axes[0].set(xlim=(anchor, anchor + 32 * period), ylim=(23, 42), ylabel='Bass MIDI candidate')
    axes[0].legend()
    for k in range(9):
        axes[0].axvline(anchor + 4 * k * period, color='gray', alpha=.3)
    for label, source, curve in folded:
        axes[1].plot(np.arange(100) / 100, curve, label=f'{label} {source}', linewidth=1)
    axes[1].set(xlabel='Beat fraction after fitted kick peak grid', ylabel='Normalized harmonic envelope')
    axes[1].legend(ncol=3)
    c = other_features['sw'][:, :int(18 * SR / 128)]
    axes[2].imshow(20 * np.log10(c + 1e-6), origin='lower', aspect='auto', extent=[0,18,36,108], cmap='magma')
    axes[2].set(ylim=(45, 82), ylabel='Other CQT MIDI bin', xlabel='First-track time (s)')
    voice = load('vocals')
    edges = np.arange(0, END, .1)
    energy = [float(db(np.sqrt(np.mean(voice[int(t*SR):int(min(t+.1,END)*SR)] ** 2)))) for t in edges]
    axes[3].plot(edges, energy, linewidth=.7)
    axes[3].axvspan(20, 23, alpha=.2, color='green', label='Listening anchor A, not event bounds')
    axes[3].axvspan(93, 96, alpha=.2, color='orange', label='Listening anchor B, not event bounds')
    axes[3].set(xlim=(0, END), ylim=(-65,-15), xlabel='First-track time (s)', ylabel='SW vocals 0.1 s RMS dBFS')
    axes[3].legend()
    fig.tight_layout()
    fig.savefig(OUT / 'track01_event_map.png', dpi=140)
    plt.close(fig)
    (OUT / 'event_map_results.json').write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
    print('EVENT_MAP_COMPLETE', flush=True)


if __name__ == '__main__':
    main()
