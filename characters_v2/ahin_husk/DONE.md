# DONE — S19: Moon Ahin's polished husks

27 October 2026 · Asia/Tashkent · Built-in image_gen.

Finished under the README's 27 October five-try rule. The front and turnaround pass my visual checks. **The formation does not pass the requested count: the best attempt has 35 husks in seven rows of five, rather than 40 in eight rows.** It is kept under the required normal filename after five formation attempts. This is not an external approval.

## Files

- `front.png` — checked polished-husk front master; supporting image required by the model-sheet workflow.
- `turnaround.png` — front, three-quarter, side and back, with matching scale and baseline.
- `formation.png` — selected formation attempt 2; synchronized unarmed fencing lunges; known count fault above.
- `card.json` — height, palette, design locks, view descriptions, checksums, attempt counts and known faults.
- `prompts.json` — exact prompts and reference paths for all ten image calls, saved/source paths, reasons, checksums and free-space checks.

## What remains wrong

`formation.png` is missing one complete row of five husks. Its camera is shallower than requested. Small fingers and silver seams are simplified at formation scale. The five formation attempts produced 30, 35, 35, 35 and 32 husks; attempt 2 has the best combination of smooth construction, regular spacing and consistent fencing pose. No sixth attempt was made.

The front took two attempts; the turnaround took three. Their rejected attempts added anatomical neck/chest lines or inconsistent joints and feet. The kept front and turnaround preserve the blank heads, simplified smooth bodies, thigh-ring seams, moulded feet, long adult proportions, polished white finish and fine silver seams. The final turnaround retains faint broad tonal shaping on the upper back, without an incised spine groove or seat cleft.

## Rejects saved

All are ordinary full-size PNG files in `characters_v2/_rejects/`:

- `ahin_husk_front_a01_collarbone_chest_modelling.png`
- `ahin_husk_turnaround_a01_clavicle_lines.png`
- `ahin_husk_turnaround_a02_anatomy_joint_drift.png`
- `ahin_husk_formation_a01_30_not_40_six_rows.png`
- `ahin_husk_formation_a02_35_not_40_seven_rows.png` — archive copy of the selected best, still-failing formation.
- `ahin_husk_formation_a03_35_not_40_seven_rows.png`
- `ahin_husk_formation_a04_35_not_40_seven_rows.png`
- `ahin_husk_formation_a05_32_not_40_four_by_eight.png`

## Verification and scope

All eleven saved PNG copies (three kept files and eight reject/archive files) are 1536×1024, byte-for-byte identical to their generator originals. Every file has one filesystem link and is a regular file, with no shortcut or symbolic link. No resizing, retouching, compositing, JPEG or WebP conversion was applied to saved art.

Checked the kept images at native size, at 200 pixels wide and with in-memory 200% inspection crops. No extra preview or temporary image was saved in the project. Flat light-grey backgrounds, upper-left neutral light, absence of text and absence of scale figures were checked. Soft gloss is the intentional Ahin-husk material exception.

Read README_START_HERE.md and its applicable reading order, the S19 brief, model-sheet rules, proportion rules, review status and relevant base-sheet metadata. The approved ordinary husk turnaround supplied the base construction and approved Moon Ahin details supplied the silver/porcelain finish. The passed new front was the first reference thereafter. No reject, old art or outside image was used as an input. No call used more than three references.

Ran `Get-PSDrive C` before each of the ten image calls. The lowest observed free space was 43,214,516,224 bytes (40.25 GiB), above the 3 GB stop threshold throughout.

Project writes were confined to `characters_v2/ahin_husk/` and S19-prefixed reject files in `characters_v2/_rejects/`. Other chats' folders, briefs and review status were not edited. Nothing was published. Stopping now as instructed.
