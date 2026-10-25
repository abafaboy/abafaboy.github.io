# REVIEW FIXES, round 1: Claude's strict review (25 October)

**Why this file exists.** The owner asked for a strict review: anything that looks AI-made, and any weird detail, gets fixed. Claude checked every finished image against `CHARACTER_DESIGNS_v2.md` and against the new strict checks in `MANHWA_STYLE_GUIDE.md`:
- 10.4, the CLEAN-UP LINE;
- 11b, the strict checks.

Find your entry below and redo what it lists.

## How to do a fix (every chat)
1. **Read** `MANHWA_STYLE_GUIDE.md` 10.4 and 11b. From now on, build every prompt in this order:
   1. the STYLE BLOCK;
   2. the CLEAN-UP LINE;
   3. the sheet description;
   4. the snippet;
   5. the NEGATIVE BLOCK.
2. **Small fixes** (shading, shoes, one prop): try an edit first.
   - Pass the kept image as the reference and ask to change only the listed thing, keeping the face, pose, proportions and locks identical.
   - If the edit drifts or blurs, regenerate from the corrected front instead.
3. **Design fixes** (a face, a garment): redo the front first, then make every other file of the entry from the new front.
4. **Move every replaced image to the rejects:**
   - characters: `characters_v2/_rejects/<id>_r1_<reason>.png`;
   - locations: `locations_v2/<id>/_rejects/`.
5. **Check:** run section 11 and section 11b on every new image, with up to 3 tries per image.
6. **Finish:**
   1. Update `card.json`, `prompts.json` and `DONE.md`; add a "Round 1 fixes" list to `DONE.md`.
   2. Stop.

**Entries with no fixes listed** finish as briefed, but run 11b on every image before accepting it.

---

## S1 · Kang Jaeha: redo 4 files
- **Shard shading** on the orange vest and the grey hoodie: the orange is covered in translucent diagonal streaks. Repaint them as a few large, clean shadow shapes.
- **Sawtooth fraying** along both vest armholes and the whole hem. Keep the edges clean, with small frayed notches and a few loose threads at the two hem corners only.
- **Files:** `front.png`, `turnaround.png`, `expressions.png`, `details.png` (the vest crops).
  - Also redo `turnaround_coat.png` if the new front changes the trousers or the shirt.
  - Keep `chibi.png`: it passes.
- **Locks stay:**
  - fringe over the LEFT eye;
  - pencil behind the RIGHT ear;
  - notebook in the LEFT chest pocket;
  - the T on the right chest and the back.

## S2 · Nib: redo the whole set
1. **Face: a goblin, not an elf.** The current face is a generic pretty template. Follow design 2.2 line by line:
   - a long pointed nose with a slight hook, which clearly sticks out in profile;
   - a heavy brow ridge;
   - a narrow angular skull and hollow cheeks;
   - a narrow pointed chin;
   - a thin, wide mouth.

   Keep the amber eyes with heavy lined lower lids, the V-notch in the LEFT ear, the one small lower fang on the LEFT, the shaggy black hair and the deadpan. He is adult and weathered, never cute.
2. **Garment: the design's cloak, not a shredded short-sleeved tunic.**
   - A knee-length charcoal hooded cloak, hood down, closed at the throat by a plain dark-iron clasp. He wears it belted at the waist like a scout's coat.
   - No sleeves: wide armholes let his long bare grey-green arms swing free.
   - Small pockets, pouches and loops are sewn onto the cloak itself.
   - The belt carries the two crossed knife sheaths at the small of his back, handles up.
3. **Tatters.**
   - Only the cloak's hem is frayed and scorched: uneven, darkened, a few notches.
   - No shredded strips on the shoulders, the armholes or the panels.
   - The scarf ends get a light fray, not sawtooth tails.
4. **Clean shading** (11b.1).
- **Files:** `front.png`, `turnaround.png`, `expressions.png`, `details.png`, `chibi.png`, `turnaround_mask.png`. The binoculars, knives, mask, hands and feet in the current details sheet are good; redraw them on the new design.

