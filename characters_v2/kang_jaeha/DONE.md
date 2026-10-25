# S1 — Kang Jaeha: DONE through Round 2

Updated 25 October 2026. The original S1 set, Round 1 garment corrections and Round 2 chibi vest-edge fix are finished. Claude accepted the near-grey backgrounds in the review preserved below. Round 2 changes only `chibi.png` among the six character sheets.

## Files

- `front.png` — full-body front master with cleaned vest/hoodie shading and restrained vest wear.
- `turnaround.png` — front, three-quarter, left profile and back at one scale and baseline, with the garment corrections carried through.
- `expressions.png` — eight heads and shoulders in a 4×2 grid, preserving public, private, calculating, shock, CARRY pain, resolve, deadpan and laughing acting.
- `details.png` — corrected vest/hoodie crops; left-pocket notebook, elastic-band notebook and blank yellowed pages, chest/back T patches, right-ear pencil and fingerless gloves.
- `chibi.png` — the same eight original gag poses with smooth vest armholes and hems, corrected by local patch compositing in Round 2.
- `turnaround_coat.png` — retained byte-for-byte. The work trousers and shirt design were not changed, so the conditional coat redo was not triggered.
- `card.json` — palette, locks, new garment rendering/wear rules and Round 1 status.
- `prompts.json` — exact prompts, reference paths and composition records for the original set and both fix rounds.
- `qa/thumbnail_contact.png` — the Round 1 six-image contact sheet; the current chibi thumbnail is `qa/round2/chibi_200px.png`.
- `qa/image_metrics.json` — Round 1 dimensions, SHA-256 hashes and background samples; Round 2 chibi verification is in `qa/round2/`.
- `qa/round1_review.json` — section 11/11b review results, three-attempt counts and preserved-file hashes.

All six current PNGs are 1536×1024. All recorded image/reference paths and JSON files were checked. No pending generation records remain.

## Round 1 fixes

- Replaced `front.png`, `turnaround.png`, `expressions.png` and `details.png` for REVIEW_FIXES.md S1.
- Repainted orange vest and grey hoodie areas with substantially simpler, large opaque cel-shadow shapes; removed the scattered translucent diagonal streaks, narrow shard patterns and unnecessary diagonal back shading.
- Smoothed vest armholes and main hem. Wear is restrained to tiny outer lower-hem corner nicks and a few threads; no continuous sawtooth fraying.
- Preserved face identity, poses, proportions, functional pockets, the two safety bands and all side locks: LEFT-eye fringe, RIGHT-ear pencil, LEFT-pocket notebook, RIGHT-chest T and large back T. The calculating expression still holds its single pencil to the lip.
- Used the corrected front as the identity and garment reference for the other three replacement sheets. Every new prompt follows STYLE BLOCK → CLEAN-UP LINE → sheet description → character snippet → NEGATIVE BLOCK.
- Kept `chibi.png` and `turnaround_coat.png` unchanged; their hashes were verified against the pre-fix files.
- Moved every replaced original to `characters_v2/_rejects/kang_jaeha_r1_<file>_shard_shading_sawtooth.png`. Discarded Round 1 candidates are also in the shared rejects folder, with `kang_jaeha_r1_` names and reasons. The original rejected duplicate-notebook chibi is still archived there. Exact prompts and references are recorded for every candidate.
- Reviewed new images full size and in the refreshed 200 px contact sheet. Garment rendering, restrained wear, face/prop continuity, hands and anatomical side locks pass visual review.

## Round 1 background note (accepted by Claude)

The Round 1 generator returned near-grey pixels with small colour variations despite exact-fill prompts. This was reported at the time. Claude subsequently measured the backgrounds, accepted the imperceptible variation, and passed the front, turnarounds, expressions and details. His review and restoration note are preserved below. No background repaint was made in Round 2.

Only `characters_v2/kang_jaeha/` and the permitted `characters_v2/_rejects/` were written. No other entry was edited.

## Claude's review, round 2 (25 October)

- **Turnarounds pass as drawn.** The profile figure in `turnaround.png` and `turnaround_coat.png` faces picture-left, so it shows his LEFT side: the fringe covers the near (left) eye, the pencil is hidden behind the far (right) ear, and the notebook sits in the near left chest pocket. That is correct.
- **Claude's mistake, reverted.** Claude briefly misjudged that profile as a right-side view, mirrored it, and wrote the mirrored sheets here; they were wrong and both originals have been put back byte for byte. The mistaken mirrored versions are kept in `../_rejects/kang_jaeha_r2_turnaround_profile_wrong_side_locks.png` and `../_rejects/kang_jaeha_r2_turnaround_coat_profile_wrong_side_locks.png`. Do not use them.
- **Background (11b.8).** The measured background is within 5 levels of #E9E9EC, which cannot be seen; Claude accepts it.
- **Still to fix: `chibi.png`.** The vests have sawtooth fraying along every armhole and hem, which round 1 should have caught (Claude's miss). It is being redone to match the clean edges of `front.png`.
- Front, expressions and details pass.


## Round 2 fixes — completed (25 October)

- **Only `chibi.png` changed among the character sheets.** `front.png`, both turnarounds, `expressions.png` and `details.png` were left untouched and verified against their pre-fix SHA-256 hashes. `card.json` was also left unchanged.
- Moved the original chibi, byte-for-byte, to `../_rejects/kang_jaeha_r2_chibi_sawtooth_vest.png`.
- Smoothed the vest armholes and lower hems in all eight figures. Removed repeating sawtooth teeth; no new fraying was added.
- Kept all eight original poses and faces. Checked 11b.10 in each figure: pencil behind anatomical RIGHT ear, fringe over anatomical LEFT eye, notebook in anatomical LEFT chest pocket, and T on anatomical RIGHT chest. Poses 2 and 7 each hold one notebook and retain an empty left chest pocket; no duplicate notebook was introduced. No figure was mirrored.
- Used one built-in imagegen edit of an atlas of cropped torso patches, with `front.png` as the clean-edge reference. Composited the edited edge strips back onto the original at native size, following the Round 2 cropped-patch instruction. Faces, hands, T patches and notebook regions were protected from the composite.
- Pixel comparison verified **zero changed pixels outside the vest-edge masks and zero changed pixels in the protected feature regions**. The result remains 1536×1024. The original archive hash was checked, and all five passed character sheets remain byte-identical.
- Ran sections 11 and 11b, including the new left/right check, on the full sheet, enlarged local vest crops and the 200 px thumbnail. The vest-edge correction passes; the accepted background and original acting/gear remain intact.
- Updated `prompts.json` with the exact patch-edit prompt, its reference images, the final composition, and three discarded intermediate mask composites. The rejected composites are archived with `kang_jaeha_r2_chibi_composite_` names.

Round 2 working and verification files are in `qa/round2/`: `prepare_patches.ps1`, `composite_patches.ps1`, `patches.json`, source and edited patch atlases, masks, `composition_verification.json`, `protected_files.json`, `review.json`, `final_vest_patch_atlas.png` and `chibi_200px.png`. These record the reproduction method, current chibi hash and all eight lock checks. Earlier QA files remain historical Round 1 snapshots.

The earlier “still to fix” chibi note in Claude's review above is resolved by this Round 2 correction. No outstanding S1 Round 2 item remains. Only this character's folder and the permitted rejects folder were written.
