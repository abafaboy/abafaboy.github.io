# PANEL BRIEF v2: drawing the rebuilt chapters (one Codex chat per part)

**Status.** The owner approved the story, every character design and the acting tests (25 October) and said "continue": chapter production starts with chapter 1. This brief replaces `PANEL_BRIEF.md`. Each chat draws one part of a chapter (the table at the end) and writes only its own files.

## 1. Read first
1. `README_START_HERE.md`.
2. `MANHWA_STYLE_GUIDE.md`, all of it. These sections matter most:
   - 2 and 4–9: light, colour, faces, acting, effects, backgrounds;
   - 10: the prompt kit (10.1 STYLE BLOCK, 10.2 recipe lines, 10.3 NEGATIVE BLOCK, 10.4 CLEAN-UP LINE, 10.5 ACTING LINES);
   - 11, 11b (1–11) and 11c (1–11): the checks;
   - 13: nothing may ever look compressed.
3. `MANHWA_ART_DIRECTION.md` section 2: the recipe of every panel in your part.
4. `CHARACTER_DESIGNS_v2.md`:
   - the fan-service block at the top;
   - the section of every character in your part;
   - their prompt snippets in section 8, word for word.
5. `bible/SCRIPT_FORMAT_v2.md`: what each panel field means.
6. `scripts_v2/chNNN.yaml`: your panels, plus the panel just before and just after each one, so camera changes and continuity hold across the cut.
7. `ACTING_TEST_BRIEF.md`, "Round 2", and `style_test_v2/acting/REPORT.md`: what went wrong in the tests and how it was fixed (section 6 below sums it up).

## 2. References (at most 5 images per image call; the tool refuses a sixth)
Pass, in this priority order:
1. **Every character who acts or speaks:** `characters_v2/<id>/front.png` (Yoo Bomi has no `front.png`: use `yoo_bomi/source_front.png`).
2. **The location:** `locations_v2/<id>/key.png`. Use `door.png`, `reverse.png`, `gate.png` or `details.png` instead when the camera matches them better.
3. **If there is room, one acting sheet for the character whose acting carries the panel:** `acting.png` for body language, `talking.png` for a talking or listening face, or `expressions.png`. Acting and talking sheets exist for Jaeha, Nib, Yerin, Mok, Lyra and Bomi.

Special looks:
- **Jaeha in the black field coat** (flash-forward P01–P07): `kang_jaeha/turnaround_coat.png`.
- **Nib with the husk mask** (from P60): `nib/turnaround_mask.png`.
- **Black Hound hunters:** `black_hound/lineup.png`.
- **The husk:** `husk/front_reference.png`.
- **The knight:** `knight_commander/front.png`, or `kneeling.png` while he kneels.
- **Stone lizards:** `stone_lizard/turnaround.png` or `pack.png`.
- **The seven summons as silhouettes:** `summon_silhouettes.png`.
- **Chibi panels:** the character's `chibi.png`.

Add the reference sentence from 10.5 to every prompt. Never pass anything from the old `characters/` or `chapters/` folders, or any real webtoon image.

## 3. How to build each prompt (style guide section 10)
1. The STYLE BLOCK.
2. The CLEAN-UP LINE.
3. The recipe line for the panel's `recipe` (10.2).
4. The panel's `camera`, `light` and `art`.
5. Its `acting`, `eyeline` and `foreground`, word for word, then the reference sentence.
6. The snippet of every character in the panel.
7. The NEGATIVE BLOCK.

## 4. What each image must be
- **Size by shape:**

| Shape | PNG size |
|---|---|
| `full`, `wide`, `vignette` | 1536×1024 |
| `strip` | 1536×1024, drawn edge to edge; the letterer shows only the middle HALF (rows 256–768), so the subject sits there |
| `tall`, `narrow-l`, `narrow-r`, `bleed` | 1024×1536 |
| `inset-l`, `inset-r` | square: the generator's native 1254×1254 (or 1024×1024); never resized |
| `kind: end` (`END.png`) | square (native 1254×1254), chibi gag on plain white |

- **Strips are never letterboxed.** In chapter 1, four strips (P05, P35, P36, P53) came back with black bars above and below a thin picture band, and all four had to be redrawn: the bars show up as black bands in the lettered chapter. Fill the whole canvas with the scene. For an eyes close-up, hair and forehead fill the top quarter and cheeks and nose the bottom quarter. Never leave black or empty bands.
- **Square sizes:** the generator returns squares at 1254×1254. Keep that native size; do not spend tries trying to get 1024×1024.