## S3 · Song Yerin: redo 5 files
- **Logo on the shoes.** Her sneakers carry a swoosh and the shape of a famous branded shoe. Draw plain white low-top canvas sneakers with white soles: no logo, no side panel, no stitching pattern.
- **Shard shading** all over the off-white jacket (translucent zigzags). Repaint it with a few large, soft folds that suit an oversized jacket: at the elbows, at the waist and under the bag strap.
- **Blush.** Her cheeks are pink in every face. Keep only a faint warmth, with stronger pink only in the crying, frozen and laughing faces.
- **Files:** `front.png`, `turnaround.png`, `expressions.png`, `details.png` (the sleeve), `chibi.png`.

## S4 · Mok Hangyu and the Black Hound: redo 1 file
- Mok's own set passes.
- **`black_hound/lineup.png`:** the mage's staff reaches the floor. Design 2.5 gives him a SHORT staff, about forearm length, topped by a small violet core and held in one hand. Edit that one detail and keep everything else.

## S5 · the husk: redo 2 files (3 if the details are done)
- **What's wrong:** the hip seams form a V like underwear, and the back shows buttocks and a spine groove.
- **What a husk is:** a mannequin.
  - The hip seams are rings round the top of each thigh.
  - The torso, back and seat are smooth, simplified forms: no navel, no cleft, no muscle lines.
  - The feet are simple, with the toes moulded together or barely marked.
- **Keep:** the matte white, the seams at the shoulders, elbows, hips and knees, the featureless oval face and the stiff hanging arms.
- **Files:** `front_reference.png`, `turnaround.png`, and `details.png` if you have already made it.

## S6 · the hushed knight-commander: fix the front, then make the rest from it
- **Helm.** It has battlements like a chess rook. Draw a plain closed great helm, flat-topped or slightly domed, with no towers or crenellations on it.
- **Face-hole.** The whole face of the helm is the black-violet hole, with cracked edges leaking violet ash. Not a hole beside visor slits.
- **Sigil.** A clear bronze emblem embossed on the breastplate as one badge: a wall with nine round towers you can count. Not a crenellated stripe across the chest.
- **Head size.** The helm is in proportion with the body (about one-seventh of the standing height), not shrunken.
- **Then** make the turnaround, `kneeling.png` and `details.png` from the new front.

## S7 · the stone lizards: redo the set
- **3D look.** The plates are bevelled polygon facets, like a low-poly model. Draw irregular hand-inked stone slabs with chipped edges, cracks and rough dry-brush texture.
- **Teeth.** They look like neat human dentures. Draw blunt, worn, uneven grinding teeth, grey-yellow and chipped.
- **Menace.** The front view reads as a grumpy frog, but these lizards kill hunters in chapter 1.
  - Give it a lower, longer, heavier head and jaw: a crocodile crossed with a tortoise.
  - Small dull eyes under a heavy brow plate.
- **Keep:**
  - 1.5 m long and 60 cm at the shoulder;
  - the squat, heavy legs and the club tail;
  - the blind, milky LEFT eye.
- **Files:** `front.png`, `turnaround.png`, `details.png`, `pack.png`.

## S8 · Kang Seoa: redo the set
- **Skirt length.** She is 15: her pleated skirt reaches the top of her knee (11b.9).
- **Keychain.** The calculator's screen glows bright green, which reads as a #00FF00 letterer screen. Draw an unlit grey LCD.
- **Files:** `front.png`, `turnaround.png`, `details.png`, `chibi.png`, and `expressions.png` if the keychain shows in it.

## S9 · Yoo Bomi: redo 2–4 files
- **Stripes on the shoes.** Her black trainers have three diagonal side stripes, which is a brand mark. Draw plain black trainers with grey soles: no stripes, no logo.
- **Bow.** Design 2.7 says compact: make it a small recurve, about 90 cm.
- **Files:** `source_front.png`, `turnaround.png`, and `details.png` and `chibi.png` if you have already made them.

## S10 · Choi Dongmin: passes so far
Run 11b on the rest of the set.

## S11 · Kett: redo the set
- **Face.** A goblin like Nib (S2 above), but young, not a human elf boy:
  - a pointed nose, shorter and straighter than Nib's;
  - a narrow pointed chin and an angular skull;
  - smooth skin and an eager, open face.
- **Stray stitches.** The cloak is scattered with small staple-like stitch marks. Remove them; keep at most one or two real sewn patches.
- **Scarf ends.** A light fray, not sawtooth tails.
- **Files:** `front.png`, `turnaround.png`, and `expressions.png` and `details.png` if you have already made them.

