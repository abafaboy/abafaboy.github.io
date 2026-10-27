# M6 — basalt boar — DONE

27 October 2026. Chapter 15. Built-in `image_gen.imagegen` mode.

Completed under the README's 27 October five-try fallback. **The turnaround is not a clean proportion pass; its remaining fault is below.** Awaiting Claude's review, with no change to the shared review board.

## Deliverables

- `front.png` — checked near-frontal full-body design anchor; attempt 4.
- `turnaround.png` — front, three-quarter, side and back in one horizontal row on one baseline; best native-size attempt 4 after five tries.
- `details.png` — basalt slab/bristles, the pair of obsidian tusks, and the small violet brow Hush crack; attempt 1.
- `charge.png` — lowered-head straight-line charge in the written-design aqueduct, with a generic 178 cm adult silhouette in the scene; attempt 3.
- `card.json` — design dimensions, palette, locks, review notes, selected-image hashes and file verification.
- `prompts.json` — all 13 exact prompts, reference paths and version hashes where needed, per-call free-space records, selection/rejection reasons and generator source paths.
- `DONE.md` — this report.

All four kept images are original **1536×1024 PNGs**, byte-identical to the generator originals. Every kept image and all nine rejects are ordinary files with link count 1: no hard links, shortcuts, resizing, re-encoding or retouching. Native PNG signatures and SHA-256 source/copy equality were verified for all 13 files.

## Remaining faults and review points

1. **Turnaround:** after five tries, the selected single-row profile remains too short for the specified 5 m nose-to-rump length against 2.5 m shoulder height: visually about **1.6–1.7:1**, rather than 2:1. It also has large empty vertical margins. Attempt 2 had a longer body but used two rows with apparent scale variation; attempt 5 returned the wrong native dimensions (2172×724). Attempt 4 was kept as the best correctly sized, single-baseline option. No sixth try was made.
2. `front.png` is near-frontal rather than perfectly orthographic. The creature's design, four legs, cloven hooves, two uninterrupted black obsidian tusks, red-brown eyes and small violet brow crack are clear.
3. `charge.png` shows the lowered-head tell and an approximate correct creature/person scale relationship. A single unlettered still cannot independently establish an exact count of three strides before impact.
4. Charge used turnaround candidate 2 while it was provisionally checked for creature design. It was later rejected for its sheet layout during final QA. The exact image hash and its archived path are preserved in `prompts.json`; no image already marked rejected was attached to a later generation call.

## Rejects

Saved unchanged in `characters_v2/_rejects/`, using only the `basalt_boar_` prefix:

- `basalt_boar_front_attempt01_rendered_texture_cropped_bristles.png`
- `basalt_boar_front_attempt02_tusk_cuffs_oblique_view.png`
- `basalt_boar_front_attempt03_cropped_crest_rendered_snout.png`
- `basalt_boar_turnaround_attempt01_short_profile_touching_views.png`
- `basalt_boar_turnaround_attempt02_two_rows_scale.png`
- `basalt_boar_turnaround_attempt03_short_profile.png`
- `basalt_boar_turnaround_attempt05_wrong_dimensions.png`
- `basalt_boar_charge_attempt01_blur_cropped_hindleg_busy_scene.png`
- `basalt_boar_charge_attempt02_clipped_rear_hoof_scale.png`

## Checks and scope

Read README_START_HERE.md with the 27 October overrides first; the story bible, Arc 3–4 beats, names, style guide, art direction, character designs and ASSETS_ARC3_BRIEF.md reading sequence; MODEL_SHEETS_BRIEF.md 1–3, PANEL_BRIEF_v2.md 4b, the style-test report, applicable art-bible guidance and reviews/STATUS.md.

The first reference for every dependent image was this entry's checked front. At most two references were used in a call. No external artwork, retired images or another chat's unapproved files were used. No scale silhouette appears on the front, turnaround or details sheets; the charge scene retains its human scale figure.

`Get-PSDrive C` was checked before **every one of the 13 image calls**. The lowest reading was **36.839 GiB**, above the 3 GB stop threshold. Final metadata verification found **40.722 GiB** free. Disk space did not stop drawing.

Kept images were inspected at native size, as in-memory 200 px thumbnails and with in-memory 200% crops. No preview or temporary image files were saved in the project. Project writes were confined to `characters_v2/basalt_boar/` and this entry's nine rejects in `characters_v2/_rejects/`. No other chat's folder or shared brief was edited. No publication or upload was performed.

Drawing stopped. The documented turnaround proportion fault remains for Claude's review under the five-try rule.

