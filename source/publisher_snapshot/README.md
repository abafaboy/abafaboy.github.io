# Published edition snapshot

Frozen settings from the publisher workspace for revised Chapters 1–7 at repository commit `fb4b585a8fb47f24b2d98b7d0122b4f7ac12f9a1`. These files add the exact lettering placements, current release validator and final public Follow timing to the recovered production collection. This handoff does not resume production or change the live reader.

## Reading these files

- `ch001/` through `ch007/` contain the publisher's `lettering_script.json`, `layout_config.json` and final `placement_manifest.json`. They record crop/scale, protected face boxes, text boxes, glyph bounds, tails and original-art hashes. The lettering JSON for all seven chapters matches the recovered collection byte for byte; layout JSON also matches except Chapter 7, whose publisher copy uses portable selected-art filenames and a separately acquired font.
- `ch007/selected_art_index.json` maps the publisher's selected-art names to original archive member names and SHA-256 hashes. Private Library lookup identifiers were omitted. The raw image files themselves are not in this source supplement.
- Chapter 1–2 `narration_recipes.json` preserves actual line recipes, engine, voice/language/speed, phonemes and constant gains. Chapter 3–7 `cast.json` and `pronunciations.json` preserve synthesis settings and casting direction. Coordination evidence was removed from the exported cast settings. These are settings, not recordings or a claim of a subjective audition.
- `published_series_manifest.json` is the byte-exact public manifest snapshot. Its relative asset paths resolve from repository `manhwa/series/my-summons-go-first/`, not from this source folder. Use it to inspect the final edition, top masks, gutters, audio durations and Follow camera cues. It is not a standalone release bundle. Final reader camera cues can differ from authoring bubble-focus coordinates in placement files.
- `tools/series_release.py` is the publisher's later implementation, including edition and top-mask preservation. Prefer it over the historical Chapter 5 copy when comparing release behavior.

Older layout files may retain intermediate hold annotations or original workspace paths. Their presence does not make an old candidate current. The published manifest, final placement source hashes and selected-art mapping identify the frozen published result. Chapters 8–10 are not part of this published snapshot.

## Release helper

Requires Python with `pathlib.Path.is_relative_to` support and Pillow. From the repository root, this read-only command validates the existing published assets:

```sh
python source/publisher_snapshot/tools/series_release.py validate manhwa/series/my-summons-go-first/series.json
```

For a future finished bundle, after production is separately resumed, its staging interface is:

```sh
python source/publisher_snapshot/tools/series_release.py validate /path/to/finished-bundle/series.json
python source/publisher_snapshot/tools/series_release.py prepare /path/to/finished-bundle/series.json --output-root /path/to/staging/manhwa/series
```

`validate` checks schema/allowed keys, safe filenames, image dimensions and readability, referenced asset existence and hashes, chapter order, gutters/masks and narration/cue bounds. `prepare` first validates, then stages referenced assets and an appended manifest. It requires consecutive chapters, preserves edition, rejects replacing released chapter directories, verifies copied bytes and protects against the manifest changing during staging. It does not generate art/audio, run Git, or deploy Pages. The JSON report includes referenced asset sizes and SHA-256 hashes; it does not assert subjective visual/audio quality or supply missing source files. Do not pass the whole `source/` collection as a release bundle.

The chapter-specific lettering builders remain in `revised_production/`. Rebuilding pixels also requires the exact accepted native art and properly licensed local fonts; this handoff deliberately omits the bulk art/audio binaries and font programs. No rebuild or chapter publication was performed for the handoff.