## S12 · the summon silhouettes: rebuild as parts plus a script
- **What's wrong:**
  - after three tries the image still has grey interior lines, an uneven background and approximate heights (your own DONE.md says so);
  - Maud reads as a man, but the story bible calls her "she": draw a broad, strong woman with cropped hair;
  - Nib and Kett come from the old Nib design and are near copies of each other.
- **How:**
  1. Draw Borro, Lyra, Pim, Maud and Caldric each as its own image: one full-body, front-view, standing figure in solid black on flat light grey. Save the kept ones as `characters_v2/summon_silhouettes/parts/<name>.png`.
  2. Do not draw Nib or Kett. Their silhouettes are made by masking their own `front.png` (S2 and S11 are redrawing those now).
  3. Write a script, `characters_v2/summon_silhouettes/composite.py` (or `.ps1`), that:
     - turns every pixel that is not background into pure black #000000 and fills any holes;
     - scales each figure to its height at one shared px/cm;
     - orders them left to right: Nib, Borro, Lyra, Pim, Maud, Caldric, Kett;
     - puts every figure's feet on one baseline, with even gaps;
     - fills the background with exactly #E9E9EC, at 1536×1024.

     Heights: Nib 105 cm, Borro 240, Lyra 185 (a working value, not canon), Pim 140 to the top of his head (the antennae rise above), Maud 190, Caldric 210, Kett 95.
  4. Run the script with the current `nib/front.png` and `kett/front.png` and save `characters_v2/summon_silhouettes.png`. In `DONE.md`, note that the script must be re-run once S2 and S11 have finished their round-1 fronts; Claude will re-run it.

## L1–L5 · the location keys
All pass. In L1 the gate opens in the pit's far wall, at the bottom between the struts; later panels keep it there, as in `gate0912_site/key.png`, `gate.png` and `gate_exit/key.png`.

---

# Round 1 results: Claude's review (25 October)

| Entry | Result |
|---|---|
| S1 Jaeha | Front, turnarounds, expressions and details **pass** (Claude re-checked them on 25 October). `chibi.png` goes to round 2 below. |
| S2 Nib | **Passes.** Claude moved the fang to his left (picture-right) in `front.png`, `turnaround.png` and the front figure of `turnaround_mask.png`. Claude's later three-quarter mask note was wrong: the original mask already covered his left eye, the near eye in that view, and the visible eye is his right. The extended mask is rejected and the original restored. |
| S3 Yerin | **Passes.** Plain shoes, clean jacket, light blush. |
| S4 Mok and the Black Hound | **Passes.** The mage's staff is short. |
| S5 husk | **Passes.** A simplified mannequin. |
| S6 knight | **Passes.** A plain helm whose whole face is the hole; a nine-tower badge, and nine towers on the crossguard; the cracked left pauldron; modern chains with a stamped link. |
| S7 lizards | **Passes.** Hand-inked slabs, worn teeth, a crocodile-tortoise head, the blind left eye in every view. |
| S8 Seoa | **Passes.** The skirt reaches the knee, and the keychain screen is grey. |
| S9 Bomi | Round 1 passed. **Round 2 (restyle) passes:** cropped bomber, crop top, denim shorts with a belt, thigh-high socks, plain trainers; face, ponytail, bow and drone unchanged. |
| S10 Choi | **Passes.** |
| S11 Kett | **Passes.** A young goblin face; one real sewn patch. |
| S12 silhouettes | **Passes** as rebuilt. One update is needed: re-mask Lyra from her approved `lyra/front.png` (design 2.10) instead of the earlier part, and re-run the composite. |
| S14 Lyra | Front approved by the owner. Next: turnaround, expressions, details. |
| L1–L5 | **Pass.** |

---

# Round 2: Claude's second strict pass (25 October, night)

The owner went to sleep and left every decision to Claude. Claude re-checked every sheet, including the chibi sheets and the left/right side of every lock in every view (new check 11b.10). Find your entry and do only what it lists. Follow "How to do a fix" above; for a small local fix, edit only a cropped patch and composite it back, so the rest of the sheet stays pixel-identical.

