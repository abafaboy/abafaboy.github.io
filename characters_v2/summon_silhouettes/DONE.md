# S12 — summon silhouettes

Round 2 Lyra update completed on 2026-10-25 (Asia/Tashkent).
Final image: `characters_v2/summon_silhouettes.png`.
Status: **PASS**.

## Round 2 update

- Read CHARACTER_DESIGNS_v2.md section 2.10 and inspected the approved `characters_v2/lyra/front.png`.
- Replaced `parts/lyra.png` with a solid-black mask extracted from that approved front. No Lyra image was generated or redrawn.
- Changed Lyra from the retired 185 cm working value to her canon **182 cm**, exactly **364 pixels** at the unchanged 2 px/cm scale.
- Measured stature from the top of her head to her soles, excluding the bow. The head-only source region is [640, 0, 880, 190], and the traced head starts at source row 3. Pale silver-white hair contour gaps are closed before filling the mask.
- Added `--only-lyra` to `composite.py` and used it for this update. It reuses the other six existing parts, so a newer Nib front is not silently introduced as a second character change.
- All six other part PNGs remain byte-identical; their scaled silhouettes remain pixel-identical. The existing centered-row layout adjusts horizontal placement to maintain the same even gaps.
- Updated `card.json`, `prompts.json`, `qa/validation.json`, `qa/pixel_audit.json` and the 200 px proof.

## Current heights

| Figure | Height | Exact body height |
|---|---:|---:|
| Nib | 105 cm | 210 px |
| Borro | 240 cm | 480 px |
| Lyra | **182 cm, canon** | **364 px** |
| Pim | 140 cm to furry scalp | 280 px |
| Maud | 190 cm | 380 px |
| Caldric | 210 cm | 420 px |
| Kett | 95 cm | 190 px |

Pim's antennae/headset retain their 46 px extension above the scalp. Lyra's bow is excluded from her height measurement even if its tip rises above her head.

## Replaced PNGs archived

All are in `characters_v2/_rejects/`:

- `summon_silhouettes_r2_old_lyra_part.png`
- `summon_silhouettes_r2_old_lyra_source.png`
- `summon_silhouettes_r2_old_lyra_lineup.png`
- `summon_silhouettes_r2_old_lyra_thumbnail.png`
- `summon_silhouettes_r2_old_lyra_mask_incomplete_head.png` — initial pale-hair segmentation proof, rejected before delivery.

The retired generated Lyra source is no longer used by the compositor. The old card is retained as `qa/r2_previous_card.json` to verify preservation of the other six silhouettes.

## Verification

- Inspected the final part and composite at full size and the composite at 200 px wide.
- Final dimensions: exactly 1536×1024.
- Exactly two RGB colours: **#000000** (288,151 pixels) and **#E9E9EC** (1,284,713 pixels).
- Lyra's head-to-sole height is exactly 364 px; a separate in-memory check raised the bow above her head and confirmed that the head measurement did not change.
- Shared occupied foot row remains **y=790**; all six gaps remain exactly **26 empty pixel columns**.
- Enclosed holes are filled, including after scaling. No clipping or grey interior detail.
- Other six part files are byte-identical and their scaled shapes are pixel-identical to the archived previous sheet.
- Re-running `composite.py --only-lyra` produced a byte-identical final PNG.
- Lyra, Nib and Kett front hashes remained unchanged during the work. Those folders were never edited; only their `front.png` files were read.
- Approved Lyra front SHA-256: `c3845140e327175287c192579850cde6243c83494b0d8dc065291743b5d6228a`.
- Final PNG SHA-256: `54dfa317d26a1c0d819996a64f65b6bf8d4bc4b6dcef0473dd0829cf2ead0dac`.

## Reproduce this Lyra-only update

```powershell
& 'C:\Users\abafa\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\abafa\Videos\MySummonsGoFirst\characters_v2\summon_silhouettes\composite.py' --only-lyra
```

Omitting `--only-lyra` refreshes all three front-derived masks from the current Lyra, Nib and Kett fronts. Use that only for a requested full front refresh, including the earlier S2/S11 handoff. The current delivery intentionally preserves the other six parts.

## Round 1 fixes retained

Four separately drawn parts remain: Borro, Pim, Maud and Caldric. Maud is a broad, strong woman with cropped hair, surgeon's plate, apron, bone saw and needle case. Borro's ragged hip points were removed. Nib and Kett remain masks from their own fronts. The exact two-colour compositor, source provenance, reject history, baseline, order, physical scale and gap rules remain in place.

The original round-1 prompts and round-0 history remain in `prompts.json`. Only S12-owned files and S12-prefixed rejects were written. Work stopped after this DONE.md update.
