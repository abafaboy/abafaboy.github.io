# Fight audit and re-storyboard: My Summons Go First, chapters 10–12

**Method.** I read ch010–ch012.yaml, CHARACTER_DESIGNS_v2, MANHWA_ART_DIRECTION, the style guide (§7–9) and PANEL_BRIEF_v2. Then I looked at every lettered page of every fight in order, as 3-page contact sheets at 480 px wide. I also opened the original art at 700–760 px for every panel I criticise below. The sheets and helper scripts are deleted, and nothing outside my folder was touched.

**Sequences found:**
- **ch010:** one fight, the tower: P31–P55, with P28–P30 as its set-up.
- **ch011:** the shutter (P03–P05), the alleys (P15–P39), the footbridge (P40–P64), and the boss reveal (P68–P73). The reveal is not a fight, but ch012's fight starts on it.
- **ch012:** Heat (P01–P08) and the freezer lane (P12–P29).
- **Not fights:** ch010 P11–P12 (Borro flattening the bed is a comic splash) and ch012 P55–P58 (Moon Ahin's husk drill).

---

## 0. Calibration check (the main session's ch011 notes, tested on ch010–012)

1. **"Bodies are posed."** Confirmed, with exceptions.
   - Posed:
     - ch011 P15: Nib squats square to the camera, knives hanging.
     - ch011 P22: Borro stands beside the shield, legs straight, facing us.
     - ch011 P32: a symmetrical front-on wide stance while two hounds hit him.
     - ch011 P62: Nib steps down the stairs with both arms flung out.
     - ch010 P44: Jaeha in a T-pose.
     - ch012 P26: Nib walks upright up the coils.
   - Real weight and line of action: ch010 P39 (Borro's lunge), P43 and P50; ch011 P27 (the granny's follow-through), P42 (Nib's lunge) and P53; ch012 P04, P21 and P27.
2. **"Eye level, medium or wide."** Confirmed. The bigger fault is that one shot repeats:
   - ch011 P41, P53 and P62 are the same low shot from the foot of the stairs, with hound backs in the foreground and Nib facing us.
   - ch010 P38 and P45 are both low from behind Borro.
   - Action close-ups (a blade, a foot planting, a claw) appear only in ch012 P02 and P27 and ch011 P57.
3. **"Hits never visibly land."** Corrected: contact is drawn in about a dozen panels, and the lettering hides it.
   - Contact in the art:
     - ch010 P39 (white bursts on the shield), P50 (X-slash burst on the throat), P53 (knives in the neck).
     - ch011 P04 (the shutter dented in the shape of the head), P23, P27 (the radish exploding on the head), P42, P53, P57 (the drone exploding on the head).
     - ch012 P01 (jaw on shield), P02 (sparks), P04 (steam on the shield), P27 (scales shattering round the blades).
   - What hides it is the SFX on top (section 5, pattern 1).
   - Contact is truly missing only where the script wrote the result instead of the hit:
     - ch011 P16: the blades are up at Nib's shoulders; the hound bursts below him.
     - ch011 P25: Nib floats above an untouched hound.
     - ch011 P48: the deck rests on Borro's raised hands, not his shell.
     - ch011 P62: no hound is under the blades.
     - ch010 P38 and P45: no shield-on-hound contact.
     - ch012 P28.
4. **"SFX do the work."** Confirmed.
   - There are 25 XL SFX in the action beats: ch010 6, ch011 14, ch012 5.
   - Multi-word repeats: THUD THUD THUD, KRASH KRASH KRASH, SHK SHK SHRAKK, BOOM BOOM BOOM (twice), SHRAKK SHRAKK SHRAKK, WHAM... WHAM..., KACHUNK KACHUNK, TAP TAP TAP (twice).
   - In ch010, 12 of the 19 SFX between P31 and P55 sit on a fighter, a face or the contact. ch011 and ch012 are the same or worse. For example:
     - ch011 P60: FSSSHHHHH hides the granny completely.
     - ch011 P64: KRRRRAAASSHHHH runs across Borro's mask and chest.
     - ch012 P01: KRANNNGGG sits on the serpent's head at the contact.
     - ch010 P46: SHRAKK sits on Yerin's hand on the wound.
5. **"Detailed background during the hit."** Mostly confirmed. The style guide's density ladder already says impact panels get 0% background; most ignore it.
   - Exceptions that work: ch010 P50; ch011 P16, P42 (flat white top), P55 (red flash); ch012 P01, P04, P13 (blue speed lines), P27.
6. **"Choreography doesn't read."** Confirmed.
   - The two biggest beats are wide shots with small figures: ch011 P48 (Borro holding the bridge) and ch012 P28 (the kill).
   - **Premise error:** the "P51 WHAM" panel is **P55**. P51 is Seoa walking backwards. What fails in P55:
     - The camera is a flat eye-level side view.
     - Lying down, Nib is longer than the hound's body; at 105 cm he should be shorter than it.
     - The jaws are above the knife, not on it.
     - The dropped knife in the foreground is the biggest object in the panel and pulls the eye away from the jaws.
7. **"Windows on top of action."** Confirmed.
   - Windows on action beats:
     - ch010 P44 is a whole system panel between the climber's leap (P43) and the heave (P45).
     - ch011 P53 (the window over the hounds he is fighting), P54 (on the leap) and P71.
     - ch012 P23.
   - Carry windows also cover the hands that show the carry: ch010 P40 and P46, ch011 P24 and P49.

**Two causes the brief does not list (both measured):**
- **`full` renders at 1536×1024, the same as `wide`.** This is in PANEL_BRIEF_v2 "Size by shape", and every full panel in these chapters is 1536×1024. So "the chapter's biggest image" (ch011 P48), ch011 P72, and ch012 P01 and P28 are no bigger on the page than a talk panel.
- **SFX are placed before the art exists.** The script fixes each SFX's position (`at: [x,y]`) and size, and the letterer puts it there. That is why SFX keep landing on the contact. The `impact` recipe's "large SFX space along the diagonal" adds to it.

**Rule 7 ("violence happens between panels"): drop it for monster fights**, in both MANHWA_ART_DIRECTION §3.7 and the style guide §9's last bullet.
- Replace it with: "Contact is shown; gore is not. Draw the instant of contact: a blade on a throat, a skull on a shield, jaws on a blade. Monsters burst into ash outward from the contact point. On people, blood is a spray or a splash, never a wound close-up. Human deaths stay off-panel (silhouette or splash)."
- The rule is one cause, not the main one. It explains why the scripts write results ("bursts into ash", "slashes a hound in two") and the art draws results. The lettering and the `full` size do more damage.

---

## How to read the tables

**Status.** The status is the first word of the "replaces" column:
- **KEEP**: the art stays as it is.
- **KEEP, re-letter**: the art stays; only the SFX or window moves. No image generation is needed.
- **REDRAW**: the panel is drawn again from the new row.
- **NEW**: a panel that did not exist.
- **CUT**: the panel goes.

**Shapes, as the pipeline really renders them:**

| Shape | Size and use |
|---|---|
| wide | 1536×1024 |
| tall | 1024×1536 |
| bleed | 1024×1536, lettered edge to edge with no margin; used only for peaks |
| inset | 1254×1254, shown at half the column width |
| strip | the middle half of a 1536×1024 |

**Lettering rules for every row:**
- Lettering goes on after the art, placed beside the contact on the side the blow travels toward.
- It never goes over a face, the hand doing the action, or the contact.
- One word per impact.
- XL only on a bleed peak.

**Image prompts.** No text in any image. In rear views, always state Borro's side: "seen from behind, the shield on his LEFT forearm, on the IMAGE-LEFT".

**Narration.** NEW quick beats (insets and strips) can share the narration line of the panel next to them. Where a panel moves, its narration line moves with it.

---

## CHAPTER 10: A Roof, Not a Garden

### T: The tower gate (P31–P55): 5/10
The pack moves only when the alpha howls. Borro holds the 60 cm beam while Nib runs the rim and cuts the alpha's throat; Borro then drops the slab and the pack with it.

**What works:**
- The tell, plan and exploitation chain is the best-built fight in these chapters: P33 (the howl), P34 (the notebook), P35 (the plan), P36 (the orders).
- P28, P32 and P35 set up the beam and the drop.
- P43 (a hound in the air over the shield, with speed lines) is a proper manhwa panel.
- P49 (the knife's glint behind the raised head) is a good anticipation.
- P50 (the tilted X-slash, burst on the throat, speed lines) is the best panel in the chapter.

**What is wrong:**
- **P38 (tall, the opening blow).** The shield stands at Borro's side, not across the beam, and the pack walks single file past its edge. There is no speed. Seen from behind, the shield is on his RIGHT arm. It is the same camera as P45.
- **P39.** Two hounds stand on their hind legs pawing at the shield, like dogs at a door: no charge, no crumple. It is two actions in one panel (the hit, and a hound flying off). KRANNGG (XL) runs across Borro's legs and torso.
- **P40.** The window covers his hand on his chest, which is the carry.
- **P42.** Nib leaps square to the camera with his arms out, the same as P41. KRAKK covers his legs and the slab that breaks, which is the cause of the leap.
- **P44.** A front-on T-pose system panel is inserted between the anticipation (P43) and the payoff (P45). It kills the beat.
- **P45 (tall, the heave).** It is the same camera as P38, with the shield on his RIGHT arm again. WHOOOMM (XL) covers his shell and hip. The hounds are small, flailing shapes; the shove's contact is not the focus.
- **P46.** SHRAKK sits on Yerin's hand on the wound and the window covers the bottom third. The panel's two subjects are both covered.
- **P48.** The swing round the column is not drawn: Nib is already crouched, small, in the lower left of a wide eye-level shot.
- **P51.** The shield stands propped and unheld. STOMP covers the heel's impact.
- **P52.** KRRRRRRUMBLE (XL) sits across Borro, the only figure in the panel.
- **P53.** The alpha's last lunge is not drawn. SHHUNK (XL) covers Nib's torso.
- **Jaeha's reading.** From P48 to P54 there is no Jaeha panel, so the payoff of his plan never shows on his face.
- **Video format.** 18 of the 23 panels from P31 to P53 are 3:2 wides.

**Count: 25 → 32 panels (+28%).** 19 KEEP (9 of them re-lettered), 6 REDRAW, 7 NEW.
- Axis: the team and Borro are on the image-left, facing right; the pack comes from the image-right.
- The Nib–alpha exchange gets its own axis at T23: Nib on the left, the alpha on the right.
- Nib's knives in this chapter are held in a forward grip, to match the kept P49–P53.

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| T01 | KEEP P31 | wide | as drawn | eight hounds slink out between the far columns (a slow line is right for an anticipation) | as drawn | HHHHHH (S) as now | (silent) |
| T02 | KEEP P32 | tall | as drawn | the pack fanned out, the alpha behind, the beam leading to them | as drawn | GRRRRRRR (L) as now | — |
| T03 | KEEP P33, re-letter | wide | as drawn | the alpha howls; every head snaps round | as drawn | AWOOOOOOO (L, not XL): from the open jaw rising to the upper left; the pack's heads stay clear | — |
| T04 | KEEP P34 | wide | as drawn | the notebook sketch | — | — | note: "THEY ONLY MOVE WHEN THE BIG ONE HOWLS. CUT THE HOWL, AND THE PACK BREAKS." |
| T05 | KEEP P35 | wide | as drawn | the plan overlay | — | — | inner: "THE SLABS WON'T HOLD HIM. THE BEAM WILL. AND THE EDGES ARE STILL ATTACHED." |
| T06 | KEEP P36 | wide | as drawn | Jaeha gives the orders | — | — | "BORRO, STAND ON THE BEAM AND DON'T LET ANYTHING PAST YOU." / "NIB, GO ROUND THE EDGE. CUT THE BIG ONE'S THROAT. THEN THE HOWLING STOPS." |
| T07 | KEEP P37 | wide | as drawn | three-way link-view | — | VMMM (S) | window [FIELD FORM · NIB 05:00 · BORRO 05:00 · LINKED] as now |
| T08 | REDRAW P38 | tall | over Borro's LEFT shoulder at 2.3 m, 28 mm, looking straight down the beam to the far column | Borro (field form) is planted mid-beam, feet one behind the other along the 60 cm beam, knees bent, weight low. The shield is on his LEFT forearm, held square ACROSS the beam with its edges overhanging the drop on both sides; its top edge crosses the lower third of the frame. His RIGHT palm is flat on its back. Beyond the rim the pack charges single file at full stretch, the lead hound 6 m out. | the beam as one hard perspective line; slab edges crumbling into black on both sides; violet ash streaming off the hounds; background desaturated 50% | THUD (S): at the lead hound's paws | — |
| T09 | NEW | wide | worm's-eye on the beam's surface, 20 cm up, 3 m in front of the shield, 24 mm, looking back along the beam | The lead hound is in mid-bound AT the camera. Its split jaw is wide and foreshortened, teeth nearest the lens; forelegs reaching, hind legs fully extended in one stretched line from tail to jaw. Two more come single file behind it. | background dropped to speed lines converging on the lens; concrete chips spitting off the beam's edges | none | — |
| T10 | REDRAW P39 | tall, dutch 15° | side-on at beam height from over the drop, 35 mm | The lead hound's skull smashes into the shield's dented boss and its body crumples behind the head: shoulders folding, hind legs lifting off the beam. Borro leans INTO the blow: LEFT forearm in the strap, RIGHT shoulder and RIGHT palm driving the shield's back, knees bent, one C-curve from his rear heel to his head. His RIGHT heel slides back half a step, ploughing up concrete dust. | hard white burst exactly at the boss; impact radials; flat white-to-orange background; flying chips | KRANNGG (L): behind the hound's hindquarters at the upper right, along its line of travel (-8°); clear of Borro and the boss | — |
| T11 | NEW | inset-r | high, looking straight down past the shield's outer edge into the void, 35 mm | A second hound glances off the shield's edge and drops into the dark floors below, legs splayed, ash trailing. Only the shield's edge and Borro's RIGHT hand show at the top of the frame. | downward speed lines; the floors below black | none | — |
| T12 | KEEP P40, re-letter | wide | as drawn | Jaeha staggers as the hit lands in him; Yerin grabs his arm | as drawn | THOOM (M): off his face, onto the ring's lower-left edge | window [CARRY · BORRO · 30%] moves to the top edge, clear of both faces and of his hand on his chest |
| T13 | KEEP P41, re-letter | wide | as drawn (high along the rim) | Nib runs the rim, arms out for balance, the drop beside him | as drawn | TAP TAP TAP (S): at his heels only | — |
| T14 | NEW | inset-l | extreme close-up, low, at the rim's lip, 50 mm | Nib's bare LEFT foot is planted on the rim; the concrete under the heel cracks and breaks away, toes clawing at the crumbling lip | crack lines; falling grit; black void below | KRAK (S): under the foot, beside the crack | — |
| T15 | REDRAW P42 | wide, dutch 12° | worm's-eye from below the rim against the dusk sky, 24 mm | Nib is in mid-leap, stretched along one diagonal (a C from his trailing LEFT foot to his reaching RIGHT hand). His RIGHT hand closes on a hanging rebar coil at the upper right; LEFT arm swung back; knives still in their crossed sheaths; scarf streaming straight back. The broken chunk of slab drops away under him. | speed lines along the leap; falling chunks; sky gradient | KRAKK (M): on the falling chunk, lower left | — |
| T16 | REDRAW P44, moved here from between P43 and P45 | wide | close, slight low angle, 50 mm; Jaeha in the lower half, the top half empty and dark | Jaeha jolts as both summons' hits land at once: torso twisting, LEFT hand clutching the vest over his chest, head snapping back, a nosebleed starting. Amber light on the left of his face, moss green on the right. No T-pose. | flat dark background; thin amber and green threads behind him; focus lines on his face | none | window [TWO SUMMONS LINKED] CARRY LOAD IS SHARED BY THE OPERATOR · OK in the top half (its narration line moves with it) |
| T17 | KEEP P43, re-letter | wide | as drawn | the pack piles onto the shield; one hound leaps clean over the top at Borro's head | as drawn | SKRRRK (S): off his head, onto the claws on the iron at the lower right | — |
| T18 | NEW | strip | ECU of Borro's husk face, 85 mm | the two round eye-holes blaze moss green and the mask's cord pulls taut (the wind-up) | black; green glow only at the eye-holes | none | — |
| T19 | REDRAW P45 | bleed (peak 1) | worm's-eye from the beam 2 m in front of the shield, 20 mm, looking up | Borro heaves. The shield drives forward AT the camera, its riveted face and dented boss foreshortened across the lower half. His masked head and blazing eye-holes show above the rim, his shoulders behind it. His RIGHT foot stamps forward beside the shield's lower corner, toes over the beam's edge. The pack is hurled back past and above the camera: three hounds in silhouette, legs flailing, two dropping off the sides. The clinging hound hangs from the top rim by its jaws. | radial speed lines bursting out from the boss; background dropped to a moss-green-to-white flash; flying chips | WHOOOMM (XL): across the sky above his head, along the flying hounds' arc | — |
| T20 | NEW | inset-r | close on Borro's LEFT forearm in the shield strap, three-quarter, 50 mm | The clinging hound's hooked foreclaws rake down the cloth wrap on his LEFT forearm: three grey scratch lines through the cloth into stone-grey skin, grit and fibres flying. He is stone, so there is no blood. | short radials at the claw tips; flat dark background | SKRK (S): along the rake | — |
| T21 | KEEP P46, re-letter | wide | as drawn | the gash opens on Jaeha's RIGHT shoulder; Yerin's mint hand is on it | as drawn | SHRAKK (M): off Yerin's hand, above his shoulder along the gash's diagonal | window [CARRY · 2 SUMMONS · LOAD 110%] moves to the bottom-right corner, clear of both hands |
| T22 | KEEP P47 | inset-l | as drawn | Yerin afraid; Jaeha still watching the fight | — | — | "YOU'RE TAKING BOTH OF THEIR HITS!" / "THAT'S THE DEAL I MADE." |
| T23 | REDRAW P48 | wide | high, from above the far column's top, looking down, 24 mm | Nib swings round the column on the rebar: RIGHT fist on the coil, arm straight, body flung out near-horizontal, legs together trailing the curve (a tight C). His LEFT hand draws one knife in a forward grip. Far below at the column's base is the alpha's back and raised head with flaring cracks, facing away toward the beam, with Borro's green glow far beyond. | curved speed lines following the swing; dusk rim light on Nib; background 50% | WHIP (S): on the speed lines behind his feet | — |
| T24 | KEEP P49 | wide | as drawn | the alpha's head thrown back to howl; the knife's amber glint behind it | as drawn | HHHHHHH (S) | — |
| T25 | KEEP P50, re-letter | tall | as drawn | the X-slash across the throat (peak 2) | as drawn | SHRAKK (L): off Nib's arms, below the burst along the slash's diagonal on the alpha's dark chest | — |
| T26 | NEW | inset-r | close, slight low angle, 85 mm | The private grin: Jaeha at the core wall, blood under his nose, eyes narrowed, one corner of his mouth up, half his face in shadow; an amber and a green glint in his pupils. | flat black; focus lines | none | (silent) |
| T27 | KEEP P51, re-letter | wide | as drawn | Borro stamps beside the beam; the hounds stumble | as drawn | STOMP (M): beside the heel along the crack line, not on the impact | — |
| T28 | KEEP P52, re-letter | wide | as drawn (high, looking down) | the slab drops away with the hounds | as drawn | KRRRRRRUMBLE (L): off Borro, onto the void at the lower right, angled down with the fall | — |
| T29 | NEW | inset-l | over Nib's LEFT shoulder at his eye level, 24 mm | The dying alpha lunges: split jaw wide, coming AT the camera, teeth foreshortened, violet ash pouring from the X-cut on its throat. Nib's two knife tips are raised at the bottom edge of the frame. | speed lines converging on the lens; flat violet-black | none | — |
| T30 | KEEP P53, re-letter | wide | as drawn | Nib steps inside the bite and drives both knives up into the neck cracks; it bursts into ash | as drawn | SHHUNK (M): off Nib's torso, into the ash cloud at the upper right beside the blades | — |
| T31 | KEEP P54 | wide | as drawn | aftermath | — | — | (silent) |
| T32 | KEEP P55 | wide | as drawn | Jaeha slides down the wall | — | HAA... HAA... (S) | window [CARRY LOAD 140% · OVERLOAD WARNING] as now |

---

## CHAPTER 11: Market Break

### S: The shutter (P03–P05): 6/10
A hound slams into the tteok shop's shutter while the kimchi granny holds it.

**What is wrong:**
- The dent in the shape of the hound's head is a good idea and well drawn.
- BANNNG (XL) is lettered across both bodies.
- There is no anticipation: we never see the hound coming.
- Seoa has a hand on the granny's back rather than bracing. That fits her (she directs), so it is not a redraw.

**Count: 3 → 4.**

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| S01 | KEEP P03 | wide | as drawn | herding everyone into the back room | — | KRRRRANNG (M) as now | "EVERYONE INTO THE BACK! GRANNY, LOCK THE SHUTTER!" |
| S02 | NEW | inset-r | close, inside the shop at the shutter's slats, 50 mm | Through the gaps in the lowered shutter, a hound's eyeless head drops low; its shoulders bunch as it takes one step back to charge. Red emergency light stripes it. | slats as black bars; red light; flat dark | GRRR (S): at the slats | — |
| S03 | KEEP P04, re-letter | wide | as drawn | the shutter bulges inward in the shape of the head; the granny braces | as drawn | BANNNG (L, not XL): off both bodies, onto the bare shutter metal above the bulge, angled with the dent | — |
| S04 | KEEP P05 | inset-l | as drawn | Seoa against the shutter, routing her brother in | — | — | "COME IN BY THE PHARMACY ALLEY. THIRD LEFT AFTER THE KIMCHI SHOP." / "IT'S TOO NARROW FOR TWO OF THEM SIDE BY SIDE." |

### A: The alleys (P15–P39): 4/10
Borro plugs the funnel square while Nib herds hounds from the awnings and the granny clubs one that slips past. Then a second wave forces both summons back to the bridge.

**What works:**
- P16: low, tilted, a white and orange flash, the hound bursting.
- P26–P27: the granny's bat stance and full follow-through, with the radish exploding on the head. This is the best-read hit in the chapter.
- P29: the nod.

**What is wrong:**
- **P22.** The "square where three alleys meet" is one straight alley. Borro stands front-on beside the shield, which blocks nothing. The funnel plan (P20) never pays off on screen.
- **P23.** The art is fine, but KRANNG (XL) covers the shield's top and the climbing hound, which is the contact.
- **P25.** "Drops onto a hound, knives first" is drawn as Nib hanging in the air with both hands up by his head, like a surrender, feet dangling; the hound runs untouched below him. The script puts two actions (the run and the drop) in one panel.
- **P28.** The kill is a small top-down inset with Nib lying along the hound's body, the limbs mixed.
- **P32.** Two hounds hit him from two sides, drawn as a symmetrical front-on stance with two small sparks. KRANG covers one hound. Two actions in one panel.
- **P36.** "Boiling up out of the stairwell, climbing over each other" is drawn as a file of hounds walking past the stairwell railing.
- **P39.** The art is dynamic, but KRASH KRASH KRASH spans the whole panel, and the shield is carried at his side rather than in front.

**Count: 25 → 28 (+12%).** 19 KEEP (4 re-lettered), 6 REDRAW, 3 NEW.

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| A01 | KEEP P15 | wide | as drawn | the ignition: Nib's eye flares; Borro (rest form) raises the shield | as drawn | — | window [FIELD FORM · NIB 05:00 · LINKED] as now; (silent) |
| A02 | KEEP P16, re-letter | tall | as drawn | Nib at the end of a cross-slash in mid-leap; the hound bursting below him | as drawn | SHRAKK (L): off his arms and knees, onto the white field at the upper right along the slash's diagonal | — |
| A03 | KEEP P17 | wide | as drawn | Bomi arrives | — | — | "MY PARENTS ARE SAFE BEHIND THEIR SHUTTERS. WHAT DO YOU NEED?" / "YOUR DRONE, HIGH UP. I NEED TO SEE THE WHOLE MARKET." |
| A04 | KEEP P18 | wide | as drawn | the drone feed | — | VWEEE (S) | (silent) |
| A05 | KEEP P19 | wide | as drawn | Jaeha over Bomi's shoulder | — | — | Seoa (phone): "THE FISH LANE ONLY HAS ONE WAY OUT: UP THE STAIRS TO THE FOOTBRIDGE." |
| A06 | KEEP P20 | wide | as drawn | the plan | — | — | inner: "EVERY ALLEY IS ONE HOUND WIDE. SO THEY ALL REACH BORRO ONE AT A TIME." |
| A07 | KEEP P21 | inset-l | as drawn | the orders | — | — | whisper: "BORRO, THE LITTLE SQUARE WHERE THREE ALLEYS MEET. NIB, DRIVE THEM TO HIM." |
| A08 | REDRAW P22 | wide | bird's-eye, straight down from 8 m, 28 mm | Three 1.8 m alleys meet in a Y at a 4 m square among the stall awnings. Borro (field form) is planted in the square, feet wide. The shield on his LEFT forearm is wedged across the mouth of the lower alley wall to wall, its edges touching both shop fronts; his RIGHT hand is on its top edge. The two alleys behind him are dark and empty. In the lower alley, the first hounds' backs come single file. | full detail (this is the geography panel); awnings cropped at the frame edges; bulbs as points of light | THUNK (S): at the shield's foot | window [BORRO · FIELD FORM 05:00 · LINKED] over the awnings at the top, not over Borro |
| A09 | NEW | wide | Borro's view over the shield's top rim, 2.2 m up, 35 mm, down the alley | The lead hound charges up the 1.8 m alley straight at the camera, head low, jaws opening. Four more follow nose to tail; there is no room for two. Across the bottom of the frame: the shield's riveted rim and Borro's RIGHT fingers curled over it. | the alley walls streaked into converging speed lines; background 30%; ash trails | none | — |
| A10 | KEEP P23, re-letter | wide | as drawn (low, behind the pack) | the lead hound crumples against the shield; the next one climbs | as drawn | KRANNG (L): off the shield's top and the climbing hound, onto the left wall above the charging hound's back, angled down the alley | — |
| A11 | KEEP P24, re-letter | inset-r | as drawn | Jaeha flinches; the green ring | as drawn | THOOM (S): on the ring's edge, off his face | window [CARRY · BORRO · 25%] moves to the top, clear of his hand on Bomi's shoulder |
| A12 | NEW (the first half of P25) | wide | low, side-on, level with the awning tops, 35 mm, tracking | Nib sprints across the striped canvas awnings, body pitched forward 45°. His RIGHT foot pushes off and the canvas dents under the bare sole; his LEFT knee drives forward. Reverse-grip knives along his forearms, arms pumping, scarf straight back. Ahead of him is the dark gap of the alley between two awnings. | horizontal speed lines; the arcade roof and bulbs at 30% | TAP TAP (S): at the denting canvas | — |
| A13 | REDRAW P25 (the second half) | tall | worm's-eye from the alley floor, 20 mm, straight up through the gap between two awnings | Nib drops feet first and knives first AT the camera: bare soles and both reverse-grip blades foreshortened, knees bent to land, scarf flaring up above. In the lower third, close and out of focus, is the back of the hound he lands on, flinching low and about to bolt toward the square. | radial speed lines from the gap; awning stripes cropped at the edges; amber glint on the blades | WHUMP (M): on the hound's shoulders, lower right | — |
| A14 | KEEP P26 | wide | as drawn | a hound slinks toward the shutter; the granny steps out with the daikon over her shoulder | — | HHHHH (S) | — |
| A15 | KEEP P27, re-letter | wide | as drawn | the full-body swing; the radish explodes on the hound's head | as drawn | BONK (L, comic): off her torso, just left of the exploding radish, along the swing arc (+10°) | "NOT IN MY ALLEY, YOU UGLY DOG!" |
| A16 | REDRAW P28 | inset-l | high three-quarter from a stall awning, 35 mm | Nib lands in a crouch on the dazed hound's back among the tubs: LEFT knee on its spine, LEFT palm flat between its shoulder blades, RIGHT fist driving the reverse-grip knife straight down into the crack along its back. The hound bursts into ash outward from the blade. The snapped radish lies on the wet floor beside them. | ash burst from the stab point; short radials; red tubs simplified | SHK (S): beside the blade | — |
| A17 | KEEP P29 | wide | as drawn | Nib's nod to the granny | — | — | "GOOD SWING, GRANDMOTHER." / "I'VE GOT MORE RADISHES. GO!" |
| A18 | KEEP P30 | wide | as drawn | Seoa leads the line out | — | STEP STEP STEP (S) | "TWELVE, THIRTEEN, FOURTEEN. EVERYONE HOLD HANDS. DON'T LET GO." |
| A19 | KEEP P31 | wide | as drawn | Yerin heals; Choi carries a granny | — | SHIIING (S) | whisper: "I'M NOT FREEZING. I'M NOT FREEZING. I'M NOT." |
| A20 | REDRAW P32 (the first hound) | wide, dutch 10° | low, behind the first hound's hindquarters, 28 mm | Borro pivots on his LEFT foot and swings the shield round on his LEFT forearm into the first hound's open jaws as it leaps out of the second alley. Its teeth slam into the iron and its body folds against it. His hips turn with the pivot (a twist through the torso), RIGHT arm tucked in, eyes calm. | white burst at the contact of jaws on iron; debris; background 30% | KRANG (M): above the contact, on the side the hound came from | — |
| A21 | NEW (the second hound, from P32) | inset-r | close on Borro's RIGHT shoulder, 50 mm | The second hound's jaws snap on the slate plates capping his RIGHT shoulder and skid: teeth scraping, sparks and slate chips flying, a tuft of moss torn loose. His calm masked face is turned toward it at the frame edge. | sparks; short radials at the teeth; flat background | KLAK (S): beside the sparks | — |
| A22 | KEEP P33 | wide | as drawn | the nosebleed | — | DRIP (S) | window [CARRY · 2 SUMMONS · LOAD 90%] as now |
| A23 | KEEP P34 | wide | as drawn | the live stream | — | BLIP BLIP BLIP (S) | phone stream as now |
| A24 | KEEP P35 | inset-r | as drawn | heat pours from the stairwell | — | HSSSSS (S) | (silent) |
| A25 | REDRAW P36 | tall | worm's-eye at the stairwell's top step, 20 mm | The second wave boils up out of the violet-lit stairwell. One lead hound bursts over the top step at the camera, jaws open and foreshortened. Behind and below it is a solid black mass of hounds climbing over each other's backs, in silhouette with only their edges lit violet. Heat shimmer above them. | violet underlight; heat-shimmer lines; melting ice running off the stall edges | AWOOOOOOOO (L): across the top over the arcade roof, not over the hounds | — |
| A26 | KEEP P37 | wide | as drawn | the drone view of the flood | — | — | (silent) |
| A27 | KEEP P38 | wide | as drawn | Jaeha shouts | — | — | "THEY'RE GOING FOR THE FOOTBRIDGE! BORRO, NIB, FALL BACK TO THE STAIRS!" |
| A28 | REDRAW P39 | wide | worm's-eye at the street's centre line, 3 m ahead of him, 20 mm | Borro charges straight at the camera behind the shield. The shield is on his LEFT forearm, held in front, its riveted face and boss foreshortened across the lower half. His masked head and green eye-holes show above the rim, his body pitched hard forward. Stalls and plastic tubs burst aside to both edges of the frame; one hound bounces off the shield's top corner. Nib is a small silhouette running the awnings at the upper right. | speed lines converging on the lens; debris and produce flying outward; background 40% | KRASH (M, one word): on a flying stall at the left edge | — |

### B: The footbridge (P40–P64): 3/10
Nib holds the stairs alone while the pier fails and Borro catches the falling deck with fourteen people on it. When Nib's form runs out, Bomi's drone, Choi's extinguisher and the granny buy the minute; then Borro walks out as the bridge comes down.

**What works:**
- P40 (the geography) and P41 (the face-off).
- P42's art: a real lunge, a flat white top, contact.
- P43–P46: the collapse builds clearly.
- P52 (Borro's calm face under the deck).
- P56–P57: the drone, with contact drawn.
- P64's art: big, low, the bridge falling behind him.

**What is wrong:**
- **P48, the chapter's peak.** It was scripted `full` and rendered 1536×1024. Borro is about a fifth of the frame's height, on a rubble mound that fills the lower two-thirds. The deck rests on his raised hands, not his shell. The fourteen people are a strip of heads at the top edge, and KRRRRRUNNNCH (XL) fills the sky. At video size, the moment the arc builds to is a small grey figure.
- **P41, P53 and P62 use the identical camera** (see section 0).
- **P53 → P54: the screen direction flips mid-exchange.** In P53 the hounds come from the image-left; in P54 the hound leaps from the image-right.
- **Windows on action.** P53's window sits over the hounds he is fighting; P54's window sits on the leap.
- **P55.** See section 0, point 6.
- **P59.** GRRRRR is lettered on Nib's shoulders.
- **P60.** Three figures do different things among the hounds. FSSSHHHHH hides the granny; BONK sits on the contact.
- **P62.** "Dives down the stairs" is drawn as stepping down, upright, arms flung out to the sides, with no hound under the blades. SHRAKK SHRAKK SHRAKK (XL) runs across his waist.
- **P64.** KRRRRAAASSHHHH sits across Borro's mask and chest.
- **SFX on the contact:** P42 (SHK SHK SHRAKK across the bursting hound), P44 (KRRAAAKK over the crack it names) and P57 (KRAKSH across the hound).
- **Jaeha's reading.** The cooldown gamble has no calculating panel; Jaeha's only panels in this fight are pain and the re-call.

**Count: 25 → 31 (+24%).** 18 KEEP (9 re-lettered), 7 REDRAW, 6 NEW.
- Stair axis, taken from the existing P54, P55, P57 and P59: Nib holds the top step on the image-left; the stairs and the hounds are on the image-right.
- P42 is redrawn mirrored to fit this axis. A flipped image would move Nib's mask to the wrong eye, so it cannot simply be flipped.

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| B01 | KEEP P40 | wide | as drawn | the footbridge, the line of people, the flood | — | AWOOO (S) | (silent) |
| B02 | KEEP P41 | tall | as drawn | the face-off: Nib alone on the top step | — | SHING (S) | "A WALL AGAIN. FINE." |
| B03 | REDRAW P42 (the same idea, mirrored) | wide | eye level, side-on to the stairs, 35 mm | Nib lunges down from the top step: RIGHT foot planted one step down, LEFT leg extended behind on the top step, torso low, one diagonal from his LEFT heel to his RIGHT blade. His RIGHT arm ends a backhand reverse-grip slash through the lead hound's throat, and the hound bursts into ash from the blade. His LEFT arm is cocked back with the second knife; the next hound rears behind. | top half flat white with horizontal speed lines (as now); ash burst at the blade; amber streak along the slash | SHRAKK (M): in the white field above the burst, along the slash | — |
| B04 | KEEP P43 | wide | as drawn | the road bulges | — | RRRMMMMM (L) as now | (silent) |
| B05 | KEEP P44, re-letter | wide | as drawn | the pier cracks | — | KRRAAAKK (L): off the crack, beside the pier over the dark road, angled up along the crack | (silent) |
| B06 | KEEP P45, re-letter | wide | as drawn | the deck sags; Seoa holds the child | — | KYAAAA (M): off the people, into the sky at the upper left | — |
| B07 | KEEP P46 | wide | as drawn | Jaeha sees the bridge | — | — | "BORRO! THE PIER!" |
| B08 | KEEP P47, re-letter | wide | as drawn | Borro drops onto the road and runs under | — | BOOM (M, one word): at the cracking footfall | — |
| B09 | NEW | strip | ECU, low, at the pier's top where it meets the deck, 50 mm | The pier's head bursts outward in chunks and the deck's underside drops past the camera, a black gap opening above the stump. | falling chunks; dust; red strobe | KRAK (S) | — |
| B10 | REDRAW P48 | bleed (THE chapter peak) | worm's-eye from the road 2 m from his feet, 20 mm, almost straight up | Borro catches the falling deck on his back. He is bent forward under it, his humped slate shell and both shoulders pressed flat to the concrete underside. His RIGHT palm is flat on the underside, elbow bent. His LEFT hand clamps the top edge of the shield, which stands wedged upright between the heaved road and the deck beside the pier stump at the right. Head bowed, eye-holes blazing green, legs braced wide, knees bent. Borro fills 70% of the frame's height. Over the deck's edge at the very top: three small heads and reaching hands. Moss and tiny flowers are crushed against the concrete. | hard white burst where the shell meets the concrete; concrete dust blasting outward; moss-green outline blazing; background dropped to steam lit red | KRRRRRUNNNCH (XL, the chapter's only XL): along the deck's underside at the upper left, angled with the deck's tilt; never over Borro | — |
| B11 | NEW | inset-r | close, low, at Borro's bare feet, 35 mm | His feet sink into the heaved asphalt under the weight: the road cracks in a ring round them, chunks tilt up, toes splay, the ankle wraps strain. | ring of crack radials; dust puffs; red strobe | KRRK (S): on the crack ring | — |
| B12 | KEEP P49, re-letter | wide | as drawn | Jaeha drops to one knee; the green ring cracks the pavement | as drawn | THOOOM (L): off his arm, onto the crack ring beside his knee | window [CARRY · 2 SUMMONS · LOAD 160% · OVERLOAD] moves to the top edge |
| B13 | KEEP P50 | strip | as drawn | eyes | — | — | inner: "HE CARRIED A VILLAGE ACROSS A BRIDGE ONCE. TODAY HE'S CARRYING THE BRIDGE." |
| B14 | KEEP P51 | wide | as drawn | Seoa walks backwards along the deck | — | — | "KEEP WALKING! DON'T RUN, AND DON'T STOP!" |
| B15 | KEEP P52 | inset-l | as drawn | Borro's face under the deck | — | — | "TAKE YOUR TIME, LITTLE ONES. I AM SLOW ON PURPOSE." · window [BORRO · FIELD FORM 00:50] as now |
| B16 | REDRAW P53 | wide | high, behind Nib's RIGHT shoulder at the top of the stairs, looking down them, 28 mm | Nib sweeps a hound off the step with a RIGHT backhand in reverse grip, the blade at its jaw; it topples back onto the hounds piling up the stairs below (a dark mass, only the nearest two in focus). A heap of grey ash lies round his bare feet. His amber outline is broken into flickering dashes. | short radials at the blade; ash; stairs at 50% | SHRAKK (M): beside the toppling hound, lower right | no window (it moves to B17) |
| B17 | NEW | inset-l | close on Jaeha on one knee at the road's edge, 50 mm, slight high angle | Blood runs over his lip. His eyes flick from the deck to the stairs and his lips move as he counts. His LEFT palm is flat on the cracked pavement. | flat dark; faint amber light from the left | none | window [NIB · FIELD FORM 00:08] in the calm top; (silent) |
| B18 | NEW (takes P54's window) | strip | ECU of Nib's uncovered RIGHT eye beside the mask's edge, in the left third, 85 mm | The amber in his eye goes out like a blown candle: the iris dull, the pupil wide. | black; one fading amber streak | none | window [NIB · FIELD FORM ENDED · COOLDOWN 01:00] on the black right two-thirds |
| B19 | REDRAW P54 | tall | from behind Nib, over his shoulder, on the top step, 24 mm | A hound launches off the stairs at him, fully stretched in the air, jaws wide, foreclaws reaching AT him and the lens. Nib is in rest form with no outline: shoulders sagging, both knives hanging low in his fists, his weight falling back onto his LEFT heel. | speed lines converging on Nib; the bridge lamp behind the hound, so it reads as a silhouette | none | (silent) |
| B20 | REDRAW P55 | wide, dutch 15° | close, low at the deck surface beside Nib's head, 35 mm | The hound's split jaws clamp on the blade of the one knife Nib holds crosswise a hand's width above his throat: RIGHT fist on the grip (image-left), LEFT palm flat on the spine (image-right), elbows locked, teeth gritted, ears flat. Only the hound's head and one forepaw on his chest are in frame; its body is cropped. In the lower-right corner, small, the other knife spins away on the concrete. | red flash background; impact radials at the jaws on the blade; ash and drool flecks | WHAM (L): at the upper right above the hound's neck, away from both faces | — |
| B21 | KEEP P56, re-letter | wide | as drawn (over Bomi's shoulder, at shoulder height) | Bomi steers the drone up the stairs | as drawn | VWEEEEEEEE (M): trailing behind the drone along its path, not across the stairs | "SORRY, BABY! MOMMY'LL BUY YOU A NEW ONE!" |
| B22 | KEEP P57, re-letter | wide | as drawn | the drone explodes on the hound's head and knocks it off Nib | as drawn | KRAKSH (L): off the hound's body, into the sky at the upper left along the drone's travel | — |
| B23 | KEEP P58 | inset-r | as drawn | signal lost | — | — | phone stream as now; (silent) |
| B24 | KEEP P59, re-letter | wide | as drawn | the hounds mass again; Nib stands his ground | as drawn | GRRRRR (S): off Nib's back, onto the lead hound's jaws | window [COOLDOWN 00:12] moves to the sky at the top, off the stairs |
| B25 | REDRAW P60 (Choi only) | wide | low, from the steps above, looking down at Choi, 24 mm | Choi is planted on the bottom step, legs wide. His RIGHT hand squeezes the lever with the red canister braced on his RIGHT hip; his LEFT hand aims the black hose up the stairs. The white blast comes straight AT the camera and swallows the two nearest hounds' heads as they jerk back. | the cloud as hard clumped shapes, not fog; strobe light | FSSSHHHHH (M): along the blast's right edge, clear of Choi | — |
| B26 | NEW (the granny's half of P60) | inset-r | side-on, close, 50 mm | The kimchi granny swings a fresh daikon two-handed (yellow gloves stacked, LEFT below RIGHT) into the jaw of a hound staggering out of the cloud. The radish's fat end bursts on its teeth; her follow-through carries past her LEFT shoulder, headscarf flying. | comic white flash; radish chunks; flat pale background | BONK (M, comic): beside the jaw, along the swing | — |
| B27 | KEEP P61 | wide | as drawn | Jaeha raises his bloody hand: the re-call | — | — | window [COOLDOWN 00:00 · NIB · FIELD FORM 05:00] as now; (silent) |
| B28 | NEW (tone flip) | strip | ECU of Nib's RIGHT eye inside the white cloud, 85 mm | The amber blazes back on, brighter than before, and his outline crackles back along his cheek. | white cloud background; amber flare | none | (silent) |
| B29 | REDRAW P62 | tall, dutch 15° | low, side-on, mid-stairs, 24 mm | Nib dives headfirst down the stairs out of the cloud, one straight line from his pointed toes to his knives, like a thrown knife. Both reverse-grip blades sweep outward through the necks of the two lead hounds, each bursting into ash exactly at the blade edge. The cloud behind him is torn by his passage; the rest of the pack is a dark mass below. | amber speed lines along the dive; two ash bursts at the contacts; background reduced to cloud and black | SHRAKK (L, one word): below the second burst, along the dive | — |
| B30 | KEEP P63, re-letter | wide | as drawn | Seoa steps off with the last child | — | — | "IS EVERYONE OFF?" / "EVERYONE'S OFF! ALL FOURTEEN!" · window [BORRO · FIELD FORM 00:02] moves to the sky at the upper right, off the granny and child |
| B31 | KEEP P64, re-letter | tall | as drawn | Borro walks out with the shield overhead; the bridge falls behind him | as drawn | KRRRRAAASSHHHH (L): off his mask and chest, onto the collapsing bridge at the upper right, angled with the fall | — |

### R: The serpent rises (P68–P73): 5/10 (not a fight)
**What is wrong:**
- **P72** was scripted `full` and rendered wide. The serpent stands in the middle distance like a cobra, with Borro small at its right. The scale is roughly right, but at video size it is a mid-frame shape with nothing in the foreground to measure it against. SHHHRRRAAAAAAAA covers its coils.
- **P71.** BRRRRRRMMMMM covers the dome it names.

**Count: 6 → 6.**

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| R01 | KEEP P68 | wide | as drawn | steam from the cracks | — | HSSSSSSSS (M) | (silent) |
| R02 | KEEP P69 | wide | as drawn | Choi sweating | — | — | "WHY IS IT SO HOT? IT'S OCTOBER." |
| R03 | KEEP P70 | strip | as drawn | Jaeha's eyes | — | — | (silent) |
| R04 | KEEP P71, re-letter | wide | as drawn | the road heaves into a dome; Borro backs away | — | BRRRRRRMMMMM (L): off the dome, along the cracks at the bottom | window [COOLDOWN 00:00 · BORRO · FIELD FORM 05:00] moves to the sky at the top right, off the dome |
| R05 | REDRAW P72 | bleed | worm's-eye from the road behind Borro, 20 mm | The serpent bursts out of the street and rears into the night: its hooded, horned head at the very top of the frame, jaws opening, yellow slit eyes looking down. Its car-thick body is a jade-and-gold column rising from the broken road, slabs of road and bridge falling off its coils. Borro is small in the lower foreground with his back to us, the shield raised on his LEFT forearm (image-left), his head level with its lowest coil. A building's dark third-floor windows beside its head give its height. | steam lit violet from below; heat shimmer; falling slabs | SHHHRRRAAAAAAAA (L): across the top above its head, not on the body | — |
| R06 | KEEP P73 | wide | as drawn | the eye | — | — | window [BREAK BOSS: MARSH SERPENT (C)] as now |

---

## CHAPTER 12: His Summons Go First

### H: Heat (P01–P08): 5/10
The serpent slams Borro's shield; Nib's knives skid off its scales; its steam burns land in Jaeha's hands. Then the ice gives Jaeha its tell.

**What works:**
- P02 (sparks, so the contact is shown).
- P03 (the notched knife).
- P07 (the frost insert).

**What is wrong:**
- **P01** was scripted `full` and rendered wide. The art is good: the head hits the shield with a white burst and Borro is in a deep squat. But:
  - The head is cut off by the top edge, and KRANNNGGG (XL) sits on it and on the contact.
  - The low tilted camera in the script became a level shot from behind Borro.
  - Nib's frog jump (both knees up, both fists by his shoulders) is a second action in the same panel.
- **P04.** FSSSHHHHHHHH sits on the serpent's head and jaw.
- **P06.** The car-thick coils are drawn as a thin snake on a blank grey floor, with no road, no rubble and no person for scale.

**Count: 8 → 8.** 6 KEEP (3 re-lettered), 2 REDRAW. Axis: the serpent is on the image-left.

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| H01 | REDRAW P01 | bleed (the opening peak) | worm's-eye from the rubble beside Borro's RIGHT foot, 20 mm, dutch 12° | The serpent's horned, hooded head, as long as a car, slams straight down from the top of the frame onto Borro's shield. The shield is raised overhead on his LEFT forearm, his RIGHT palm flat on its back. Borro crouches deep under it, knees bent, bare feet sinking, the road cracking in a ring round them. The jaw is shut; its chin and the shield's boss meet in the top third. Nib is NOT in this panel; his attack is H02. | hard white burst at the chin on the shield; steam exploding off the scales; a ring of debris; background dropped to violet-lit steam | KRANNNGGG (XL): right of the burst in the steam, angled -8°; never on the head or the contact | — |
| H02 | KEEP P02, re-letter | wide | as drawn | Nib's knives skid off the scales in sparks | — | SKRRRANG (M): off his face, at the far end of the spark spray | — |
| H03 | KEEP P03 | inset-l | as drawn | Nib checks the notched knife | — | — | "MY KNIVES DON'T BITE IT." |
| H04 | KEEP P04, re-letter | wide | as drawn | the steam jet on the shield | — | FSSSHHHHHHHH (L): off the head, inside the jet's lower edge along it; the jaw and the red-hot shield edge stay clear | — |
| H05 | KEEP P05, re-letter | wide | as drawn | the blisters rise; Yerin catches his wrists | — | TSSSS (S): beside the blistering fingers, off his chest | window [CARRY · BORRO · BURNS · 40%] as now |
| H06 | REDRAW P06 | wide | high, 10 m over the broken road, 28 mm | The serpent's car-thick coils slide off the fallen bridge's slabs toward the lit fish section. One coil crushes a fish stall flat; the tail drags through a spilled tray of crushed ice. Borro (2.4 m) stands small beside a coil for scale, the shield on his LEFT arm. | background fully drawn: rubble, the market's lit edge, strobes, steam | SHHHHRRRR (S): along the coil | — |
| H07 | KEEP P07 | wide | as drawn | frost on the tail | — | KRIK... KRIK... (S) | (silent) |
| H08 | KEEP P08 | strip | as drawn | Jaeha's eyes narrow | — | — | (silent) |

### F: The lure and the freezer lane (P12–P29): 5/10
Jaeha baits the serpent into the dead-end freezer lane, Borro shuts the mouth behind it, and the cold slows it until Nib can put both knives through the brittle scales on its brow.

**What works:**
- P19–P20: the bait. His back hits the frosted wall, the jaws rise over him, then the polite smile. This is the best acting in the three chapters.
- P24 (the clouding eye).
- P27: the knives into the brow, with contact, a burst and weight.

**What is wrong:**
- **P13.** From left to right the order is jaws, Jaeha, shield, Borro, so the shield guards Borro from Jaeha. "HEY! OVER HERE!" is lettered as an SFX across the serpent's head.
- **P14.** Three people do three actions in a row. Seoa (15, pleated skirt) does a hip-high side kick at the truck door, which breaks her no-fan-service rule. KACHUNK KACHUNK covers the granny's head.
- **P16.** Borro walks INSIDE the lane, between Jaeha and the serpent; in P21 he shuts the mouth BEHIND it. The geography is impossible.
- **P21.** The pose is strong, but it is seen from outside, so the trap never visibly closes on the serpent. KACHUNNNG (XL) covers his shell, and in this rear view the shield is on his RIGHT arm.
- **P22.** A high, wide thrash with no contact.
- **P23.** Two actions (the hit and the flinch at the far end). The window covers Borro's legs. Jaeha stands just beyond the tail, so the 40 m lane reads as a few metres.
- **P26.** "Sprinting" is drawn as walking upright up the coils.
- **P28 (the kill)** was scripted `full` and rendered wide. Nib and Jaeha are tiny, and KSSSHHHHHHHHH (XL) sits over the head that is bursting.

**Count: 17 drawn → 18 (+6%).** 10 KEEP including the title (2 re-lettered), 7 REDRAW, 2 NEW, 1 CUT. Axis: the lane's mouth is on the image-left, the dead end on the image-right.

| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| F01 | KEEP P12 | wide | as drawn | Yerin grabs his vest | — | — | "YOU CAN'T EVEN HOLD A PENCIL! WHAT ARE YOU GOING TO DO?" / "WHAT I ALWAYS DO. I'M THE BAIT." |
| F02 | REDRAW P13 | wide, dutch 10° | low, just behind the serpent's lowered head (its horned hood cropped in the left foreground), 28 mm | The serpent's yellow slit eye in profile at the left edge, its pupil swinging to track the running man. In the mid-ground Jaeha sprints image-right across the fish lane, both arms waving over his head, mouth open. One step behind him and nearer the head, Borro runs with the red-hot shield on his LEFT forearm turned toward the jaws, its glowing face to the camera; it overlaps only Jaeha's trailing leg. | blue speed lines behind the runners (as now); steam; the shield's red glow | none | "HEY! OVER HERE!" becomes Jaeha's shout balloon (it was lettered as an SFX) |
| F03 | REDRAW P14 | wide | eye level down the freezer lane, 35 mm | In the foreground the kimchi granny hauls a walk-in freezer door open, both yellow-gloved hands on its long handle, leaning back with her whole weight, heels dug in; cold mist pours out over her boots. In the mid-ground, small, Seoa pulls a refrigerated truck's back door wide with both hands on its handle, leaning back. No kick; the camera is at her eye level. Behind her, her son is a silhouette hauling another door. | mist as hard clumped shapes along the floor; white fluorescent light | KACHUNK (S): at the granny's door latch only | — |
| F04 | KEEP P15 | full | — | title card | — | — | title |
| F05 | REDRAW P16 (one fix) | tall | as drawn (eye level from the dead end) | The same image with Borro REMOVED from inside the lane: only Jaeha, running toward us and looking back, and the serpent's head pushing in through its steam at the mouth. If Borro shows at all, he is a tiny silhouette outside the mouth, behind the head. | as drawn | HFF HFF HFF (S) | — |
| F06 | KEEP P17, re-letter | wide | as drawn | the serpent slides in; crates topple | — | KRASH (M): at the toppling crates, off the coil | — |
| F07 | KEEP P18 | inset-r | as drawn | frost on the scales | — | KRIK KRIK (S) | (silent) |
| F08 | KEEP P19 | wide | as drawn | his back hits the wall; the head rises | — | THUD (S) | — |
| F09 | KEEP P20 | inset-l | as drawn | the polite smile | — | — | "I'M SORRY, SIR. I WALK IN FIRST. IT'S MY JOB." |
| F10 | REDRAW P21 | tall (peak 2) | low, INSIDE the lane at the serpent's tail, looking back at the mouth, 24 mm | The frosted tail coils across the foreground. At the mouth, narrowed to 2.5 m by the last refrigerated truck, Borro slams the door shield down on its edge; its bottom edge bites the concrete in a spray of sparks, riveted face toward us. Borro is behind it, masked head and green eye-holes above the rim, his RIGHT hand (image-left) clamped on the top edge, his shell jammed against the lane wall. The street light outside is cut to a sliver. | spark burst at the shield's foot; a ring of frost dust; cold white light; mist swirling against the iron | KACHUNNNG (L): at the shield's foot beside the sparks | "THE DOOR IS SHUT." (Borro, top right) |
| F11 | CUT P22 | — | — | the thrash is folded into F12 | — | — | its narration line moves to F12 |
| F12 | REDRAW P23 (the hit) | wide, dutch 12° | low, outside the mouth, side-on to the shield, 35 mm | The frosted tail hammers the shield from inside; the iron bulges toward us at the hit and frost crystals burst at the contact. Borro absorbs it: LEFT forearm in the strap, RIGHT palm flat high on the shield, RIGHT shoulder driven into it, knees bent, heels skidding a hand's width on the concrete. | white-blue burst; frost shards; short, slow radials | BOOM (M, one word): at the contact on the shield's upper corner | — |
| F13 | NEW (the carry half of P23) | inset-r | close on Jaeha at the dead end, 50 mm | He jolts against the frosted wall as the blow lands in him: a moss-green ring pulsing from his chest, his head knocked back against the wall, blood running from his nose, blistered fingers splayed on the frost. | flat; frost patterns on the wall; green ring | THOOM (S): at the ring's edge | window [CARRY · 2 SUMMONS · LOAD 130% · NIB 00:40 · BORRO 01:30] in the calm top |
| F14 | KEEP P24 | wide | as drawn | the clouding eye and the crack | — | — | (silent) |
| F15 | KEEP P25 | inset-r | as drawn | Jaeha points at the brow | — | — | "NIB. THE CRACK ON ITS BROW. THE SCALES ARE BRITTLE NOW." · window [NIB · FIELD FORM 00:30] as now |
| F16 | REDRAW P26 | tall, dutch 12° | low, from the lane floor, 24 mm | Nib sprints up the frozen coils like a stair, body pitched forward 45°. His RIGHT foot pushes off a coil, toes gripping the frosted scales, frost chips spraying; his LEFT knee drives high. Reverse-grip knives along his forearms, arms pumping, scarf streaming straight back. The hooded head is at the top of the frame. | amber speed lines along his path; frost spray; white fog | TAP TAP TAP (S): at his heels | — |
| F17 | NEW (the anticipation) | wide | high, above and behind the serpent's head, 35 mm | Nib springs off the last coil over the brow, both reverse-grip knives raised high over his head in both fists, his body arched back like a drawn bow. The violet Hush crack glows on the brow below him, centred in the frame. | speed lines rising round him; frosted scales below; dark background | none | — |
| F18 | KEEP P27, re-letter | wide | as drawn | both knives go through the brow scales into the crack | — | KRAKKK (L): off Nib and the eye, beside the orange burst at the upper right, angled down along the stab | — |
| F19 | REDRAW P28 | bleed (peak 3) | low, from the dead end behind Jaeha, 20 mm, looking up | The serpent's head rears into the roof and bursts apart from the brow crack outward, into violet ash and frost shards; the fluorescent tubes shatter. Nib is flung clear at the upper right, a sharp silhouette against the burst, knives out, scarf flaring. Jaeha's head and shoulders are in the lower foreground, his back to us, his face tilted up into the falling ash. | the burst centred on the brow; violet and white; shards; background dropped | KSSSHHHHHHHHH (XL): across the lower third over the dark falling ash; never on the burst | — |
| F20 | KEEP P29 | wide | as drawn | aftermath | — | flicker... flicker... (S) | (silent) |

---

## Patterns across chapters 10–12

1. **The lettering buries the action.**
   - About two-thirds of the action SFX sit on a fighter, a face, the key limb or the contact (ch010: 12 of 19).
   - Most action SFX are XL (25 in the action beats), and multi-word repeats (BOOM BOOM BOOM) are common.
   - The cause is that SFX positions and sizes are fixed in the script before the art exists.
   - Fix:
     - Replace `at:` with an anchor ("beside contact, trailing side").
     - The letterer places SFX after looking at the art.
     - One word per impact; XL only on a bleed peak (one or two per chapter).
     - Change the `impact` recipe's "large SFX space along the diagonal" to "a small space beside the contact; the contact itself stays clear".
2. **`full` = `wide`, so the peaks are small.**
   - The biggest beats render at 1536×1024: ch011 P48 and P72, ch012 P01 and P28.
   - Fix: in PANEL_BRIEF_v2, make every peak a `bleed` (1024×1536, lettered edge to edge), with the main figure filling at least 60% of the height.
3. **Fights are built from wides.**
   - About three tall panels per fight; ch010 has 18 wides in 23 panels.
   - Fix: wides only for geography and aftermath. Every exchange gets at least one close-up (a foot, a blade, a claw, an eye) and a tall for its key blow.
4. **One camera per fighter.**
   - Nib's stair defence uses the same shot three times (ch011 P41, P53, P62); Borro is filmed from behind twice in a row (ch010 P38, P45).
   - Fix: the board states the camera of every panel; no two in a row from the same position.
5. **Two actions per panel, and one gets lost.**
   - ch010 P38, P39; ch011 P25, P32, P60; ch012 P14, P23.
   - Fix: split them, as in the tables.
6. **Monsters pose instead of attack.**
   - Hounds walk in lines (ch010 P31, P38; ch011 P36) or stand on their hind legs at the shield (ch010 P39).
   - The serpent is a flat tube seen from the side, often with nothing to give its size (ch012 P06).
   - Fix: every action row describes the monster's body (stretched leap, crumple, recoil) and includes a scale object.
7. **Borro is drawn as a man standing next to a door.**
   - The shield stands beside him instead of across or in front: ch010 P38 and P51; ch011 P22 and P39; ch012 P13.
   - In all three rear views the shield is on his RIGHT arm (ch010 P38, P45; ch012 P21); the front views are correct.
   - Inference: the model mirrors his front sheet when it draws him from behind.
   - Fix: every prompt says where the shield is in relation to the threat ("across the beam", "between Jaeha and the jaws"), and every rear view gets a line naming its image side.
8. **Nib has two stock poses.**
   - "Airplane arms": ch010 P42; ch011 P62; ch012 P28.
   - The "frog jump" (both knees up, fists by his shoulders): ch011 P16; ch012 P01.
   - Fix: use a lunge, a dive or a backhand, with the planted foot named.
9. **Windows sit on action, and carry windows cover the carry.**
   - ch010 P44 and P46; ch011 P53, P54 and P71; ch012 P23.
   - Fix: move them to a reaction or eyes panel next to the beat, as in the tables (T16, B17, B18, F13).
10. **Jaeha reads the fight before and after it, rarely during.**
    - ch010 has no Jaeha panel from P48 to P54; ch011 has no panel of him counting Nib's cooldown.
    - ch012 does this right (P08, P19–P20, P25).
    - Fix: one calculating panel at each turn of a fight (T26, B17).
11. **Geography and axis slips.**
    - ch012 P16 contradicts P21; ch011 flips direction from P53 to P54; ch011 P22 is not a square; ch010 P38's shield is not across the beam.
    - Fix: each fight's board names its axis.
12. **The scripts write results, not contact.**
    - "Bursts into ash", "slashes a hound in two" and "drives it toward the square" get drawn as the aftermath.
    - Fix: write the contact ("the blade meets the throat; the burst starts at the blade"), together with the rule 7 change.
13. **A rule breach outside the fight standard.** ch012 P14: Seoa's hip-high side kick in a pleated skirt. F03 removes it.

**Totals.** ch010 66 → 73 panels; ch011 73 → 83; ch012 70 → 71. Across the boards:
- 29 REDRAW, 19 NEW and 1 CUT.
- 28 KEEP panels need re-lettering only, with no image generation.
