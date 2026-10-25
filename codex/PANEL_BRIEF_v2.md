# PANEL BRIEF v2: drawing the rebuilt chapters (one Codex chat per part)

**Status.** The owner approved the story, every character design and the acting tests (25 October) and said "continue". Chapter 1 is finished and the owner loved it ("holy this is great. i approve"); chapters 2 onward are drawn the same way. This brief replaces `PANEL_BRIEF.md`. Each chat draws one part of one chapter (the tables in section 9) and writes only its own files.

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
- **Continuity across chapters:** for the first part of a chapter, you may pass ONE finished panel from the end of the previous chapter (`chapters_v2/ch<previous>/art/`) so the light, the place and the looks carry over. Never pass a panel from the old `chapters/` folder.
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
4. The panel's `camera`, `light` and `art`, then a **scale and camera line**: the camera height and angle, where the horizon sits, the real sizes of the people and objects in the shot (section 4b), and "full model-sheet proportions, no compressed bodies; crop at the frame edge instead".
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

## 4b. Proportions, scale and perspective (the owner's direction, 25 October)

After chapter 1 went out, the owner and a reader both pointed at the same faults: "the body poses are weird", "the proportions", and in P09 the people were far too big for the scaffolding, the tent and the van ("they look way too small", said of the scaffolding). The owner's words: "be more strict about the proportions. the bodies sometimes look small and compressed when they shouldn't. also judge harshly on how things should look from a certain camera angle." Claude now rejects any panel that breaks these rules, so check them before you keep an image.

