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


if __name__ == "__main__":
    unittest.main()
