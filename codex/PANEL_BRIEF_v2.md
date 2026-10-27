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
- Take up to 5 tries per panel; if it still fails, keep the best and note its faults in your DONE file (README_START_HERE, 27 October). A targeted edit of your own kept image is allowed: crop, edit, then composite back at the original pixel size.
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

### Chapter 3: The Ninth Wall (`scripts_v2/ch003.yaml`)

**Chapter 3 rules:**
- **The flashback (P01–P08) is drawn in greys,** a memory: desaturated blue-grey and stone, with ONE warm colour, Kett's mustard scarf. Hush-spawn are black shapes leaking violet ash. In the flashback Nib has no mask and wears the Ninth Wall's colours (rendered in grey); use `nib/front_seal2_nomask.png`. Kett: `kett/front.png` (about 95 cm). The commander is the knight BEFORE he was hushed: intact armour, the sigil, a whole cloak, a CLOSED great helm with a visor slit and NO face-hole; his face is never shown. Location: `locations_v2/ninth_wall/key.png`.
- **Present day (P10–P63):** the boss room as in chapter 2. Nib in rest form from P14 to P47 (dull eyes, no glow, no outline); field form and LINKED from P49; his seal 2/5 look from P51 (`nib/turnaround_seal2.png`). The husk mask stays on in the present day.
- **The trap (P20–P47):** the side archway is about 7 m high, with a rusted iron portcullis hanging in its groove; the two pillars flanking it have rows of spike holes; the square pressure plates lie in front of it. The knight (4.5 m) fits under the arch kneeling.
- **Scale and perspective (section 4b)** are checked on every panel, the wide shots above all: P01, P16, P19, P22, P27, P30, P45, P47.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | The grey flashback. No art for P09 (`caption`). |
| `B` | P10–P17 | P10 is back in colour. |
| `C` | P19–P26 | No art for P18 (`title`). P22 is the overhead `plan` view of the trap. |
| `D` | P27–P34 | The trap springs. |
| `E` | P35–P41 | |
| `F` | P42–P48 | |
| `G` | P49–P55 | P53 is the seal 2/5 splash: make it count. |
| `H` | P56–P63 and `END.png` | |

### Chapter 4: Harvest or Release (`scripts_v2/ch004.yaml`)

**Chapter 4 rules:** Nib has his seal 2/5 look (`nib/turnaround_seal2.png`) with the husk mask, field form and LINKED until P51, rest form (and wrapped in a gold foil blanket) from P52. The knight's face-hole holds a real face for ONE panel (P28): an old soldier's, scarred and grey-bearded (`knight_commander/` for the armour). The gate exit uses `locations_v2/gate_exit/key.png` and Choi Dongmin's sheets. The billboard (P56) is flat #00FF00; P57 shows the broadcast itself, Mok at a podium in a black suit, with the bottom quarter plain for the news graphic.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | |
| `B` | P09–P14 | No art for P15 (`title`). P13 is the kill splash. |
| `C` | P16–P23 | P18 is a desaturated memory inset. |
| `D` | P24–P31 | P27–P31: the release; P28 is the one real face. |
| `E` | P32–P38 | P38 is chibi. |
| `F` | P39–P45 | Window panels: leave the window areas as the dark hall. |
| `G` | P46–P52 | P49 is the dive-out splash. |
| `H` | P53–P60 and `END.png` | |

### Chapter 5: A Few Words at My Memorial (`scripts_v2/ch005.yaml`)

**Chapter 5 rules:** Jaeha is bandaged (forehead bandage, gauze on his right cheekbone, left hand wrapped). Nib has his seal 2/5 look with the mask, rest form all chapter, and stands like a doll in public. Mok wears a black suit and tie at the memorial. P03 is Bomi's glamour intro: her full design, a beautiful face, a confident full-figure pose, never a low angle up her shorts (fan-service rules at the top of `CHARACTER_DESIGNS_v2.md`). Seoa (15) is never drawn with any fan service. Baek is seen only from behind, in silhouette, or as a reflection; his face is never shown. Locations: `memorial_hall`, `rooftop_room` (key_day, key_night, interior), `kanghan_monitor`.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P03: Bomi's glamour intro. |
| `B` | P08–P14 | No art for P15 (`title`). |
| `C` | P16–P23 | |
| `D` | P24–P31 | |
| `E` | P32–P39 | P33 is Seoa's name card. |
| `F` | P40–P47 | P44 is chibi. |
| `G` | P48–P53 | |
| `H` | P54–P59 and `END.png` | Kanghan: Baek from behind only. |

