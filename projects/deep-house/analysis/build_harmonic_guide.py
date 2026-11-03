"""Synthesize a newly played harmonic guide; never read reference recordings.

This is a production proposal, not a transcription or recreation claim.
Bass roots come from the documented first-track measurements; chord voicings
and synthesized timbres are deliberately provisional implementation choices.
"""
from pathlib import Path
import json
import hashlib
import numpy as np
import scipy.signal as sig
import soundfile as sf
import pyloudnorm as pyln

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'local/deep-house/harmonic_guide_20261103'
SR = 48000
BPM = 105
BEAT = 60 / BPM
BARS = 10


def hz(midi):
    return 440 * 2 ** ((midi - 69) / 12)


def envelope(t, duration, attack=.012, release=.09):
    return np.minimum(t / attack, 1) * np.minimum(np.maximum(duration - t, 0) / release, 1)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    n = round(BARS * 4 * BEAT * SR)
    t = np.arange(n) / SR
    bass = np.zeros(n)
    chords = np.zeros((n, 2))
    drums = np.zeros(n)
    events = [(0, 16, 30, 'Gb1'), (16, 30, 34, 'Bb1'),
              (30, 32, 25, 'Db1'), (32, 40, 30, 'Gb1')]
    for start, end, midi, name in events:
        a, b = round(start * BEAT * SR), min(n, round(end * BEAT * SR))
        q = np.arange(b - a) / SR
        phase = 2 * np.pi * hz(midi) * q
        tone = np.sin(phase) + .17 * np.sin(2 * phase) + .055 * np.sin(3 * phase)
        bass[a:b] += .18 * tone * envelope(q, (b-a)/SR)
    # A simple ducking shape is a guide choice, not an inferred compressor preset.
    since_beat = np.mod(t, BEAT)
    bass *= .28 + .72 * (1 - np.exp(-since_beat / .095))
    voicings = [(0, 16, [54, 58, 61, 65]), (16, 32, [58, 61, 65]),
                (32, 40, [54, 58, 61, 65])]
    for start, end, notes in voicings:
        a, b = round(start*BEAT*SR), min(n, round(end*BEAT*SR))
        q = np.arange(b-a)/SR
        env = envelope(q, (b-a)/SR, attack=.11, release=.45)
        for k, midi in enumerate(notes):
            phase = 2*np.pi*hz(midi)*q
            tone = np.sin(phase) + .11*np.sin(2*phase) + .025*np.sin(3*phase)
            pan = .32 if k % 2 == 0 else .68
            chords[a:b, 0] += .019*tone*env*np.sqrt(1-pan)
            chords[a:b, 1] += .019*tone*env*np.sqrt(pan)
    rng = np.random.default_rng(105)
    for beat in range(BARS*4):
        a = round(beat*BEAT*SR)
        m = min(n-a, round(.34*SR))
        q = np.arange(m)/SR
        phase = 2*np.pi*(48*q + 42*.018*(1-np.exp(-q/.018)))
        drums[a:a+m] += .16*np.sin(phase)*np.exp(-q/.085)*np.minimum(q/.003, 1)
        if beat % 4 in [1, 3]:
            m = min(n-a, round(.10*SR)); q = np.arange(m)/SR
            noise = rng.standard_normal(m)
            noise = sig.sosfilt(sig.butter(2, [180, 2300], btype='bandpass', fs=SR, output='sos'), noise)
            drums[a:a+m] += .019*noise*np.exp(-q/.022)
        a = round((beat+.5)*BEAT*SR)
        m = min(n-a, round(.07*SR)); q = np.arange(m)/SR
        noise = sig.sosfilt(sig.butter(2, [3200, 6500], btype='bandpass', fs=SR, output='sos'), rng.standard_normal(m))
        drums[a:a+m] += .010*noise*np.exp(-q/.015)
    mix = np.column_stack([bass+drums, bass+drums]) + chords
    fade = np.minimum(np.arange(n)/(SR*.008), 1)*np.minimum(np.arange(n-1, -1, -1)/(SR*.07), 1)
    mix *= fade[:, None]
    source_lufs = float(pyln.Meter(SR).integrated_loudness(mix))
    mix *= 10 ** ((-20-source_lufs)/20)
    if abs(mix).max() >= 1:
        raise ValueError('Guide would clip')
    path = OUT/'R01_harmony_guide_10bars_105bpm.wav'
    sf.write(path, mix, SR, subtype='PCM_16')
    sf.write(OUT/'guide_bass_diagnostic.wav', bass, SR, subtype='FLOAT')
    record = {'file':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
              'sample_rate':SR,'channels':2,'seconds':n/SR,'bpm':BPM,'bars':BARS,
              'target_lufs':-20,'source_lufs_before_gain':source_lufs,
              'peak_dbfs':float(20*np.log10(abs(mix).max())),
              'source':'Locally synthesized oscillators/noise only; no reference recording or generated song read.',
              'bass_events':[{'start_beat':a,'end_beat':b,'midi':m,'note':name,'hz':hz(m)} for a,b,m,name in events],
              'chord_voicings_midi':voicings,
              'limits':'Newly played guide. Voicing, sound and ducking are implementation proposals, not the original stems or exact transcription.',
              'uploaded_to_suno':False}
    (OUT/'guide_manifest.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    print(json.dumps(record,indent=2))


if __name__ == '__main__':
    main()
