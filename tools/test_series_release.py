import json
from pathlib import Path
import tempfile
import unittest

from PIL import Image
from series_release import prepare_release, validate_release


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "bundle"
        self.output = self.root / "site"
        self.source.mkdir()
        self.manifest = self.source / "series.json"
        self.data = {"schema_version": 1, "slug": "test-series", "title": "Reader test", "chapters": [{"n": 1, "title": "First", "width": 1080, "segments": [["001.webp", 2400]]}]}
        self.write_bundle()

    def write_bundle(self):
        for chapter in self.data["chapters"]:
            directory = self.source / f"ch/{chapter['n']:03d}"
            directory.mkdir(parents=True, exist_ok=True)
            for name, height in chapter["segments"]:
                if "/" not in name:
                    Image.new("RGB", (chapter["width"], height), "#20242a").save(directory / name)
        self.manifest.write_text(json.dumps(self.data))

    def test_visual_release_without_audio_and_referenced_files_only(self):
        (self.source / "private-notes.txt").write_text("Must remain outside the site")
        target = prepare_release(self.manifest, self.output)
        _, assets = validate_release(target)
        self.assertEqual(list(assets), ["ch/001/001.webp"])
        self.assertFalse((target.parent / "private-notes.txt").exists())
        self.assertEqual((self.source / "ch/001/001.webp").read_bytes(), (target.parent / "ch/001/001.webp").read_bytes())

    def test_append_preserves_existing_chapter_and_rejects_replacement(self):
        target = prepare_release(self.manifest, self.output)
        original = (target.parent / "ch/001/001.webp").read_bytes()
        self.data["chapters"][0].update(n=2, title="Second")
        self.write_bundle()
        prepare_release(self.manifest, self.output)
        self.assertEqual([1, 2], [c["n"] for c in validate_release(target)[0]["chapters"]])
        self.assertEqual(original, (target.parent / "ch/001/001.webp").read_bytes())
        before = target.read_bytes()
        with self.assertRaisesRegex(ValueError, "cannot be replaced"):
            prepare_release(self.manifest, self.output)
        self.assertEqual(before, target.read_bytes())

    def test_missing_or_incorrect_assets_rejected_before_staging(self):
        (self.source / "ch/001/001.webp").unlink()
        with self.assertRaisesRegex(ValueError, "Missing or unsafe"):
            prepare_release(self.manifest, self.output)
        self.assertFalse(self.output.exists())
        self.write_bundle()
        Image.new("RGB", (540, 1200)).save(self.source / "ch/001/001.webp")
        with self.assertRaisesRegex(ValueError, "dimensions"):
            validate_release(self.manifest)

    def test_path_traversal_and_private_schema_fields_rejected(self):
        self.data["chapters"][0]["segments"][0][0] = "../../private.webp"
        self.manifest.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, "plain filename"):
            validate_release(self.manifest)
        self.data["chapters"][0]["segments"][0][0] = "001.webp"
        self.data["future_plot"] = "Not release metadata"
        self.manifest.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, "unsupported fields"):
            validate_release(self.manifest)

    def test_no_empty_or_out_of_sequence_release(self):
        self.data["chapters"] = []
        self.manifest.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, "finished chapter"):
            prepare_release(self.manifest, self.output)
        self.data["chapters"] = [{"n": 2, "title": "Second", "width": 1080, "segments": [["001.webp", 2400]]}]
        self.write_bundle()
        with self.assertRaisesRegex(ValueError, "consecutively"):
            prepare_release(self.manifest, self.output)

    def test_narration_cues_preserve_exact_image_anchors(self):
        self.data['chapters'][0]['audio'] = {'file': 'voice.wav', 'duration': 20, 'cues': [
            {'t': 0, 'segment': '001.webp', 'y': 0},
            {'t': 5, 'segment': '001.webp', 'y': 1200, 'panel': 1, 'line': 2}]}
        # Asset validation is separate from native media playback tests.
        (self.source / 'ch/001/voice.wav').write_bytes(b'test-only asset')
        self.write_bundle()
        target = prepare_release(self.manifest, self.output)
        released, assets = validate_release(target)
        self.assertEqual(released['chapters'][0]['audio'], self.data['chapters'][0]['audio'])
        self.assertIn('ch/001/voice.wav', assets)

    def test_invalid_narration_timing_and_positions_are_rejected(self):
        first = {'t': 0, 'segment': '001.webp', 'y': 100}
        bad_cues = [
            [],
            [{'t': 1, 'segment': '001.webp', 'y': 0}],
            [first, {'t': 0, 'segment': '001.webp', 'y': 200}],
            [first, {'t': 21, 'segment': '001.webp', 'y': 200}],
            [first, {'t': 2, 'segment': 'missing.webp', 'y': 200}],
            [first, {'t': 2, 'segment': '001.webp', 'y': 2401}],
            [first, {'t': 2, 'segment': '001.webp', 'y': 0}],
            [first, {'t': 2, 'segment': '001.webp', 'y': 200, 'panel': False}],
        ]
        for cues in bad_cues:
            with self.subTest(cues=cues):
                self.data['chapters'][0]['audio'] = {'file': 'voice.wav', 'duration': 20, 'cues': cues}
                self.write_bundle()
                with self.assertRaises(ValueError):
                    validate_release(self.manifest)

    def test_gutters_reference_only_current_segments_and_preserve_image_bytes(self):
        self.data['chapters'][0]['gutters'] = {'001.webp': 220}
        self.write_bundle()
        original = (self.source / 'ch/001/001.webp').read_bytes()
        target = prepare_release(self.manifest, self.output)
        self.assertEqual((target.parent / 'ch/001/001.webp').read_bytes(), original)
        for gutters in [{'missing.webp': 20}, {'001.webp': -1}, {'001.webp': True}, {'001.webp': 1001}]:
            self.data['chapters'][0]['gutters'] = gutters
            self.write_bundle()
            with self.assertRaisesRegex(ValueError, 'gutter'):
                validate_release(self.manifest)


if __name__ == "__main__":
    unittest.main()
