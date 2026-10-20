#!/usr/bin/env python3
"""Generate private current-source dialogue with the supplied local Kokoro model."""
import argparse
import concurrent.futures
import hashlib
import importlib.metadata
import json
from pathlib import Path
import threading

import numpy as np
import onnxruntime as ort
import soundfile as sf
from kokoro_onnx import Kokoro
from pronunciation import phonemize_dialogue


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--model', type=Path, required=True)
    p.add_argument('--voices', type=Path, required=True)
    p.add_argument('--workers', type=int, default=2)
    p.add_argument('--only-id', action='append', help='Generate only selected source record IDs into a fresh recordings directory')
    p.add_argument('--recordings-directory', type=Path)
    args = p.parse_args()
    assert importlib.metadata.version('kokoro-onnx') == '0.6.1'
    assert importlib.metadata.version('onnxruntime') == '1.31.0'
    lines = json.loads((args.package / 'timing/dialogue.json').read_text())['lines']
    if args.only_id:
        lines = [line for line in lines if line['id'] in args.only_id]
        assert {line['id'] for line in lines} == set(args.only_id), 'Unknown source record ID'
    cast = json.loads((args.package / 'voices/cast.json').read_text())['cast']
    output = args.recordings_directory or args.package / 'recordings'
    output.mkdir(exist_ok=True)
    state = threading.local()

    def generate(line):
        if not hasattr(state, 'kokoro'):
            opts = ort.SessionOptions()
            opts.intra_op_num_threads = 2
            opts.inter_op_num_threads = 1
            session = ort.InferenceSession(str(args.model), sess_options=opts, providers=['CPUExecutionProvider'])
            state.kokoro = Kokoro.from_session(session, str(args.voices))
        k = state.kokoro
        v = cast[line['speaker']]
        settings = v['settings']
        phonemes = phonemize_dialogue(k.tokenizer, line['text'], settings['lang'])
        samples, rate = k.create(phonemes, v['voice_id'], speed=settings['speed'], lang=settings['lang'],
                                 is_phonemes=True, trim=True, sentence_pause=.25, clause_pause=.10)
        assert rate == 24000 and len(samples) and np.isfinite(samples).all()
        rms = float(np.sqrt(np.mean(samples.astype(np.float64) ** 2)))
        peak = float(np.max(np.abs(samples)))
        assert peak > 0 and rms > 0
        gain = min(1.8, .15 / rms, .88 / peak)
        adjusted = samples * gain
        path = output / line['wav_file']
        assert not path.exists(), 'Refusing to replace a prior recording: ' + str(path)
        sf.write(path, adjusted, rate, subtype='PCM_16')
        record = {**{key: line[key] for key in ['id', 'speaker', 'text']},
                  **{key: v[key] for key in ['engine', 'voice_id', 'settings']},
                  'wav': path.name, 'phonemes': phonemes, 'samples': len(samples), 'duration': len(samples) / rate,
                  'raw_rms': rms, 'raw_peak': peak, 'gain': gain, 'output_peak': float(np.max(np.abs(adjusted))),
                  'output_rms': float(np.sqrt(np.mean(adjusted.astype(np.float64) ** 2))),
                  'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        (output / (line['id'] + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({'id': line['id'], 'speaker': line['speaker'], 'seconds': record['duration']}), flush=True)
        return record

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        records = list(pool.map(generate, lines))
    (output / 'recordings.json').write_text(json.dumps({'recordings': records}, ensure_ascii=False, indent=2) + '\n')
    print('COMPLETE', len(records), flush=True)


if __name__ == '__main__':
    main()
