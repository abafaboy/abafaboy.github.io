#!/usr/bin/env python3
"""Assemble verified per-line recordings and measured Follow cues, privately.

No TTS service, model, credential, repository writer, or deployment is invoked.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import struct
import subprocess
import wave

RATE = 24000


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def build(package, cast_file, recordings_file, output, pacing_file):
    package = Path(package).resolve(strict=True)
    output = Path(output).resolve()
    require(not output.exists(), 'Output must be a new directory; existing work is preserved')
    source = read_json(package / 'timing/dialogue.json')['lines']
    panels = read_json(package / 'timing/panels.json')
    visual = read_json(package / 'assets/series.visual-only.private.json')
    cast = read_json(cast_file)['cast']
    pacing = read_json(pacing_file)
    require(pacing.get('screen_text_policy') == 'visual-only',
            'Explicit screen_text_policy=visual-only is required for this 56-dialogue build; screen narration needs a separate verified plan')
    for field in ['intro_seconds', 'line_gap_seconds', 'panel_gap_seconds', 'silent_panel_seconds', 'outro_seconds']:
        require(type(pacing.get(field)) in (int, float) and math.isfinite(pacing[field]) and pacing[field] > 0,
                'Pacing needs positive finite ' + field)
    extra_holds = pacing.get('panel_extra_visual_hold_seconds', {})
    require(isinstance(extra_holds, dict), 'Extra visual holds must map source panel numbers to seconds')
    for number, seconds in extra_holds.items():
        require(number in {str(panel['panel']) for panel in panels} and type(seconds) in (int, float)
                and math.isfinite(seconds) and seconds >= 0, 'Invalid extra visual reading hold')
    speakers = {line['speaker'] for line in source}
    require(set(cast) == speakers, 'Cast must cover exactly the source speaker labels')
    for speaker, voice in cast.items():
        for field in ['engine', 'voice_id', 'evidence']:
            require(isinstance(voice.get(field), str) and voice[field].strip(), 'Missing established ' + field + ' for ' + speaker)
        require(isinstance(voice.get('settings'), dict), 'Missing settings for ' + speaker)
        require(not voice['voice_id'].startswith('TEST_ONLY') or pacing.get('test_only') is True,
                'Test voices cannot enter a real output')
    recordings_path = Path(recordings_file).resolve(strict=True)
    records = read_json(recordings_path)['recordings']
    require(len(records) == len(source) == 56, 'Exactly 56 per-line recordings are required')
    require(len({r['id'] for r in records}) == 56, 'Recording IDs must be unique')
    by_id = {r['id']: r for r in records}
    chunks = {}
    measurements = {}
    for line in source:
        require(line['id'] in by_id, 'Missing recording: ' + line['id'])
        rec = by_id[line['id']]
        voice = cast[line['speaker']]
        for field in ['speaker', 'text']:
            require(rec.get(field) == line[field], 'Source mismatch for ' + line['id'] + ': ' + field)
        for field in ['engine', 'voice_id', 'settings']:
            require(rec.get(field) == voice[field], 'Voice mismatch for ' + line['id'] + ': ' + field)
        path = (recordings_path.parent / rec['wav']).resolve(strict=True)
        require(path.is_file() and not Path(recordings_path.parent / rec['wav']).is_symlink(), 'Unsafe recording')
        with wave.open(str(path), 'rb') as wav:
            require((wav.getnchannels(), wav.getsampwidth(), wav.getframerate(), wav.getcomptype()) == (1, 2, RATE, 'NONE'),
                    'Recordings must be PCM16 mono 24000Hz: ' + line['id'])
            n = wav.getnframes()
            pcm = wav.readframes(n)
        require(n > 0 and len(pcm) == n * 2, 'Empty or truncated recording: ' + line['id'])
        peak = max(abs(v[0]) for v in struct.iter_unpack('<h', pcm))
        require(peak > 0, 'Silent placeholder recording: ' + line['id'])
        chunks[line['id']] = pcm
        measurements[line['id']] = {'samples': n, 'peak_pcm16': peak, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    by_line = {line['id']: line for line in source}
    timeline = []
    cues = []
    pcm_chunks = []
    sample = 0
    previous_y = -1
    offsets = {}
    total = 0
    for name, height in visual['chapters'][0]['segments']:
        offsets[name] = (total, height)
        total += height

    def pause(seconds):
        nonlocal sample
        count = round(seconds * RATE)
        pcm_chunks.append(bytes(count * 2))
        sample += count

    def cue(segment, y, panel=None, line=None):
        nonlocal previous_y
        top, height = offsets[segment]
        require(0 <= y <= height and top + y >= previous_y, 'Follow coordinates must be monotonic and within image bounds')
        value = {'t': sample / RATE, 'segment': segment, 'y': y}
        if panel is not None:
            value['panel'] = panel
        if line is not None:
            value['line'] = line
        if cues and cues[-1]['t'] == value['t']:
            require(cues[-1]['segment'] == segment and cues[-1]['y'] == y, 'Conflicting simultaneous Follow cues')
            cues[-1].update(value)
        else:
            cues.append(value)
        previous_y = top + y

    cue(visual['chapters'][0]['segments'][0][0], 0)
    # Match the published per-panel lead/hold/transition pattern.
    first_panel = True
    for panel in panels:
        ids = panel['lines']
        if not first_panel:
            cue(panel['segment'], panel['y_top'], panel['panel'])
        else:
            first_panel = False
        pause(pacing.get('dialogue_lead_seconds', pacing['intro_seconds']))
        if not ids:
            pause(pacing.get('silent_panel_holds', {}).get(str(panel['panel']), pacing['silent_panel_seconds']))
            cue(panel['segment'], panel['y_bottom'], panel['panel'])
        else:
            for index, id_ in enumerate(ids):
                line = by_line[id_]
                cue(line['segment'], line['focus_y'], line['panel'], line['line'])
                start = sample
                pcm_chunks.append(chunks[id_])
                sample += len(chunks[id_]) // 2
                cue(line['segment'], line['focus_y'], line['panel'], line['line'])
                timeline.append({**line, **measurements[id_], 'start_sample': start, 'end_sample': sample,
                                 'start': start / RATE, 'end': sample / RATE})
                pause(pacing['line_gap_seconds'] if index + 1 < len(ids) else pacing.get('panel_tail_seconds', pacing['panel_gap_seconds']))
            cue(panel['segment'], panel['y_bottom'], panel['panel'])
        extra_hold = extra_holds.get(str(panel['panel']), 0)
        pause(extra_hold)
        if extra_hold:
            cue(panel['segment'], panel['y_bottom'], panel['panel'])
        pause(pacing['panel_gap_seconds'])
    pause(pacing['outro_seconds'])
    cue(panels[-1]['segment'], panels[-1]['y_bottom'], panels[-1]['panel'])
    output.mkdir(parents=True)
    target = output / 'ch/005'
    shutil.copytree(package / 'assets/ch/005', target, ignore=shutil.ignore_patterns('audio.wav', 'audio.mp3'))
    with wave.open(str(target / 'audio.wav'), 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(RATE)
        for chunk in pcm_chunks:
            wav.writeframesraw(chunk)
    subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', str(target / 'audio.wav'),
                    '-codec:a', 'libmp3lame', '-b:a', '128k', str(target / 'audio.mp3')], check=True)
    chapter = visual['chapters'][0]
    chapter['audio'] = {'file': 'audio.mp3', 'duration': sample / RATE, 'cues': cues}
    write_json(output / 'series.json', visual)
    write_json(output / 'timing.private.json', {'sample_rate': RATE, 'duration_samples': sample, 'lines': timeline,
                                               'pacing': pacing, 'cast': cast, 'test_only': pacing.get('test_only', False)})
    from series_release import validate_release
    validate_release(output / 'series.json')
    result = {'dialogue_recordings': len(timeline), 'panels': len(panels), 'silent_panels': sum(not p['lines'] for p in panels),
              'cues': len(cues), 'duration_seconds': sample / RATE, 'test_only': pacing.get('test_only', False),
              'human_listening_qa': 'required; waveform and source matching do not establish pronunciation or performance'}
    write_json(output / 'build.private.json', result)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--cast', type=Path, required=True)
    parser.add_argument('--recordings', type=Path, required=True)
    parser.add_argument('--pacing', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.package, args.cast, args.recordings, args.output, args.pacing), indent=2))
    except (OSError, ValueError, KeyError, wave.Error, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')