1. **Bodies are never compressed.** Every figure keeps its model-sheet proportions in every shot, measured from the `front.png` sheets:
   - Jaeha, Mok, Choi, Lyra and Moon Ahin: 7.5–8 heads tall;
   - Yerin, Seoa and Bomi: about 7–7.5 heads;
   - Nib: about 6 heads (a small head on a lanky body; his arms reach his knees; his head reaches Jaeha's belt);
   - adults' legs are about half their height (the crotch at mid-height).

   If a body doesn't fit the frame, **crop it at the frame edge** (at the knees, the waist or the chest). Never shorten legs or a torso, never enlarge a head, and never shrink a whole body to squeeze it in.
2. **Poses carry real weight.** Every pose must be one a real body can hold: weight on a clear leg or spread between both, joints bending the way joints bend, shoulders and hips tilting against each other. No mannequin stances (the husk is the only exception), no floating feet, and no limbs at impossible angles.
3. **One camera, one horizon.** Write the camera height into every prompt and keep every figure on it:
   - **Eye level** (about 1.6 m): the horizon runs through the heads of all standing adults, near or far. Far figures are smaller, but their heads stay on the horizon.
   - **High camera** (looking down): we see the tops of heads and shoulders, bodies taper toward the feet, and verticals converge downward. Figures far below are small.
   - **Low camera** (looking up): we see chins and the undersides of arms, verticals converge upward, and figures tower.
   - **One floor, one ground plane:** the farther away a figure stands, the higher its feet sit in the frame (still below the horizon) and the smaller it is, at the same rate for everyone.
4. **Real-world scale.** Write the anchors your panel contains into the prompt:
   - people: a standing adult is 1.6–1.9 m (the scale chart in `CHARACTER_DESIGNS_v2.md` section 1);
   - fixtures: a door 2.1 m, a stair step 18 cm, a guard rail 1.1 m, a storey 3 m;
   - sites: a scaffold level 2 m, a pop-up tent 3 m, a street-light pole 8–10 m, a cut-and-cover subway pit 15–20 m deep;
   - vehicles: a car 1.5 m tall, a van 2 m.

   Giants and monsters keep their own sizes: the knight is 4.5 m standing, and Jaeha reaches his mid-thigh.
5. **Small people in wide shots stay correctly built.** A 15 m pit wall is about eight people tall; a 10 m pillar is five or six. Figures that small still have their full head count.
6. **Before you keep an image, check:**
   - Does each full figure have its head count and long enough legs?
   - Does each figure match the others and the props and architecture around it?
   - Does each figure sit in the room's perspective: the right horizon, the right foreshortening for the camera height, feet on the floor?
   - Would a real camera at that height and angle see the scene this way (tops of heads from above, chins from below, converging verticals)?

   If any answer is no, redraw it.

## 5. Checks (every panel)
- Run sections 11, 11b (1–11) and 11c (1–11), and the section 4b checks above. Look at the full size, then at 200 px wide.
- Take up to 3 tries per panel. A targeted edit of your own kept image is allowed: crop, edit, then composite back at the original pixel size.
- Rejects go to `chapters_v2/chNNN/art/_rejects/<id>_<try>_<reason>.png`.

## 6. Lessons from the acting tests (chapter 1)
- **Hands drift into pockets and onto hips.** Give every hand the job the `acting` line names, and check each hand at full size.
- **Props must never float.** Mok's tower shield is on his left arm, standing on its edge with a hand on it, or slung on his back by a strap across his chest. The one exception is P31, where his right forearm is through the grip. His sword is sheathed at his belt unless drawn.
- **Never duplicate a prop.** When Jaeha holds his notebook, his left chest pocket is empty.
- **No unscripted prop events.** Parts are drawn by different chats at the same time, so a prop that changes state in one panel (a notebook flying away in chapter 1's P45) contradicts the panels after it. Props stay where the script and the design put them.
- **Empty areas for windows are part of the scene.** When a panel leaves room for a system window (P55–P57), that room is the dark hall itself, fading naturally. It is never a flat rectangle with a hard straight edge, and it never cuts through a head or a figure.
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

## 9. Chapter parts

Each chapter's table lists the panels for each part. A chat draws only its own part, of only the chapter its prompt names, into `chapters_v2/chNNN/art/`.

### Chapter 2: Who's in Charge (`scripts_v2/ch002.yaml`)

The whole chapter happens in the boss room (`locations_v2/boss_room/`), seconds after chapter 1 ends: green-dusk shafts from the broken roof, the knight's red face-hole, and cyan only from system windows and the husk's broken shards.

**Chapter 2 rules (read them before your first panel):**
- **Nib wears the cracked husk mask in every panel,** over the upper LEFT of his face, with the hood down. References: `nib/turnaround_mask.png` and `nib/front.png`; `nib/acting.png` or `nib/talking.png` if there is room. His eyes glow faintly amber the whole chapter (field form).
- **From P27 on, Nib is LINKED:** a thin amber outline flickers along his body in every panel where he appears. Keep it subtle: no aura, no beams.
- **Jaeha** is in his vest. A thin nosebleed from P02; after the CARRY hit (P42) it bleeds again; Yerin's healing stops it (P51), but dried blood stays on his lip and chin to the end. Pencil behind the RIGHT ear, fringe over the LEFT eye. The notebook is in his LEFT chest pocket until P25, then in his hands or under his left arm (and the pocket is empty).
- **The knight's tell:** his cracked, loose LEFT pauldron, on the picture-right side when he faces us, dips before every sweep. Reference: `knight_commander/front.png`.
- **The pillar** Jaeha and Yerin hide behind stays the same pillar from P05 to the end.
- **Effects:** LINK and CARRY are amber (Nib's colour): a thin amber thread of light (P26), the split-frame `link-view` (P27), the amber impact ring of CARRY (P41–P42). Yerin's healing is soft mint-white, never cyan. The `plan` panel (P32) has clean cyan tactical lines with no text.
- **Window space:** P06, P18, P22, P26, P36, P39, P42, P49 and P53 carry system windows near the top. That area is the dark hall (or plain background) fading naturally: never a flat rectangle, never across a head.
- **Strips** (P29, P33, P40, P47) are drawn edge to edge at 1536×1024; the letterer shows the middle half.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P01 continues chapter 1's last panels: you may pass `chapters_v2/ch001/art/P62.png` as the one continuity reference. P07 is Nib's name card. |
| `B` | P08–P14 | No art for P15 (`title`). |
| `C` | P16–P22 | P16 is the establishing shot of the hall from high above. |
| `D` | P23–P29 | P26 is the LINK window panel; P27 is the split-frame `link-view`; P29 is Nib's point of view (thin amber vignette). |
| `E` | P30–P36 | P32 is the `plan` panel. |
| `F` | P37–P43 | P42 is the `carry` recipe. |
| `G` | P44–P50 | P47 is an extreme close-up strip of Nib's uncovered eye. |
| `H` | P51–P56 | P54: the knight's roar. |
| `I` | P57–P60 and `END.png` | P57 is the sigil close-up through Nib's eyes. END: chibi gag on plain white. |

### Chapter 1 parts (done)

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
