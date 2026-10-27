# M1 ash rats / swarm mother — INCOMPLETE, REVIEW REQUIRED

No image is approved. Three front-reference attempts completed; all failed self-QA. This DONE records the stopped execution and review delivery, not completion of the M1 asset set.

## Files

- `front.png`: final failed front reference, untouched native 1536×1024 PNG, review only.
- `_rejects/ash_rat_front_01_hip_scale_high_camera.png`: first attempt, rat too large and high apparent camera.
- `_rejects/ash_rat_front_02_threequarter_scale.png`: second attempt, still too large and three-quarter view.
- `_rejects/ash_rat_front_03_scale_final.png`: third attempt, still too large; byte-identical to `front.png`.
- `prompts.json`: exact generation requests, ordered approved reference paths and SHA256 hashes, outputs and reviews.
- `review.json`: per-image self-QA, approximate native-pixel scale checks and blocker.
- `card.json`: brief-grounded identity, size, palette and design locks.
- `SHA256SUMS`: hashes of every other delivered file.

## Exact blocker and missing work

The ordinary ash rat must be about 70 cm nose-to-rump plus a hairless tail, **knee-high** beside a 178 cm adult (`CHARACTER_DESIGNS_v2.md` 4b.1; `PANEL_BRIEF_v2.md` chapter 6). Its highest back is visibly above the silhouette's knee in every attempt. Approximate rat-hunch/adult-height ratios are 0.477, 0.369 and 0.457. These are measurements, not an invented canonical centimetre shoulder height. The first/final approach hip/thigh height. Body length is not independently measurable in the front view.

The second also rotates into three-quarter view. The final front has weak/missing ash leakage from eyes/spine, a roughly 19 px paw-versus-man baseline mismatch, subtle background tonal variation and overly fissured hide requiring strict review. All keep the rodent muzzle, chisel incisors, grey/black blotches and hairless tail, but those do not cure the major failures.

`MODEL_SHEETS_BRIEF.md` section 2 says: “Make the front view first. When it passes, pass it as the reference image for the other views, the expressions, the details and the chibi sheet.” `ASSETS_ARC2_BRIEF.md` repeats front-first for M1–M4. No passing front exists, and the three-total-try cap is exhausted. Therefore **turnaround.png, details.png, swarm.png and swarm_mother.png were not generated**. Do not use a failed front or add a fourth attempt without Claude's verdict/redo instruction.

## References, checks and preservation

The working cloud executor was verified ready. Fresh `msgf-bible` and `msgf-art` were fetched and the current handoff, start/read-order sources, M1 brief, review board and design rules checked. No M1 verdict or pre-existing M1 delivery existed. The prior failed executor had zero images/in-flight calls per the parent handoff; no duplicate generation occurred here.

Every call attached four inspected original approved PNGs: `characters_v2/stone_lizard/turnaround.png` (creature ink/cel comparison), `characters_v2/kang_jaeha/front.png` (adult proportion comparison), `style_test_v2/acting/A3_P23.png` and `B3_P29.png` (two house-style anchors). No rejected generation was used as a reference; no S16, S2b, retired or outside art was used. No mandatory reference exceeded the runtime five-input limit. Built-in image_gen only; no alternate provider or bypass.

All delivered PNGs decode as native 1536×1024 RGB and match their generator originals byte for byte. No resizing, conversion, PNG re-save, retouching, composite or thumbnail was made. Originals remain in `/workspace/generated_images/`. Exact requests/logs are separate under `/workspace/m1-work/`; S16 remains untouched.

Only `inbox/M1/` plus one `INBOX.md` row are delivered to `msgf-art`. No main, canonical approved art, other entry, brief, bible, script, secret or font file was modified/published. No tool denial, quota or startup failure occurred in this executor. Stop for Claude verdict; dependent generation is pending, not approved.
