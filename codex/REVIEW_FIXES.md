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
