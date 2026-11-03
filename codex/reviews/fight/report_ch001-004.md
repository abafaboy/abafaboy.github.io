# Fight audit and re-storyboard: My Summons Go First, chapters 1-4

None of the 13 fight sequences reaches 8/10 (range 5 to 7.5), so each one has a storyboard below. The scripts' choreography is good. The art fails on the knight's bodies, the humans' bodies, the beats between cause and effect, and the lettering.

## Read first: ch003 had no judge pages
- **The pack is missing.** `/home/claude/work/judge/ch003_final/` is empty. The pack was wiped at the last rebuild, and the strip segments `judge_pack.py` needs are gone. Only `recap.mp4`, `layout.json` and `strip.html` survive in `/home/claude/work/ch003/out/`.
- **How I judged ch003.** I rebuilt the strip from `recap.mp4` (frames at 8 fps, stitched, anchored on the art) and checked every ch003 fight panel against real video frames. So ch003 is judged on what the viewer actually saw.
- **The rebuilt pages are kept.** They are in `/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/fight/ch001-004/ch003_rebuilt_pages/` (44 pages). Use them for reading order only. The doubled helm at the top of P10 comes from my stitching, not from the art. Delete the folder if nobody needs it.
- **Cleanup.** Contact sheets, frames and the other intermediate files are deleted.

## Calibration against your ch011 notes
- **Posed bodies.** Confirmed for the knight and the humans. Corrected for Nib: his attack panels have real lines of action (ch002 P03, P14, P19, P35; ch004 P13).
- **Eye-level, medium or wide camera.** Mostly corrected: ch1-4 use low and worm's-eye angles often. Wide impact shots with small figures remain (ch001 P22, ch002 P05 and P22, ch003 P12).
- **Hits never land.** Corrected: contact is drawn on most of Nib's exchanges (ch002 P03, P17, P20, P21, P35, P41; ch003 P33, P37, P41, P54; ch004 P13). It still holds for the first kills (ch001 P39) and the trap spikes (ch003 P32).
- **SFX doing the drawing's work.** Confirmed for ch001 P39, which is a 1620 px panel containing nothing but a red smear and a giant SFX. Elsewhere the problem is placement, not repetition: 13 SFX sit on the fighter (list under Patterns). Repeated triples are rare and quiet.
- **Few speed lines; detailed background stays during the hit.** Corrected: most impacts drop to flat orange, white or red with drawn speed lines.
- **Choreography doesn't read.** Corrected for the set pieces in ch2-4 (the shoulder tell, the floor-plate trap, the crack in the rim). Confirmed for ch001 P38-P39 and P45.
- **System windows on action beats.** Only three cases: ch002 P22, ch003 P36 and P46. Most windows already sit on quiet panels.

## Rule 7 ("violence happens between panels"): drop it
- **What it caused.** ch001 P39, the series' first kills, shows no knight, no sword and no swing; it plays for about 5 seconds on video. The same rule is why the spikes in ch003 P32 never visibly strike. Wherever the scripts ignored the rule (Nib's blows), the art is the best in the run.
- **Replacement wording.** "Blows land in the panel: draw the moment of contact (blade on armour, pommel on knives, spike into a joint) with a radial burst at the contact point. Only gore and death stay off panel. A human death is drawn as the blow sweeping dark silhouettes, with contact on their weapons and never on faces or bodies, then an aftermath silhouette. Blood only as a spray or splash; no wound close-ups."
- **Related changes.**
  - Retire tone-flip (b), the panel of speed texture with no figure, for blows; keep it for time skips.
  - Amend `CHARACTER_DESIGNS_v2.md` §2.5 ("Deaths happen between panels") to match.

## Lettering: why SFX land on fighters (measured)
- **The script sets SFX positions before the art exists.** Example: ch001 P41's `at: [0.82, 0.2]` lands exactly on Mok's recorded face box `[0.491, 0.139, 0.608, 0.339]`.
- **The face check did not fire.** `autostrip2.py` has kept SFX off faces since 27 Oct (commit 5dad6d0). ch001 was lettered on 29 Oct with that face box present in `strip.html`. Yet KLANNNG covers Mok's whole head, and `letter_build.log` has no "SFX COVERS A FACE" warning.
- **Possible cause (not verified).** `facesOf()` returns nothing when `img.naturalWidth` is 0, for example if the art has not loaded yet. Test this before trusting a re-letter.
- **Contact and `keep` boxes are newer.** Keeping SFX off REVIEW `contact` boxes and script `keep` boxes was added today (fad811b, 4 Nov 01:32), after ch1-4 were lettered.
- **ch1-4 scripts have no `keep` boxes.** So SFX over bodies and limbs will not move by themselves; those panels need `keep` boxes.
- **Coordinates in the SFX column.** Positions below are in the script's convention: `at` as [x, y] fractions of the panel, plus `rot`.

## Conventions used below
- **Screen direction.** Nib's and Jaeha's side is image-left and attacks left to right; the knight is image-right. Any flip is marked.
- **Sides.** "His LEFT" is the character's own left; "image-left" is the screen.
- **Hands.** `hand_ref` files are in `characters_v2/hands/`.
- **New panels.** Insert them with suffix IDs (for example P21b). They can share the neighbouring panel's narration line or run silent; several panels already have no narration.
- **Panel IDs per chapter.** ch001 63 → 67; ch002 60 → 61; ch003 63 → 65; ch004 60 → 63. That is +4% overall, and no sequence exceeds +30% except 1A (5 → 6, one panel added).

---

# Chapter 1: Bait

| seq | panels | what happens | grade |
|---|---|---|---|
| 1A Stone lizards | P20-P24 | Jaeha counts the bites and moves Yerin one step before the tail lands | **5/10** |
| 1B The knight wakes | P36-P49 | The knight rises, kills the flankers and hits Mok's shield; Jaeha drags Yerin clear; Mok locks them in | **5/10** |
| 1C The last husk | P50-P63 | The knight drags Yerin out; the last husk becomes a door; Nib catches the blade | **7/10** |

Not a fight: P14-P16, where the trap shreds the husk. P16 is a good impact panel (spikes visibly enter the husk, white field, low angle), so KEEP it.

## 1A Stone lizards (5/10): what is wrong
- **P20 works.** Low behind the shield-bearer, the lead lizard's jaws are on the shield rim with sparks, and the contact is shown.
- **P21 has no wind-up.**
  - The tail is a relaxed S along the floor, not coiled.
  - CRUNCH, the sound of an off-panel bite, is lettered across Jaeha's chest.
  - Three figures share the panel, so the speaker of "TAKE ONE STEP TO YOUR LEFT" is small.
- **P22, the payoff, does not read.**
  - The club tail rises vertically like a long neck and taps the wall beside her head; it reads as a long-necked animal's head, not a tail sweeping through where she stood.
  - Yerin stands flat to the wall exactly as in P21, so the step, which is the whole point, is never drawn.
  - It is a wide panel with no tilt (the script asks for one), and the figures are under half the panel height.

