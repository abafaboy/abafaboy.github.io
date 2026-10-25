# S2 — Nib — Round 2 complete

25 October 2026. Completed only REVIEW_FIXES.md Round 2, entry S2.

## Round 2 fixes

- `turnaround.png`: added one V-notch to the profile figure's anatomical LEFT ear, on its lower edge near the tip. He faces picture-left, so this visible ear is his LEFT.
- `details.png`: added the same lower-edge near-tip V-notch to the bottom-left masked head's anatomical LEFT ear, on picture-right.
- `chibi.png`: redrew the eight gags from the approved `front.png`, then cleaned the small remaining edge and tooth details. Only anatomical LEFT ears have one V-notch; exposed RIGHT ears have smooth edges. Cloak hems are uneven and scorched with sparse shallow nicks. Every visible mouth has one lower LEFT fang, including the snack, puffed-cheek and laughing poses. The laugh has a plain upper tooth band and one upward lower fang. The sheet field is flat #E9E9EC.

## Pixel preservation

The ear edits used source crops, built-in image generation, and tiny antialiased composites. The generated notch shapes were traced onto the original ears using their actual underlying hair/background colours.

- Turnaround: exactly **28 pixels** changed, within inclusive x=980–986, y=81–89.
- Details: exactly **31 pixels** changed, within inclusive x=535–540, y=633–642.
- Exhaustive comparison of all four raw BGRA channels at every pixel confirms **every other pixel is identical** to each archived original. This includes Claude's fang correction, all faces, masks, gear, clothing and backgrounds.
- `front.png`, `expressions.png` and the Claude-restored `turnaround_mask.png` remain byte-for-byte identical to their task-start versions.

## Checks and provenance

Ran MANHWA_STYLE_GUIDE sections 11 and 11b, including the new left/right check 11b.10, at full output size and 200 px width. Checked all eight chibi faces, ears, mouth corners, hems, hands, feet and attached gear. No extra fangs, opposite-ear notches, sawtooth cloak hems, text, logos or glow were introduced. Existing accepted turnaround/details rendering and backgrounds were preserved outside the requested ear patches.

All six current model sheets are 1536×1024 PNGs. Validated `prompts.json`, all recorded local image/reference paths, current image hashes and the required blocks in every new prompt.

- `prompts.json` records exact prompts, image references, rejected attempts, current hashes, restoration history and deterministic cleanup.
- `round2_fix/QA.json` records the raw-pixel comparison, immutable-file hashes, per-pose side-lock checks and section 11/11b review.
- `round2_fix/apply_ear_patches.ps1` reproduces the two local composites.
- `round2_fix/chibi_precision.ps1` reproduces the final mouth, smooth right-ear edges and background cleanup from the raw third generation.
- `round2_fix/verify.ps1` reproduces pixel/hash verification and final mouth/thumbnail review images.
- Built-in generation attempts: one per ear crop, three for the chibi sheet. Two earlier chibi attempts are rejected.

## Replaced originals

Moved the three supplied originals to:

- `../_rejects/nib_r2_turnaround_profile_ear_notch.png`
- `../_rejects/nib_r2_details_masked_ear_notch.png`
- `../_rejects/nib_r2_chibi_ear_hem_locks.png`

## Round 1 fixes and corrected mask review

Round 1 rebuilt the full set around the angular adult goblin face, hooked nose, heavy brow, hollow cheeks and pointed chin, and replaced the shredded tunic with the sleeveless knee-length hood-down belted cloak. Claude accepted the redesign and locally corrected the fang side.

Claude subsequently retracted the three-quarter mask-extension instruction. The original mask already covered the anatomical LEFT near eye; the amber eye beyond the nose bridge is his RIGHT eye and must remain visible. Claude rejected the extension and restored the correct original before this Round-2 task. The old mask-extension acceptance claims are superseded. This task preserved the restored `turnaround_mask.png` exactly.

S2 is done and stops here.
