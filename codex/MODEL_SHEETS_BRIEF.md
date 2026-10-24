# MODEL SHEETS BRIEF: the new cast in style V2

**When.** Step 1 (Jaeha and Nib) follows straight on from the V2 style check in `STYLE_TEST_BRIEF.md`, if both check panels passed. Step 2 waits for the owner's OK on Jaeha and Nib.

**Style.** V2 · Cinematic cel, the only STYLE BLOCK to use (`MANHWA_STYLE_GUIDE.md` 10.1).

**Read first:**
- `README_START_HERE.md`;
- `MANHWA_STYLE_GUIDE.md`;
- `CHARACTER_DESIGNS_v2.md`: every section, and use the prompt snippets in section 8 word for word;
- `bible/ART_BIBLE.md` A5b (chibi);
- your own `style_test_v2/REPORT.md`, so the sheets avoid what went wrong in the check panels.

## What a set contains

All sheets are 1536×1024 PNGs on a flat light-grey background #E9E9EC, lit by soft neutral light from the upper left. They carry NO text and NO labels. Notes go in `card.json`.

| File | Contents |
|---|---|
| `turnaround.png` | Full body: front, three-quarter, side and back, standing in a neutral pose, all at the same scale with feet on one baseline |
| `expressions.png` | 8 heads and shoulders in a 4×2 grid. Use the expressions listed in the character's design; where none are listed: neutral, smile, anger, shock, sadness, fear, determination, laughing. |
| `details.png` | Close-ups of every lock and prop (for Jaeha: the notebook, the pencil, the vest patch, the gloves) |
| `chibi.png` | Jaeha, Nib, Yerin, Seoa and Bomi only. ART_BIBLE A5b: 2.5 heads tall, 8 gag poses, same colours and locks. |
| `card.json` | id, name, height, the hex palette from the design, the locks, and the prompt file used |
| `prompts.json` | The exact prompts and reference images for every kept image and every reject |

## Order, and where to stop

1. **`characters_v2/kang_jaeha/` and `characters_v2/nib/`.**
   - Then write `characters_v2/READY_JAEHA_NIB.md`, listing the files and anything you are unsure about.
   - **STOP.** These two define the series, so the owner checks them before the rest.
2. **After the owner's OK**, in this order:
   - `song_yerin`, `mok_hangyu`;
   - `black_hound/lineup.png`: the six hunters and Mok in a row, front view, at the same scale;
   - `husk`: a turnaround, plus a details sheet with three cracking stages and the chapter 1 cyan-crack version;
   - `knight_commander`: a turnaround standing, the kneeling pose in chains, and details of the sigil, the face hole (calm and hostile), the cracked left pauldron and the modern chain cuff with its stamped mark;
   - `stone_lizard`: a turnaround, with details of the blind left eye and the club tail;
   - `kang_seoa`, `yoo_bomi`, `choi_dongmin`;
   - `kang_jaeha/turnaround_coat.png`: Jaeha in the black field coat, needed for the chapter 1 flash-forward;
   - `kett`: a turnaround, needed for the chapter 3 flashback;
   - `summon_silhouettes.png`: the seven summons (Nib, Borro, Lyra, Pim, Maud, Caldric, Kett) as solid black silhouettes standing in a row at scale, from `CHARACTER_DESIGNS_v2.md` section 2.9, for the chapter 1 flash-forward;
   - `characters_v2/scale_chart_v2.png`: everyone in `CHARACTER_DESIGNS_v2.md` section 1, standing in a row on one baseline.

## How to keep a character on model
- **Reference the turnaround.** Make the front view first. When it passes, pass it as the reference image for the other three views, the expressions, the details and the chibi sheet.
- **Same words every time.** Use the same STYLE BLOCK, the same snippet and the same NEGATIVE BLOCK for every image of a character.
- **Check the locks in every view, every time:**
  - Jaeha's fringe over the LEFT eye and pencil behind the RIGHT ear;
  - Nib's notch in the LEFT ear and fang on the LEFT, and his amber eyes;
  - the knight's sigil and cracked LEFT pauldron;
  - the lizards' blind LEFT eye.
- **Redo an image** (up to 3 times) if it fails any check in `MANHWA_STYLE_GUIDE.md` section 11. Put rejects in `characters_v2/_rejects/` with the reason in the file name.

## Never
- Use anything in the old `characters/` folder as a reference, or write into it.
- Use real webtoon images, or real title, studio or artist names, in a prompt.
- Put text, labels, brand logos or wordmarks in a sheet. The vest's block T is the one exception; emblems without letters, like the hound's head, are drawn.