## 1A storyboard (5 → 6)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1A-1 KEEP | P20 | full | as drawn | as drawn: the lead lizard bites the shield rim | as drawn | CRUNCH as lettered | caption "ONE BITE." |
| 1A-2 REDRAW | P21 | tall | low, from the floor beside the shield rim, three-quarter from the lizard's LEFT hip, 18 mm | ONE action, the tail cocks: jaws clamp the shield rim at the image-left edge (shield and the shield-bearer's boots cropped, no face); body twists in a C-curve away from the shield; club tail swung back and up to image-right, coiled tight like a cocked whip, aimed at Yerin; the milky LEFT eye on the near side; Yerin small but sharp in the upper-right background, frozen against the wall, both hands locked on her bag strap | short tension ticks along the coiled tail; grit falling from the club; muted, desaturated background | CRUNCH (M) at the jaws [0.18, 0.62], rot 8; keep Yerin clear | inner (Jaeha): "TWO BITES. THE TAIL COMES AFTER THE THIRD." |
| 1A-3 NEW | (line moved from P21) | inset-r | close, three-quarter, eye level, 50 mm | Jaeha's head snaps up from the notebook: pencil stopped mid-word in his RIGHT hand, notebook open in his LEFT, eyes narrowed and calm, mouth open on a polite request | flat pale-green gradient; focus lines to his eyes | none | "TAKE ONE STEP TO YOUR LEFT, PLEASE." |
| 1A-4 REDRAW | P22 | wide | facing the wall at Yerin's chest height, 24 mm, dutch tilt 12° | ONE moment: Yerin has just stepped to her LEFT (image-right), LEFT sneaker landing, RIGHT sneaker still sliding in a dust puff, body rigid, eyes shut, ponytail flung to image-right; the stone club comes in flat from image-left and smashes the wall where her head was, a finger's width from her face; only the last metre of tail is in frame; she fills 85% of the height | flat hot orange behind the crater; radial burst and jagged hand-inked chunks at the contact; horizontal speed lines along the tail; hem and ponytail blown sideways | WHAAM (XL) above the tail [0.25, 0.2], rot -6; keep the club head and her face clear | silent |
| 1A-5 KEEP | P23 | wide | as drawn | as drawn | as drawn | TREMBLE | "HOW DID YOU KNOW IT WOULD DO THAT?" |
| 1A-6 KEEP | P24 | inset-r | as drawn | as drawn | as drawn | none | "JUST A LUCKY GUESS. ARE YOU ALL RIGHT?" / inner "IT WASN'T A GUESS." |

## 1B The knight wakes (5/10): what is wrong
- **P37: the rise is a statue.** The knight stands straight and square to camera, arms hanging, legs apart. Nothing in the chains moves and nothing lifts. KRRRSSH is lettered across its chest just under the helm.
- **P38: the target is missing.** Four small hunters run in a column in a high wide shot. The knight is not in the panel, so it does not work as geography either.
- **P39: the first kills are never drawn.** The panel is 1620 px of black with a red smear and a vertical SHHRRAAAANG: no knight, no sword, no swing.
- **P40 works.** Silhouetted bodies, a broken spear and a splash on the pillar.
- **P41: good art, ruined by lettering.** Mok is in a long braced lunge behind the shield, with sparks where the blade meets the rim, but KLANNNG covers his whole head.
- **P42-P44 work.** Jaeha calculates; the high-angle proof; the over-the-shoulder shot on frozen Yerin, though she is small.
- **P45: the rescue moves the wrong way.**
  - Jaeha and Yerin both fly to image-left, toward the blade and away from the pillar at image-right, so it reads as him diving at the sword.
  - KRAKOOOM covers Yerin's legs and the gap between her and the impact.

## 1B storyboard (14 → 16)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1B-1 KEEP | P36 | strip | as drawn | the red light switches on in the helm | as drawn | VMMM | none |
| 1B-2 REDRAW | P37 | tall | worm's-eye from the floor 3 m in front of the knight, 14 mm, dutch 15° | caught mid-rise: LEFT knee still on the floor, RIGHT foot planted forward and pushing, torso unfolding up and toward the camera in a C-curve so the red face-hole is the highest point; RIGHT hand dragging the long sword up, its point still scraping stone at image-left; snapped chains whipping up from both wrists; Jaeha tiny in the bottom-right corner, back to us, leaning back on his heels, left hand on the door frame | upward speed lines behind the knight; sparks at the scraping point; motion arcs on the chains; stone chips jumping round knee and foot; dark, with the face-hole the brightest point | KRRRSSH (XL) at the sword point [0.22, 0.8], rot -10, along the blade; keep the body and helm clear | none |
| 1B-3 REDRAW | P38 | wide | high, from above the iron door looking down the hall, 24 mm (the one geography shot) | the knight mid-hall, turned toward the door; four hunters as small figures running low along both pillar lines, two each side, converging on its back (one shared action, so a pack); Mok bottom-left behind his raised shield, cropped, free hand cupped at his mouth | drawn hall; thin dust trails behind the runners; no speed lines | TATATAT (S) by the right-hand runners [0.78, 0.6] | Mok: "NOW! HIT IT FROM BEHIND WHILE IT'S BUSY!" |
| 1B-4 NEW | first half of P39 | wide | low, from behind the spearman's right shoulder (shoulder and levelled spear cropped bottom-left, no face), 24 mm, dutch 10° | ONE action, the wind-up: the knight twists its torso hard to its RIGHT, its RIGHT arm drawing the long sword back behind its right hip, blade trailing, weight sinking onto its right rear foot; the cracked LEFT pauldron dips a hand's width (the ch2 tell, planted here); the red face-hole turned back over its shoulder at the spear | muted; tension lines round the twisted torso; a red glint along the edge | CLNK (S) at the pauldron [0.7, 0.3] | none |
| 1B-5 REDRAW | P39 | tall | low behind the knight's RIGHT hip (hip and cloak cropped in the right foreground), looking along the blade, 18 mm, dutch 20° | the follow-through: RIGHT arm fully extended at the end of a flat waist-high sweep from image-right to image-left, torso unwound, LEFT foot planted, cloak swirling; in the blade's path, two hunters as flat black silhouettes swept off their feet (no faces, no wounds, no blood), a spear snapping, the mage's staff spinning away with its core going dark | background dropped to black with red speed lines along the arc; painted motion smear on the blade only; white-red flashes where the blade meets their weapons | SHHRRAAAANG (XL) along the arc [0.45, 0.35], rot -15, inside the panel; keep the knight's arm clear | none |
| 1B-6 KEEP | P40 | wide | as drawn | aftermath silhouettes | as drawn | THUD | off-panel (crossbow): "THIS THING ISN'T A C-GRADE BOSS AT ALL!" |
| 1B-7 KEEP art, RE-LETTER | P41 | wide | as drawn | the blade hits Mok's shield; he skids back | as drawn | KLANNNG moved off his head onto the shield face below the burst [0.2, 0.55], rot 15 | none |
| 1B-8 KEEP | P42 | wide | as drawn | Jaeha calculating behind the pillar | as drawn | none | inner: "IT'S SLOW TO TURN IN ALL THAT ARMOUR." |
| 1B-9 KEEP | P43 | inset-r | as drawn | the sweep hits whatever is in front | as drawn | none | inner: "AND IT ALWAYS HITS WHATEVER IS IN FRONT OF IT." |
| 1B-10 KEEP | P44 | wide | as drawn | Yerin frozen in front of the drawn-back sword | as drawn | SHAKE SHAKE | Jaeha: "GET OUT OF ITS WAY! DON'T STAND IN FRONT OF IT!" |
| 1B-11 NEW | first half of P45 | strip | extreme close-up, side-on, 85 mm | Jaeha's black fingerless-gloved RIGHT hand closing fully round Yerin's thin wrist (her off-white, mint-trimmed sleeve past the wrist), his forearm straining toward image-right; hand_ref reaching_grabbing_wrist.png | flat orange; speed lines along the pull | none | none |
| 1B-12 REDRAW | P45 | tall | low at the pillar's base looking out into the hall, the pillar's edge down the image-right side, 18 mm, dutch 15° | the yank and the smash, one moment: Jaeha in the right foreground, back foot at the pillar, throws his weight back toward it (body a C-curve leaning to image-right, LEFT palm slapping the pillar edge), RIGHT arm hauling Yerin by the wrist; Yerin yanked off her feet toward him, legs, ponytail and bag strap trailing to image-left; behind her at image-left the sword smashes point-first into the floor where she stood | flat hot orange beyond the pillar; radial white burst at the blade's contact; hand-inked stone fanning up; a crack racing toward the pillar; speed lines along both bodies to image-right; white rim on Jaeha | KRAKOOOM (XL) at the impact [0.22, 0.72], rot 10, along the crack; keep both figures clear | none |
| 1B-13 KEEP | P46 | wide | as drawn | as drawn | as drawn | SHAKE SHAKE | "STAY BEHIND ME AND KEEP YOUR BACK TO THE PILLAR." / "I CAN'T FEEL MY LEGS. I CAN'T MOVE THEM." |
| 1B-14 KEEP | P47 | wide | as drawn | as drawn | as drawn | none | "PULL BACK, ALL OF YOU! SHUT THAT DOOR!" / "THE TRAP RAT WILL KEEP IT BUSY." |
| 1B-15 KEEP | P48 | wide | as drawn | as drawn | as drawn | KA-CHUNK | none |
| 1B-16 KEEP | P49 | inset-l | as drawn | as drawn | as drawn | none | "THEY... THEY LOCKED US IN HERE WITH IT?" / inner "OF COURSE THEY DID." |

