# Separate-series releases

The existing `/manhwa/` reader, assets, manifest, storage keys, narration, and
Follow behavior remain independent. Engagement is added through external
modules; the original reader's inline player/progress script stays unchanged.
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
requires `n`, `title`, `width`, and nonempty `segments`; `thumbnail` is optional. An optional `pdf` names a finished reading PDF beside the chapter images; the reader provides a download link. Publish flattened reading copies without embedded restricted fonts.
`width` and segment heights must match decoded image dimensions. Use PNG,
JPEG, or WebP; widths are at most 4096 px, and segments at most 10000 px tall.
Use plain filenames without paths. All chapters in the public manifest have
been released; never add future titles, outlines, scripts, or the story bible.
An optional `framing_height` gives the source-pixel span that narration must keep in view. The reader sizes its desktop column to that span while retaining a minimum comfortable reading width.

An optional `gutters` object maps segment filenames to spacing after the image
in pixels at the chapter width, for example `{"001.webp": 220}`. Spacing scales
with the reader width; the finished image bytes remain unchanged.

The new series release requires genuine character voiceover and synchronized
Follow as well as the improved, finished lettering. Keep its release held until
the final narration, image coordinates, and listening/Follow QA are complete.
The generic reader can still display visual-only chapters. Chapter narration is:

```json
"audio": {
  "file": "audio.mp3",
  "duration": 125.3,
  "cues": [
    {"t": 0, "segment": "001.webp", "y": 0},
    {"t": 4.2, "segment": "002.webp", "y": 160, "panel": 1, "line": 1},
    {"t": 9.6, "segment": "002.webp", "y": 920, "panel": 1}
  ]
}
```

`duration` is optional, in seconds. Native audio controls appear only when an
audio file is declared; playback never starts automatically. The controls stay
available while scrolling. Follow appears when validated cues are supplied and
starts enabled. A cue's `t` is the time in seconds at which its anchor should be
in view. `segment` is an exact filename from the chapter's segment list; `y` is
the focus point's distance from the top of that image in pixels at the manifest's
chapter width. Use the lower edge of a spoken text block so its full text remains
visible. The reader moves only as far as needed to reveal that focus point,
keeping a whole panel in view when it fits below the controls. `panel` and `line` are optional positive, one-based identifiers
for timing QA. They add no visible text. The example is schema documentation,
not a timing track for a release.

The first cue must start at zero. Times strictly increase; anchors follow
reading order and stay within the image bounds. Supply anchors for the final
spoken lines and panel transitions, measuring against the final lettered pages.
The reader interpolates between these anchors below the sticky controls. Hold
each spoken text focus from its actual line start to line end, then transition
to the next focus during the recorded pause. After the final line, focus the
panel's lower edge to complete the view if it is taller than the viewport.
Line-entry cues retain their one-based source lettering index.
Pausing stops movement; seeking catches up only while Follow is on. Wheel,
touch, keyboard, or scrollbar reading turns Follow off. Turning it on catches
up to the current narration position. A missing audio file reports the problem
without blocking visual reading. No placeholder or silent narration belongs in
a release. This release workflow leaves the original reader's playback logic
and progress storage keys unchanged.

Adding audio to an already released chapter needs a separately validated
manifest update; this append-only preparation tool intentionally refuses to
replace released chapter entries. Video can remain a separate export.

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
