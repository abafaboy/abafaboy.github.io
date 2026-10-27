# MODEL SHEETS BRIEF: the new cast in style V2 (one Codex chat per entry)

**When.** Now. Several Codex chats run at the same time, one per entry in section 4.
- Each chat draws only its own entry and writes only in its own folder.
- Never touch another chat's folder.

**Style.** V2 · Cinematic cel, the only STYLE BLOCK to use (`MANHWA_STYLE_GUIDE.md` 10.1).

**Read first:**
- `README_START_HERE.md`;
- `MANHWA_STYLE_GUIDE.md`;
- `CHARACTER_DESIGNS_v2.md`: your character's section and their prompt snippet in section 8, used word for word;
- `bible/ART_BIBLE.md` A5b (chibi);
- `style_test_v2/REPORT.md`, if it exists, so you avoid what went wrong in the V2 check panels.

## 1. What a set contains

All sheets are 1536×1024 PNGs on a flat light-grey background #E9E9EC, lit by soft neutral light from the upper left. They carry NO text and NO labels. Notes go in `card.json`.

| File | Contents |
|---|---|
| `turnaround.png` | Full body: front, three-quarter, side and back, standing in a neutral pose, all at the same scale with feet on one baseline |
| `expressions.png` | 8 heads and shoulders in a 4×2 grid. Use the expressions listed in the character's design; where none are listed: neutral, smile, anger, shock, sadness, fear, determination, laughing. |
| `details.png` | Close-ups of every lock and prop (for Jaeha: the notebook, the pencil, the vest patch, the gloves) |
| `chibi.png` | Only where the entry says so. ART_BIBLE A5b: 2.5 heads tall, 8 gag poses, same colours and locks. |
| `card.json` | id, name, height, the hex palette from the design, the locks, and the prompt file used |
| `prompts.json` | The exact prompts and reference images for every kept image and every reject |

## 2. How to keep a character on model
- **Reference the turnaround.** Make the front view first. When it passes, pass it as the reference image for the other views, the expressions, the details and the chibi sheet. Your own new images are the only references allowed.
- **Same words every time.** Use the same STYLE BLOCK, the same snippet and the same NEGATIVE BLOCK for every image of the character.
- **Check the locks in every view, every time:**
  - Jaeha: fringe over the LEFT eye, pencil behind the RIGHT ear;
  - Nib: notch in the LEFT ear, fang on the LEFT, amber eyes;
  - the knight: the sigil and the cracked LEFT pauldron;
  - the lizards: the blind LEFT eye.
- **Redo an image** (up to 5 times) if it fails any check in `MANHWA_STYLE_GUIDE.md` section 11. Put rejects in `characters_v2/_rejects/<id>_<reason>.png`.

## 3. Finish
- When every file of your entry exists, write `characters_v2/<id>/DONE.md`, listing the files and anything you are unsure about.
- Do not stop to ask; finish the entry.

## 4. Entries (one chat each)

| # | Folder | Draw |
|---|---|---|
| S1 | `characters_v2/kang_jaeha/` | Turnaround, expressions (the 8 in his design), details, chibi. Then `turnaround_coat.png`: the same turnaround in the black field coat (design 2.1, "Other looks"). |
| S2 | `characters_v2/nib/` | Turnaround (hood down), expressions, details (ear notch, fang, knives, binoculars, the cracked husk mask), chibi. Then `turnaround_mask.png`: the front and three-quarter views wearing the husk mask over his left eye. |
| S3 | `characters_v2/song_yerin/` | Turnaround, expressions, details (bag, sleeve cross, the healing glow in her hands), chibi |
| S4 | `characters_v2/mok_hangyu/`, then `characters_v2/black_hound/` | Mok's turnaround, expressions (camera smile, off-camera dead eyes and others) and details (shield, emblem, chain, sword). Then `black_hound/lineup.png`: the six hunters of design 2.5 and Mok, standing in a row, front view, same scale, with Mok's turnaround as reference. |
| S5 | `characters_v2/husk/` | Turnaround. `details.png`: three cracking stages, and the chapter 1 version with glowing cyan cracks and glitching edges. |
| S6 | `characters_v2/knight_commander/` | Standing turnaround. `kneeling.png`: kneeling in the snapped chains, front and three-quarter. `details.png`: the sigil, the face-hole calm and hostile, the cracked left pauldron, a chain cuff with its stamped mark (a shape, no letters), and the sword's crossguard. |
| S7 | `characters_v2/stone_lizard/` | Turnaround (side, front, top, back). `details.png`: the blind left eye, the teeth, the club tail. `pack.png`: three lizards together, mid-hunt. |
| S8 | `characters_v2/kang_seoa/` | Turnaround, expressions, details (glasses, calculator keychain), chibi |
| S9 | `characters_v2/yoo_bomi/` | Turnaround, expressions, details (camera drone, bow), chibi |
| S10 | `characters_v2/choi_dongmin/` | Turnaround, expressions, details (rescue jacket, coffee cup) |
| S11 | `characters_v2/kett/` | Turnaround, expressions, details. A young adult, never a mascot. |
| S12 | `characters_v2/summon_silhouettes.png` | One image: the seven summons (Nib, Borro, Lyra, Pim, Maud, Caldric, Kett) as solid black silhouettes standing in a row at scale, from design 2.9, on light grey |
| S14 | `characters_v2/lyra/` | Design 2.10. She fronts the YouTube thumbnail, so make her as attractive as the design says: a beautiful face and figure in the revealing outfit, never nudity or anything explicit, always a confident stance.<br>1. Make `front.png` first and STOP; Claude shows it to the owner.<br>2. Then the turnaround.<br>3. Then `expressions.png`: smug half-smile; showing-off laugh; vain pout; competitive glare; aiming (still, one eye narrowed); shock; eyes shining at applause or money; sad, thinking of her lost brother.<br>4. Then `details.png`: the bow; the flute; the braid beads; the chest guard, bracer and glove; the boots. |
| S15 | `characters_v2/moon_ahin/` | Design 2.11, drawn early (25 October) so she is in the owner's sheets. The owner wants as much fan service and as many beautiful characters as possible: make her a cold, flawless beauty with a slender, curvy figure in the revealing white coat-dress as designed (deep V, hip slit on her LEFT leg, sheer thigh-highs), never nudity or anything explicit; an elegant, confident stance.<br>1. Make `front.png` first and STOP; Claude reviews it.<br>2. Then the turnaround (front, three-quarter, profile, back; the slit on her LEFT side, the baton in her RIGHT hand, the ribbon bow at the back of her head; run 11b.10 on every view).<br>3. Then `expressions.png`: the cold half-smile; contempt, looking down her nose; conducting, eyes closed in concentration; a polite public smile; the eyebrow twitch when her husks lose; cold anger; startled (rare); a faint real smile.<br>4. Then `details.png`: the baton; the ribbon bow; the gloves; the boots and the stocking top at the slit; the coat-dress buttons and belt; one of her polished husks next to an ordinary matte husk for contrast. |
| S13 | `characters_v2/scale_chart_v2.png` | Claude opens this one last, after S1–S11: everyone in design section 1 standing in a row on one baseline, each from their own front view |

## 5. Never
- Use anything in the old `characters/` folder as a reference, or write into it.
- Use real webtoon images, or real title, studio or artist names, in a prompt.
- Put text, labels, brand logos or wordmarks in a sheet. The vest's block T is the one exception; emblems without letters, like the hound's head, are drawn.
