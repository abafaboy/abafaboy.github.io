# Separate-series releases

The existing `/manhwa/` landing page, `manhwa/read.html`, assets, manifest,
storage keys, narration, and Follow behavior remain independent and unchanged.
The separate visual reader uses:

- Series: `/manhwa/series/?series=<slug>`
- Chapter: `/manhwa/series/read.html?series=<slug>&ch=1`
- Manifest: `/manhwa/series/<slug>/series.json`
- Images: `/manhwa/series/<slug>/ch/001/001.webp`, etc.

No series or chapters are registered by this preparation. Add the public
discovery link only with the first completed release.

## Finished-chapter input

Deliver a release bundle with `series.json` and the referenced assets in the
same relative tree shown below. Supply only finished, lettered vertical-webtoon
segments in reading order. A script or raw, unlettered panels are production
inputs, not a readable release. Do visual QA before preparing a release.

```json
{
  "schema_version": 1,
  "slug": "approved-series-slug",
  "title": "Approved public series title",
  "synopsis": "Optional approved, spoiler-free public description.",
  "chapters": [
    {
      "n": 1,
      "title": "Approved public chapter title",
      "width": 1080,
      "segments": [["001.webp", 2400], ["002.webp", 1800]],
      "thumbnail": "thumb.webp"
    }
  ]
}
```

Only `schema_version`, `slug`, `title`, and `chapters` are required at series
level. A series-level `cover` may name an image beside `series.json`. A chapter
requires `n`, `title`, `width`, and nonempty `segments`; `thumbnail` is optional.
`width` and segment heights must match decoded image dimensions. Use PNG,
JPEG, or WebP; widths are at most 4096 px, and segments at most 10000 px tall.
Use plain filenames without paths. All chapters in the public manifest have
been released; never add future titles, outlines, scripts, or the story bible.

Audio and video are not required. Optional chapter narration is:

```json
"audio": {"file": "audio.mp3", "duration": 125.3}
```

`duration` is optional, in seconds. Native audio controls appear only when an
audio file is declared; playback never starts automatically. The new reader
does not implement narration-driven Follow yet. Adding it later requires an
explicit keyframe schema and tests for user scrolling and toggling. It must
not change the old reader. Adding audio to an already released chapter needs
a separately validated manifest update; this append-only preparation tool
intentionally refuses to replace released chapter entries. Video can remain
a separate export.

## Materialize in the consuming cloud workspace

Upstream local paths are not shared with this executor. Supply Library file
references: exact `library_file_id`, `file_id`, filename, and version where
available, plus expected sizes/SHA-256 hashes for the release bundle or assets.
One ZIP containing the public release tree is convenient; inspect archive
members and reject traversal/symlinks before extraction outside the repository.

Use the current ChatGPT Library skill. For a resolved Library reference, use
the available `library_prepare_materialize` tool and the skill's current
`library_file_transfer.py` helper. Retain the complete transfer objects and
Library identity, and apply returned xattrs. For list/search results, use the
skill's current `library_download.py` helper with the complete result instead.
Do not transfer signed URLs manually or reuse another executor's local paths.

The consuming executor must check that files actually exist in its own
workspace, inspect their byte counts and SHA-256 hashes, compare any supplied
expected values, and retain Library/version provenance outside the public
repository. A preparation response or upstream download is not proof that
local bytes exist. Treat materialization as unverified until readable local
bytes and their hashes have actually been checked.

## Local preparation and release checks

```bash
python3 tools/series_release.py validate /workspace/release-input/series.json
python3 tools/series_release.py prepare /workspace/release-input/series.json
python3 tools/series_release.py validate manhwa/series/approved-series-slug/series.json
python3 -m unittest discover -s tools -p 'test_series_*.py'
```

The preparation tool copies only referenced public assets, verifies their
copied bytes, and emits asset hashes and sizes. It appends consecutive finished
chapters; it refuses to overwrite released chapters or conflicting assets.
Existing chapter files remain untouched. The updated manifest is installed
last. Review the diff and all finished pages on a phone-sized viewport before
committing the release; never commit a temporary fixture or private notes.

Use the environment's existing native HTTPS Git origin. Branch creation has
been verified with an actual push; GitHub CLI API requests returned Forbidden.
Do not change credentials or permissions or substitute a denied connector.
Main-branch writes and a successful Pages deployment require their own actual
evidence. A branch push, dry run, or local preview does not establish deployment.
