#!/usr/bin/env python3
"""Merge source-matched recordings into a fresh directory; never fill gaps."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import wave


def merge(package, manifests, output):
    package, output = Path(package).resolve(strict=True), Path(output).resolve()
    if output.exists():
        raise ValueError('Output must be a new directory')
    source = json.loads((package / 'timing/dialogue.json').read_text())['lines']
    cast = json.loads((package / 'voices/cast.json').read_text())['cast']
    found = {}
    for manifest in manifests:
        manifest = Path(manifest).resolve(strict=True)
        for record in json.loads(manifest.read_text())['recordings']:
            if record['id'] in found:
                raise ValueError('Duplicate source recording: ' + record['id'])
            path = manifest.parent / record['wav']
            if path.name != record['wav'] or path.is_symlink():
                raise ValueError('Unsafe recording path')
            if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
                raise ValueError('Recording hash mismatch: ' + record['id'])
            found[record['id']] = (record, path)
    if set(found) != {line['id'] for line in source}:
        missing = {line['id'] for line in source} - set(found)
        extra = set(found) - {line['id'] for line in source}
        raise ValueError(f'Incomplete source coverage; missing={sorted(missing)}, extra={sorted(extra)}')
    ordered = []
    for line in source:
        record, path = found[line['id']]
        voice = cast[line['speaker']]
        if any(record.get(k) != line[k] for k in ['speaker', 'text']):
            raise ValueError('Source mismatch: ' + line['id'])
        if not voice.get('voice_id') or not voice.get('settings'):
            raise ValueError('Unresolved voice: ' + line['speaker'])
        if any(record.get(k) != voice[k] for k in ['engine', 'voice_id', 'settings']):
            raise ValueError('Cast mismatch: ' + line['id'])
        with wave.open(str(path), 'rb') as wav:
            if (wav.getnchannels(), wav.getsampwidth(), wav.getframerate(), wav.getcomptype()) != (1, 2, 24000, 'NONE'):
                raise ValueError('Unexpected audio format: ' + line['id'])
            if wav.getnframes() != record['samples'] or record['samples'] <= 0:
                raise ValueError('Unexpected audio sample count: ' + line['id'])
        ordered.append(record)
    output.mkdir(parents=True)
    for record in ordered:
        shutil.copy2(found[record['id']][1], output / record['wav'])
        (output / (record['id'] + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    (output / 'recordings.json').write_text(json.dumps({'recordings': ordered}, ensure_ascii=False, indent=2) + '\n')
    return {'recordings': len(ordered), 'output': str(output)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--recordings', type=Path, action='append', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(merge(args.package, args.recordings, args.output), indent=2))
    except (OSError, ValueError, KeyError, wave.Error) as error:
        parser.exit(1, str(error) + '\n')
