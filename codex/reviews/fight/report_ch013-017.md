# MSGF fight audit and re-storyboard: chapters 13–17

I looked at every page of every fight in order, from the lettered judge pages (`/home/claude/work/judge/chNNN_final/`). I also compared 25 key panels against the original art (`chapters_v2/chNNN/art/PNN.png`) and pulled counts from the scripts. My contact sheets and script are deleted, and `/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/fight/ch013-017/` is empty.

## Decisions the main session has to make (I can't make them from here)

1. **Re-letter before redrawing. This is the biggest, cheapest fix.** In these chapters the hit is usually drawn; then the SFX or the window is placed on top of it. I checked this against the original art.
   - Under the SFX, the art shows: Nib's strike (ch15 P04, P23, P34), Nib's face (ch15 P35), Mok's shocked face (ch17 P01, P43) and Jaeha's stop-arm (ch16 P15).
   - It also shows the white contact burst where tusk or clapper meets shield (ch13 P40; ch15 P02, P14; ch17 P26, P45, P49).
   - In ch17 P52, the payoff panel, all five team members are drawn and the window covers them.
   - Measured from the scripts: 39 of the 50 impact SFX are placed in the top 40% of the panel (`at` y ≤ 0.40), and 27 of the 50 are XL. 64 of the 65 action panels ask for `calm: top`. Low-angle action shots put the heads and the contact point exactly there.
   - **The fix belongs in the lettering step, not the art:** place SFX after looking at the art, beside the contact point, never over a face, hand, weapon or the contact itself; size L at most, XL only on the chapter's 1–3 peaks; windows never on impact, anticipation or splash panels.
2. **`full` panels come out the same size as `wide`.** All 7 `full` peak panels are 1536x1024, the same as any wide panel: ch15 P01, P34; ch16 P37; ch17 P01, P21, P30, P52. So the peaks are not bigger than anything else. My boards use `tall` (1024x1536) for peaks. Either do the same or change what `full` renders as.
3. **No panel frame is ever tilted.** Every border in all five chapters is axis-aligned, though the impact recipe asks for 10–20°. My boards put the tilt inside the drawing ("dutch 15°").
4. **Rule 7 ("violence happens between panels"): I recommend dropping it for fights.** Wording is at the end. It contradicts the impact recipe ("the hit at its peak"). The model already produces platform-safe contact, e.g. ch15 P23's tusk raking Borro's forearm with a short red spray.

## Grades

| ch | sequence | panels | grade /10 |
|---|---|---|---|
| 13 | The test (construct) | P36–P46 | 5 |
| 14 | The door (flashback; action, not a fight) | P39–P44 | 6 |
| 15 | First charge | P01–P06 | 4 |
| 15 | Second charge | P11–P15 | 5 |
| 15 | The failed pass | P21–P27 | 4 |
| 15 | The pass | P32–P39 | 6 |
| 16 | Blade trap | P14–P16 | 5 |
| 16 | The flood | P28–P42 | 6 |
| 16 | The bell drop | P46–P53 | 7 |
| 17 | The yank | P01–P04 | 5 |
| 17 | The rise and the first toll | P20–P31 | 5 |
| 17 | The plan and the chalk run | P32–P40 | 6 |
| 17 | Mok's shield | P41–P49 | 5 |
| 17 | Inside the ring | P50–P54 | 4 |
| 17 | Thirty seconds | P55–P66 | 6 |

By chapter: ch13 5, ch15 5, ch16 6, ch17 5. Every sequence is below 8, so every one has a storyboard. My estimate: re-lettering alone would lift ch17 P01–P04 and ch16 P15 to about 7. The rest also need the redraws.

