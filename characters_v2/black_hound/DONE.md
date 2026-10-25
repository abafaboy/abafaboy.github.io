# S4 DONE — Black Hound lineup

Round 2 completed 25 October 2026, Asia/Tashkent. Hunter 5 was restyled with the built-in imagegen tool on a cropped patch, then composited into the original lineup with Python/Pillow as explicitly requested.

## Files

- `lineup.png` — final 1536×1024 PNG, seven full-body hunters in one front-view row.
- `card.json` — updated hunter-5 design, approved 168 cm height, locks and QA.
- `prompts.json` — exact prompts, crop references, rejected versions and composite provenance.
- `round2_patch.py` — crop preparation, masked compositing and pixel verification.
- `round2/pixel_check.json` — measured preservation checks and SHA-256 hashes.
- `DONE.md` — this completion record.

The original lineup order stays: spearman; axe fighter; ponytail sword-and-buckler fighter; Mok; mage; crossbow woman (hunter 5); bald shield-bearer.

## Round 1 fixes

- The mage's staff was shortened to a forearm-length one-handed staff with a small violet core.
- Its floor-reaching predecessor remains archived at `../_rejects/black_hound_r1_long_staff.png`.
- That accepted short-staff correction remains pixel-identical in Round 2.

## Round 2 fixes

- Read the Round 2 S4 instructions, updated design 2.5, the new hunter-5 snippet, and checks 11 and 11b.
- Restyled only hunter 5 as an adult Korean beauty in her late twenties: sleek chin-length black bob, winged eyeliner, red lips and cool confident expression; athletic, curvy figure.
- Her waist-cropped black guild jacket is open over a fitted opaque black tank with a low scoop neckline. The small dark-crimson hound remains on her anatomical left chest, picture-right. She has fitted black tactical trousers and her thigh holster.
- Kept her original compact crossbow, forearms, gloves, hand grips and black boots to preserve the pose and avoid changing the bald hunter's hand behind the weapon.
- Used the exact prompt order: V2 STYLE BLOCK, CLEAN-UP LINE, crop edit description, new hunter-5 snippet, NEGATIVE BLOCK.
- Generated the edit from the 416×624 crop `round2/source_crop.png`, with crop box `[1012,260,1428,884]` in the original lineup. Resized only the generated crop back to source scale; never resized the full lineup.
- Composited only inside the reviewed hunter-5 foreground mask, excluding original background pixels, adjacent hunters, shields, crossbow/hand regions and boots. No full-frame generated pixels replaced the original.
- Moved the old lineup to the exact requested archive: `../_rejects/black_hound_r2_lineup_old_hunter5.png`.
- Updated `card.json`, `prompts.json` and this file. No Mok-set files or other chat folders were changed.

## Verification

Reviewed the final full-size lineup, the close crop, and the 200 px-wide thumbnail under sections 11 and 11b: mature adult facial design, clean cel shadows, no sawtooth cloth, no brand marks, correct hound side, coherent gear, preserved hand anatomy, no new extra limbs, no blur or plastic sheen. Clothing is opaque and non-explicit; no nudity.

Measured results in `round2/pixel_check.json`:

- Final canvas: 1536×1024 PNG.
- Edited foreground pixels: 45,251.
- Changed pixels outside hunter 5's edit mask: **0**.
- Changed original background pixels in the crop: **0**.
- Changed protected crossbow/hand pixels: **0**.
- Other hunters, Mok and shields remain pixel-identical to the archived original.
- Original archive hash and final file hash verified; final pixels match the reviewed composite.

The original neutral-grey background, including its existing slight variation from exact solid `#E9E9EC`, was preserved pixel-for-pixel as requested. Generated colours still approximate the recorded production palette. Original adjacent shoulder contacts remain unchanged.

## Archives and reproducibility

- `../_rejects/black_hound_r2_lineup_old_hunter5.png` — exact pre-restyle file.
- `../_rejects/black_hound_r1_long_staff.png` — Round 1 replaced file.
- `../_rejects/black_hound_s4_lineup_crowded_silhouettes.png` — initial layout reject.

The crop source, generated crop, masks and comparison artifacts are retained in `round2/`. The exact Round 2 generation prompt is recorded for `black_hound_hunter5_r2_crop_01`; the final derived asset is `black_hound_lineup_r2_01`. Running `round2_patch.py composite` reproduces the candidate from the preserved inputs; do not rerun preparation or finalization over the completed artifacts.

Project writes were confined to `characters_v2/black_hound/` and its named reject archives.
