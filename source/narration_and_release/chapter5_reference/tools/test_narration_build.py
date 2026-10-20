"""Synthetic audio is test-only and exists solely in temporary directories."""
import json
import math
from pathlib import Path
import struct
import subprocess
import tempfile
import unittest
import wave

from build_narration import build, RATE, write_json

PACKAGE = Path(__file__).resolve().parents[1]


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='ch5-audio-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        lines = json.loads((PACKAGE / 'timing/dialogue.json').read_text())['lines']
        self.cast = {'cast': {s: {'engine': 'TEST_ONLY_fixture', 'voice_id': 'TEST_ONLY_' + s,
                                 'settings': {}, 'evidence': 'Synthetic test fixture, never release audio'} for s in {l['speaker'] for l in lines}}}
        tone = self.root / 'test-tone.wav'
        with wave.open(str(tone), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
            w.writeframes(b''.join(struct.pack('<h', int(2000 * math.sin(2 * math.pi * 220 * i / RATE))) for i in range(RATE // 10)))
        self.records = {'recordings': [{**{k: line[k] for k in ['id', 'speaker', 'text']},
                                       **{k: self.cast['cast'][line['speaker']][k] for k in ['engine', 'voice_id', 'settings']},
                                       'wav': tone.name} for line in lines]}
        self.pacing = {'intro_seconds': .8, 'line_gap_seconds': .35, 'panel_gap_seconds': .65,
                       'silent_panel_seconds': 1.8, 'outro_seconds': 1.2, 'screen_text_policy': 'visual-only', 'test_only': True}
        self.pacing['panel_extra_visual_hold_seconds'] = {'36': 3.0}

    def run_build(self):
        for name, data in [('cast.json', self.cast), ('recordings.json', self.records), ('pacing.json', self.pacing)]:
            write_json(self.root / name, data)
        return build(PACKAGE, self.root / 'cast.json', self.root / 'recordings.json', self.root / 'output', self.root / 'pacing.json')

    def test_complete_measured_cues_and_holds(self):
        result = self.run_build()
        self.assertEqual(result['dialogue_recordings'], 56)
        self.assertEqual(result['panels'], 38)
        self.assertEqual(result['silent_panels'], 8)
        manifest = json.loads((self.root / 'output/series.json').read_text())
        chapter = manifest['chapters'][0]
        cues = chapter['audio']['cues']
        lines = json.loads((self.root / 'output/timing.private.json').read_text())['lines']
        with wave.open(str(self.root / 'output/ch/005/audio.wav'), 'rb') as wav:
            self.assertEqual(wav.getnframes(), round(result['duration_seconds'] * RATE))
            expected_bytes = wav.getnframes() * 2
        decoded = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(self.root / 'output/ch/005/audio.mp3'),
                                  '-f', 's16le', '-acodec', 'pcm_s16le', '-'], stdout=subprocess.PIPE, check=True).stdout
        self.assertEqual(len(decoded), expected_bytes, 'MP3 must be the newly assembled audio, not a previous copy')
        self.assertEqual(cues[0]['t'], 0)
        self.assertTrue(all(b['t'] > a['t'] for a,b in zip(cues, cues[1:])))
        for line in lines:
            for t in ['start', 'end']:
                self.assertTrue(any(c['t'] == line[t] and c.get('panel') == line['panel'] and c.get('line') == line['line'] and c['y'] == line['focus_y'] for c in cues))
        self.assertEqual({c['panel'] for c in cues if 'panel' in c}, set(range(1,39)))
        phone_holds = [c for c in cues if c.get('panel') == 36 and 'line' not in c]
        phone_bottom, phone_hold_end = phone_holds[-2:]
        self.assertEqual(phone_bottom['y'], phone_hold_end['y'])
        self.assertEqual(phone_bottom['segment'], phone_hold_end['segment'])
        self.assertAlmostEqual(phone_hold_end['t'] - phone_bottom['t'], 3.0)
        next_panel_top = next(c for c in cues if c.get('panel') == 37 and 'line' not in c)
        self.assertAlmostEqual(next_panel_top['t'] - phone_hold_end['t'], self.pacing['panel_gap_seconds'])
        print('TEST_FIXTURE_RESULT', json.dumps(result, sort_keys=True))

    def test_unverified_voice_is_rejected(self):
        self.cast['cast']['TAEO']['voice_id'] = None
        with self.assertRaisesRegex(ValueError, 'Missing established voice_id'):
            self.run_build()
        self.assertFalse((self.root / 'output').exists())

    def test_wrong_text_is_rejected(self):
        self.records['recordings'][0]['text'] = 'An obsolete chapter line'
        with self.assertRaisesRegex(ValueError, 'Source mismatch'):
            self.run_build()

    def test_missing_line_is_rejected(self):
        self.records['recordings'].pop()
        with self.assertRaisesRegex(ValueError, 'Exactly 56'):
            self.run_build()

    def test_screen_policy_must_be_explicit(self):
        del self.pacing['screen_text_policy']
        with self.assertRaisesRegex(ValueError, 'Explicit screen_text_policy'):
            self.run_build()

    def test_no_silent_placeholder(self):
        path = self.root / 'test-tone.wav'
        with wave.open(str(path), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(RATE * 2))
        with self.assertRaisesRegex(ValueError, 'Silent placeholder'):
            self.run_build()

    def test_existing_work_is_preserved(self):
        (self.root / 'output').mkdir()
        (self.root / 'output/keep').write_text('original')
        with self.assertRaisesRegex(ValueError, 'existing work is preserved'):
            self.run_build()
        self.assertEqual((self.root / 'output/keep').read_text(), 'original')


if __name__ == '__main__':
    unittest.main()
