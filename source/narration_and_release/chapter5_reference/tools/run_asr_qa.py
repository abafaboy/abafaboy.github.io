#!/usr/bin/env python3
"""Unprompted offline recognition; no claim of subjective audition."""
import argparse
import concurrent.futures
import dataclasses
import difflib
import hashlib
import importlib.metadata
import json
from pathlib import Path
import re
import subprocess

import numpy as np

from faster_whisper import WhisperModel


def words(text):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text.lower().replace('’', "'"))


def differences(expected, actual):
    a, b = words(expected), words(actual)
    return [{'operation': tag, 'source': a[i:j], 'recognized': b[k:l]}
            for tag, i, j, k, l in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if tag != 'equal']


def decode(path):
    # The installed PyAV19 removed metadata_errors expected by faster-whisper1.2.1.
    # Use its documented float32/16kHz waveform input with the existing FFmpeg.
    pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-ar', '16000', '-ac', '1',
                          '-f', 'f32le', '-'], stdout=subprocess.PIPE, check=True).stdout
    return np.frombuffer(pcm, dtype='<f4')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument('--model', default='small.en')
    p.add_argument('--model-cache', type=Path, required=True)
    p.add_argument('--names-only', action='store_true')
    p.add_argument('--review-from', type=Path)
    p.add_argument('--full-track-only', action='store_true')
    p.add_argument('--clips-only', action='store_true')
    p.add_argument('--only-id', action='append', help='Recognize only selected existing recording IDs')
    p.add_argument('--output', type=Path, default=Path(__file__).resolve().parents[1] / 'qa/content_audio/asr_result.json')
    a = p.parse_args()
    a.output.parent.mkdir(parents=True, exist_ok=True)
    model = WhisperModel(a.model, device='cpu', compute_type='int8', cpu_threads=4, num_workers=2,
                         download_root=str(a.model_cache))
    lines = json.loads((a.package / 'recordings/recordings.json').read_text())['recordings']
    if a.only_id:
        if not a.clips_only or a.full_track_only:
            p.error('--only-id requires --clips-only and excludes --full-track-only')
        lines = [line for line in lines if line['id'] in a.only_id]
        if {line['id'] for line in lines} != set(a.only_id):
            p.error('Unknown recording ID')
    if a.names_only:
        lines = [line for line in lines if any(name in line['text'] for name in ['Taeo', 'Nib', 'Chae'])]
    if a.review_from:
        prior = [json.loads(path.read_text()) for path in a.review_from.glob('*.json')]
        selected = {line['id'] for line in prior if line['differences']}
        lines = [line for line in lines if line['id'] in selected]
    source_for_full_track = lines
    if a.full_track_only:
        lines = []
    options = dict(language='en', beam_size=5, temperature=0, condition_on_previous_text=False,
                   initial_prompt=None, hotwords=None, vad_filter=False, word_timestamps=True,
                   no_speech_threshold=None)

    def transcribe(line):
        path = a.package / 'recordings' / line['wav']
        segments, info = model.transcribe(decode(path), **options)
        segments = [dataclasses.asdict(s) for s in segments]
        text = ' '.join(s['text'].strip() for s in segments).strip()
        result = {'id': line['id'], 'speaker': line['speaker'], 'voice_id': line['voice_id'],
                  'source': line['text'], 'recognized': text, 'differences': differences(line['text'], text),
                  'segments': segments, 'wav_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        checkpoint = a.output.parent / (a.output.stem + '_lines')
        checkpoint.mkdir(exist_ok=True)
        (checkpoint / (line['id'] + '.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps({key: result[key] for key in ['id', 'source', 'recognized', 'differences']}), flush=True)
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(transcribe, lines))
    output = {'method': 'automated recognition only; no audio was subjectively heard', 'model': a.model,
              'faster_whisper_version': importlib.metadata.version('faster-whisper'),
              'ctranslate2_version': importlib.metadata.version('ctranslate2'),
              'options': options, 'source_or_name_prompt_supplied': False, 'lines': results,
              'preprocessing': 'FFmpeg decoded PCM to mono16kHz float32 documented waveform input; no text supplied',
              'normalized_exact_lines': sum(not r['differences'] for r in results), 'line_count': len(results)}
    if not a.names_only and not a.review_from and not a.clips_only:
        path = a.package / 'assets/ch/005/audio.mp3'
        segments, info = model.transcribe(decode(path), **{**options, 'vad_filter': True})
        output['full_mp3'] = {'segments': [dataclasses.asdict(s) for s in segments],
                              'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        output['full_mp3']['recognized'] = ' '.join(s['text'].strip() for s in output['full_mp3']['segments'])
        output['full_mp3']['differences'] = differences(' '.join(l['text'] for l in source_for_full_track), output['full_mp3']['recognized'])
    a.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print('COMPLETE', len(results), output['normalized_exact_lines'], flush=True)


if __name__ == '__main__':
    main()
