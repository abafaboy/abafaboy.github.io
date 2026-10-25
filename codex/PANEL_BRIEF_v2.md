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
Chapters 6–12 need the Arc 2 sheets and keys in `ASSETS_ARC2_BRIEF.md` (Borro S16, Baek S17, the neighbours S18, Moon Ahin's husks S19, the monsters M1–M4 with the swarm mother and the alpha, the places L6–L12). A part may start only when every sheet it names exists and has a `DONE.md`. Every Arc 2 sheet carries a faint 178 cm silhouette: use it to check the scale of every monster and giant in your panels (section 4b).

### Chapter 6: Trap Rats (`scripts_v2/ch006.yaml`)

**Chapter 6 rules:** Jaeha has a small plaster on his right cheekbone and no other bandages. Nib has his seal 2/5 look with the mask and plays a husk in public (stiff, arms hanging); field form and LINKED (amber) only P26–P36. Ash rats: `ash_rat/` (70 cm, knee-high); the swarm mother P38–P40: `ash_rat/swarm_mother.png` (1.4 m, hip-high). The sewer: `sewer_gate/key.png` inside, `outside.png` at dusk (P44–P51). The landlady (P52–P54): `neighbourhood/lineup.png`, on `rooftop_room/stairs_night.png`. Bomi's room (P55–P60): `bomi_room/outside.png` and `interior.png`. P07 and P47 carry phone live-stream overlays: keep those areas calm. Bomi: never a low angle up her shorts.

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

**Chapter 8 rules:** Gomi the cat: `neighbourhood/gomi.png`, huge and fat next to Nib. Nib is in rest form (no glow) except P42–P55. Through-the-eyes panels (P02, P14, P16, P17) carry a thin amber vignette. The Han River enclosure: `hanriver_gate/key.png` and `bank_dusk.png`, at the blue hour with the bridge lights coming on. The car park: `carpark_gate/key.png`; the ramp is 30 m long and 6 m wide, its lower third wet. The drowned hound: `drowned_hound/` (1.7 m at the shoulder: a head taller than Jaeha). The vest has Seoa's red stitches on the back patch from P25; the bite bandage on Jaeha's LEFT forearm from P47 (the bite is P38).

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

**Chapter 10 rules:** Borro arrives: `borro/` sheets. He is 2.4 m: in the rooftop room (ceiling 2.2 m) he must stoop or sit; on the rooftop he is taller than the water tank (2 m); Jaeha reaches his chest. His husk face (a white oval with two small eye-holes, tied with cord) is on in public from P25. Field form: moss-green eyes and outline (P44–P57). P12 is the bed-crushing splash (the metal bed folds flat). P15 is Borro's name card (full figure, name-card gradient dark slate to moss green). The tower: `tower_gate/outside.png` and `key.png`; the long beam is 60 cm wide and the slabs either side are cracking away; the drop is several floors. Ash hounds: `ash_hound/` (hip-high); the alpha: `ash_hound/alpha.png` (chest-high). P37 is a three-way split `link-view`. Jaeha's RIGHT ankle bruise (P20–P21): long, thin, many-jointed finger marks.

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