## S1 · Kang Jaeha: `chibi.png`
- **Sawtooth vests.** In all eight chibi figures the vest is cut into jagged teeth along every armhole and hem, which round 1 should have caught (Claude's miss). Make the vest edges smooth like `front.png`: clean armholes and hem, with at most one or two tiny notches at the lower hem corners.
- Keep everything else: the poses, faces, pencil (RIGHT ear), fringe (LEFT eye), notebook (LEFT chest pocket, and never a second notebook in the pocket when he holds one), T patch on the right chest.
- Move the old file to `_rejects/kang_jaeha_r2_chibi_sawtooth_vest.png`.

## S2 · Nib: three small lock fixes
1. **`turnaround.png`, profile figure.** He faces picture-left, so we see his LEFT side and the near ear is his left ear, but it has no notch. Add the same V-notch as in the front view (on the ear's lower edge, near the tip). Patch only that ear; keep Claude's fang fix and every other pixel identical.
2. **`details.png`, masked head (bottom left).** The picture-right ear is his left ear and has no notch. Add it, patching only that ear.
3. **`chibi.png`.** In every figure only his LEFT ear has the one V-notch; his right ear has a clean edge (now both ears are ragged). The cloak hem is uneven and scorched with a few notches, never sawtooth teeth. Check that the one lower fang is on his LEFT in every figure where the mouth shows. Redraw the chibi sheet from `front.png` if patching would take longer.
- Move each replaced file to `_rejects/nib_r2_<file>_<reason>.png`.

## S4 · Black Hound: restyle hunter 5 in `black_hound/lineup.png`
- The owner asked for as much fan service and as many beautiful characters as possible. Hunter 5, the crossbow woman, becomes a striking beauty (design 2.5 and her new snippet in section 8): a sleek black chin-length bob, winged eyeliner, red lips; the guild jacket cropped at the waist and worn open over a fitted black tank top with a low scoop neckline; fitted black tactical trousers with a thigh holster; black boots; the crossbow.
- Edit only her figure (crop, edit, composite back). Every other hunter, Mok, the shields and the background stay pixel-identical.
- Move the old file to `_rejects/black_hound_r2_lineup_old_hunter5.png`.

## S8 · Kang Seoa: `chibi.png` (done by Claude)
- The keychain hung on her LEFT in seven chibi figures but on her RIGHT in the turnaround. Claude mirrored those seven figures in place, so it hangs on her right in every sheet. Nothing else in her design is one-sided.

## S15 · Moon Ahin: new entry
- See `MODEL_SHEETS_BRIEF.md` S15 and design 2.11.

## A1 · the acting test, round 2
- See `ACTING_TEST_BRIEF.md`, "Round 2".

---

# Round 2 results: Claude's review (25 October)

| Entry | Result |
|---|---|
| S1 Jaeha | **Passes.** `chibi.png` vest edges are smooth; every lock on its side. The other sheets passed earlier. |
| S2 Nib | **Passes.** The V-notch is on his left ear in the profile and on the masked head; the chibi ears and fangs are correct, and its hems match the approved front. |
| S4 Black Hound | **Passes.** Hunter 5 restyled (sleek bob, red lips, cropped jacket open over a low-necked tank top); everyone else pixel-identical. |
| S8 Seoa | **Passes** (Claude moved the chibi keychain to her right). |
| S14 Lyra | **Passes.** The profile now carries the quiver at her right hip. |
| S15 Moon Ahin | **Passes.** Claude separated the back-of-head bow study from the torso study in `details.png`. |
| P1 Jaeha acting | **Passes.** |
| P2 Nib acting | **Passes.** The three talking mouths now show one lower fang at his left corner. |
| P3 Yerin acting | **Passes.** |
| P4 Mok acting | **Passes.** The selfie phone is plain, with one round lens. |
| P5 Lyra acting | **Passes.** Pose 2 redrawn right-handed; Claude then re-routed its upper bowstring to the real bow tip and evened out the regenerated slot's lighter background. |
| P6 Bomi acting | **Passes** (Claude erased two bows that stood on their tips with nothing holding them). |
| A1 acting test | A1, A2=B2, B1, B3, B5 and A3 **pass**; the dialogue run changes faces line by line. B4/P31: Mok's face reads angry instead of dead-flat, and a second notebook sits in Jaeha's pocket; being edited. The script now has Mok haul the shield up with his right arm in P31, matching the drawing. |

**25 October, afternoon.** Every character sheet passes. Claude built the scale charts (`scale_chart_v2.png`, the full row; `scale_chart_v2_cast.png` and `scale_chart_v2_giants.png`, readable splits) and sent the owner one 62-page PDF of all sheets, with no colour codes. The B4/P31 edit of the acting test is still running.
