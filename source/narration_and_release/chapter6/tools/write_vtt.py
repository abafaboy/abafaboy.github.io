#!/usr/bin/env python3
"""Write exact-source captions only from complete measured Chapter 6 timing."""
import argparse
import json
from pathlib import Path


def timestamp(samples, rate):
    milliseconds = round(samples * 1000 / rate)
    seconds, ms = divmod(milliseconds, 1000)
    minutes, sec = divmod(seconds, 60)
    hours, minute = divmod(minutes, 60)
    return f'{hours:02d}:{minute:02d}:{sec:02d}.{ms:03d}'


def write_vtt(package, timing_path, output):
    package = Path(package)
    timing = json.loads(Path(timing_path).read_text())
    source = json.loads((package / 'timing/dialogue.json').read_text())['lines']
    lines, rate = timing['lines'], timing['sample_rate']
    if timing.get('test_only') or len(lines) != len(source) or len(lines) != 65 or rate != 24000:
        raise ValueError('Requires complete measured timing for 65 real recordings')
    result, previous = ['WEBVTT', ''], -1
    for line, original in zip(lines, source):
        if any(line.get(k) != original[k] for k in ['id', 'speaker', 'text']):
            raise ValueError('Timing differs from approved source')
        start, end = line['start_sample'], line['end_sample']
        if not (type(start) is int and type(end) is int and previous <= start < end <= timing['duration_samples']):
            raise ValueError('Invalid measured interval')
        previous = end
        result.extend([line['id'], f'{timestamp(start, rate)} --> {timestamp(end, rate)}',
                       f'{line["speaker"]}: {line["text"]}', ''])
    output = Path(output)
    if output.exists():
        raise ValueError('Output must be a new file')
    output.write_text('\n'.join(result) + '\n', encoding='utf-8')
    return {'captions': len(lines), 'output': str(output)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--timing', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(write_vtt(args.package, args.timing, args.output), indent=2))
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + '\n')