## 1C The last husk (7/10): what is wrong
- **P50, P51 and P53-P54 work.**
- **P52: the drag is skipped.**
  - In P50 Jaeha shields Yerin behind the pillar; in P52 she is already out on the floor. The reader never sees the gauntlet take her.
  - The knight is in the same frontal, legs-apart stance as P37 and P50, and the raised sword has no wind-up.
- **P55-P57: the tension leaks.** Three system panels sit between the raised sword and the strike with no reminder of the blade. This is acceptable as a time freeze.
- **P58: readable, but flat and badly lettered.** It has a red field, speed lines and the husk with arms spread. But the blade is side-on, and the vertical SHHHRAANG spills out of the panel: its "NG" shows in the black gutter at the bottom of P57's page.
- **P60, the hook, works.** Sparks at the crossed knives under the blade, husk shards with cyan glow, Yerin in the foreground. Nib is square to camera with knees out; this silhouette recurs five more times by ch4.
- **P61-P63 work.**

## 1C storyboard (14 → 15)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 1C-1 KEEP | P50 | tall | as drawn | the knight looms round the pillar | as drawn | DOOM DOOM | none |
| 1C-2 KEEP | P51 | strip | as drawn | trembling hand | as drawn | none | caption "I HAVE ONE HUSK LEFT IN ME TODAY. ONLY ONE." |
| 1C-3 NEW | (the drag in P52's text) | wide | low at floor level beside the pillar's base, 20 mm, dutch 10° | ONE action: the knight's huge LEFT gauntlet (image-right, round the pillar edge, cropped at the wrist) has hooked the strap of Yerin's pink bag and yanks; Yerin slides out on her side toward image-right, one arm thrown back toward the pillar, face turned back in shock; the strap a taut straight line from her shoulder to the gauntlet | speed lines along the pull; dust trail behind her; dark with a red rim | SKRRT (S) under her sliding hip [0.45, 0.85]; keep the strap and gauntlet clear | none |
| 1C-4 REDRAW | P52 | tall | worm's-eye from the floor beside Yerin's head, 16 mm | the knight over Yerin, torso arched back in a deep wind-up (backward C-curve), RIGHT arm raising the long sword high overhead, blade catching red light at the top; LEFT gauntlet still holding the strap taut down to her; Yerin in the bottom foreground on her side, propped on one elbow, other hand raised uselessly, face turned up; Jaeha out of frame | dark; red rim light; tension lines round the raised arm | none | silent |
| 1C-5 KEEP | P53 | strip | as drawn | Jaeha's eyes | as drawn | none | "GO FIRST. ONE MORE TIME." |
| 1C-6 KEEP | P54 | tall | as drawn | the cracked husk shields Yerin | as drawn | VZZZT | none |
| 1C-7 KEEP | P55 | wide | as drawn | system | as drawn | D-DING | window [OPERATOR CANDIDATE DETECTED] |
| 1C-8 KEEP | P56 | tall | as drawn | system | as drawn | none | windows [SENT FIRST: 312 TIMES] / [LEFT SOMEONE BEHIND: 0 TIMES] |
| 1C-9 KEEP | P57 | wide | as drawn | system | as drawn | none | window + "A DOOR? WHAT KIND OF DOOR, AND TO WHERE?" |
| 1C-10 REDRAW | P58 | tall | low behind the husk (its white legs planted wide in the bottom foreground, cropped at the knees), 16 mm, dutch 15° | the strike comes at the reader: the long sword straight down at the camera, foreshortened, the bright edge and bronze tower crossguard huge at the top, the knight's RIGHT gauntlet on the grip; the husk's spread arms at the frame edges, cracks glowing cyan | flat red; speed lines converging along the blade onto the husk's head | SHHHRAANG (XL) vertical along the blade [0.5, 0.4], rot -80, entirely inside the panel | none |
| 1C-11 KEEP | P59 | strip | as drawn | caption panel | as drawn | none | window [SOMEONE ANSWERED.] |
| 1C-12 KEEP | P60 | bleed | as drawn | Nib catches the blade | as drawn | KRANNNG | none |
| 1C-13 KEEP | P61 | strip | as drawn | Yerin's eye | as drawn | none | silent |
| 1C-14 KEEP | P62 | wide | as drawn | Nib looks back | as drawn | none | "WHO'S IN CHARGE HERE?" |
| 1C-15 KEEP | P63 | inset-r | as drawn | Jaeha's raised finger | as drawn | BLINK BLINK | "I THINK... IT'S ME?" |

---

# Chapter 2: Who's in Charge

| seq | panels | what happens | grade |
|---|---|---|---|
| 2A First moves | P01-P05 | Nib holds the blade one-handed, kicks it aside, and drags Jaeha and Yerin to the pillar as it smashes the floor | **6/10** |
| 2B Nib's first charge | P11-P24 | Launch, knee rake, run up the blade, helm slash; swatted into a pillar | **6.5/10** |
| 2C Link and the counter | P25-P37 | Jaeha links, spots the pauldron tell and calls the duck; Nib opens the armpit seam | **7.5/10** |
| 2D Pommel and Carry | P38-P44 | The pommel hammers Nib; Jaeha takes half the blow through Carry | **6.5/10** |

Not a fight: P53-P60 (the roar and the sigil).

## 2A First moves (6/10): what is wrong
- **P01: the signature image is too small.** A 105 cm goblin holding a boss's blade with one knife, unbothered, is drawn as a wide shot with Nib at about 40% of the panel height.
- **P03 is the best body mechanics in ch1-4.**
  - The line of action runs from the planted LEFT foot through the twisted torso to the RIGHT heel on the flat of the blade, knives out for balance.
  - White flash at the contact, white field, speed lines.
  - Only the lettering ("KL") touches the contact.
- **P04: a tangle.** Nib has one fist in Yerin's collar and the other in Jaeha's vest; the two of them are piled at the left with legs overlapping, and SKRRRRRT crosses Jaeha's legs. Three bodies and two grips are exactly what the model cannot separate.
- **P05: the impact reads, the people don't.** A high wide on orange; the three are a small pile in the bottom-right, and KRAKOOOM covers the top half.

## 2A storyboard (5 → 5)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 2A-1 REDRAW | P01 | tall | low from the floor beside Yerin's head (her cheek and hair cropped bottom-left), 18 mm | Nib big in frame (60% of the height) holding the giant blade with ONE knife: the blade's spine across his LEFT forearm, LEFT knife braced under it; RIGHT knife loose in reverse grip at his hip; weight sunk on bent knees, bare toes gripping; head turned back over his RIGHT shoulder toward the pillar (image-right), deadpan, eyelids half-lowered; blade enters from top-left, the knight's gauntlets and red face-hole high above, cropped; husk shards glowing faint cyan round his feet; hand_ref reverse_grip_knives.png | sparks where the steel grinds; red rim light from above; dark | GRRRIIND (L) along the blade spine [0.3, 0.12], rot -8; keep his head clear | "YOU'RE IN CHARGE? THEN WHY ARE YOU THE ONE BLEEDING?" |
| 2A-2 KEEP | P02 | inset-r | as drawn | Jaeha's nosebleed | as drawn | DRIP | "OH. I DIDN'T EVEN NOTICE THAT." / inner "THAT CALL TOOK A LOT MORE OUT OF ME THAN A HUSK." |
| 2A-3 KEEP art, RE-LETTER | P03 | tall | as drawn | spinning heel kick | as drawn | KLANNNG moved off the heel-blade contact into the white upper-right [0.62, 0.12], rot -12 | none |
| 2A-4 REDRAW | P04 | wide | overhead, straight down from about 6 m, 28 mm, the floor as one plane | the drag as a clean diagram: Nib at the top sprinting toward the pillar (top-right), leaning far forward, both long arms straight back; LEFT fist in the shoulder of Jaeha's vest, RIGHT fist in Yerin's collar; Jaeha (left) and Yerin (right) on their backs, side by side with a clear gap, heels scraping; Jaeha's right hand on his bloody nose; Yerin hugging her bag. Fallback if it tangles: show Yerin only as her dust trail and sneakers at the frame edge | two long dust trails; speed lines along the drag; the falling sword's shadow spreading across the floor at the bottom | SKRRRRRT (M) between the dust trails [0.5, 0.78] | none |
| 2A-5 REDRAW | P05 | wide | eye level at the floor, 24 mm, dutch 12° | the sword point punches into the floor at image-left-centre, exactly where the two dust trails begin; at image-right, the pillar's edge with Nib's bare heel and the hem of Yerin's jacket just vanishing behind it (cropped) | radial white burst at the contact; hand-inked stone erupting in a fan; flat hot orange with radial speed lines | KRAKOOOM (XL) above the contact along the blade [0.35, 0.22], rot 10 | none |

## 2B Nib's first charge (6.5/10): what is wrong
- **P11-P14 work.** P14, the launch (a horizontal streak with red-green speed lines and dust where his feet kicked off), is strong.
- **P16: a mild screen-direction flip.** After the title card, Nib runs up and left from the pillar, having launched left to right in P14.
- **P17: lettering on the fighter.** Contact is shown (sparks at the back of the knee), but SKRANNG is lettered across Nib's thighs.
- **P19 is excellent.** Low behind Nib as he runs up the lowered blade like a ramp, the helm looming over him.
- **P20: lettering on the fighter.** The skid off the rim is drawn, but SKREEE crosses Nib's torso.
- **P21 is good.** The gauntlet's knuckles land in his ribs with a white burst; his back arches and the knives fly wide.
- **P22: the weakest panel in the exchange is the one that ends it.**
  - Nib is about 15% of the panel height at the far right.
  - [FIELD FORM 03:31] sits on the impact beat.
  - KRASSHH covers his legs.
- **No Jaeha beat for eight panels.** From P14 to P22 the MC is never shown reading the fight.

## 2B storyboard (13 → 14)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 2B-1 KEEP | P11 | wide | as drawn | the knight turns toward the pillar | as drawn | GRRRNNK | none |
| 2B-2 KEEP | P12 | wide | as drawn | as drawn | as drawn | none | "YOU SAY YOU'RE IN CHARGE. SO GIVE ME AN ORDER." / "UM... SUMMONS GO FIRST?" |
| 2B-3 KEEP | P13 | inset-l | as drawn | as drawn | as drawn | none | "THEY ALWAYS DO." |
| 2B-4 KEEP | P14 | tall | as drawn | the launch | as drawn | TAK, SHHHT | none |
| 2B-5 REDRAW | P16 | full | high and wide from above and behind Jaeha's pillar (its top cropped bottom-left), 24 mm | geography with direction fixed: Nib a dark streak racing from image-left to image-right toward the knight (centre-right, turning to meet him); two tiny figures (orange vest, off-white jacket) at the pillar's base; pillars about 10 m | drawn, detailed; thin dust trail behind Nib | TATATAT (S) behind Nib [0.35, 0.72] | none |
| 2B-6 KEEP art, RE-LETTER | P17 | wide | as drawn | knee rake | as drawn | SKRANNG moved off Nib's thighs to above the sparks at the knee [0.75, 0.2], rot -10 | none |
| 2B-7 KEEP | P18 | wide | as drawn | reaction (correct place for a window) | as drawn | none | window [SEAL 1/5 · NIB'S POWER IS LIMITED TO 20%] |
| 2B-8 KEEP | P19 | tall | as drawn | run up the blade | as drawn | TAK TAK TAK | "TWENTY PERCENT OF ME. THIS IS EMBARRASSING." |
| 2B-9 NEW | none | strip | extreme close-up at the pillar's edge, 85 mm | Jaeha's eyes tracking upward after Nib, fringe over his LEFT eye, sweat at the temple, lower lids tight: calculating, not only afraid | black with a band of red light | none | silent |
| 2B-10 KEEP art, RE-LETTER | P20 | wide | as drawn | helm slash skids | as drawn | SKREEE moved off Nib's torso to above the rim sparks [0.7, 0.1], rot -6 | none |
| 2B-11 KEEP | P21 | tall | as drawn | the backhand | as drawn | WHAAM | none |
| 2B-12 REDRAW | P22 | tall | close, beside the far pillar at Nib's height, 24 mm, dutch 15° | Nib's back slams into the pillar face at image-right (continuing P21's direction): body folded into a C round the impact, arms and knives flung forward, scarf whipping past his face; he fills 60% of the height | radial crater of cracked stone with a white flash at the contact; debris bursting toward the camera; speed lines from image-left along his flight; background dropped to a dust-grey gradient | KRASSHH (XL) along the flight path [0.28, 0.4], rot 8; keep Nib clear; no window here | none |
| 2B-13 KEEP | P23 | inset-l | as drawn | Jaeha's shout | as drawn | FLINCH | "NIB!" |
| 2B-14 KEEP + UI | P24 | wide | as drawn | Nib lands and spits | as drawn | PTOO; [FIELD FORM 03:31] window moved here, top-left | "HE'S FASTER THAN HE LOOKS, AND HIS ARMS ARE TOO LONG." |

## 2C Link and the counter (7.5/10): what is wrong
- **The structure is the cleanest in ch1-4.** The seven setup panels (P25-P31) are each a different shot.
- **P32 is a good plan panel.** Pencil raised like a baton, a cyan arc for the sweep, a circle on the pauldron, an arrow for the duck. Two weak points:
  - The knight stands with its sword held out instead of winding up.
  - Nib is about 40 px tall.
- **P33 is the tell, close: excellent.**
- **P34: strong, but the danger isn't sold.** Flat orange, the sweep with speed lines, the scarf tip cut. But the blade and Nib sit in two separate bands with a clear gap, so "a finger's width" never shows.
- **P35 is among the best panels in the run.** Worm's-eye view, Nib uncoiling up into the armpit seam, violet ash, a white field, and the SFX clear of him.
- **P36: the payoff is lost.**
  - It is an eye-level wide: the knight nearly upright with a hand at its side, Nib tiny at the left.
  - A window runs across the top.
  - "Something finally hurt it" does not show.

## 2C storyboard (13 → 13)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 2C-1 KEEP | P25 | wide | as drawn | notebook | as drawn | FLIP | note "KNIGHT. SLOW TO TURN. HITS WHATEVER IS IN FRONT. LEFT SHOULDER?" / inner "I CAN'T SEE HIS SHOULDER FROM HERE. I NEED TO SEE WHAT NIB SEES." |
| 2C-2 KEEP | P26 | tall | as drawn | system | as drawn | DING | window [NEW SKILL: LINK] |
| 2C-3 KEEP | P27 | wide | as drawn | link view | as drawn | VMMMM | [LINK · NIB] |
| 2C-4 KEEP | P28 | inset-r | as drawn | as drawn | as drawn | TWINGE | inner "HIS RIBS. I CAN FEEL HIS RIBS AS IF THEY WERE MINE." |
| 2C-5 KEEP | P29 | strip | as drawn | POV of the pauldron | as drawn | none | silent |
| 2C-6 KEEP | P30 | wide | as drawn | as drawn | as drawn | none | "HIS LEFT SHOULDER DROPS BEFORE EVERY SWEEP!" |
| 2C-7 KEEP | P31 | inset-l | as drawn | as drawn | as drawn | TWITCH | "STOP SHOUTING. I CAN HEAR YOU THINKING NOW." |
| 2C-8 KEEP | P32 | wide | as drawn | plan | as drawn | none | link "NOT YET. WAIT FOR THE SHOULDER." |
| 2C-9 KEEP | P33 | strip | as drawn | the pauldron drops | as drawn | CLNK | none |
| 2C-10 REDRAW | P34 | tall | at floor level in front of Nib's face, looking along his back, 16 mm, slight dutch | Nib flat on his chest, chin on the stone, arms tucked, knives along his forearms, eyes rolled up at the blade; the blade's flat passes a finger's width over his back, its bright edge filling the top third, sweeping image-right to image-left; the severed tip of his red scarf fluttering in its wake | flat hot orange; horizontal speed lines along the blade; dust blown flat by its wind; thin amber outline on Nib | VSHHHHH (XL) in the top band along the blade [0.5, 0.1], rot -4; keep the gap clear | link "NOW!" at the top of this panel |
| 2C-11 KEEP | P35 | wide | as drawn | the seam strike | as drawn | SHRAKKK | none |
| 2C-12 REDRAW | P36 | wide | low three-quarter from behind Nib (back and shoulders cropped bottom-left, landing crouch, knives low and wide), 24 mm | the knight staggers back one heavy step: RIGHT foot sliding back, torso bent sideways over the wound (C-curve), LEFT gauntlet clamped over the seam under its left arm with violet ash pouring between the fingers, sword point dragging | violet ash drifting in the green shafts; floor cracking under its back foot; no speed lines | DOOM (M) at the sliding foot [0.62, 0.84]; [FIELD FORM 02:14] moved into the black gutter after this panel | none |
| 2C-13 KEEP | P37 | inset-r | as drawn | as drawn | as drawn | none | "YOU SAW THAT COMING FROM ALL THE WAY OVER HERE?" |

## 2D Pommel and Carry (6.5/10): what is wrong
- **P38: the wind-up mostly reads, but nothing moves.**
  - The knight is upright, holding the sword point-up and pommel-down over Nib.
  - Nib's arms are spread like a wrestler's.
  - The pommel is a small disc mid-frame instead of a hammer coming at the reader.
- **P39-P40 work.** This is the correct use of a system beat.
- **P41: good contact, covered.** The pommel lands on the crossed knives, an amber ring bursts from the contact, a white field; but DOOOOM sits on the pommel and gauntlet.
- **P42 works.**
- **P44 doesn't read.** "Shoves the pommel aside and rolls clear" isn't there: the hilt lies on the floor beside a crouching Nib like a dropped object, detached from the knight.

## 2D storyboard (7 → 7)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 2D-1 REDRAW | P38 | tall | worm's-eye from beside Nib's knee (his crouched back and head in the bottom foreground), 14 mm, dutch 15° | the knight whirls round, torso twisted at the waist, cloak swinging wide, both gauntlets on the grip driving the bronze disc pommel straight down at the camera like a hammer, foreshortened huge at top-centre; Nib's head snapping up, knives rising into a cross; hand_ref grip_hilt_two_hands.png | speed lines converging on the pommel's path; red face-hole light; thin amber outline on Nib | WHUMM (L) beside the pommel's path [0.22, 0.2], rot -10; keep the pommel clear | none |
| 2D-2 KEEP | P39 | wide | as drawn | system | as drawn | D-DING | window [NEW SKILL: CARRY] |
| 2D-3 KEEP | P40 | strip | as drawn | eyes | as drawn | none | "YES. GIVE IT TO ME." |
| 2D-4 KEEP art, RE-LETTER | P41 | wide | as drawn | the pommel lands | as drawn | DOOOOM moved off the pommel to the lower-left over the flying stone [0.22, 0.75], rot -8 | none |
| 2D-5 KEEP | P42 | tall | as drawn | carry | as drawn | THUMP | window [CARRY · 50% OF THE HIT MOVED TO THE OPERATOR] |
| 2D-6 KEEP | P43 | inset-l | as drawn | as drawn | as drawn | none | "WHAT HAPPENED? NOTHING EVEN TOUCHED YOU!" |
| 2D-7 REDRAW | P44 | wide | low, medium, 35 mm | Nib comes up onto one knee mid-roll at image-left, one knife braced on the floor, head snapping back over his shoulder toward the pillar (off-panel left), uncovered eye wide, mouth slightly open; at image-right the pommel still buried in a crater, the sword attached and rising out of frame with the knight's gauntlet on the grip at the top edge | dust rising from the crater; red light; amber outline | none | silent |

---

# Chapter 3: The Ninth Wall (judged from the video)

| seq | panels | what happens | grade |
|---|---|---|---|
| 3A Holding the gate (flashback) | P06 | Nib alone on the gatehouse roof cutting down Hush-spawn | **7/10** |
| 3B The refusal | P10-P14 | Nib won't attack his commander; Jaeha hauls him clear; field form ends | **6/10** |
| 3C The trap springs | P27-P35 (plan P19-P26) | Jaeha baits the knight across the plates; spikes and the portcullis pin it | **7/10** |
| 3D The pinned knight | P36-P48 | The knight fights the bars, Yerin draws a blind swing, and it tears free and floors Jaeha | **5.5/10** |
| 3E Seal break and the catch | P49-P56 | Nib comes back by choice, breaks seal 2/5 and catches the blade over Jaeha | **6/10** |

P57-P63 (the commander speaks) is talk under a blade lock.

## 3A Holding the gate (7/10): what is wrong
- **It works as a montage under narration.** Knives are buried in Hush-spawn with ash bursts (contact), the field is grey with speed lines, the camera is low and tilted, and the SFX sits in empty sky.
- **It is two strikes in one body.** Both arms are flung out in opposite directions in a wide lunge: a cool X pose, not one blow with a follow-through.

## 3A storyboard (1 → 1)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 3A-1 REDRAW | P06 | tall | low, tilted 15°, 20 mm, on the gatehouse roof | ONE strike: Nib in the follow-through of a backhand slash with his RIGHT knife, arm fully extended behind him to image-right, torso twisted at the waist, weight on his planted LEFT foot on a fallen grey banner, RIGHT heel lifted; the Hush-spawn he cut splits into violet ash at image-right; LEFT knife reversed along his forearm, ready; more black shapes pouring over the parapet as flat silhouettes | greys and violet ash; speed lines along the slash arc; sky reduced to streaks | SHRAKK (XL) along the arc in the sky [0.3, 0.15], rot -12 | none (narration) |

## 3B The refusal (6/10): what is wrong
- **P10 and P11 work.** The P11 refusal close-up is the best acting in the chapter.
- **P12: the save is far and crowded.**
  - It is a high wide with three figures: Yerin curled at the left, Jaeha seen from above, Nib being pulled.
  - The blade hits the pillar's edge about a metre from Nib, not "a hand's width".
  - KRAKOOM is lettered over Jaeha's legs and Yerin.

## 3B storyboard (5 → 5)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 3B-1 KEEP | P10 | tall | as drawn | the sword raised over the pillar | as drawn | none | "NIB, TAKE ITS LEGS! NOW!" |
| 3B-2 KEEP | P11 | inset-r | as drawn | refusal | as drawn | none | "NO. NOT HIM. I WON'T." |
| 3B-3 REDRAW | P12 | tall | low at floor level from behind the pillar's corner (its edge down the image-right side), looking out into the hall, 18 mm, dutch 15° | Jaeha in the foreground throws himself backward toward the camera, body a C-curve, RIGHT fist knotted in the back of Nib's cloak, notebook in his LEFT; Nib yanked backward off his bare feet toward the camera, limp, knives trailing, eye still on the knight; at image-right the blade smashes into the pillar's edge a hand's width from Nib's trailing foot; Yerin only as her white sneakers at the left border | flat hot orange beyond the pillar; radial white-orange burst at the contact; jagged hand-inked stone; speed lines along the pull; white rim on Jaeha | KRAKOOM (XL) at the contact [0.78, 0.3], rot -10; keep both figures clear | none |
| 3B-4 KEEP | P13 | strip | as drawn | the amber drains | as drawn | none | silent |
| 3B-5 KEEP | P14 | wide | as drawn | system | as drawn | BZZT | window [FIELD FORM ENDED] |

## 3C The trap springs (7/10): what is wrong
- **The set-up is the best in ch1-4: keep all of P19-P26.** The plate and spike holes (P20), the floor-plan sketch (P21), the overhead cyan plan (P22) and the eyes (P23).
- **P27-P29 work as geography.**
- **P30: the charge is a walk.** The knight is upright, sword raised in its right hand, one leg striding: no forward lean, no foreshortened foot, no dust.
- **P31 works.**
- **P32: the spikes don't strike.** Three horizontal spikes cross the knight's legs like fence bars. Nothing shows them striking or locking a joint: no flash where they meet armour, no buckled plate, the legs in a standing stance.
- **P33 works.** The portcullis's spiked bar bites the shoulders with debris; the knight is on its knees with Jaeha small behind the bars.
- **P34-P35 work.**

## 3C storyboard (9 → 10)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 3C-1 KEEP | P27 | full | as drawn | Jaeha walks out | as drawn | TAK TAK | none |
| 3C-2 KEEP | P28 | inset-l | as drawn | Nib watches | as drawn | none | silent |
| 3C-3 KEEP | P29 | wide | as drawn | Jaeha waves in the arch | as drawn | none | "OVER HERE, SIR! I'M THE ONLY THING ALIVE IN FRONT OF YOU." |
| 3C-4 REDRAW | P30 | tall | worm's-eye from the floor just in front of Jaeha's boots (boots and shins planted in the bottom foreground), 14 mm, dutch 10° | the knight charges straight at the camera across the square plates, leaning far forward, its LEFT foot slamming down huge and foreshortened in the foreground, RIGHT arm raising the long sword back over its shoulder, chains streaming back, red face-hole low and forward | stone chips and dust bursting from under the foot; speed lines converging on the camera; green shafts behind | DOOM (L) at the landing foot [0.25, 0.72]; one DOOM only | none |
| 3C-5 NEW | none | strip | extreme close-up, 85 mm | Jaeha's eyes level and unblinking, lower lids tight, red light growing across his face as the knight arrives | black with a band of red light | none | silent |
| 3C-6 KEEP | P31 | strip | as drawn | foot on the centre plate | as drawn | CLICK | none |
| 3C-7 REDRAW | P32 | wide | low at ankle height, three-quarter from the knight's front-left, 20 mm | spikes drive in from both pillars and punch into the gaps behind the knight's knees and at its ankle joints, stopping it mid-stride: front knee buckling, back heel lifted off the plate | white flash; radial bursts and sparks where each spike tip strikes armour; plates buckling; stone dust erupting from the holes; speed lines along the spikes | SHHNNNK (L) at the left spike hole along the spike [0.12, 0.35], rot -8; keep the knees clear | none |
| 3C-8 KEEP | P33 | tall | as drawn | the portcullis slams | as drawn | KA-DOOOM | none |
| 3C-9 KEEP | P34 | wide | as drawn | pinned | as drawn | none | "THREE HUNDRED AND TWELVE RAIDS, SIR. I KNOW A TRAP WHEN I SEE ONE." |
| 3C-10 KEEP | P35 | inset-l | as drawn | Yerin and Nib stunned | as drawn | none | "HE TRAPPED A BOSS. HE ACTUALLY TRAPPED A BOSS." |

## 3D The pinned knight (5.5/10): what is wrong
- **P36: a window on the action.** [COOLDOWN 00:12] is lettered across the middle of the strip, on top of the gauntlets bending the bars, which is the panel's whole action.
- **P37 works.** The helm rams the bars with impact lines at the contact, and Jaeha flinches with his arms up.
- **P39: a stiff pose.** Yerin's flash is a straight-armed, square stance at medium size, eye level.
- **P40: the blind swing has no target.**
  - VWOOOM lies across the knight's shoulder against its helm.
  - The blade's speed lines run along the bottom edge toward an off-panel pillar.
  - The bottom half of the panel is knees and floor.
- **P41: good contact, covered.** The blade bites the pillar a hand above Yerin's head while Nib pulls her down, but KRAKK sits on the blade and the contact.
- **P42-P45 work.** P45 is a strong silent beat.
- **P46: another window on the action.** [COOLDOWN 00:03] sits on top of the knees as the spikes snap.
- **P47 and P48 work.**

## 3D storyboard (13 → 13)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 3D-1 KEEP art, RE-LETTER | P36 | strip | as drawn | gauntlets bend the bars | as drawn | GRRRRK kept; [COOLDOWN 00:12] moved off the gauntlets into the black gutter before P37 | none |
| 3D-2 KEEP | P37 | wide | as drawn | helm rams the bars | as drawn | KLANNNG | none |
| 3D-3 KEEP | P38 | wide | as drawn | Jaeha shouts | as drawn | none | "YERIN! LIGHT UP YOUR HANDS AS BRIGHT AS YOU CAN, THEN HIDE!" / "KEEP IT BUSY TILL NIB'S BACK!" |
| 3D-4 REDRAW | P39 | wide | low from the floor beside the pillar's base, 18 mm | Yerin steps out from behind the pillar toward image-right, RIGHT foot planted forward, body leaning into the step, both palms thrust out at the camera, foreshortened, fingers spread, blazing mint-white; eyes squeezed half shut, ponytail swinging; Nib crouched at the pillar's base behind her, one arm up against the glare; hand_ref healing_palms.png | mint-white flare washing the frame; long shadows thrown behind them; focus lines radiating from her palms | FWASHHH (L) beside her palms [0.82, 0.14], rot -6 | none |
| 3D-5 REDRAW | P40 | tall | low behind the knight's RIGHT hip under the portcullis (bars across its back in the foreground, sparks where they grind), 20 mm, dutch 15° | the knight twists toward image-left, its RIGHT arm swinging the long sword in a flat forehand arc out between the bars toward the mint glow on the far pillar (image-left background), red face-hole turned toward the light | motion smear on the blade; speed lines along the arc; the mint glow as the visible target; red sparks at the bars | VWOOOM (XL) along the arc [0.35, 0.55], rot -14; keep the helm clear | none |
| 3D-6 KEEP art, RE-LETTER | P41 | wide | as drawn | the blade bites the pillar | as drawn | KRAKK moved off the blade and contact into the space above [0.3, 0.1] | none |
| 3D-7 KEEP | P42 | wide | as drawn | Jaeha bangs the bars | as drawn | BANG BANG | "HEY! SIR! I'M STILL RIGHT HERE!" |
| 3D-8 KEEP | P43 | inset-l | as drawn | as drawn | as drawn | none | "IS THIS WHAT YOU DO EVERY SINGLE DAY?" |
| 3D-9 KEEP | P44 | inset-r | as drawn | as drawn | as drawn | none | "USUALLY THERE'S LESS SCREAMING." |
| 3D-10 KEEP + UI | P45 | wide | as drawn | Nib watches | as drawn | [COOLDOWN 00:03] moved here, into the calm top | silent |
| 3D-11 KEEP art, RE-LETTER | P46 | wide | as drawn | spikes snap | as drawn | PANG PANG PANG kept; window removed (now on P45) | none |
| 3D-12 KEEP | P47 | tall | as drawn | the knight tears the portcullis out | as drawn | KRRRANNG | none |
| 3D-13 KEEP | P48 | tall | as drawn | system (right place) | as drawn | none | window [COOLDOWN 00:00] |

## 3E Seal break and the catch (6/10): what is wrong
- **P49 is acceptable.** A standing arrival in the cyan circle.
- **P50-P53 work.** The seal-break splash (P53) is symmetric and frontal, which is right for a power-up.
- **P53 to P54: Nib teleports.** He is at the far pillar through P53 and at the arch in P54, with no dash or streak across the hall; the 40% power is never shown moving.
- **P54: the upgrade is invisible.** The contact is drawn (white burst and sparks, a debris shockwave), but it is the same silhouette as ch001 P60 and ch002 P41 (arms overhead, knives crossed, knees out). "This time his feet don't slide an inch" doesn't show.

## 3E storyboard (8 → 9)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 3E-1 KEEP | P49 | tall | as drawn | Nib rises in the cyan circle | as drawn | VWUMM | off-panel: "NIB! COME BACK!" |
| 3E-2 KEEP | P50 | wide | as drawn | as drawn | as drawn | none | "YOU CALLED ME BACK." |
| 3E-3 KEEP | P51 | inset-r | as drawn | as drawn | as drawn | none | "I TOLD YOU. EVERYONE COMES BACK." |
| 3E-4 KEEP | P52 | wide | as drawn | system | as drawn | KRRRNK | window [NIB ANSWERED A SECOND CALL BY CHOICE] |
| 3E-5 KEEP | P53 | bleed | as drawn | seal break | as drawn | VWOOOOSH | none |
| 3E-6 NEW | none | wide | low at floor level, side-on, 20 mm, dutch 10° | Nib crosses the hall in one dash from image-left to image-right, body almost horizontal, knives back along his forearms, the new wall-blue lining and red scarf streaming; at the far right edge the knight's blade already descending toward the arch | background dropped to horizontal speed lines; amber speed trail behind him; floor plates cracking under each footfall | SHHT (M) behind him [0.28, 0.55] | none |
| 3E-7 REDRAW | P54 | tall | worm's-eye from behind Jaeha on the floor (head and shoulder cropped bottom-right), 16 mm, dutch 12° | Nib planted between Jaeha and the knight in an asymmetric strut: LEFT foot forward, RIGHT leg braced straight back, the body one straight diagonal from back heel to crossed knives, catching the giant blade overhead; feet perfectly still (no skid marks) while the stone cracks in a ring under them | white-amber flash at the contact; a shockwave ring blowing dust outward; sparks; red light from above | KRANNNG (XL) along the blade above the contact [0.35, 0.12], rot -10; keep Nib and the contact clear | none |
| 3E-8 KEEP | P55 | wide | as drawn | Nib holds the blade | as drawn | none | "I STILL WON'T KILL HIM." / "BUT I'LL HOLD HIM FOR YOU." |
| 3E-9 KEEP | P56 | inset-r | as drawn | as drawn | as drawn | none | "THAT'S ALL I NEED. HOLD HIM, AND I'LL FIND THE WAY." |

---

# Chapter 4: Harvest or Release

| seq | panels | what happens | grade |
|---|---|---|---|
| 4A The finisher | P01-P14 | Under the blade lock Jaeha carries half the weight, finds the crack and counts the sweep; Nib drives both knives into the rim | **7/10** |

Not fights:
- P36-P38, the sword-drop gag.
- P45-P49, the escape. P46, Nib's kick, has a real line of action and is fine.

## 4A The finisher (7/10): what is wrong
- **P01-P11 tell the hold well.** The camera changes on every panel. P03 (Jaeha's back in the foreground, Nib on one knee under the horizontal blade, cracks spreading) is strong. The hold reuses the ch1 silhouette.
- **P12: the wind-up the chapter waits for isn't drawn.**
  - The knight stands square with its sword held straight out to its side like a signpost: no twist, no rear-back, and no visible pauldron dip.
  - The caption "THE SHOULDER DROPS... WAIT FOR IT..." describes what the art doesn't show.
  - Nib's coiled crouch is right.
- **P13 is the best impact in ch1-4, with one flaw.** Nib is in mid-air driving both knives into the glowing crack, with a red-white burst at the contact and the sweep passing under him with heavy speed lines. But SHRAKKK runs across his hips and thighs.
- **P14: no landing.** The chapter cuts from the hit straight to a still wide with the BOSS DEFEATED window; there is no landing or reaction beat.

## 4A storyboard (14 → 17)
| new | replaces | shape | camera | action | effects in the art | SFX (text, where) | dialogue kept |
|---|---|---|---|---|---|---|---|
| 4A-1 KEEP | P01 | wide | as drawn | blade lock | as drawn | GRRRIIND | "I HEARD YOU, COMMANDER. I'LL END IT." |
| 4A-2 KEEP | P02 | strip | as drawn | the hole flares red | as drawn | VMMMM | none |
| 4A-3 KEEP | P03 | tall | as drawn | the knight bears down | as drawn | KRRRK | none |
| 4A-4 KEEP | P04 | strip | as drawn | eyes | as drawn | none | "CARRY. GIVE ME HALF OF IT." |
| 4A-5 KEEP | P05 | wide | as drawn | carry | as drawn | THOOM | window [CARRY · 50% OF THE LOAD MOVED TO THE OPERATOR] |
| 4A-6 KEEP | P06 | inset-l | as drawn | the load eases | as drawn | none | silent |
| 4A-7 KEEP | P07 | wide | as drawn | Yerin heals | as drawn | SHIIING | "KEEP GOING. I'LL KEEP YOU ON YOUR FEET." |
| 4A-8 KEEP | P08 | wide | as drawn | link view | as drawn | none | inner "THERE. A CRACK IN THE RIM OF THE HOLE." |
| 4A-9 KEEP | P09 | strip | as drawn | the crack | as drawn | TH-THUM | silent |
| 4A-10 KEEP | P10 | wide | as drawn | as drawn | as drawn | none | "I SEE IT TOO. DO IT. HE ASKED US TO." |
| 4A-11 KEEP | P11 | inset-r | as drawn | as drawn | as drawn | none | "THEN WE DO IT TOGETHER. ON MY CALL." |
| 4A-12 REDRAW | P12 | tall | low behind Nib's crouch (his back, wall-blue lined cloak, crossed sheaths and coiled legs in the bottom foreground, weight on the balls of his bare feet, knives back along his forearms), 16 mm | the knight wrenches its sword free and rears back for the sweep: torso twisted hard to its RIGHT (image-left), RIGHT arm drawing the long sword back behind its right hip, blade trailing low; the cracked LEFT pauldron (image-right) dipping | tension lines on the wound-up body; muted dark; red face-hole | none (CLNK moves to 4A-13) | inner "THE SHOULDER DROPS... WAIT FOR IT..." |
| 4A-13 NEW | none | strip | extreme close-up, 85 mm | the cracked LEFT pauldron drops a hand's width; the same framing as ch002 P33, so the reader recognises the tell | red light; hard shadow under the plate; armour edge to edge | CLNK (M) [0.72, 0.4] | silent |
| 4A-14 NEW | (line moved from P13) | strip | extreme close-up, 85 mm | Jaeha's eyes with the amber link glint, fringe over his LEFT eye, the instant of the call | black; amber and red light across the eyes | none | "NOW!" |
| 4A-15 KEEP art, RE-LETTER | P13 | bleed | as drawn | the finishing strike | as drawn | SHRAKKK moved off Nib's hips to the top-right above the burst [0.75, 0.08], rot -12 | none (its "NOW!" is on 4A-14) |
| 4A-16 NEW | none | wide | low, side-on, 28 mm | Nib lands in a crouch at image-left, one hand down, knives out wide, scarf and cloak settling; behind and above him at image-right the knight frozen at the end of its sweep, blade tip stopped a hand off the floor, thin rays of white light breaking out of the crack in its rim | dust settling; white light rays; no speed lines | TAK (S) at his landing foot [0.2, 0.86] | silent |
| 4A-17 KEEP | P14 | wide | as drawn | aftermath (right place for the window) | as drawn | D-DING | window [BOSS DEFEATED] |

---

# Patterns across ch001-ch004
1. **The knight never moves its weight.** It is drawn standing square, symmetric and legs apart in ch001 P37 (the rise), P50 and P52; ch002 P11, P32 and P36; ch003 P30 (the charge); and ch004 P12 (the sweep). Every wind-up is a static stance, so the tell (the pauldron dip) only reads in the dedicated inserts (ch002 P33). Fix: every knight anticipation panel names a torso twist and a weight shift.
2. **Nib has one defensive silhouette.** Arms overhead, knives crossed, knees out, in six panels: ch001 P60, ch002 P41, ch003 P54, ch004 P01, P03 and P06. The seal 1/5 to 2/5 power-up is invisible.
3. **Nib in attack is the best art in the run.** ch002 P03, P14, P19 and P35, and ch004 P13 show real lines of action, contact and dropped backgrounds. The model draws a small fast figure in motion well, and a giant or a human in motion badly: Yerin's step (ch001 P22), the hunters' run (P38), Jaeha's dive in the wrong direction (P45), Yerin's flash (ch003 P39).
4. **Lettering sits on the fighter in 13 panels.**
   - ch001: P21 (CRUNCH on Jaeha's chest), P37 (KRRRSSH on the knight's chest), P41 (KLANNNG over Mok's whole head), P45 (KRAKOOOM over Yerin's legs).
   - ch002: P17 (SKRANNG on Nib's thighs), P20 (SKREEE on his torso), P22 (KRASSHH on his legs), P41 (DOOOOM on the pommel).
   - ch003: P12 (KRAKOOM on Jaeha's legs and Yerin), P40 (VWOOOM against the helm), P41 (KRAKK on the blade and contact).
   - ch004: P13 (SHRAKKK on Nib's hips).
   - Plus one overflow: ch001 P58's SHHHRAANG spills out of its panel and leaves a stray "NG" in the gutter.
   - The cause is in the Lettering section above.
5. **Impacts drawn as wide shots shrink the fighter.** ch001 P22 (Yerin under half the height), ch002 P05 (about 15%), ch002 P22 (about 15%, plus a window), ch003 P12. On the video, a figure at 15-40% of a wide panel is roughly 10-30% of the frame height.
6. **The "between" beats are skipped.** The script often puts the cause in one panel and the result in the next, with no transfer beat:
   - ch001 P51 to P52: Yerin is dragged out off panel.
   - ch003 P53 to P54: Nib crosses the hall off panel.
   - ch002 P36: the stagger is never drawn.
   - ch004 P13 to P14: no landing.
7. **Multi-body acting in one action panel produces tangles or tiny figures.** The scripts' `acting` blocks give three people simultaneous actions: ch001 P45, ch002 P04, ch003 P12. Keep it to two figures in focus.
8. **What already works and should stay.**
   - Flat orange, white or red fields with drawn speed lines at impacts.
   - Contact on Nib's blows.
   - Jaeha reading the fight in every chapter: notebook inserts, eyes strips, cyan plan panels.
   - Windows mostly on quiet beats. The exceptions are ch002 P22 and ch003 P36 and P46.
9. **Screen direction mostly holds.** Breaks: ch001 P45 (the save moves toward the blade) and ch002 P16 (a mild flip after P14).
10. **Rule 7 is the root of the worst panel** (ch001 P39). See the verdict above.

# Notes for the main session
- The ch003 judge pack is missing; details and the rebuilt pages are in the first section.
- Re-lettering alone fixes about nine of the 13 lettering cases, once the face check is confirmed to fire. Two more need a `keep` box: ch002 P41 (the pommel) and ch003 P41 (the blade). The other two are already redrawn above (ch003 P40, ch001 P58).
- Nothing in this report came from memory. I made no changes outside my own folder.