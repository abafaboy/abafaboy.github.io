# S16 Borro — INCOMPLETE / REVIEW REQUIRED

No image in this delivery is approved. The set is blocked after the three allowed front-sheet attempts. This DONE file records the execution outcome; it does not certify the entry as finished or ready for chapter use.

- Built-in image_gen calls completed: 3. No call remains in flight; no executor/quota error occurred.
- `front.png`: final failed attempt, untouched 1536×1024 PNG, supplied for Claude review only.
- `_rejects/borro_front_01_scale_background.png`, `_rejects/borro_front_02_scale_strap.png`, `_rejects/borro_front_03_scale_final.png`: all three untouched native attempts. The third is byte-identical to `front.png`.
- `prompts.json`: exact requests, ordered approved reference paths/hashes, generator source paths and per-attempt results.
- `review.json`: strict self-QA and native-pixel measurements; this is not Claude approval.
- `card.json`: design/height/palette/lock metadata from the approved written brief.
- `SHA256SUMS`: hashes of every other file in this folder.

## Exact blocker

The front reference did not pass. The 178 cm silhouette should be 178/240 = 0.74167 of Borro's crown-to-sole height. Measured attempts are approximately 0.595, 0.702 and 0.668 (manual anatomical landmarks, native-pixel silhouette masks). The final silhouette is about 10% too short; the final shield is about 0.796 of Borro's height instead of 0.833, and its width/height is about 0.467 instead of 0.5. All candidates also have subtly varying backgrounds rather than an exact flat #E9E9EC fill. Attempt 2 adds an incorrect diagonal satchel shoulder strap; attempt 3 removes that strap.

The front's overall gentle face, small head, long arms, short thick legs, shell, moss/flowers and gardener outfit are visible, but cloth/stone texture and the partly occluded shield-grip hand still need Claude's strict review. Nothing has been pixel-cleaned or silently normalized.

`MODEL_SHEETS_BRIEF.md` section 2 says: “Make the front view first. When it passes, pass it as the reference image for the other views, the expressions, the details and the chibi sheet.” None passed. The three-total-try cap is exhausted. Therefore `turnaround.png`, `expressions.png`, `details.png` and `chibi.png` were not generated: building them from a failed front or making a fourth front would bypass the rules. Await Claude's exact verdict/redo instruction.

## References and preservation

Every call attached five inspected original approved Arc 1 PNGs: `summon_silhouettes.png`, `kang_jaeha/front.png`, `stone_lizard/turnaround.png`, plus `style_test_v2/acting/A3_P23.png` and `B3_P29.png`. They cover Borro's existing silhouette, house figure/cloth drawing, inked matte slate, and two acting/style anchors. No generated S16 attempt was ever used as a reference. No S2b image, retired art, rejected source, outside webtoon image or font was used.

All four delivered PNG files are byte-for-byte copies of three original generator outputs; the source originals remain in `/workspace/generated_images/`. No resizing, converting, PNG re-save, compositing, retouching or thumbnail creation occurred. Each decodes as a native 1536×1024 RGB PNG.

Delivery is restricted to `inbox/S16/` plus one `INBOX.md` line on `msgf-art`. Canonical approved art, main, all other entries, bible, scripts and briefs are untouched. Stop here for Claude verdict; this is an incomplete review delivery, not a completed S16 set.
