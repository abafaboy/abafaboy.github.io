# DONE — S8 — Kang Seoa

Round 1 fixes completed 25 October 2026.

## Round 1 fixes

- Corrected `front.png` first. The grey plaid pleated skirt now reaches the top of the knee and covers the entire thigh.
- Replaced the calculator's bright-green screen with a blank, matte, unlit neutral-grey LCD throughout the revised set.
- Regenerated `turnaround.png` from the corrected front, then `details.png` and `chibi.png` from that corrected design lineage.
- Preserved the knee-reaching skirt in all four turnaround views and all eight chibi poses.
- Cleaned diagonal shard-like shading from the details sheet's bag/blazer crop into a few broad opaque shadows.
- Restored the crying chibi's locked round glasses and removed uneven ground-shadow patches.
- Retained `expressions.png` exactly, as the S8 review permits when no keychain is visible. This sheet shows neither the calculator nor the skirt; its SHA-256 is unchanged.
- Used the required prompt order for every Round 1 generation and edit: STYLE BLOCK, CLEAN-UP LINE, sheet description, character snippet, NEGATIVE BLOCK.
- Moved every replaced drawing, its original generated source, and superseded QA thumbnails into S8-prefixed files in `characters_v2/_rejects/`. Rejected intermediate attempts are recorded too.

## Current files

- `front.png` — corrected front anchor, knee-reaching hem and grey LCD.
- `turnaround.png` — front, three-quarter, left profile and back; matching scale and baseline.
- `details.png` — round glasses, calculator front/three-quarter/back, and its actual zipper attachment.
- `chibi.png` — eight full-body 2.5-head gag poses, with glasses, knee-reaching skirts and unlit grey LCDs.
- `expressions.png` — original eight heads and shoulders, retained unchanged.
- `card.json` — updated palette, skirt/LCD locks, Round 1 changes and strict-check results.
- `prompts.json` — exact original and Round 1 prompts, corrected reference lineage, rejection reasons and archived image locations.
- `validation.json` — dimensions, SHA-256 values, zero-bright-green check, retained-expression hash, prompt-order and archive checks.
- `generation_sources/` — untouched current generator outputs and exact current reference pixels.
- `finalize_sheets.ps1` — background-only export normalization. The old green-screen conversion has been removed.
- `qa_thumbnail.png` — all five sheets, each reduced to 200 px wide.

## Verification

All five final model images are 1536×1024 PNGs with flat #E9E9EC backdrops. Sections 11 and 11b were run at full size and 200 px wide. Checks covered the knee-reaching hems, unlit LCDs, face and glasses locks, matte cel rendering, broad opaque fold shadows, purposeful gear, plain shoes, anatomy, view/pose counts and absence of lettering or brand marks.

Automated verification passed for PNG sizes, final hashes, background corners, zero bright-green pixels, unchanged expression-sheet bytes, exact Round 1 prompt order, every saved reference and every replacement archive. All drawing and artistic corrections used built-in image_gen. Technical export only standardizes the exterior light-grey background and leaves the grey LCDs unchanged.

The manifest records 12 rejected drawing candidates across both rounds plus 7 supporting source/thumbnail archives. These are all S8-prefixed files under `characters_v2/_rejects/`.

No outstanding observed issue remains after the final local checks. Writes were confined to `characters_v2/kang_seoa/` and S8's files in `characters_v2/_rejects/`. Nothing was published.