- **No image** for `kind: title` and `kind: caption` panels.
- **PNG straight from the generator,** never JPEG or WebP, never resized or re-saved (section 13).
- **No text in the art.** No letters, bubbles, sound effects or captions. The only exception is Jaeha's T patch. Leave the panel's `calm` zone simple for the lettering.
- **Screens.** A `ui` entry with `on: screen` means the screen is flat #00FF00 (P10). Near-pure green such as (13,252,4) is fine: the letterer keys any strong green, so do not spend tries chasing exact values. `on: float` windows are added by the letterer: draw nothing for them, but leave the area the art text describes calm.
- **Chibi panels** (`style: chibi`) use the chibi sheets: 2.5 heads tall, gag faces, a simple flat background.
- **Breaking and bursting effects** ("shards", "debris") are hand-inked jagged pieces with ink outlines and flat colour, never bevelled 3D facets (11b.6).

## 5. Checks (every panel)
- Run sections 11, 11b (1–11) and 11c (1–11). Look at the full size, then at 200 px wide.
- Take up to 3 tries per panel. A targeted edit of your own kept image is allowed: crop, edit, then composite back at the original pixel size.
- Rejects go to `chapters_v2/chNNN/art/_rejects/<id>_<try>_<reason>.png`.

## 6. Lessons from the acting tests (chapter 1)
- **Hands drift into pockets and onto hips.** Give every hand the job the `acting` line names, and check each hand at full size.
- **Props must never float.** Mok's tower shield is on his left arm, standing on its edge with a hand on it, or slung on his back by a strap across his chest. The one exception is P31, where his right forearm is through the grip. His sword is sheathed at his belt unless drawn.
- **Never duplicate a prop.** When Jaeha holds his notebook, his left chest pocket is empty.
- **Eyelines go exactly where the `eyeline` field says.** Check the pupils.
- **Mouths:** the speaker's mouth is open mid-line; listeners react.
- **The door stays at picture-right from P27 to P32.**
- **Light:** the boss-room door scenes are lit red from the lamp; the fortress is green-dusk; the pit is cold LED floodlight.
- **Fan service:** the crossbow hunter (hunter 5) is the restyled beauty in `black_hound/lineup.png`. Yerin stays covered and is never drawn sexy.
- **Sides:** check every side lock (11b.10): Jaeha's fringe over his LEFT eye, pencil behind his RIGHT ear, notebook in his LEFT chest pocket; Nib's notch in his LEFT ear and one lower fang on his LEFT; the mask over Nib's LEFT eye; the lizards' blind LEFT eye; the knight's cracked LEFT pauldron.

## 7. Heads (for the lettering)
After every kept panel, record the head box of every visible character in your `REVIEW_<part>.json`. Use valid JSON, with coordinates as fractions of the image (0 to 1). The letterer aims every bubble tail at these boxes.

```json
{"P07": {"heads": {"kang_jaeha": [0.42, 0.18, 0.55, 0.40]}, "verdict": "ok", "problems": []}}
```

## 8. Files (write only these)
- `chapters_v2/chNNN/art/<id>.png`: the kept panels.
- `chapters_v2/chNNN/art/_rejects/`: rejects.
- `chapters_v2/chNNN/art/PROMPTS_<part>.json`: the exact prompt and reference files for every kept image and reject.
- `chapters_v2/chNNN/art/REVIEW_<part>.json`: heads, per section 7.
- `chapters_v2/chNNN/art/PROGRESS_<part>.md`: one line after each panel.
- `chapters_v2/chNNN/art/DONE_<part>.md`: when your part is finished. List each panel, its tries, and anything you are unsure of. Then STOP.

Never edit the script, the briefs, the sheets or another part's files.

## 9. Chapter 1 parts

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | Flash-forward at Gwanghwamun: Jaeha in the coat, the seven summons as silhouettes, Nib only as an outline in P04 (no mask yet). No art for P08 (`caption`). |
| `B1` | P09, P10, P12, P13, P14 | P10 has a #00FF00 phone screen. P13 is chibi. **P11 is done:** copy `style_test_v2/acting/A1_P11.png` to `P11.png` byte for byte and record its heads. |
| `B2` | P15–P20 | The fortress corridor and the first lizards. P18 is Jaeha's name-card panel. |
| `C` | P21, P22, P24, P26, P30 | **Done already (copy byte for byte from `style_test_v2/acting/`, then record their heads):** `A3_P23.png`→`P23.png`, `B1_P27.png`→`P27.png`, `B2_P28.png`→`P28.png`, `B3_P29.png`→`P29.png`, `B4_P31.png`→`P31.png`, `B5_P32.png`→`P32.png` (P32 stays 1536×512). No art for P25 (`title`). Match the light and look of the copied panels. |
| `D1` | P33–P38 | The boss room and the knight. |
| `D2` | P39–P43 | |
| `E1` | P44–P49 | |
| `E2` | P50–P54 | |
| `F` | P55, P56, P57, P58, P60, P61, P62, P63 and `END.png` | No art for P59 (`caption`). Nib with the husk mask from P60. The P60 splash is the chapter's biggest image: make it count. |