### Arc 2 sheets come first
Chapters 6–12 need the Arc 2 sheets and keys in `ASSETS_ARC2_BRIEF.md` (Borro S16, Baek S17, the neighbours S18, Moon Ahin's husks S19, the monsters M1–M4 with the swarm mother and the alpha, the places L6–L12). A part may start only when every sheet it names exists and has a `DONE.md`. Every Arc 2 sheet carries a faint 178 cm silhouette: use it to check the scale of every monster and giant in your panels (section 4b). Nib's seal 2/5 sheets carry none, like his base sheets: his height comes from `scale_chart_v2.png` (his head reaches a 178 cm man's belt).

### Chapter 6: Trap Rats (`scripts_v2/ch006.yaml`)

**Chapter 6 rules:** Jaeha has a small plaster on his right cheekbone and no other bandages. Nib has his seal 2/5 look with the mask and plays a husk in public (stiff, arms hanging); field form and LINKED (amber) only P26–P36. Ash rats: `ash_rat/` (70 cm, knee-high); the swarm mother P38–P40: `ash_rat/swarm_mother.png` (1.4 m, her back just above a man's hip); attach `ash_rat/scale_card.png` whenever a person or Nib shares the panel with them. The sewer: `sewer_gate/key.png` inside, `outside.png` at dusk (P44–P51). The landlady (P52–P54): `neighbourhood/lineup.png`, on `rooftop_room/stairs_night.png`. Bomi's room (P55–P60): `bomi_room/outside.png` and `interior.png`. P07 and P47 carry phone live-stream overlays: keep those areas calm. Bomi: never a low angle up her shorts.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | P02 strip. P06 is chibi. P07: the drone's point of view, left half calm for the stream overlay. |
| `B` | P09–P17 | P15 the tripwire insert; P16 the net impact. No art for P18 (`title`). |
| `C` | P19–P26 | P20: the swarm's reveal. P25 strip: the drone in the empty tunnel. P26: the window panel (field form starts). |
| `D` | P27–P34 | P27–P28: Nib's whirl in field form; P33 is the `plan` panel. |
| `E` | P35–P42 | P38: the swarm mother. P41: the boss window (two windows, keep the top half dark vault). |
| `F` | P43–P51 | Outside at dusk. P46 is an extreme close-up strip of Jaeha's eyes. |
| `G` | P52–P60 and `END.png` | The landlady on the stairs, then Bomi's room. P60 is the ECU strip of Bomi's eyes. |

### Chapter 7: Ten Thousand Won a Trap (`scripts_v2/ch007.yaml`)

**Chapter 7 rules:** At home in the morning (P01–P16) Jaeha wears the hoodie only, and Nib has no mask in P01–P02 (`nib/front_seal2_nomask.png`); he slaps the mask on in P03. The vest is slashed through the T patch from P42 (one long straight cut). Choi: `choi_dongmin/`. The survey gate: `survey_gate/outside.png` (P18), `key.png` (P23), `trap_chamber.png` (P28–P56); the exit: `survey_gate/exit_dusk.png` (P57). The two saboteurs are generic (script continuity): the shield-bearer is Black Hound hunter 6 from chapter 1. The grain is clean bright gold against centuries of grey dust: that contrast is the clue, so keep it readable. P72 (the memory) is grey with one colour, the red sky.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | The rooftop morning; P03 is the mask-slap gag. |
| `B` | P09–P16 | No art for P17 (`title`). P15 is the notebook insert. |
| `C` | P18–P25 | P22 ECU strip; P25 is a `link-view` split frame. |
| `D` | P26–P33 | P29 is Nib's point of view; P32 is the `plan` panel. |
| `E` | P34–P41 | P35 is the grain-fall splash. |
| `F` | P42–P49 | P42 the sword through the vest; P45 strip (the notebook snapping shut). |
| `G` | P50–P58 | The bluff, the confession; the exit at dusk from P57. |
| `H` | P59–P66 | The deal with Bomi; P65 is chibi; P66 the Kanghan watcher. |
| `I` | P67–P72 and `END.png` | The vest at night; P71 ECU strip of Seoa's eyes; P72 the grey memory. |

### Chapter 8: Eyes (`scripts_v2/ch008.yaml`)

**Chapter 8 rules:** Gomi the cat: `neighbourhood/gomi.png` with `neighbourhood/scale_card.png` (60 cm long; standing, her ears reach just over half Nib's height), huge and fat next to Nib; never take her size from `lineup.png`, which draws her too big. Nib is in rest form (no glow) except P42–P55. Through-the-eyes panels (P02, P14, P16, P17) carry a thin amber vignette. The Han River enclosure: `hanriver_gate/key.png` and `bank_dusk.png`, at the blue hour with the bridge lights coming on. The car park: `carpark_gate/key.png`; the ramp is 30 m long and 6 m wide, its lower third wet. The drowned hound: `drowned_hound/` with `drowned_hound/scale_card.png` (1.7 m at the shoulder, level with Jaeha's eyes; with its head up it stands a head taller than him). The vest has Seoa's red stitches on the back patch from P25; the bite bandage on Jaeha's LEFT forearm from P47 (the bite is P38).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P11 | P01 high over Mangwon's roofs; P09 the LINK LV. 3 window; P11 strip. No art for P12 (`title`). |
| `B` | P13–P20 | The enclosure under the bridge; P14 and P16 are `link-view` panels. |
| `C` | P21–P27 | P23 is chibi; P25 the car park from the top of the ramp. |
| `D` | P28–P35 | P32 is the `plan` panel. |
| `E` | P36–P43 | P36 the hound's reveal; P41 ECU strip; P42 field form window. |
| `F` | P44–P51 | P48 the kill splash. |
| `G` | P52–P58 | Windows on P52, P53 and P57: keep the top half dark. |
| `H` | P59–P70 and `END.png` | The landlady (P59–P60), the dinner, the hook windows (P66, P67, P69); P65 strip; P70 ECU strip. |

### Chapter 9: Not Yet, Operator (`scripts_v2/ch009.yaml`)

**Chapter 9 rules:** Jaeha wears the hoodie (no vest) and the forearm bandage, at home and in the Call. Nib has no mask all chapter. The Call: `call_void/key.png`, an endless plane of still black water under a starless sky, the rifts 8 m tall and 30–60 m away (Jaeha is a speck in wide shots). The bell silhouette (P25–P29) is only ever a black silhouette against fire (`CHARACTER_DESIGNS_v2.md` 2.15). The river rift and the ward rift (P20–P21) show figures from behind only. The Hush (P38–P53) is the black water and one many-jointed black hand on Jaeha's RIGHT ankle; frost spreads from that ankle in the real room. The glitch window (P40) has offset red and blue fringes. No art for P05 (`caption`) or P16 (`title`).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P04, P06–P10 | The frozen room (P01–P04), then the warm room ten minutes earlier. P03 ECU strip. |
| `B` | P11–P15 | P15 is the CALL button insert. |
| `C` | P17–P24 | P17 the Call from 30 m up; P22 the offer window. |
| `D` | P25–P32 | P28 is the bell splash; P29 the [DECLINED] window. |
| `E` | P33–P40 | P35 the TERMS window; P36 ECU strip; P40 the glitch. |
| `F` | P41–P49 | The real room (P41) and the hand pulling him under. |
| `G` | P50–P57 and `END.png` | The countdown; P56 the hill that breathes; P57 the eyes opening (ECU strip). |

### Chapter 10: A Roof, Not a Garden (`scripts_v2/ch010.yaml`)

**Chapter 10 rules:** Borro arrives: `borro/` sheets. He is 2.4 m: in the rooftop room (ceiling 2.2 m) he must stoop or sit; on the rooftop he is taller than the water tank (2 m); Jaeha reaches his chest. His husk face (a white oval with two small eye-holes, tied with cord) is on in public from P25. Field form: moss-green eyes and outline (P44–P57). P12 is the bed-crushing splash (the metal bed folds flat). P15 is Borro's name card (full figure, name-card gradient dark slate to moss green). The tower: `tower_gate/outside.png` and `key.png`; the long beam is 60 cm wide and the slabs either side are cracking away; the drop is several floors. Ash hounds: `ash_hound/` (hip-high); the alpha: `ash_hound/alpha.png` (its shoulder level with a man's chin); attach `ash_hound/scale_card.png`. P37 is a three-way split `link-view`. Jaeha's RIGHT ankle bruise (P20–P21): long, thin, many-jointed finger marks.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | The last three seconds of the Call. |
| `B` | P08–P13 | P09 the hand reaching out; P12 the bed-crushing splash. No art for P14 (`title`). |
| `C` | P15–P21 | P15 Borro's name card; P16 the summon window. |
| `D` | P22–P29 | The landlady (P22); the tower (P25 outside, P28 inside). |
| `E` | P30–P37 | P32 the pack and the alpha; P35 `plan`; P37 three-way `link-view`. |
| `F` | P38–P45 | P40 `carry`; P45 the shield-heave splash. |
| `G` | P46–P53 | P46 `carry` (the gash on his RIGHT shoulder); P50 the throat strike. |
| `H` | P54–P61 | The aftermath and the windows; outside at dusk from P59. |
| `I` | P62–P66 and `END.png` | P62 ECU strip; P64 the smoke over Mangwon. |

### Chapter 11: Market Break (`scripts_v2/ch011.yaml`)

**Chapter 11 rules:** The market: `mangwon_market/key.png`, `fish_lane.png` and `footbridge.png`. The alleys are 1.5–2 m wide: Borro's shield fills one wall to wall; the hounds come single file. The footbridge is 30 m long, 5 m over a four-lane road, with one central pier; in the P48 splash Borro holds it up from the heaved road (his shell and shoulders under the deck). The grannies: `neighbourhood/lineup.png`. Seoa is in charge, never rescued: she leads and counts people, the rice-cake bag always on her wrist; never any fan service. Bomi's drone breaks at P57; no drone after that. Nib: field form P15–P53, rest form P54–P60, field form again from P61. The serpent appears only at the very end (P72–P73): `marsh_serpent/` and `scale.png` (its head as high as a third floor).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P07 is a jagged split two-shot. |
| `B` | P08–P13 | P08 ECU strip; P12 the break-rule window. No art for P14 (`title`). |
| `C` | P15–P21 | P15 window; P18 the drone's overhead view; P20 `plan`. |
| `D` | P22–P29 | Borro's square; the radish (P27, a comic BONK). |
| `E` | P30–P37 | P36 the second wave's reveal. |
| `F` | P38–P45 | The footbridge from P40 (high wide shot). |
| `G` | P46–P53 | P48 is the chapter's biggest image: Borro holding the bridge. P50 ECU strip. |
| `H` | P54–P61 | P57 the drone's sacrifice; P58 the stream's SIGNAL LOST. |
| `I` | P62–P68 | P64 the bridge's fall (splash). |
| `J` | P69–P73 and `END.png` | P70 ECU strip; P72 the serpent bursts out of the road. |

### Chapter 12: His Summons Go First (`scripts_v2/ch012.yaml`)

**Chapter 12 rules:** The serpent spits scalding steam; Borro's shield glows dull red where it hits (P04–P14). In the freezer lane (`fish_market/key.png`) frost spreads over the serpent's scales and it slows: frost means it is failing. Jaeha's palms are blistered red from P05 and plastered from P43. Baek's face is shown for the first time in P50 (his name card: full figure, name-card gradient black to smoky violet); before that only his tower. P56 is Moon Ahin's glamour panel: her full design (`moon_ahin/` sheets), a beautiful cold face, a confident full-figure pose, the camera level, never aimed up the slit; her husks: `ahin_husk/`. The Kanghan guild hall: `kanghan_guild_hall/key.png`. Bomi's new drone has a pink ribbon (from P43). Bomi's parents: `neighbourhood/lineup.png`.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P05 `carry` (blistering palms). |
| `B` | P08–P14 | P08 ECU strip; P11 `plan`. No art for P15 (`title`). |
| `C` | P16–P22 | The freezer lane; P21 the shield-door splash. |
| `D` | P23–P29 | P28 the serpent's death (full splash). |
| `E` | P30–P36 | Windows on P30, P31 and P33. |
| `F` | P37–P43 | P37 a TV with a #00FF00 screen; the school; the radish granny; Bomi's restaurant. |
| `G` | P44–P49 | P45 is chibi; P49 Kanghan Tower. |
| `H` | P50–P56 | P50 Baek's name card; P54 strip; P56 Moon Ahin's glamour panel. |
| `I` | P57–P63 | The husks turn; the rooftop dinner. |
| `J` | P64–P70 and `END.png` | P68 ECU strip; P70 the last panel. |

### Arc 3-4 sheets come first
Chapters 13-33 need the sheets, keys and props in `ASSETS_ARC3_BRIEF.md` (Han Sora S20, Nib's seal 3/5 S21, Minseok S22, the crew and Kanghan staff S23, Auntie Geum S24, the Arcs 3-4 cast S25, the monsters M5-M9, the places L13-L20 and the props sheet P1). A part may start only when every sheet it names exists and has a `DONE.md`. Every sheet carries a faint 178 cm silhouette: use it to check the scale of every giant and monster (section 4b). Fan service as in chapters 6-12: Lyra, Moon Ahin, Han Sora and Bomi get confident glamour panels, never a camera aimed up a skirt, down a top or at the chest; Seoa (15), Yerin and Dami's daughter never.

### Chapter 13: The Hearing (`scripts_v2/ch013.yaml`)

**Chapter 13 rules:** Jaeha wears the vest with the collar of a borrowed white shirt showing (Seoa insisted), plasters on both palms, the bite bandage on his LEFT forearm. Nib (seal 2/5, mask) and Borro (husk face) stay in rest form all chapter and play husks, badly: stiff, arms hanging; Borro ducks under every doorway. Places: `assoc_lobby/key.png`, `assoc_hearing_room/key.png`, `assoc_arena/key.png`. The training construct: `training_construct/` (4 m; Jaeha reaches its hip; it moves on rails of light). Mok wears a navy suit with the small red hound's-head pin. Inspector Ryu, the lawyer and the guard: `arc3_cast/lineup.png`. The crossbow woman in the gallery is Han Sora in her Black Hound look (`han_sora/`), the brass compass in her lap at the hook.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | No art for P10 (`title`). |
| `B` | P11–P17 | - |
| `C` | P18–P24 | P22 ECU strip |
| `D` | P25–P30 | - |
| `E` | P31–P38 | P32 window (keep the top half calm); P33 phone screen #00FF00; P34 ECU strip |
| `F` | P39–P46 | P41 `carry`; P42 `plan` |
| `G` | P47–P54 | P47 phone screen #00FF00; P51 phone screen #00FF00 |
| `H` | P55–P60 | P58 `chibi` |
| `I` | P61–P66 and `END.png` | P65 strip |

### Chapter 14: The Compass (`scripts_v2/ch014.yaml`)

**Chapter 14 rules:** Han Sora's first glamour panel (P03) and name card (P05): `han_sora/` Black Hound look, the compass on its chain round her RIGHT wrist; never a camera aimed at her chest. Jaeha wears the hoodie only (no vest), the notebook in the hoodie's front pocket. Nib wears the mask at the store and none at home; he flashes into field form for one second under the table twice (P17, P19: an amber eye, a thin amber outline). The store at night: `conv_store/key.png`. The flashback (P38-P44) is grey with only the two orange vests in colour: `hanriver_gate_flashback/key.png`, Minseok and the young cast in `oh_minseok/`.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P02 strip; P03 splash; P05 name card; P06 ECU strip |
| `B` | P08–P12 | No art for P13 (`title`). |
| `C` | P14–P19 | P14 ECU strip; P16 `link-view` |
| `D` | P20–P24 | - |
| `E` | P25–P32 | P27 `chibi`; P29 phone screen #00FF00; P30 ECU strip |
| `F` | P33–P40 | P38 strip |
| `G` | P41–P47 | P44 strip |
| `H` | P48–P54 | P52 ECU strip |
| `I` | P55–P60 and `END.png` | P58 strip; P59 phone screen #00FF00 |

### Chapter 15: Pass (`scripts_v2/ch015.yaml`)

**Chapter 15 rules:** The aqueduct gate: `aqueduct_gate/outside.png` and `key.png`: one stone channel 6 m wide on tall arches over a gorge under a pale yellow sky, one way in and one way out. The basalt boar: `basalt_boar/` (its shoulder a head above Borro's head; it lowers its head three strides before it hits). Nib (amber) and Borro (moss green) are in field form most of the chapter. Bomi's new drone with the pink ribbon stays OFF in her hands. P34 is the PASS splash.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P01 the reveal; P03 window (keep the top half calm); P06 `carry` |
| `B` | P08–P12 | No art for P13 (`title`). |
| `C` | P14–P19 | P15 `carry`; P16 ECU strip |
| `D` | P20–P25 | P24 `carry` |
| `E` | P26–P30 | P29 `plan`; P30 window (keep the top half calm) |
| `F` | P31–P37 | P33 strip; P34 splash |
| `G` | P38–P44 | P40 window (keep the top half calm); P41 window (keep the top half calm); P44 `chibi` |
| `H` | P45–P50 | P48 window (keep the top half calm); P50 window (keep the top half calm) |
| `I` | P51–P55 | P51 window (keep the top half calm); P53 ECU strip |
| `J` | P56–P60 and `END.png` | P58 window (keep the top half calm) |

### Chapter 16: The Hero Raid (`scripts_v2/ch016.yaml`)

**Chapter 16 rules:** The dam spillway: `dam_gate/key.png` (press tents, cameras, the rope line); the drowned cathedral: `drowned_cathedral/key.png`, `crypt.png`, `doors.png`. Black Hound in clean jackets; the sealers carry the Kanghan stake (`props_v2/arc3/props.png`). Jaeha carries a box of chalk; his chalk arrows mark every junction, and one points the wrong way. Nib stays in rest form (Sora's compass is near); Borro is in field form only P35-P42; Bomi's drone hides in Borro's moss from P61, its lens peeking out between the flowers.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | P05 phone screen #00FF00 |
| `B` | P07–P10 | P10 ECU strip; No art for P11 (`title`). |
| `C` | P12–P18 | P13 window (keep the top half calm) |
| `D` | P19–P25 | P23 strip |
| `E` | P26–P30 | - |
| `F` | P31–P38 | P35 window (keep the top half calm); P37 splash; P38 `carry` |
| `G` | P39–P45 | - |
| `H` | P46–P53 | - |
| `I` | P54–P60 | P55 `link-view` |
| `J` | P61–P68 and `END.png` | P68 ECU strip |

### Chapter 17: Thirty Seconds (`scripts_v2/ch017.yaml`)

**Chapter 17 rules:** The bell chamber: `boss_chamber_bells/key.png` (intact). The stake's web of violet light spreads over the bronze doors. The Drowned Bell-Ringer: `bell_ringer/` (6 m: Borro reaches its waist, Jaeha its knee); its toll is a ring of force a step beyond its reach (`toll.png`). Mok is soaked from P03. Splashes P30 and P52; the enrage timer windows keep the top half calm.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | - |
| `B` | P09–P15 | No art for P16 (`title`). |
| `C` | P17–P24 | P21 the reveal; P22 window (keep the top half calm); P24 window (keep the top half calm) |
| `D` | P25–P32 | P27 `carry`; P30 splash |
| `E` | P33–P40 | P39 phone screen #00FF00 |
| `F` | P41–P47 | P46 `carry` |
| `G` | P48–P54 | P52 splash |
| `H` | P55–P60 | P59 window (keep the top half calm) |
| `I` | P61–P66 and `END.png` | P62 window (keep the top half calm); P64 window (keep the top half calm); P65 ECU strip |

### Chapter 18: Lyra (`scripts_v2/ch018.yaml`)

**Chapter 18 rules:** The Call: `call_void/key.png`, with only the river rift open (a wide river under a silver sky). Lyra's arrival splash (P33, full height) and name card (P38): `lyra/` sheets, a confident entrance, never aimed up her skirt; Jaeha flustered, Nib flat. Borro is buried to the waist in rubble from P05, still holding the shield up, the drone in his moss. Nib's field form ends at P45.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P01 window (keep the top half calm); P03 `carry` |
| `B` | P08–P12 | P08 window (keep the top half calm); No art for P13 (`title`). |
| `C` | P14–P19 | P14 window (keep the top half calm) |
| `D` | P20–P25 | P24 strip |
| `E` | P26–P31 | P31 window (keep the top half calm) |
| `F` | P32–P38 | P33 splash; P35 phone screen #00FF00; P38 name card |
| `G` | P39–P45 | P41 window (keep the top half calm); P45 window (keep the top half calm) |
| `H` | P46–P50 | P49 window (keep the top half calm); P50 strip |
| `I` | P51–P57 | P51 ECU strip |
| `J` | P58–P64 and `END.png` | P63 ECU strip |

### Chapter 19: Borrowed Thunder (`scripts_v2/ch019.yaml`)

**Chapter 19 rules:** The chamber is ruined from P10: `boss_chamber_bells/ruined.png` (half the dome fallen, shafts of light, the doorway 6 m up the back wall with no stair). Lyra's first arrow stays wedged in the bell's crack from P07. Mok holds Jaeha up from behind for the second try. P34 is the Borrowed Thunder splash. Sora appears in the high doorway at the end.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | P01 window (keep the top half calm); P02 `carry`; P04 `carry` |
| `B` | P07–P11 | P10 splash; No art for P12 (`title`). |
| `C` | P13–P19 | - |
| `D` | P20–P26 | P24 window (keep the top half calm) |
| `E` | P27–P33 | - |
| `F` | P34–P38 | P34 splash |
| `G` | P39–P44 | P40 window (keep the top half calm); P41 window (keep the top half calm); P44 window (keep the top half calm) |
| `H` | P45–P50 | P47 phone screen #00FF00; P49 window (keep the top half calm) |
| `I` | P51–P55 | - |
| `J` | P56–P60 | P57 ECU strip |
| `K` | P61–P65 and `END.png` | - |

### Chapter 20: Three of Five (`scripts_v2/ch020.yaml`)

**Chapter 20 rules:** `boss_chamber_bells/ruined.png`, with two ropes hanging from the high doorway from P03. Mok's second team: six hunters (two swords, a spear, an archer, a core-staff mage, the ch 7 shield-bearer). Only Nib is in field form; every hit he takes opens on Jaeha: LEFT upper arm (P23), RIGHT thigh (P27), RIGHT forearm (P31), cheek (P35). P41 is the seal 3/5 armour splash: `nib/turnaround_seal3.png`. Minseok's phone in its cracked orange case: `props_v2/arc3/props.png`.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | - |
| `B` | P07–P10 | P08 window (keep the top half calm); P10 ECU strip; No art for P11 (`title`). |
| `C` | P12–P20 | P13 window (keep the top half calm); P18 strip; P20 `carry` |
| `D` | P21–P27 | P23 `carry`; P27 `carry` |
| `E` | P28–P34 | P31 `carry` |
| `F` | P35–P39 | P35 `carry`; P39 ECU strip |
| `G` | P40–P45 | P40 window (keep the top half calm); P41 splash |
| `H` | P46–P51 | - |
| `I` | P52–P56 | P53 splash |
| `J` | P57–P61 | - |
| `K` | P62–P66 and `END.png` | P62 ECU strip; P66 phone screen #00FF00 |

### Chapter 21: Ask Him (`scripts_v2/ch021.yaml`)

**Chapter 21 rules:** The climb up the ropes (P03), the collapsing passage (P04), then the spillway at midday (`dam_gate/key.png`). Jaeha is bandaged and carried on Yerin's back P03-P05; the head-sized core rides in a sling on his chest. Nib wears the seal 3/5 armour from now on. P09 is Lyra's glamour flourish, framed from the knees up. Bomi's drone lifts out of Borro's moss at P17. P35 is the ECU of Mok's eyes. The video (P44-P52) is drawn as a shaky phone image: Minseok close, lit by his phone, no rim in view. Police: `arc3_cast/lineup.png`. The rooftop (P64) and Baek's office with the blinds half down (P65-P67, `kanghan_office/day.png`).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | - |
| `B` | P08–P12 | No art for P13 (`title`). |
| `C` | P14–P18 | - |
| `D` | P19–P23 | - |
| `E` | P24–P30 | P29 phone screen #00FF00 |
| `F` | P31–P37 | P35 ECU strip; P36 phone screen #00FF00 |
| `G` | P38–P43 | P42 phone screen #00FF00; P43 strip |
| `H` | P44–P49 | - |
| `I` | P50–P55 | P51 strip; P54 phone screen #00FF00 |
| `J` | P56–P63 | - |
| `K` | P64–P67 and `END.png` | - |

### Chapter 22: The Last Seconds (`scripts_v2/ch022.yaml`)

**Chapter 22 rules:** P01-P03 are news footage drawn as TV images with the bottom fifth calm for the lower third; P04 is the store's TV (#00FF00). Jaeha is bandaged and limps with a walking stick at the columbarium (`columbarium/key.png`, `niche.png`). P24 is the grey memory: young Mok slipping the orange phone out of young Jaeha's vest. The rooftop party at dusk: `rooftop_room/party_dusk.png`; P32 chibi; Bomi's glamour leap (P33, from the knees up) and Lyra on the water tank (P40). Moon Ahin conducts alone in the guild hall (P47 glamour; `kanghan_guild_hall/key.png`, `ahin_husk/formation.png`). P56 is the video's last seconds: pier 7 through the white shimmer of the rim (`hanriver_gate/pier7.png`).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | P01 TV footage (keep the bottom fifth calm); P02 TV footage (keep the bottom fifth calm); P03 TV footage (keep the bottom fifth calm); P06 phone screen #00FF00 |
| `B` | P07–P10 | No art for P11 (`title`). |
| `C` | P12–P19 | - |
| `D` | P20–P27 | P23 strip |
| `E` | P28–P33 | P32 `chibi` |
| `F` | P34–P39 | P34 phone screen #00FF00; P36 phone screen #00FF00 |
| `G` | P40–P45 | - |
| `H` | P46–P50 | P46 strip; P48 phone screen #00FF00 |
| `I` | P51–P58 | P55 strip; P57 ECU strip; P58 `link-view` |
| `J` | P59–P66 and `END.png` | P60 phone screen #00FF00; P66 strip |

### Chapter 23: Under the Bridge (`scripts_v2/ch023.yaml`)

**Chapter 23 rules:** P01-P10 are through Nib's eyes in a thin amber vignette, over `hanriver_gate/inside_fence.png` and `pier7.png`. From P26 the crew kit: `crew/lineup_kit.png` (Jaeha is number 4); Pyo's name card at P28. P35 is underwater: Borro walking on the riverbed, Lyra swimming beside him, graceful. P38 is the canyon splash (`farm_canyon/key.png`); the walkways and trap stones: `farm_canyon/walkway.png`. Foreman Gu and the engineers: `crew/kanghan_lineup.png`. Moon Ahin arrives at the end with her forty husks (`ahin_husk/`).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | P01 `link-view`; P03 `link-view`; P04 `link-view`; P06 phone screen #00FF00 |
| `B` | P07–P10 | P07 `link-view`; No art for P11 (`title`). |
| `C` | P12–P18 | P16 `plan` |
| `D` | P19–P24 | - |
| `E` | P25–P32 | P28 name card |
| `F` | P33–P40 | P38 splash; P40 `link-view` |
| `G` | P41–P47 | P44 window (keep the top half calm); P45 ECU strip |
| `H` | P48–P54 | - |
| `I` | P55–P61 | P60 strip |
| `J` | P62–P66 and `END.png` | P66 strip |

### Chapter 24: The Puppeteer (`scripts_v2/ch024.yaml`)

**Chapter 24 rules:** Moon Ahin's name card is a tall full-figure glamour panel (P02); then the visor-fog gag (P03) and Nib's flat stare (P04). Canyon wyverns: `canyon_wyvern/` (dog-sized bodies, 4 m wings), diving in a flock. P21: three husks fall away still in formation; P22: the ECU of her eyebrow twitching. Nib in field form P25-P36. P47 is Lyra on Borro's shell in the river. The carved coral giant (P48, `farm_canyon/relief.png`); the locked grille and the cleft from P50.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | P02 name card; No art for P10 (`title`). |
| `B` | P11–P18 | P16 the reveal |
| `C` | P19–P26 | P22 ECU strip |
| `D` | P27–P32 | P30 `plan`; P32 `carry` |
| `E` | P33–P38 | P36 window (keep the top half calm) |
| `F` | P39–P44 | - |
| `G` | P45–P52 | - |
| `H` | P53–P60 and `END.png` | P53 strip; P58 `link-view`; P60 strip |

### Chapter 25: Same Kind (`scripts_v2/ch025.yaml`)

**Chapter 25 rules:** The ladder down the cleft, then `farm_canyon/pipe_gallery.png`, `junction.png` and `glass_wall.png`. Borro and Lyra join at P12, out of a side channel of water. Ash hounds: `ash_hound/`; the alpha howls before the pack moves. P41 is the Borrowed Thunder splash through the pinned alpha. No. 17 shatters (P38). A smudge of dust on Moon Ahin's white coat-dress.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | No art for P10 (`title`). |
| `B` | P11–P18 | - |
| `C` | P19–P25 | - |
| `D` | P26–P33 | P27 `plan`; P30 the reveal; P33 window (keep the top half calm) |
| `E` | P34–P41 | P36 the reveal; P40 `carry`; P41 splash |
| `F` | P42–P47 | - |
| `G` | P48–P54 | - |
| `H` | P55–P60 and `END.png` | P58 ECU strip |

### Chapter 26: Core Farm (`scripts_v2/ch026.yaml`)

**Chapter 26 rules:** The side passage and the iron door from the ch 14 flashback, propped open with cables through it; the scratched words are added by the letterer as a label (P09). P06 is the grey memory. P15 is the pit splash: `farm_pit/key.png` with the Warden (`tide_warden/`, eyes closed until his lid lifts at P59). The chain-link comparison (P32-P35, props sheet). Red alarm light from P53: `farm_pit/alarm.png`.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P05 strip |
| `B` | P08–P12 | No art for P13 (`title`). |
| `C` | P14–P21 | P15 splash; P16 window (keep the top half calm) |
| `D` | P22–P29 | - |
| `E` | P30–P37 | P30 `plan`; P31 ECU strip; P32 `link-view` |
| `F` | P38–P44 | - |
| `G` | P45–P52 | P51 phone screen #00FF00 |
| `H` | P53–P60 and `END.png` | P55 strip; P57 `link-view` |

### Chapter 27: Alarm (`scripts_v2/ch027.yaml`)

**Chapter 27 rules:** The great drain half-pipe along the pit wall: `farm_pit/drain_pipe.png`. Sora returns in Kanghan colours (`han_sora/turnaround_kanghan.png`) with the tactical squad (`crew/kanghan_lineup.png`): a tall glamour panel stepping off the elevator (P11), and soaked after the flood (P37, from the knees up). P36 is the flood splash. The Warden's eye opens (ECU) and he speaks; to humans it is only a hum.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | P01 `plan`; No art for P10 (`title`). |
| `B` | P11–P17 | - |
| `C` | P18–P24 | P18 `carry` |
| `D` | P25–P31 | P28 `carry` |
| `E` | P32–P37 | P36 splash |
| `F` | P38–P45 | - |
| `G` | P46–P53 | P46 ECU strip; P47 the reveal |
| `H` | P54–P60 and `END.png` | P54 strip |

### Chapter 28: Not Equipment (`scripts_v2/ch028.yaml`)

**Chapter 28 rules:** Moon Ahin's video (P23-P31): her phone in her RIGHT hand, the recording screen drawn plainly with a red dot, and what it shows drawn inside its frame. P18 is a soft sea-green memory: Minseok sitting cross-legged at the Warden's feet. P36 is the splash of Borro tearing out the pipe. The rim's iris closing far above (P44). The drain tunnels from P52: `farm_drains/key.png`.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P06 window (keep the top half calm); P07 ECU strip |
| `B` | P08–P14 | - |
| `C` | P15–P20 | No art for P21 (`title`). |
| `D` | P22–P26 | - |
| `E` | P27–P31 | P31 strip |
| `F` | P32–P38 | P33 ECU strip; P36 splash; P37 `carry` |
| `G` | P39–P44 | P43 window (keep the top half calm) |
| `H` | P45–P52 | - |
| `I` | P53–P60 and `END.png` | P59 window (keep the top half calm) |

### Chapter 29: Sandbags (`scripts_v2/ch029.yaml`)

**Chapter 29 rules:** The drain tunnel's arches and keystones; the slab on Borro; P16 shows three threads pouring into Jaeha at once. Draw a soft grey vignette on Jaeha's point-of-view panels from P17. The crew lever the slab off Borro (P30). The shaft and the barricade of shields at the top: `farm_drains/shaft.png` (P52-P60).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P02 window (keep the top half calm); P05 `carry` |
| `B` | P08–P10, P12–P14 | P08 `plan`; No art for P11 (`title`).; P12 window (keep the top half calm); P14 window (keep the top half calm) |
| `C` | P15–P21 | P15 ECU strip; P16 `carry`; P17 `link-view`; P20 window (keep the top half calm) |
| `D` | P22–P29 | P23 window (keep the top half calm) |
| `E` | P30–P37 | P37 window (keep the top half calm) |
| `F` | P38–P45 | - |
| `G` | P46–P53 | P47 window (keep the top half calm) |
| `H` | P54–P60 and `END.png` | P54 strip; P59 window (keep the top half calm) |

### Chapter 30: The Rim (`scripts_v2/ch030.yaml`)

**Chapter 30 rules:** The charge up the shaft; the sludge mouth; the canyon face and the rim ledge (`farm_canyon/rim_ledge.png`) across a 40 m gap, the iris closing in sparks (P15 splash). Moon Ahin's conducting splash (P21) and the husk bridge, a lattice locked wrist to ankle (P23). From P33, white threads run from Jaeha to all 29 husks; P49: a bruise blooms on his forearm in the shape of a crack. Sora at the far end: P54 tall, P57 the ECU along her sights.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P01 `plan` |
| `B` | P08–P12 | P08 `carry`; No art for P13 (`title`). |
| `C` | P14–P19 | P15 splash |
| `D` | P20–P25 | P21 splash |
| `E` | P26–P30 | - |
| `F` | P31–P36 | P31 window (keep the top half calm); P32 ECU strip; P33 `carry` |
| `G` | P37–P44 | P43 window (keep the top half calm) |
| `H` | P45–P52 | P47 `link-view`; P49 `carry`; P52 window (keep the top half calm) |
| `I` | P53–P60 and `END.png` | P57 ECU strip; P60 window (keep the top half calm) |

### Chapter 31: Two Pulses (`scripts_v2/ch031.yaml`)

**Chapter 31 rules:** The standoff on the husk bridge; Sora's repeating crossbow, the heavy violet-tipped bolt and the compass on her RIGHT wrist. P25 is the Borrowed Thunder II splash; P26 the compass shattering. Borro holds the iris plates apart at the slit (P36). P44 is a red window on black. Outside under the bridge from P45 (`hanriver_gate/sealed.png`, night, mud): Jaeha's phone screen and his shaking hands.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | No art for P09 (`title`). |
| `B` | P10–P15 | P10 window (keep the top half calm); P12 ECU strip; P13 `link-view`; P14 window (keep the top half calm) |
| `C` | P16–P21 | P18 window (keep the top half calm) |
| `D` | P22–P30 | P22 `carry`; P25 splash |
| `E` | P31–P37 | P31 window (keep the top half calm) |
| `F` | P38–P44 | P40 window (keep the top half calm) |
| `G` | P45–P52 | - |
| `H` | P53–P60 and `END.png` | P55 phone screen #00FF00; P56 ECU strip; P60 strip; P60 phone screen #00FF00 |

### Chapter 32: Buried (`scripts_v2/ch032.yaml`)

**Chapter 32 rules:** The Gate Rescue van smashes the fence (P01); foil blankets; dawn over the river (P14); Saebyeok alone at the water's edge (P16). The Association lobby (P18); Deputy Director Hwang's lapel pin (P25); the break room's TV (`gate_rescue_room/key.png`). Moon Ahin in a fresh coat-dress, hair loose, no ribbon (P33 glamour, a Kanghan Tower corridor). Baek's office by day (`kanghan_office/day.png`). The rusted lamp on the niche's ledge (P44). Sora's car at dusk (`sora_car/key.png`). Draw a faint tremor line on Jaeha's fingers whenever his hands show.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | - |
| `B` | P10–P16 | P11 phone screen #00FF00; No art for P17 (`title`). |
| `C` | P18–P25 | P22 TV footage (keep the bottom fifth calm); P24 ECU strip |
| `D` | P26–P32 | - |
| `E` | P33–P37 | - |
| `F` | P38–P42 | - |
| `G` | P43–P47 | - |
| `H` | P48–P54 | - |
| `I` | P55–P60 and `END.png` | P56 ECU strip |

### Chapter 33: Garbage (`scripts_v2/ch033.yaml`)

**Chapter 33 rules:** The rooftop dinner at dusk (`rooftop_room/party_dusk.png`); Dami's daughter (`crew/dami_daughter.png`); Moon Ahin's glamour on a plastic stool beside Lyra (P07); Saebyeok with the fruit basket. The chopsticks (P10-P11, ECU) and the fall (P13). The hospital (`hospital/key.png`) and the road south (`expressway_night/key.png`). Busan: `geum_stall/dawn_wide.png` and `interior.png`. Auntie Geum: `geum_okran/` sheets; her name card P31 and the verdict splash P36. The sea gate (`busan_sea_gate/key.png`, `crack.png`) P61-P63; the final splash P66 with a faint violet stain on the horizon. The tremor line on Jaeha's fingers all chapter.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P02 phone screen #00FF00 |
| `B` | P08–P13 | P11 ECU strip; No art for P14 (`title`). |
| `C` | P15–P22 | P16 window (keep the top half calm); P17 ECU strip |
| `D` | P23–P30 | - |
| `E` | P31–P37 | P31 name card; P36 splash |
| `F` | P38–P44 | P41 ECU strip |
| `G` | P45–P50 | - |
| `H` | P51–P58 | P51 window (keep the top half calm) |
| `I` | P59–P66 and `END.png` | P60 strip; P63 the reveal; P64 window (keep the top half calm); P66 splash |

### Arc 5 sheets come first
Chapters 34-40 need the sheets, keys and props in `ASSETS_ARC5_BRIEF.md` (Wave C: Jaeha's training look S26, the Arc 5 cast S27, the flashback cast S28, Pim S29, the beach looks S30, Han Sora's pool look and new compass S31, the monsters M10-M12, the places L21-L24 and the props sheet P2), plus these from earlier waves: Borro S16, Director Baek S17, Moon Ahin's husk S19, Han Sora S20, Nib's seal 3/5 S21, Auntie Geum S24, the Arcs 3-4 cast S25 (Hwang), the Call L8, Baek's office L10, and Geum's stall and the sea gate L20. A part may start only when every sheet it names is **APPROVED** in `codex/reviews/`. Every sheet carries a faint 178 cm silhouette: use it to check the scale of every giant and monster (section 4b); the Deep Lantern is about 150 m long, so Jaeha is smaller than one of her fingers. Fan service as before: Lyra, Moon Ahin, Han Sora and Bomi get confident glamour panels, never a camera aimed up a skirt, down a top or at the chest; Seoa (15) and Yerin never. Nib wears his seal 3/5 armour and the cracked husk mask in public throughout Arc 5. Jaeha wears his `training` look (`kang_jaeha/turnaround_training.png`) all arc.

### Chapter 34: Just One More (`scripts_v2/ch034.yaml`)

**Chapter 34 rules:** Busan at 4:00 AM in the dark (`busan_breakwater/night.png`, then `key.png` at dawn): Geum on a battered red moped shouting through a rolled-up newspaper; Borro carries Jaeha like a sack of rice (P05). The fish market (`busan_fish_market/key.png`) and the aunties (`arc5_cast/lineup.png`); P20 is the window's small print, an insert with no people. Geum's tent (`geum_stall/interior.png`): Seoa on a video call, drawn on the phone (P30), and Bomi's call. Lyra in the surf at dawn (P33 glamour, the camera at her eye level; Jaeha walks into a lamppost, P34). Sora in the black car with binoculars and her new slim silver compass on her LEFT wrist (`han_sora/details_compass2.png`). Tuesday at 10:30 PM: Nib and Lyra spar in field form on the stony shore under a work lamp while Jaeha carries both (P50). P09 and P27 are still before dawn (sunrise is about 6:40); Borro and Lyra sleep halfway along the breakwater in P54. The brine crawler (`brine_crawler/`) from P56; P62 is Geum's splash with the ladle raised. Draw a faint tremor line on Jaeha's fingers when his hands show.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | No art for P10 (`title`). |
| `B` | P11–P18 | - |
| `C` | P19–P26 | P19 ECU strip; P20 the small-print window (insert) |
| `D` | P27–P32 | P30 a video call drawn on the phone; P32 `chibi` |
| `E` | P33–P37 | P33 Lyra's glamour in the surf |
| `F` | P38–P45 | P42 window (keep the top half calm) |
| `G` | P46–P53 | P50 `carry` |
| `H` | P54–P62 and `END.png` | P56 the reveal; P62 splash |

### Chapter 35: The Wall (`scripts_v2/ch035.yaml`)

**Chapter 35 rules:** P01-P08 at night on the tetrapods (`busan_breakwater/end.png`, `night.png`): Geum's held strike rings like a bell and throws a thin white ring of force. **The flashback P09-P22 is drawn in greys** (`busan_breakwater_flashback/key.png`), with violet only for the sea and the gate light and amber only for the fighters made of light: Geum at 52 with the steel boat door (`geum_okran/turnaround_flashback.png`), the fishermen as her crew (no uniforms), the man in the dark coat whose face is NEVER shown (`operator_1/flashback.png`), the five figures of light and the vast swimming shape with its lantern (`light_fighters/`); P20 is the thing rising with the same lantern burning violet (`deep_lantern/head.png`, `hand.png`; only a wall of hide, the crest and one hand); P21 no gore, the arm lost in a white flash; P22 the lid being built. Back in colour from P23. The cold store and its slit (`busan_fish_market/cold_store.png`, `cold_store_gate/slit.png`), the flooded shrine (`cold_store_gate/key.png`) and the Reef Hermit (`reef_hermit/`; P46 `out_of_shell.png`). P38 is Lyra's beauty shot in the fight, at her eye level. The Call at the hook (`pim_tower/through_rift.png`) and Pim's eyes an inch from Jaeha's face (P61; `pim/`, no headset).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P08 | - |
| `B` | P09, P11–P15 | P09 strip; greys from P09; No art for P10 (`title`). |
| `C` | P16–P22 | greys; P16 `carry`; P20 the reveal |
| `D` | P23–P26 | colour again; P24 ECU strip |
| `E` | P27–P33 | P28 window (keep the top half calm) |
| `F` | P34–P39 | P35 the reveal; P38 Lyra's beauty shot |
| `G` | P40–P45 | - |
| `H` | P46–P50 | P49 splash |
| `I` | P51–P56 | P51 window (keep the top half calm); P56 `chibi` |
| `J` | P57–P61 and `END.png` | P60 window (keep the top half calm); P61 splash |

### Chapter 36: Pim (`scripts_v2/ch036.yaml`)

**Chapter 36 rules:** The Call (`call_void/key.png`) and Pim's rift (`pim_tower/through_rift.png`); P08 is Pim's world through the rift (`pim_tower/key.png`). While Jaeha is in the Call his body stands rigid on the breakwater with glowing cyan eyes (P05, P19). P23 is Pim's leap through the rift, wings flared (splash). P26 he lands face-first at Lyra's boots; P27 Busan's noise. Geum's floral headscarf goes on Pim's antennae like a bonnet (P30, `pim/details.png`); P31 his name card. Sora's spinning compass in the black car (P35). Thursday: the PC bang owner chases Pim and the headset down the market aisle (P37); from P37 Pim wears the headset (`pim/details.png`). P41 is a chat on Jaeha's phone (#00FF00). P48 is Pim's first field form at sunrise (`pim/turnaround_field.png`). P55 the lid from above and something under it: only a violet glow and one curve of hide (`busan_sea_gate/key.png`, `deep_lantern/side.png`). P57 the voice over the empty sea: leave the upper two thirds dark and empty for the lettering.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | - |
| `B` | P07–P10 | P08 Pim's world; P09 ECU strip; No art for P11 (`title`). |
| `C` | P12–P18 | - |
| `D` | P19–P24 | P23 splash; P24 window (keep the top half calm) |
| `E` | P25–P30 | - |
| `F` | P31–P35 | P31 name card |
| `G` | P36–P40 | - |
| `H` | P41–P45 | P41 phone screen #00FF00; P42 `chibi` |
| `I` | P46–P53 | P48 field form; P49 `link-view`; P51 window (keep the top half calm) |
| `J` | P54–P62 and `END.png` | P55 `link-view`; P56 ECU strip; P57 splash (upper two thirds empty); P60 glitch window |

### Chapter 37: Make Him Come to Us (`scripts_v2/ch037.yaml`)

**Chapter 37 rules:** The Association's Busan branch (`assoc_busan/outside.png`, `key.png`) and Branch Chief Yang (`arc5_cast/lineup.png`); Hwang is drawn ON the video-call screen (P06-P09; `arc3_cast/lineup.png`), and P09 shows the hexagon pin under his lapel for an instant. The barge from the window (`kanghan_barge/far.png`). The rooftop pool (`hotel_pool/key.png`): P17 is Sora's glamour (`han_sora/front_pool.png`, the camera above her waist level); Jaeha studies the sky. The anchor drawing on her tablet and his own stamped link beside it (P20-P21; `props_v2/arc5/props.png`). The beach (`busan_beach/key.png`): P29 is Lyra's swimsuit glamour (`lyra/front_swimsuit.png`), P30 Bomi with her drone (her design; never a low angle up her shorts), the Kanghan PR pair (`arc5_cast/`). P42 is Moon Ahin's summer glamour (`moon_ahin/front_summer.png`) with Saebyeok's parasol and her husks carrying luggage. The barge's gangway (`kanghan_barge/key.png`). The breakwater at golden hour (`busan_breakwater/end.png`); P53 Pim's field form. P61 the barge at sunset, floodlights on.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P06 Hwang drawn on the screen |
| `B` | P08–P12 | P09 the pin; P10 ECU strip; No art for P13 (`title`). |
| `C` | P14–P20 | P15 phone screen #00FF00; P17 splash (Sora's glamour) |
| `D` | P21–P27 | - |
| `E` | P28–P34 | P29 splash (Lyra's glamour); P31 phone screen #00FF00 |
| `F` | P35–P40 | P40 phone screen #00FF00 |
| `G` | P41–P45 | P42 splash (Moon Ahin's glamour) |
| `H` | P46–P50 | P49 `chibi` |
| `I` | P51–P56 | P53 field form; P54 `link-view` |
| `J` | P57–P61 and `END.png` | P61 the barge at sunset |

### Chapter 38: Store (`scripts_v2/ch038.yaml`)

**Chapter 38 rules:** Friday in four training sessions on the breakwater, at 4:00, 8:00, 12:00 and 16:00 (the light changes: before dawn under a work lamp, morning, hard noon, gold afternoon). Geum's held strike splits a tetrapod (P06). When Jaeha holds force, his RIGHT arm and then his chest glow white-gold (`kang_jaeha/store_glow.png`); from P17 his RIGHT index finger is splinted with a chopstick. The barge drilling far out (P18). The old fisherman's boat (`fishing_boat/key.png`) and the barge's rail with Sora (`kanghan_barge/key.png`). P31 is Lyra's dive glamour in the swimsuit (`lyra/front_swimsuit.png`), at her eye level. The LINK views under the water (P34-P37): the lid with Kanghan's anchor bolts and the crack (`busan_sea_gate/crack.png`), then the violet glow and a curve of hide below. Everyone goes out on the boat, Borro included, so it rides low (P28); the boat comes in to the barge's fender to fetch Lyra (P41). Moon Ahin in her summer look (P42-P44). The tent at night: Nib unmasked inside it. Seoa arrives in her school uniform (P47 on; never any fan service). The tent at 6:58 (`geum_stall/interior.png`). P56 the violet burst under the barge (splash-sized).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P06 | P04 and P06 impacts |
| `B` | P07–P10 | P10 ECU strip; No art for P11 (`title`). |
| `C` | P12–P19 | P12 window (keep the top half calm); P14 `carry`; P17 the splint |
| `D` | P20–P27 | P21 `carry`; P23 window (keep the top half calm); P25 `carry` |
| `E` | P28–P34 | P31 splash (Lyra's dive); P34 `link-view` |
| `F` | P35–P41 | P35 `link-view`; P37 `link-view` |
| `G` | P42–P46 | P45 `carry`; P46 window (keep the top half calm) |
| `H` | P47–P55 | P51 `chibi` |
| `I` | P56–P61 and `END.png` | P56 the violet burst; P58 window (keep the top half calm) |

### Chapter 39: The Wall of Busan (`scripts_v2/ch039.yaml`)

**Chapter 39 rules:** The fight stays at the NECK of the breakwater (`busan_breakwater/neck.png`, `break.png`), with the fish market, its pier and sea wall 200 m behind. The market's evacuation (P03-P09: Seoa on a crate with the red megaphone; Bomi on the roof, `busan_fish_market/roof.png`; Choi's van and Yerin). P10 repeats the framing of ch 35's flashback line, in colour. P12 the lid bursting (splash). P17 the four field forms in a row (splash: `pim/turnaround_field.png`). P22 Geum's glory, her younger self's grey ghost behind her (`geum_okran/turnaround_flashback.png`). P27 Moon Ahin's battle glamour in her white coat-dress. P30 the husk wall along the sea wall, cyan threads to Jaeha. P34-P46: the leviathan's back (`deep_lantern/side.png`), Kanghan's harpoons (`props_v2/arc5/props.png`), the barge towed in and run aground on the breakwater's tetrapods, Nib running a taut chain up from its bow and knocking out the shackle pins; Sora lowers her crossbow (P44). P47 THE DEEP LANTERN at full height (`deep_lantern/head.png`). The lure: the crowd's and Seoa's eyes glazed violet (P51-P52); the fighters, under the lamp, are in its shadow. In P55 Seoa wakes on Pim's signal and hauls a lured little boy back from the edge (never a damsel). P73: Moon Ahin sends twelve husks running for the flank; sixteen hold the sea wall. P54 Pim's signal from the harbour light tower (splash). P60 the two walls under her hand (`deep_lantern/hand.png`). Jaeha bleeds from the nose and ears from P61.

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P07 | P03 phone screen #00FF00; P06 live-stream overlay area calm |
| `B` | P08–P12 | P12 splash; No art for P13 (`title`). |
| `C` | P14–P19 | P14 the reveal; P17 splash; P18 `link-view` |
| `D` | P20–P25 | P22 splash (Geum's glory) |
| `E` | P26–P33 | P27 splash (Moon Ahin); P30 `carry` (the husk wall) |
| `F` | P34–P40 | P34 the reveal |
| `G` | P41–P46 | P42 Nib on the chain |
| `H` | P47–P52 | P47 the reveal; P48 ECU strip |
| `I` | P53–P57 | P54 splash (Pim's signal); P56 phone screen #00FF00 |
| `J` | P58–P66 | P60 the two walls; P61 `carry`; P63 ECU strip |
| `K` | P67–P73 and `END.png` | P72 window (keep the top half calm); P73 the hand raised |

### Chapter 40: First Kill (`scripts_v2/ch040.yaml`)

**Chapter 40 rules:** Jaeha glows white-gold while he holds the strike (P02-P24, `kang_jaeha/store_glow.png`); the countdown windows run 00:10 (P03: HOLD 00:30 → 00:10, too heavy), 00:07 (P12), 00:04 (P15), 00:03 (P16), 00:02 (P22). P06: Jaeha's four threads, and Moon Ahin's own cyan threads from her baton to her twelve husks. The husk stair up her flank (P09 splash, at Moon Ahin's eye level); Geum's throw (P11); her other hand knocks the lower steps into the sea, cracked, not smashed (P15); all 28 husks are at dinner (P50). On her head: the crack 10 m long at the base of the crest (`deep_lantern/head.png`); the three lost boats far out on the black sea in a bank of violet haze that hides the lighthouse (P18, P21). P24 RELEASE (splash: no gore, the forearm lost in the light). P27 the lantern flaring white (`deep_lantern/lantern.png`, `freed.png`). P33 she dissolves into light. P34-P38 the fall and Lyra's dive. The core (`props_v2/arc5/props.png`) hangs over the water (P39), flies to him (P44). Dinner on the breakwater (P47-P56; Jaeha's RIGHT arm in a sling from P48); P56 the quest-complete window. Seoul: Baek's office at night (`kanghan_office/key.png`), Bomi's stream drawn on the wall screen (P57). The hook after midnight on the breakwater (`busan_breakwater/night.png`): Pim's hearing as a lilac vignette on black (P63); Nib's knives on the stone (P65).

| Part | Panels to draw | Notes |
|---|---|---|
| `A` | P01–P09 | P02 `carry`; P04 ECU strip; P06 `link-view`; P09 splash |
| `B` | P10–P16 | P11 the throw; P13 `link-view`; P16 window (keep the top half calm); No art for P17 (`title`). |
| `C` | P18–P25 | P24 splash |
| `D` | P26–P33 | P26 ECU strip; P27 splash; P31 window (keep the top half calm) |
| `E` | P34–P38 | P36 underwater |
| `F` | P39–P46 | P39 window (keep the top half calm) |
| `G` | P47–P51 | P51 `chibi` |
| `H` | P52–P56 | P52 phone screen #00FF00 |
| `I` | P57–P60 | P57 Baek's wall screen drawn |
| `J` | P61–P67 and `END.png` | P63 `link-view`; P67 ECU strip |

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
