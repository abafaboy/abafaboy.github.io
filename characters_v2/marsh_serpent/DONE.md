# M4 — marsh serpent — DONE

27 October 2026. Drawing complete; candidate delivery for Claude's review. No shared approval state was changed.

## Delivered

- `front.png` — the front master, full coiled creature; attempt 3.
- `turnaround.png` — full coiled length from the side, frontal head/hood, head profile; attempt 1.
- `details.png` — paired horns, yellow slit pupil, jade scales with gold banding, small ash-leaking brow crack, and frost forming on scales; attempt 1.
- `scale.png` — rearing beside a two-storey market building and a pedestrian footbridge, with one ordinary 178 cm scale person; attempt 5, best of five with faults below.
- `card.json` — identity, design dimensions, palette, locks and file map.
- `prompts.json` — exact prompts, references, source paths, attempt decisions, rejection reasons and C: free-space checks for all ten image calls.
- `DONE.md` — this completion report.

All four kept images and all six rejects are native 1536 × 1024 PNGs copied byte-for-byte from the built-in image_gen.imagegen output. SHA-256 hashes match their generator originals. None was resized, retouched, sharpened, re-encoded, made into a shortcut or hard-linked. Windows hard-link inventory returned exactly one file name for each saved PNG.

## Review result and remaining faults

The front, turnaround and details passed my visual checks for drawn cel finish, creature continuity, two horns, yellow slit pupils, jade/gold palette, the small Hush crack and the required detail coverage. Sheets contain no human scale silhouette or text. The profile clarifies that the horns sweep toward the rear of the skull. The unspecified belly was resolved as muted pale-ochre scutes.

**The scale scene is not a clean metric-scale pass.** Following README_START_HERE.md's 27 October rule 3, I stopped after five attempts and kept the strongest overall version under the normal filename.

Remaining scale-scene faults:
- The thickest ground segment still reads somewhat too thick against the adult; the intended diameter is 1.5 m, or about 84% of the adult's 178 cm height.
- The footbridge deck visually reads lower than the intended 5 m road clearance. The building and comparison person also do not share a perfectly unambiguous depth plane, so the six-metre facade comparison is approximate.
- The raised silhouette reads around third-floor height, but the exact nine-metre scene target and twenty-metre body centreline cannot be certified from the posed image. Design values in card.json remain authoritative.

No further images remain to draw for M4. The scale faults are left explicitly for Claude's review under the five-try rule; there was no sixth attempt.

Inspected each result at full size, then a 200 px-wide thumbnail of every kept image and selected ink/scale/frost/bridge crops at 200%. The QA composites existed only in memory: no previews or temporary images were saved in the project. No obvious lossy compression blocks, colour bleeding or upscaling artifacts appeared.

## Rejects saved as ordinary PNG files

- `characters_v2/_rejects/marsh_serpent_front_try1_rendered_scale_shading.png` — bevelled per-scale rendering.
- `characters_v2/_rejects/marsh_serpent_front_try2_long_brow_fissure.png` — long brow split and busy scale shading.
- `characters_v2/_rejects/marsh_serpent_scale_try1_trunk_too_thick.png` — excessive trunk girth.
- `characters_v2/_rejects/marsh_serpent_scale_try2_perspective_comparison.png` — unreliable foreground scale-person comparison.
- `characters_v2/_rejects/marsh_serpent_scale_try3_oversized_comparison_person.png` — person oversized against the facade.
- `characters_v2/_rejects/marsh_serpent_scale_try4_bulging_ground_coils.png` — ground coils too thick and facade receding.

## References and disk guard

Read README_START_HERE.md and the applicable files in its reading order, ASSETS_ARC2_BRIEF.md M4, MODEL_SHEETS_BRIEF.md sections 1–3, PANEL_BRIEF_v2.md sections 2 and 4b, style-test notes, reviews/STATUS.md and reviews/L9.md. Applied the 27 October overrides first.

Front attempts had no image references. Every subsequent call used the passed front as reference one. Turnaround and details used only this entry's new sheets. Scene references were the approved L9 market/footbridge keys; later retries used only the footbridge plus the front. No call used more than three references. No rejected image, retired art or outside image was used as an input.

Ran Get-PSDrive C before every image call. Available space before drawing ranged from approximately 42.18 to 39.36 GiB, always above the 3 GB stop threshold. Final verification found approximately 39.03 GiB free. No low-space stop was triggered.

All project writes were confined to characters_v2/marsh_serpent/ and this entry's six named PNGs in characters_v2/_rejects/. Other chats' folders and shared source/review files were untouched. Nothing was published or uploaded.

Stopping here as requested.
