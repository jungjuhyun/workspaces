"""Run BS-RoFormer-SW on contextual generated-song excerpts.

Local diagnostics only. No Suno generation, upload, or AI direct listening.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import logging
import sys
import time

import numpy as np
import soundfile as sf
import torch

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT/'local/deep-house/generation_R01S006_20261103'
OUT = RUN/'sw_review_20261103'
MODELS = Path('C:/tmp/audio-separator-models')
PARTS = ['bass', 'drums', 'other', 'vocals', 'guitar', 'piano']
EXCERPTS = {'body': (28, 76), 'voice': (72, 114), 'break': (136, 182)}


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8*1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    global RUN, OUT, EXCERPTS
    sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-dir', type=Path, default=RUN)
    parser.add_argument('--label', default='G12')
    parser.add_argument('--voice-context', type=int, nargs=2)
    parser.add_argument('--body-context', type=int, nargs=2)
    args = parser.parse_args()
    requested_run = args.run_dir.absolute()
    RUN = requested_run.resolve()
    OUT = RUN/'sw_review_20261103'
    if args.label != 'G12':
        OUT = OUT/args.label
    if args.voice_context:
        EXCERPTS = {**EXCERPTS, 'voice':tuple(args.voice_context)}
    if args.body_context:
        EXCERPTS = {**EXCERPTS, 'body':tuple(args.body_context)}
    if RUN.drive.upper() != 'C:' or RUN != requested_run:
        raise RuntimeError('Analysis must remain physically on C')
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((RUN/'execution_record.json').read_text(encoding='utf-8'))
    g12 = next(r for r in manifest['outputs'] if r['label'] == args.label)
    source = Path(g12['file'])
    assert sha(source) == g12['sha256']
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA unavailable; inspect before running a slow CPU separation')
    torch.set_num_threads(4)
    torch.manual_seed(0)
    record = {'status': 'separating', 'label':args.label, 'source': str(source), 'source_sha256': sha(source),
              'model_file': str(MODELS/'BS-Roformer-SW.ckpt'),
              'model_sha256': sha(MODELS/'BS-Roformer-SW.ckpt'),
              'config_file': str(MODELS/'BS-Roformer-SW.yaml'),
              'config_sha256': sha(MODELS/'BS-Roformer-SW.yaml'),
              'package': importlib.metadata.version('audio-separator'),
              'torch': torch.__version__, 'device': torch.cuda.get_device_name(0),
              'settings': {'autocast': True, 'overlap': 2, 'batch_size': 1,
                           'normalization_threshold': 1.0, 'amplification_threshold': 0.0,
                           'sample_rate': 44100, 'context_added': True},
              'comparison_limit': 'Reference reused old CPU SW outputs; generated song uses GPU autocast. Not bit-identical re-execution of historical settings.',
              'ai_direct_listening': False, 'suno_create_clicks': 0, 'excerpts': {}}
    record_path = OUT/'sw_separation_record.json'
    if record_path.exists():
        old = json.loads(record_path.read_text(encoding='utf-8'))
        if (old['source_sha256'] == record['source_sha256'] and
                old['model_sha256'] == record['model_sha256'] and
                old['config_sha256'] == record['config_sha256'] and
                old['settings'] == record['settings']):
            record['excerpts'] = old['excerpts']
    from audio_separator.separator import Separator
    separator = None
    for name, (a, b) in EXCERPTS.items():
        previous = record['excerpts'].get(name)
        if previous and previous['source_interval_s'] == [a, b] and all(Path(r['file']).is_file() and
                            sf.info(r['file']).samplerate == 44100 and
                            abs(sf.info(r['file']).duration-(b-a)) < 1/44100
                            for r in previous['outputs']) and len(previous['outputs']) == 6:
            print('REUSE_COMPLETED_SW', name, flush=True)
            continue
        input_path = OUT/f'{args.label}_{name}_{a}_{b}.wav'
        with sf.SoundFile(source) as f:
            sr = f.samplerate
            f.seek(round(a*sr))
            x = f.read(round((b-a)*sr), dtype='float32', always_2d=True)
        assert len(x) == round((b-a)*sr)
        sf.write(input_path, x, sr, subtype='FLOAT')
        if separator is None:
            separator = Separator(log_level=logging.INFO, model_file_dir=str(MODELS),
                                  output_dir=str(OUT/'stems_sw'), output_format='WAV',
                                  normalization_threshold=1.0, amplification_threshold=0.0,
                                  sample_rate=44100, use_soundfile=True, use_autocast=True,
                                  mdxc_params={'segment_size':256, 'override_model_segment_size':False,
                                               'batch_size':1, 'overlap':2, 'pitch_shift':0})
            separator.load_model('BS-Roformer-SW.ckpt')
            assert separator.torch_device.type == 'cuda'
            print('SW_LOADED_ON_CUDA', flush=True)
        start = time.time()
        separator.separate(str(input_path))
        outputs = []
        for part in PARTS:
            paths = list((OUT/'stems_sw').glob(f'{input_path.stem}_({part})_*.wav'))
            if len(paths) != 1:
                raise RuntimeError(f'Unexpected SW output for {name}/{part}: {paths}')
            path = paths[0]
            info = sf.info(path)
            assert info.samplerate == 44100 and info.channels == 2
            assert abs(info.duration-(b-a)) < 1/44100
            outputs.append({'part':part, 'file':str(path), 'sha256':sha(path),
                            'seconds':info.duration, 'subtype':info.subtype})
        record['excerpts'][name] = {'source_interval_s':[a,b], 'input':str(input_path),
                                     'input_sha256':sha(input_path), 'elapsed_s':time.time()-start,
                                     'outputs':outputs}
        record_path.write_text(json.dumps(record, indent=2), encoding='utf-8')
        print('SW_EXCERPT_COMPLETE', name, flush=True)
    record['status'] = 'all_three_contextual_excerpts_separated_and_headers_verified'
    record_path.write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(f'{args.label}_SW_SEPARATION_COMPLETE', flush=True)


if __name__ == '__main__':
    main()