Not graded: ch13 P52–P55 (Mok's squeeze, Nib reaching for a knife) and ch16 P62–P68 (the doors). Both are tension beats, not fights. One fix there: in ch16 P67, GRRRRRRRND covers Mok's smile in the closing gap, which is the cliffhanger image that ch17 P01 pays off. Move the SFX vertically down the right door's edge.

## Checking the chapter-11 calibration against ch13–17

| ch11 finding | ch13–17 | evidence |
|---|---|---|
| Bodies posed, not fighting | **Partly confirmed** | Stiff and square: ch13 P44 (construct symmetrical, arms hanging); ch17 P21, P52, P60 (the Bell-Ringer square to the camera, symmetrical); ch17 P42 (Mok square, not lunging). Real line of action exists too: ch15 P21 (Nib coiled), P02 and P14 (Borro's weight into the shield), ch17 P25 (overhead wind-up), P28 (Nib's lunge-slash), ch14 P42 and P43. In ch13 the stiffness is the intended gag (they are playing husks). |
| Eye-level camera, little foreshortening | **Confirmed** | Most impacts are side-on at eye level or slightly low. None of the 44 impact panels brings a weapon, fist or tusk toward the camera. The only foreshortening is the boar's head-on charge in two non-impact panels (ch15 P01, P32). |
| Hits never land, contact replaced by debris and SFX | **Corrected** | The contact is usually drawn, then covered by lettering (see decision 1). Visible after lettering in ch17 P37 and ch15 P22. |
| SFX do the drawing's work and cover the fighter | **Confirmed, and worse** | Nib is entirely under SKRANG (ch15 P04), under SHRAKK (P23), under KRA-THOOOOM (P34); his face is under KRAKKKK (P35). Mok's face is under GRAB (ch17 P01) and KRAKKK (P43). Young Jaeha's face is under BOOOM (ch14 P42), and his line "LET GO! HE'S STILL IN THERE!" is lettered as an SFX across his face (P43). Borro's head and arms are under GRRRRRRAAAAND (ch16 P37). |
| Few speed lines or bursts; background stays | **Partly corrected** | Bursts and speed lines are present in most impacts: ch17 P26 drops to a white radial background; ch17 P41 and P45 use flat colour with speed lines; ch16 P15 an orange gradient. The background stays in ch13 P40, ch15 P02 and P22, ch17 P49. |
| Choreography doesn't read | **Confirmed, different cause** | The scripted chains are sound. They break because (a) the striker is hidden; (b) result panels skip the step (ch15 P24: the cut that should transfer to Jaeha's arm isn't drawn; ch17 P56: the swat isn't shown, only the splash); (c) one panel holds several beats (ch15 P22, P34; ch16 P49); (d) staging contradicts the script (ch17 P43: Jaeha stands outside Mok's shield; ch13 P44: the construct is idle, but P46 says it froze mid-swing); (e) a tangle (ch17 P49). |
| Windows on top of action | **Confirmed** | 7 action panels carry windows: ch13 P36; carry panels ch15 P06, P24, ch16 P38, ch17 P27, P46; splash ch17 P52, where the window covers the whole team. |

---

## How to read the boards

- **Marks:**
  - **KEEP:** art and lettering stay as they are.
  - **KEEP·RL:** keep the art; re-letter as the SFX column says.
  - **REDRAW:** new art from the row.
  - **NEW:** an added panel.
  - **CUT:** a removed panel.
- **Shapes and sizes:** `tall` = 1024x1536 (all peaks); `wide` = 1536x1024. SFX sizes are S, M, L, XL. "As drawn" means the existing art.
- **Screen direction:** in ch15 the boar stays on screen left and Borro on the right. In ch17 the giant stays on screen right; the one flip, at P37, is motivated by the redrawn P35.
- **Character locks:** Borro's shield is always on his LEFT forearm. Nib wears the mask (ch13 and ch15–17), with knives in reverse grip and bare feet.

---

## Chapter 13 — The Hearing

### The test, P36–P46 (grade 5)
The construct powers up; Borro and Nib "march like husks"; the construct swings at Borro; Nib darts between its legs, runs up its thigh and taps the core. 00:04.

**What's wrong**
- **P36:** the [05:00] window sits across the construct's shins and the floor between it and the trio. GRRRRIND covers its head, and the head turning is the beat.
- **P38:** the gag isn't drawn. Nib's arms hang at his sides (no flipper pose), so FLAP FLAP carries the joke. He is also unmasked, though the cast says `nib: mask` and he is playing a husk. Alone on a blank wall, with nothing for scale, he reads as a tall teenager.
- **P40:** the only hit. The art has the swinging arm and a burst at the fist-on-shield contact, and XL KRANNG covers both. There is no wind-up before it.
- **P44:** the tall peak is spent on a static construct (arms down, symmetrical). Nib has his back to the camera, his body flat against the stone, and there is no sense of speed. The construct isn't mid-swing, which P46 needs.
- **P46:** two beats in one small wide panel (the freeze, and Nib's comic snap back into husk pose).
- **Continuity:** the arena is padded grey walls in P31, P36 and P40, but stadium stands in P43 and a stone colosseum under a night sky in P44 and P46.
- **What works:** P37 (the toy-soldier march), P39, P41, P42, P45.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | NEW | strip | extreme close-up at floor level, side-on, macro | The construct's square stone foot on its rail of light; the rail flares from white to amber under it. Nothing else in frame. | amber bloom and small sparks along the rail; black background; top half left empty | none | window [05:00] moves here, top half |
| 2 | P36 KEEP·RL | wide | as drawn (low, behind the construct) | The head grinds round toward the trio; one arm lifts. | as drawn | GRRRRIND, M, on the dark wall upper right beside the neck; head, arm and trio clear. Window removed. | — |
| 3 | P37 KEEP·RL | wide | as drawn | Borro's toy-soldier march. | as drawn | KLONK ×3, S, one under each cracking footprint at floor level, not across his knees | — |
| 4 | P38 REDRAW | wide | eye level, side-on, 50 mm; Borro's marching legs cropped at the left edge for scale (Nib's head level with Borro's hip) | Nib, MASK ON, marches stiff-legged like a wind-up toy, chin up, deadpan. Both arms held straight out about 45° from his sides like penguin flippers, hands flat, fingers together, flapping at the wrists. | three short curved flap arcs at each hand; dust puffs under his bare heels; padded grey arena wall | FLAP FLAP, S, beside his RIGHT hand | — |
| 5 | P39 KEEP | wide | as drawn | Gallery chorus. | — | TOK | "...ARE THEY... DANCING?" |
| 6 | NEW | inset-r | worm's-eye from the floor beside Borro, 20 mm | The construct's pillar arm raised high, the block fist foreshortened toward the camera, about to fall. Borro small at the bottom edge, lifting his shield stiffly, face blank. | tension lines converging on the fist; grit falling off it; dark ceiling | none | — |
| 7 | P40 KEEP·RL | wide | as drawn (low, slight tilt) | The fist hits the shield; Borro skids back stiff-legged on his heels. | as drawn (arm, fist and burst are under the current SFX) | KRANNG, L not XL, on the empty floor lower left, angled with the skid; arm, fist and shield top clear | — |
| 8 | P41 KEEP | inset-r | as drawn | Jaeha flinches; moss-green ring. | — | THMP | — |
| 9 | P42 KEEP | wide | as drawn | The cyan plan line. | — | — | "NIB. BETWEEN ITS LEGS. TOUCH THE CORE. JUST TOUCH IT." |
| 10 | P43 KEEP·RL | wide | as drawn | Nib darts between the legs, husk arms still out. | as drawn | ZIP, M, on the floor speed lines behind his heels, not on his legs | — |
| 11 | P44 REDRAW | tall | worm's-eye from the construct's toes straight up its front, 18 mm, dutch 10° | Nib mid-leap between two brass bands on the thigh, body in a C-curve off the stone: LEFT hand hooked over a band, LEFT foot pushing off the band below, RIGHT arm stretched up at the glowing grille, fingers spread. Nib at least a third of the frame height. Upper right: the construct's other arm swinging down at Borro (cut by the frame, smeared), so it is mid-swing. | speed lines up his path; a dust puff on each of the three bands below him; amber grille light on his face; padded walls as in P31 | TAK ×3, S, one beside each dust puff | — |
| 12 | P45 KEEP·RL | inset-l | as drawn | The finger taps the grille. | — | TIK, S, to the right of the fingertip, on the stone | — |
| 13 | P46 REDRAW | wide | low three-quarter from the floor by its foot, 24 mm | The construct frozen mid-swing, one arm stopped in the air above Borro (small, shield up). Brass bands going dark from the chest outward; core and rails dead. | no motion lines (stillness); the last band at the fist still faintly lit | VMMmmm..., S, beside the dark core | — |
| 14 | NEW (from P46) | inset-r | eye level, medium close, beside the stone foot | Nib already landed and back in husk pose: arms hanging straight, hands limp, mask on, chin up, one bead of sweat. | flat pale grey background | none | — |

11 → 14 panels (+27%).

---

## Chapter 14 — The Compass

### The door, P39–P44 (grade 6; a flashback action beat, not a fight)
Minseok pushes young Jaeha out of the closing iron door and stays inside. The door slams. Young Choi drags the boy away. The red lamp.

**What's wrong**
- **P39:** GRRRRRRRND covers Minseok's head.
- **P40:** side-on and flat; SHOVE sits on the shove; it is unclear which side of the door is inside.
- **P42:** BOOOM covers young Jaeha's whole head; the art has the screaming face.
- **P43:** his line is lettered as an SFX across his face.
- **What works:** P41, P44, and the body mechanics in P42 and P43.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P39 KEEP·RL | tall | as drawn | Two men running for the closing gap; the pale thing stirs behind. | — | GRRRRRRRND, L, vertical along the door's closing edge beside the strip of light; Minseok's head clear | — |
| 2 | P40 REDRAW | wide | low, from OUTSIDE the door looking in through the gap, 35 mm | Minseok, inside, shoves young Jaeha out with both palms flat on the boy's chest: arms locked, RIGHT foot back and planted, his body one diagonal. Jaeha falls backward toward the camera through the gap, RIGHT hand reaching for Minseok's sleeve, LEFT arm flung back. Contact: both palms on the chest. | speed lines out of the gap toward the camera; iron edges framing; grey except the two orange vests | SHOVE, M, inside the gap beside Minseok's elbow, not on the hands | — |
| 3 | P41 KEEP | wide | as drawn | Minseok's grin between the edges. | — | — | "EVERYONE COMES BACK, KID. GO." |
| 4 | P42 REDRAW (1/2) | strip | extreme close-up on the door seam, eye level | The two iron edges meet; the last line of light pinches out. | radial white burst along the seam; dust shaken off the rivets | BOOOM, L, on the solid door above the seam (no figure in this panel) | — |
| 5 | NEW (P42, 2/2) | wide | low, three-quarter front, close on young Jaeha at the door | He slams both bare fists on the iron: a lunge with the LEFT knee bent, RIGHT leg straight behind, head forward, mouth open in a scream, tears. Contact: the sides of both fists. | small impact stars at the fists; grey | BANG BANG, S, at the fists, never over his face | — |
| 6 | P43 KEEP·RL | wide | as drawn | Young Choi hauls him off by the vest. | — | the line becomes a jagged shout balloon from young Jaeha in the empty upper left, tail to his mouth | "LET GO! HE'S STILL IN THERE!" |
| 7 | P44 KEEP | strip | as drawn | The closed door and the red lamp. | — | — | — |

6 → 7 panels.

---

## Chapter 15 — Pass (the basalt boar)

### First charge, P01–P06 (grade 4)
The boar hits Borro's shield; field form starts; Nib leaps on and his knives skid off; he is bucked off; Jaeha carries both impacts.

**What's wrong**
- **P01:** strong (low, head-on), but DUDUDUDUDUM covers the hooves and there is nothing in frame for scale.
- **P02:** XL KRAAANNG covers the shield top and Borro's head; the art has the tusk-on-shield contact.
- **P03:** a tiny wide shot with a window; the cracks and heel grooves are unreadable at video size.
- **P04:** Nib is drawn at about an eighth of the panel height on a boar that fills the frame, and SKRANG sits right on him; only his scarf shows. The narrator describes a strike nobody sees.
- **P05:** Nib is a speck under SPLASH.
- **P06:** fine; the window sits over the legs.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P01 REDRAW (fallback: KEEP·RL) | tall | worm's-eye from the water just in front of Borro, 18 mm; Borro's shield rim and LEFT shoulder in the near foreground, lower left, back to camera, for scale | The boar charges straight at the camera, head low, both obsidian tusks foreshortened at the reader, forelegs mid-stride throwing water. | spray exploding from the hooves; speed lines converging on its head; pale yellow sky | DUDUDUDUDUM, L, along the bottom edge in the water, curved with the channel, under the hooves | — |
| 2 | P02 REDRAW | wide | low three-quarter from beside the boar's shoulder, looking along its head at the shield, dutch 15°, 28 mm | Contact: skull and both tusks smash into the shield's face at frame centre; the shield bows. Borro behind it: LEFT forearm through the strap, LEFT shoulder driving in, RIGHT palm high on its back, weight on the bent RIGHT leg, LEFT heel gouging the stone as he slides. Boar left, Borro right. | radial burst at the contact; sheets of spray on both sides; background dropped to white flash | KRAAANNG, L, over the boar's rump at upper left, angled down toward the contact; Borro's face and the contact clear | — |
| 3 | P03 REDRAW | wide | high (8 m) above and behind Borro, looking down the channel | The hold: Borro still braced, the boar's head locked on the shield. Two grooves gouged behind his heels, cracks racing from them down the aqueduct's side, chips falling into the gorge. The two figures fill the lower half. | dark jagged cracks; falling chips | KRRRK, S, at the end of a crack | window [FIELD FORM · NIB 05:00 · BORRO 05:00 · LINKED] in the empty sky band at the top |
| 4 | NEW | inset-l | low from the water beside the boar's flank, looking up, 24 mm | Nib launched off the channel wall, in the air above the boar's back: body arched in a C, both knives raised high in reverse grip, scarf streaming, mask on, eye amber. | speed lines along his arc; pale sky | none | — |
| 5 | P04 REDRAW | wide | high, close over the boar's shoulders; Nib half the frame height | Nib lands on both knees on its back and drives both knife points onto a basalt plate; the points skid sideways off the stone; arms jolt, eye wide behind the mask. Contact: both tips on the plate, centre left. | a fan of sparks from the skidding tips; white scratch lines on the plate; background speed lines from the boar's motion | SKRANG, M, right of the sparks along the skid; Nib's face and hands clear | — |
| 6 | P05 KEEP·RL | wide | as drawn | The boar wheels away; Nib lands in the water. | — | SPLASH, M, in the water left of Nib, not on him | — |
| 7 | P06 KEEP·RL | wide | as drawn | Jaeha staggers; Yerin catches his elbow. | — | THOOM, S, by the rings on his chest, on the side away from Yerin | window [CARRY · 2 SUMMONS · 35%] moved to the top band |

6 → 7 panels.

### Second charge, P11–P15 (grade 5)
The boar charges again and buckles the shield; Jaeha feels the force run through him into the stone.

**What's wrong**
- **P14:** the art has the contact burst, but KRAAANG covers it and the boar's head, and the shot repeats P02's side-on brace.
- **P15:** good concept; VWWMMMM sits over his raised arm.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P11 KEEP | wide | as drawn | Far down the channel, the boar paws and lowers its head. | — | SNORRT | — |
| 2 | P12 KEEP | wide | as drawn | Jaeha's raised hands with the two threads. | — | — | "AGAIN! BORRO, HOLD IT! NIB, LOOK FOR A GAP!" |
| — | P13 | — | — | Title card, unchanged. | — | — | — |
| 3 | P14 REDRAW | wide | low, over Borro's RIGHT shoulder from behind, 24 mm, dutch 12° | The second hit from inside: the shield's back bulges toward the camera round the boss; both tusk tips punch over the top rim; Borro's LEFT shoulder drives into it, feet sliding, water piling on his calves; the boar's red eye glares over the rim. | spray bursting round all four edges; a ring of speed lines round the rim | KRAANG, L, outside the shield's right edge, angled; tusks, eye and Borro's head clear | — |
| 4 | P15 KEEP·RL | tall | as drawn | The force runs through Jaeha into the stone. | — | VWWMMMM, M, in the empty sky at the left, off his raised arm | — |

4 drawn panels → 4.

### The failed pass, P21–P27 (grade 4)
Nib jumps too early; the pulse scatters; his knife glances off; a tusk rakes Borro's arm and the same cut opens on Jaeha.

**What's wrong**
- **P22:** three beats in one wide panel. Nib reads as crouched on top of the shield, so you can't see "too early".
- **P23:** SHRAKK covers Nib. The art has his glancing knife and the tusk raking Borro's arm with a red spray: exactly the contact we want, hidden.
- **P24:** the exchange's payoff is missing: no cut on Jaeha's forearm and no nosebleed. It's a face close-up with EEEEEEEEE across the eyes and the window across the mouth.
- **What works:** P21 (over Nib's shoulder, coiled).

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P21 KEEP | wide | as drawn | Nib coiled on the wall; the boar charges. | — | DUDUDUM | — |
| 2 | NEW | inset-r | eye level, side-on from the far channel wall, 50 mm | "Too early", made visible: Nib already airborne off the wall while the boar is still two strides from the shield below him, with a clear gap of water between tusks and iron. | speed lines along his leap | none | — |
| 3 | P22 REDRAW | wide | low, close, front three-quarter on Jaeha; his RIGHT palm flat on Borro's slate shell in the near foreground (the shell fills the left third, cropped) | The hit arrives through Borro: Jaeha's body jerks, head snapping back; a ragged white-gold pulse tears up his RIGHT arm and out of his chest in a jagged bolt toward the top right, where it bursts into sparks in empty air. | white flash behind the shell; jagged pulse; scattering sparks top right | KRANG, S, at the left edge (the hit is off-panel); FZZT, S, by the sparks | — |
| 4 | P23 REDRAW (1/2) | wide | low, close on the boar's skull, dutch 15°, 28 mm | Nib's RIGHT knife glances off the basalt skull: the blade skids in sparks, his body twists off the head, LEFT arm flung out with the other knife, eye wide, mask on. | sparks; a smear on the blade; the violet crack on the brow | SKRT, S, beside the sparks | — |
| 5 | NEW (P23, 2/2) | inset-l | extreme close-up over the shield's top rim | The obsidian tusk tip rips across Borro's LEFT forearm wrap above the strap; a short red spray (no wound close-up); his fist clenches. | smear along the tusk's path; red spray | SHRAKK, M, along the tusk's path, off the arm | — |
| 6 | P24 REDRAW | wide | close and low; Jaeha's LEFT forearm foreshortened toward the camera in the foreground, his face behind it | A red line opens across his LEFT forearm exactly where Borro was raked, beside the old bandage; his RIGHT hand clutches it. Behind: one eye squeezed shut, a thin nosebleed. | a translucent moss-green ring at the cut; red flash background; focus lines to the cut | EEEEEEEEE, S, at the frame edge by his ear | window [FORCE TRANSFER FAILED · CARRY 70%] in the top band above his head |
| 7 | P25 KEEP | wide | as drawn | Yerin runs out; Choi shouts. | — | — | "SONG YERIN! THAT FLOOR IS CRACKING!" / "SO IS HE!" |
| 8 | P26 KEEP·RL | wide | as drawn | Yerin heals the cut. | — | SHIIING, S, by Yerin's hands, not on his vest | "IT WORKED. FOR HALF A SECOND, IT WORKED. NIB WAS JUST TOO EARLY." |
| 9 | P27 KEEP | inset-l | as drawn | Field form ends. | — | — | window [NIB · BORRO · FIELD FORM ENDED · COOLDOWN 01:00] |

7 → 9 panels (+29%).

### The pass, P32–P39 (grade 6)
The head drops three strides out; on impact the force passes through Jaeha into Nib, who drops onto the skull; the basalt splits; the boar falls.

**What's wrong**
- **P34 (the chapter's peak):**
  - Scripted `full` but drawn 1536x1024, like any wide panel.
  - Four figures and three beats in one frame.
  - KRA-THOOOOM sits on Nib. He is drawn at the top-left edge, and the drop that wins the fight is hidden.
- **P35:** KRAKKKK covers Nib's face.
- **What works:** P32 is the best panel of the fight. P36 and P37 are good.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P32 KEEP | tall | as drawn | The charge, seen between Borro's feet. | — | DUDUDUDUM | — |
| 2 | P33 KEEP | strip | as drawn | Three heads dropping, stride by stride. | — | — | "THREE. TWO. ONE." |
| 3 | P34 REDRAW (1/3, the hit) | wide | low at water level from the side, dutch 12°, 28 mm | Contact only: the skull slams into the shield; Borro braced (LEFT forearm in the strap, RIGHT palm high), weight on his bent RIGHT leg. Nib is not in this panel. | white burst at the contact; spray frozen in the air as hanging drops; background to white | "KRA—", L, over the boar's rump, upper left (the first half of the SFX) | — |
| 4 | NEW (P34, 2/3, the pass) | wide | close, low, front three-quarter on Jaeha; his RIGHT hand flat on Borro's shell in the near foreground | The force passes: white-gold light races from the shell into his RIGHT palm, up the arm, through his chest (back arched, head thrown back, teeth bared) and out along the amber thread rising from his LEFT hand toward the top right. | glow along the arm and chest; the amber thread brightening; dark gold gradient | none | — |
| 5 | NEW (P34, 3/3, the peak) | tall | worm's-eye from the boar's brow straight up, 16 mm | Nib drops feet-first off the shield's rim straight down at the camera, both knives point-down in reverse grip, foreshortened at the reader, arms blazing white-gold, scarf whipping up, amber eye; the thread trails up out of frame. | radial white-gold burst behind him; speed lines converging on the knife points; flat white-gold background | "—THOOOOM", XL, along the bottom band at the skull's edge, angled, never over Nib | — |
| 6 | P35 KEEP·RL | wide | as drawn | The plate splits under the knives (the art has Nib's face, the knives in the skull and the violet cracks). | as drawn | KRAKKKK, L, lower right along the cracks | — |
| 7 | P36 KEEP·RL | wide | as drawn | The boar collapses; Nib leaps clear. | — | KSSSHHHHH, M, in the water bottom right, off the boar's body | — |
| 8 | P37 KEEP | wide | as drawn | Aftermath. | — | drip... drip... | — |
| 9 | P38 KEEP | wide | as drawn | Jaeha's trembling hand. | — | SHAKE SHAKE | — |
| 10 | P39 KEEP | inset-l | as drawn | His bleeding ear, the smile. | — | EEEEEEEE | — |

8 → 10 panels (+25%). If only one panel can be redrawn here, redraw row 5 and keep the current P34 art re-lettered as row 3.

---

## Chapter 16 — The Hero Raid

### Blade trap, P14–P16 (grade 5)
Jaeha stops the line one step before a blade sweeps out of a pillar.

**What's wrong**
- **P15:** the art has Jaeha's LEFT arm flung out across the hunter. SHHWING covers it and his head.
- **Missing beat:** nothing shows him noticing the trap first.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P14 KEEP | wide | as drawn | Two hunters smirk at Jaeha's back. | — | — | "LOOK AT HIM. FAMOUS, AND STILL WALKING IN FIRST LIKE A RAT." |
| 2 | NEW (optional) | strip | extreme close-up of Jaeha's eyes, then along his eyeline | His eyes catch a hair-thin vertical slot in the pillar at waist height, a glint of steel inside. | dark; one glint | none | — |
| 3 | P15 KEEP·RL | wide | as drawn | The blade sweeps out; his arm stops the hunter. | as drawn | SHHWING, M, along the blade's arc in the lower right over the water; his arm and head clear | — |
| 4 | P16 KEEP | inset-l | as drawn | The chalk cross beside the slot. | — | SKRITCH | — |

3 → 4 panels.

### The flood, P28–P42 (grade 6)
A clean floor, a click, both doors slam, water jets in. Borro wakes and forces the doors; everyone escapes; Sora's compass sees him.

**What's wrong**
- **P31:** two XL BOOMs cover a third of the panel.
- **P37 (the peak):**
  - `full` drawn 1536x1024, a wide shape for a vertical action.
  - GRRRRRRAAAAND covers Borro's head and arms.
  - The shield-on-door contact isn't visible.
- **P38:** THOOM sits over Yerin's eyes; the scripted nosebleed isn't drawn.
- **What works:** P30 (the click) and P32 (Mok braced in the jets, tall). P33 and P39–P42 are fine.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P28 KEEP | wide | as drawn | The dry tiled nave. | — | CLONK CLONK | — |
| 2 | P29 KEEP | wide | as drawn | Jaeha warns; Mok waves him off. | — | — | "SIR, THIS FLOOR IS TOO CLEAN. EVERYTHING ELSE IN HERE IS UNDER WATER." / "THEN WALK FASTER, HERO!" |
| 3 | P30 KEEP | wide | as drawn | The tile sinks under a boot. | — | CLICK | — |
| 4 | P31 KEEP·RL | wide | as drawn | Both pairs of doors slam. | — | BOOM, M, on the near door leaf at the left edge; BOOM, M, on the far doors at the top; never over people | — |
| 5 | P32 KEEP | tall | as drawn | Water jets; Mok braced. | — | WHOOOSSSHHHH | — |
| 6 | P33 KEEP | wide | as drawn | Two hunters hauling at the rings. | — | NNNNGH | — |
| 7 | P34 KEEP | wide | as drawn | Jaeha's choice. | — | — | inner: "IF HE WAKES UP, SHE SEES IT. IF HE DOESN'T, THEY ALL DROWN." |
| 8 | P35 KEEP | wide | as drawn | Borro wakes. | — | — | window [BORRO · FIELD FORM 05:00] |
| 9 | P36 KEEP | inset-r | as drawn | The compass needle snaps to Borro. | — | TIK! | — |
| 10 | NEW | inset-r | close, low, side-on at the seam | Borro's shield edge jammed into the crack between the doors, LEFT forearm through the strap, knuckles white; water jets through the seam round it. | spray; moss-green outline on the forearm | none | — |
| 11 | P37 REDRAW | tall (peak) | worm's-eye from the water at the gap, 18 mm | Borro forces the doors apart: back and shell against the LEFT door, the shield (LEFT forearm in the strap, RIGHT palm on its back) against the RIGHT door; legs braced wide, both feet planted on the threshold, body arched. The doors grind a body's width apart; the flood bursts out past his legs toward the camera. Husk face on, green glow in the eye holes. | white torrent with speed lines toward the camera; chips falling from the hinges | GRRRRRRAAAAND, L, vertical down the RIGHT door's edge; Borro clear | — |
| 12 | P38 REDRAW (light) | wide | as drawn | Same composition; add the scripted nosebleed. | — | THOOM, S, by the pillar, off Yerin's face | window [CARRY · BORRO · 60%] to the top-left corner |
| 13 | P39 KEEP | wide | as drawn | The raid scrambles through. | — | — | "THROUGH THE GAP! EVERYONE! GO, GO, GO!" |
| 14 | P40 KEEP | wide | as drawn | The young hunter looks up at Borro. | — | — | "THE HUSK... SAVED US? WHY WOULD IT SAVE US?" / "BECAUSE YOU WERE DROWNING. GO." |
| 15 | P41 KEEP | wide | as drawn | Mok glares; Sora smiles at her compass. | — | — | "THERE YOU ARE, BIG ONE." |
| 16 | P42 KEEP | wide | as drawn | The raid sprawled outside. | — | KOFF KOFF | — |

15 → 16 panels.

### The bell drop, P46–P53 (grade 7)
Sora shoots a marked trigger; the bell falls; Jaeha steps aside without looking; the compass stays slack.

**What's wrong**
- **P49:** three beats (bolt, chain, drop) plus two flinching hunters in one panel.
- **P50:** Jaeha stands upright in the niche, so the "one calm step" isn't drawn. The bell is a cropped brown wedge that doesn't read as a bell at a glance, and WHOOOM sits across Nib.
- **What works:** P46–P48 and P51–P53.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P46 KEEP | wide | as drawn | Single file along the ledge. | — | STEP STEP | — |
| 2 | P47 KEEP | inset-r | as drawn | The marked trigger. | — | — | — |
| 3 | P48 KEEP | wide | as drawn | Sora aims casually. | — | KLIK | — |
| 4 | P49 REDRAW (1/2) | inset-l | extreme close-up, side-on | The bolt punches into the bell-shaped trigger stone beside the chalk cross; chips fly. | impact burst at the bolt tip | THUNK, S, beside the chips | — |
| 5 | NEW (P49, 2/2) | wide | worm's-eye from the ledge straight up the chain, 20 mm | A chain link bursts open; the bell starts to drop straight down at the camera, mouth foreshortened. Jaeha's head and shoulders small at the bottom edge, not looking up. | link fragments; vertical speed lines | SNAP, M, beside the broken link | — |
| 6 | P50 REDRAW | tall | low on the ledge, three-quarter front, 28 mm | Jaeha mid-step sideways into the niche: weight on his LEFT foot, RIGHT foot lifting, hands in his vest pockets, face calm. The bell is a bronze smear plunging past his shoulder an arm's length away; the ledge edge shatters. Behind him: Nib and Borro rigid in husk pose (sharp), two hunters flattened on the wall with arms over their heads (soft). | vertical speed lines on the bell's path only; stone shards | WHOOOM, L, vertical along the drop side, away from all figures | — |
| 7 | P51 KEEP·RL | wide | as drawn | The bell hits the water far below. | — | DOOOOOONNNG, L, in the dark vault at the top; the splash clear | — |
| 8 | P52 KEEP | inset-l | as drawn | The compass hangs slack. | — | — | — |
| 9 | P53 KEEP | wide | as drawn | Jaeha and Sora. | — | — | "THAT ONE WAS MARKED, MISS HAN. PLEASE READ THE MARKS." / "MY HAND SLIPPED. SORRY, HERO." |

8 → 9 panels.

---

## Chapter 17 — Thirty Seconds

Overall grade 5. The art underneath is often better than the lettered pages suggest. P25, P28, P29, P31, P37, P55 and P57 are real manhwa panels.

### The yank, P01–P04 (grade 5; about 7 with re-lettering alone)
Borro grabs Mok through the closing gap and yanks him in; Mok lands face first; the sealer stakes the door without noticing.

**What's wrong**
- **P01:** GRAB covers Mok's face; the art has his shock.
- **P02:** YANK covers the grip that connects Borro to Mok; BOOOM sits over Mok's torso.
- **P03:** SPLASSH sits over Mok's back.
- **P04:** KACHUNNG covers the sealer's legs and the stake base.
- **What works:** the art under all four has three different cameras and a clear cause and effect.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P01 KEEP·RL | as drawn | as drawn | Borro's fist closes on Mok's jacket and chain; Mok's smile breaks into shock. | — | GRAB, L, along Borro's forearm wrap at lower left, angled with the thrust; Mok's face clear | — |
| 2 | P02 KEEP·RL | wide | as drawn | Borro yanks Mok in by the collar; Mok airborne; the doors slam. | — | YANK, M, below the grip, between them at waist height; BOOOM, L, vertical on the door leaves at the right edge | — |
| 3 | P03 KEEP·RL | wide | as drawn | Mok face first at Jaeha's feet. | — | SPLASSH, M, in the water by his hands, lower right; his back and head clear | — |
| 4 | P04 KEEP·RL | wide | as drawn | The sealer drives the stake; the violet web spreads. | — | KACHUNNG, L, on the floor left of the stake's base, the violet burst clear; VWWMMMM, S, along the web on the door | — |

4 → 4 panels.

### The rise and the first toll, P20–P31 (grade 5)
The giant rises, smashes the clapper onto Borro's shield, shrugs off Nib's slashes, knocks its own bell, and the toll throws everyone except Nib.

**What's wrong**
- **P21:** the monster reveal is `full` drawn wide. It has no MC in the foreground (the recipe asks for him small, back to us) and no human for scale. RRRRRRMMMMMM covers the arm and the clapper.
- **P26:**
  - The effect is strong, but KRANNNNG covers the clapper-on-shield contact, which is drawn.
  - The drone sits on Borro's head as a white eyeball with a pink bow and reads as a second face. The same happens in P30, P45 and P49. The script hides it in the moss, as P40 draws it.
  - "Driven to one knee" isn't legible.
- **P27:** THOOM sits over Yerin's eyes; the window over Jaeha.
- **P30:**
  - `full` drawn wide; six small figures.
  - The ring reads as a circle painted on the water, not a force bursting outward.
  - DOOOOOOOOONNNNG covers the bell that rings.
- **What works:** P25, P28, P29 and P31.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P20 KEEP | wide | as drawn | The hand closes round the clapper; the bell-head lifts. | — | KLINK... KLINK... | — |
| 2 | P21 REDRAW | tall | low from behind Jaeha and Borro (lower-left foreground, backs to camera, cropped at the waist), 18 mm, looking up | The Bell-Ringer rises to its full 6 m and fills the frame: robes and rusted chains streaming water, the cracked bell-head at the top with the violet crack down its LEFT side, the clapper in its RIGHT hand dragging in the water. Scale per the spec: Borro's head at its mid-thigh, Jaeha's just above its knee. Giant on screen right. | water pouring off it; violet ash; the dark dome and hanging bells | RRRRRRMMMMMM, L, rising up the left edge, away from the bell-head | — |
| 3 | P22 KEEP | wide | as drawn | The bell-head's dark mouth. | — | — | window [BOSS: HUSHED BELL-RINGER (B)] |
| 4 | P23 KEEP | wide | as drawn | Mok backs up with his shield. | — | — | "THE STAIR IS BEHIND IT, SIR. YOU STILL WANT TO GO FIRST?" |
| 5 | P24 KEEP | wide | as drawn | Nib and Borro flare into field form. | — | — | window [FIELD FORM · NIB 05:00 · BORRO 05:00 · LINKED] |
| 6 | P25 KEEP | tall | as drawn | The overhead wind-up; Borro steps under it. | — | WHOOOOM (already along the arc) | — |
| 7 | P26 KEEP·RL | wide | as drawn | The clapper lands on the shield. Paint out the white sphere on Borro's head. | as drawn (radial white) | KRANNNNG, L, along the water band lower right, angled with the splash ring; clapper head and shield top clear | — |
| 8 | P27 KEEP·RL | wide | as drawn | Carry. | — | THOOM, S, at the ring on Jaeha's right side, off Yerin's face | window [CARRY · BORRO · 50%] to the dark top band |
| 9 | P28 KEEP | wide | as drawn | Nib's slashing run round the legs. | — | SHK SHK SHK | — |
| 10 | P29 KEEP | wide | as drawn | The giant knocks its own bell-head. | — | TONK | — |
| 11 | P30 REDRAW | tall (peak 1) | bird's-eye straight down from the dome, 16 mm | The toll: the giant at the centre, its LEFT fist just off its bell-head. A thick bronze-white shockwave ring expands outward from just beyond its arm's reach. Inside: a calm dark disc where Nib crouches at the ankle, untouched, looking up. Outside: the water flattened into white spray. Small and blurred at the frame edges: Mok skidding back behind his shield (top), Jaeha and Yerin blown against a pillar (bottom), Borro braced (left). | outward radial speed lines; the calm disc drawn with no lines at all; small bells cracking in the corners | DOOOOOOOOONNNNG, XL, curved along the outside of the ring's lower arc; bell-head and Nib clear | — |
| 12 | P31 KEEP | wide | as drawn | Jaeha on his knees, watching untouched Nib. | — | EEEEEEEE | — |

12 → 12 panels.

### The plan and the chalk run, P32–P40 (grade 6)
Jaeha works out the safe ring and sends Yerin with the chalk under Borro's shield.

**What's wrong**
- **P35:** eye level with no speed; SPLSH SPLSH sits over Yerin's legs.
- **P37:** one of the best impacts in these five chapters, with the contact visible and KRANG beside it. But the giant has flipped to screen left; the redrawn P35 motivates the flip.
- **What works:** the rest of the sequence.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P32 KEEP | wide | as drawn | The notebook sketch. | — | — | note: "THE TOLL STARTS A STEP OUTSIDE ITS REACH. INSIDE ITS ARM, YOU'RE SAFE." |
| 2 | P33 KEEP | wide | as drawn | Jaeha gives Yerin the chalk. | — | — | "WHEN IT RINGS, NOBODY WILL HEAR ME. MARK THE SAFE RING ON THE PILLARS, CLOSE IN." / "CLOSE IN? NEXT TO THAT THING?" |
| 3 | P34 KEEP | inset-r | as drawn | Jaeha's bloody smile. | — | — | "THE SAFEST PLACE IN A TRAP IS USUALLY THE WORST-LOOKING ONE." |
| 4 | P35 REDRAW | wide | low at water level in front of her, looking back the way she came, dutch 12°, 28 mm | Yerin sprints at the camera: RIGHT fist clenched round the chalk, LEFT arm pumping, teeth gritted, eyes up at the pillars. Borro one stride behind, his shield held flat over her head like a roof (LEFT forearm in the strap, RIGHT hand under its edge). The giant's shin and robe hem cropped in the near-right foreground, blurred; they run past its flank right to left. | spray kicked toward the camera; speed lines behind them | SPLSH SPLSH, S, at her feet | — |
| 5 | P36 KEEP | inset-l | as drawn | The chalk ring round the pillar. | — | SKRRITCH | — |
| 6 | P37 KEEP | wide | as drawn | The sideways swing on the shield; contact visible. | — | KRANG | — |
| 7 | P38 KEEP | wide | as drawn | Mok crouched behind his shield. | — | — | thought: "LET THEM WEAR IT DOWN. THEN I TAKE THE STAIR." |
| 8 | P39 KEEP | wide | as drawn | Bomi's phone; the stream. | — | BLIP BLIP BLIP | stream chat as scripted |
| 9 | P40 KEEP | inset-r | as drawn | The drone lens in the moss. | — | — | — |

9 → 9 panels.

### Mok's shield, P41–P49 (grade 5)
The clapper comes at Jaeha; Mok throws his shield over him and it cracks; Borro shares it; Jaeha carries the load; Mok's eyes crack; Borro throws the clapper off.

**What's wrong**
- **P41:**
  - Flat side-on shot.
  - The giant reads about 3–3.5 m: Jaeha's head is at its hip, where the spec has him reaching just above its knee.
  - WHOOOM covers the bell-head and the arc.
- **P42:** Mok stands square (no lunge), and Jaeha clutches his head with both hands: panic, not the calculating MC.
- **P43:** KRAKKK covers Mok's face (his grimace is drawn underneath). Jaeha stands outside the shield, but the script and P44 put him under it.
- **P45:** three figures in a row, side-on; KLANG sits on the overlap, which is the panel's action.
- **P46:** ring, SFX and window all on one figure.
- **P49:** a tangle of three men under two shields; WHOOMP covers the throw-off contact.
- **What works:** P44, P47 and P48.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P41 REDRAW | wide | high, over the giant's RIGHT shoulder from behind its bell-head, looking down, 35 mm | The clapper comes down at Jaeha, alone in open water: its head huge in the near foreground, foreshortened, its shadow spreading over him. He looks up, feet planted, the notebook in his RIGHT hand, eyes narrowed (calculating, not frozen). Keep the spec scale. | speed lines along the arc; the shadow on the water round him; dark water | WHOOOM, L, along the outside of the arc at the top edge, off Jaeha and the shoulder | — |
| 2 | P42 REDRAW | tall | low from the water beside Jaeha, looking up, 20 mm | Mok lunges in from the left on reflex, one long diagonal: LEFT knee bent forward, RIGHT leg straight back, foot planted. The black tower shield is thrust up over both of them (LEFT forearm in the grip, RIGHT palm shoving its lower edge). His face in profile, teeth gritted. Jaeha crouched under him, forearms up, looking at Mok in surprise. The clapper's head fills the top, coming down. | the clapper's shadow; speed lines down from it | HUP, S, beside Mok's mouth on the open side | — |
| 3 | P43 REDRAW | wide | worm's-eye from under the shield, looking up, 24 mm, dutch 15° | The impact from below: the clapper's head smashes onto the shield's face at top centre; a crack runs down through the red hound's head toward the camera. Mok's arms buckle, his grimacing face half-lit at the right. In the foreground, Jaeha's LEFT hand flat on Mok's back: he is under the shield. | radial burst at the contact; dust and water shaken off the rim; white at the contact | KRAKKK, L, along the crack on the shield's lower left; Mok's face clear | — |
| 4 | P44 KEEP | wide | as drawn | Jaeha shouts to Borro. | — | — | "BORRO! SHARE HIS SHIELD!" |
| 5 | P45 REDRAW | wide | eye level, three-quarter from the front right, 35 mm, Borro nearest the camera | Borro slides his iron shield in beside Mok's cracked one so they overlap into one roof: his shell and RIGHT shoulder under Mok's rim (RIGHT palm flat under it), LEFT forearm in his own strap pushing it up; the clapper's head rests across both. Mok cropped at the left edge; only Jaeha's two hands between them (one on Mok's back, one on Borro's shell). Drone hidden in the moss. | dust and water shaking off both rims; moss-green outline; speed lines on the sliding shield | KLANG, M, at the outer right end of Borro's shield, not on the seam | — |
| 6 | P46 KEEP·RL | wide | as drawn | Jaeha takes the load. | — | THOOOM, M, lower left, off Borro's face | window [CARRY · BORRO · 90%] up in the dark underside of the shields |
| 7 | P47 KEEP | wide | as drawn | Mok and Jaeha under the shields. | — | — | "IT'S LIGHTER. WHY IS IT LIGHTER? WHAT DID YOU DO?" / "EVERYONE COMES BACK, SIR. EVEN YOU." |
| 8 | P48 KEEP | inset-l | as drawn | Mok's eyes. | — | — | — |
| 9 | P49 REDRAW (1/2) | wide | low from behind Borro, over his shell, looking up, 24 mm | Borro heaves both shields up together: legs driving, back arched, both arms thrusting up; the clapper is flung off and out of frame top right. Mok and Jaeha are not in this panel. | speed lines upward; spray thrown off the shields | WHOOMP, L, top right where the clapper exits | — |
| 10 | NEW (P49, 2/2) | wide | high, wide lens | The result: the giant staggers back one step on screen right, RIGHT arm flung back with the clapper, chains swinging, water splashing at its heel. Borro, Mok and Jaeha small below, apart. | chain motion arcs | SPLSH, S, at its heel | — |

9 → 10 panels.

### Inside the ring, P50–P54 (grade 4)
They run inside the chalk rings; the toll smashes the walls but not them; Borro is released; Mok: "Chalk."

**What's wrong**
- **P52 (the payoff of the whole plan):** `full` drawn wide, and the [BORRO · LINK RELEASED...] window covers the team. The original art has all five drawn inside the ring, so the reader sees an empty ring and a giant.
- **P53:** the frame top and the balloon cut off Mok's face, and his face is the beat.
- **What works:** P50, P51 and P54.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P50 KEEP | wide | as drawn | Yerin waves them in. | — | — | "THE RINGS ARE MARKED! GET IN CLOSE!" |
| 2 | P51 KEEP·RL | wide | as drawn | They run in close as the fist rises. | — | SPLSH SPLSH, S, in the water lower left, off Jaeha | — |
| 3 | P52 REDRAW (fallback: KEEP art, window moved to row 4) | tall (peak 2) | high, 12 m up the dome, looking down at 60°, 18 mm | The toll bursts outward. Upper half: a bronze shockwave ring rolls away and smashes into the walls (spray, broken stone, cracking bells). Lower half: a perfectly still disc of water at the giant's feet, the whole team untouched: Jaeha against a chalk-ringed pillar, LEFT hand over his bleeding LEFT ear; Mok against the next, staring round; Yerin hugging the third; Borro with his glow gone and shield lowered; Nib crouched at the ankle. The giant's legs and robe at the top of the lower half, its fist on the bell-head cropped. | outward radial speed lines on the ring; no lines at all in the calm disc | DOOOOOOONNNG, XL, along the ring in the upper half; never over the team | — (window moves to row 4) |
| 4 | NEW | inset-r | close on Borro's husk face | The moss-green glow goes out of the eye holes; his shoulders ease (rest form). | flat dark background | none | window [BORRO · LINK RELEASED · REST FORM · COOLDOWN 01:00] above his head |
| 5 | P53 REDRAW | wide | low from the water at Mok's boots, looking up, 28 mm | Mok looks down at the white chalk line round his boots; his whole face in frame, breathing hard; the cracked shield at his LEFT side. | dust settling | none | "CHALK. YOU BEAT IT WITH CHALK." (balloon beside his head, not over it) |
| 6 | P54 KEEP | inset-r | as drawn | Jaeha, polite and bloody. | — | — | "TRAP RATS ARE CHEAPER THAN HEALING POTIONS, SIR. YOUR MEN SAID SO." |

5 → 6 panels.

### Thirty seconds, P55–P66 (grade 6)
Nib's slash at the crack enrages it; the bell rings without stopping; the walls crack; the stair falls; the CALL decision; 00:24.

**What's wrong**
- **P55:** good low angle, but SKRANNG sits on the contact.
- **P56:** the swat isn't shown; we only see the result.
- **P60:** the giant stands square and symmetrical; DONG ×4 covers the bell; you can't see the safe space shrinking.
- **P62:** the stair is a small diagonal under a window, so the crumbling doesn't read.
- **What works:** P57, P58, P59 (the window on a reaction panel, the right way), P61, P63 (five figures, acceptable as a huddle), P64, P65 and P66.

| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1 | P55 KEEP·RL | wide | as drawn | Nib on the arm slashing at the crack. | — | SKRANNG, L, upper right along Nib's arm; the sparks at the crack clear | — |
| 2 | NEW | wide | eye level, close, dutch 15°, 35 mm | The swat: the giant's huge LEFT hand sweeps across the frame and catches Nib mid-air with the backs of its fingers. Contact at his RIGHT shoulder and ribs; his body folds round the blow, both knives still in his fists. | smear on the hand; burst at the contact; flat violet background | THWAK, M, beside the contact on the open side | — |
| 3 | P56 KEEP·RL | wide | as drawn | Nib hits the water; the giant drops the clapper and grips its head. | — | SPLASH, M, right of Nib in the water | — |
| 4 | P57 KEEP | wide | as drawn | The crack widens; the bell hums. | — | MMMMMMMMMM | — |
| 5 | P58 KEEP | wide | as drawn | Jaeha and Mok look up. | — | — | "WHAT'S IT DOING?" / "IT'S NOT RINGING ONCE ANYMORE. IT'S GOING TO KEEP RINGING." |
| 6 | P59 KEEP | wide | as drawn | Jaeha's face in red light. | — | — | window [BOSS ENRAGED · 00:30] |
| 7 | P60 REDRAW | tall (peak 3) | worm's-eye from the water just outside a chalk ring, 16 mm | Ring after ring of bronze force rolls toward the camera (three visible, foreshortened, the nearest sweeping under the viewer). Beyond them the giant hunches forward in an S-curve, both hands clamped on its vibrating bell-head. Near foreground: a pillar's chalk ring, with the nearest force ring's edge creeping over the chalk (the safe space shrinking). | the bell drawn with doubled vibration outlines; ripples; outward speed lines | DONG ×4, M each, one on each ring's edge, smaller with distance; none on the bell-head | — |
| 8 | P61 KEEP | wide | as drawn | The wall cracks and bulges. | — | KRRRRAAAKK | — |
| 9 | P62 REDRAW | wide | low and close on the foot of the stair, 24 mm | The lowest steps crumble into the water, blocks breaking off and falling. The stair runs large up the frame to the small dark door 6 m up at the top right, now out of reach. | dust; falling blocks | KRUMBLE, M, beside the falling blocks | window [BOSS: HARVEST ONLY · RELEASE: NOT AVAILABLE] in the empty wall band, top left |
| 10 | P63 KEEP | wide | as drawn | All five pressed under Borro's shield. | — | — | "MY TIME IS ALMOST GONE. AND MY KNIVES DON'T BITE BRONZE!" |
| 11 | P64 KEEP | wide | as drawn | Jaeha's point of view; the cyan mark pulses. | — | — | window [CALL · HELD] |
| 12 | P65 KEEP | strip | as drawn | His eyes harden. | — | — | — |
| 13 | P66 KEEP | wide | as drawn | The countdown. | — | DONG DONG DONG | window [BOSS ENRAGED · 00:24] |

12 → 13 panels.

---

## Patterns across chapters 13–17

1. **The letterer hides the drawing.** Measured: 78% of impact SFX are placed in the top 40% of the panel, 54% are XL, and nearly every action panel asks for `calm: top`, which the low-angle art ignores. The impact recipe's "large SFX space along the diagonal" builds in the collision, because the action is drawn on that same diagonal. Confirmed against the originals in 17 panels across all five chapters.
2. **Peaks are no bigger than anything else.** `full` comes out at 1536x1024, the same as `wide`, and every frame is untilted. The 1–3 "biggest panel" peaks don't exist on the page.
3. **Borro's brace is the same shot about eight times.** Side-on, eye level, attacker on one side, shield upright: ch13 P40; ch15 P02, P14, P22, P34; ch17 P26, P37, P45. The camera is never under the shield, over his shoulder, or behind the attacker.
4. **Nib, the striker, is small and usually hidden.** About an eighth of the panel in ch15 P04, at the frame edge in P34, under the SFX in P04, P23, P34 and P35. In a 16:9 video he is a few dozen pixels.
5. **No weapon ever comes at the reader.** No foreshortening in any of the 44 impact panels.
6. **The most important beats are crammed.** Three or more actions or four or more figures sit in the key panels: ch15 P22 and P34; ch16 P49; ch17 P30 and P52.
7. **CARRY panels stack a ring, an SFX and a window on one face.** This happens in ch15 P06 and P24, ch16 P38, ch17 P27 and P46. The scripted body damage is often missing: the forearm cut in ch15 P24 and the nosebleed in ch16 P38.
8. **The narrator describes what the art hides.** For example ch15 P34 ("Nib... drops onto the boar's skull") and ch17 P52 ("inside the chalk rings the water doesn't ripple"), over a hidden Nib and a hidden team.
9. **Continuity breaks that hurt the fight's read:**
   - ch17's giant flips screen sides across P25–P49 and drifts in scale (P41).
   - ch13's arena changes design between panels.
   - ch13 P38's Nib has no mask.
   - The drone reads as an eyeball on Borro's head in ch17 P26, P30, P45 and P49. The owner wants weird or AI-looking details fixed.
10. **What already works, so keep it:**
    - Anticipation panels: ch15 P21 and P32; ch17 P20, P25, P29 and P57.
    - Panels where Jaeha reads the fight: ch15 P16, P17 and P20; ch17 P31, P34 and P65.
    - Comedy and chorus beats: ch13 P37 and P39.
    - The one window placed on a reaction panel: ch17 P59.

## Changes to art direction and process I recommend

- **Rule 7, replace it with:**
  > "Show the contact. In an impact panel the blow connects on-panel: blade sparks on stone, a clapper on a shield, a tusk raking a forearm with a short spray. Only deaths of people, wounds in close-up and gore stay off-panel or in silhouette; blood is a spray or a splash."

  The current rule contradicts the impact recipe, and the model already draws this safely (ch15 P23).
- **Impact recipe:** change "large SFX space along the diagonal" to "a clear corner for the SFX, opposite the contact point". Put the dutch tilt inside the drawing.
- **Lettering rules:** one SFX per impact; L at most, XL only on the 1–3 peaks; placed after seeing the art, beside the contact, angled with the motion; never over a face, hand, weapon or the contact. Windows only on reaction, quiet or insert panels. A dialogue line is never lettered as an SFX.
- **Shapes:** `tall` for every peak and every vertical action; wide establishing shots only at the start or end of an exchange; the figure in focus at least a third of the panel height in action panels.
- **Script fields:** add a `contact:` point and keep the SFX position relative to it, so the art leaves that spot clear and the letterer has a target.

## Measured versus judged, and memory

- **Measured:** the art sizes, the untilted frames, the SFX positions and sizes and `calm` fields from the YAML, the windows on action panels, and the lettering covering drawn content (original art compared with the lettered pages for 25 panels).
- **My judgement:** the grades, the re-letter estimates, and every storyboard choice.
- **From memory:** the owner wants weird or AI-looking details fixed and a strict art review; I used that to flag the drone-eyeball.
- **Possible new memory (from this audit):** in MSGF the lettering layer, not the art, hides most of the drawn hits. Re-letter first, then redraw.
