# P5 Lyra acting sheets — R2 correction, 25 October 2026

Claude's strict review, relayed by the user: **talking.png passes; acting poses 1 and 3–6 pass.** Pose 2 failed handedness rule 11b.10 and was the only pose redrawn in this revision.

**acting.png:** pose 2 now aims picture-right in a viewer-facing three-quarter stance. Her LEFT arm extends right with the silver bracer and bare bow hand. Her gloved RIGHT hand draws the blue string to her right cheek on picture-left. The braid and navy chest guard remain on her LEFT, picture-right; the quiver remains at her RIGHT hip, picture-left; the flute remains in her sash. Her face, revealing approved outfit and glamour are retained. Checked visually at full size and in the assembled sheet.

Used one built-in image_gen redraw from a crop of the failed pose, with the approved front, expressions and details as design references. Resampled only the generated slot into its original bounds: `(512, 0, 512, 524)` on the 1536×1024 sheet. Protected the small pose-5 hair overlap at `(720, 516, 184, 8)`.

**Pixel verification:** 266,597 changed pixels inside pose 2's replacement mask; **zero changed pixels outside it**. Poses **1, 3, 4, 5 and 6 are pixel-identical**, including the protected hair pixels. `talking.png`, `front.png`, `expressions.png`, `details.png`, `prompts.json` and `DONE.md` retain their previous SHA-256 hashes.

The old sheet was moved, byte-identically, to `characters_v2/_rejects/lyra_acting_r2_left_handed_draw.png`. Exact R2 prompt, reference paths, crop/composite bounds, visual checks, pixel counts and before/after hashes are recorded under `round_2` in `acting_prompts.json`; earlier generation history is preserved. The corrected pose was locally checked; no external re-review is claimed.

