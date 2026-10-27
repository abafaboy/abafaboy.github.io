# HF: hand and arm fixes on drawn panels (from the audit of 28 October 2026)

**Why.** After watching chapters 2 and 3 the owner said the story is "amazing" and the one problem is the hands and arms: "theyre awful. sometimes the positions and everything else is awful about arms and hands." He decided that **Codex fixes them** ("they need to be fixed by codex, you cannot fix them") and asked for "different hand references if needed for realism". Claude audited every panel of chapters 1–10 and lists the panels to fix; you draw every fix. Claude reviews each one strictly before it goes into the video.

## Your job's files
Each job names its chapters. For each chapter `chNNN`:
- **The list:** `codex/reviews/HANDS_chNNN.md`. Each entry gives the panel, who, which hand or arm, the problem, the fix sentence (each hand's job, by the character's own side), the method (edit or redraw) and the references.
- **The base images:** `chapters_v2/chNNN/art/hands_fix/base/PNN.png`. These are the exact panels in the published video. **Always start from the base file,** never from `art/PNN.png`: for some panels the file in `art/` is an older version.
- **Hand references:** `characters_v2/hands/` (job H1; `INDEX.md` says what each one shows). They are realistic photographs for anatomy only. Never paste them into a panel; draw the hand in the house style.
- **Character sheets:** the ones the list names. For hands, the `details.png` sheet shows the gloves, bandages and props.

Write only inside `chapters_v2/chNNN/art/hands_fix/`:
- `fixed/PNN.png`: the fixed panel, at exactly the base's pixel size.
- `tries/PNN_tN.png`: every try (and `tries/PNN_tN_crop.png`, the crop you sent, for edits).
- `prompts.json`: the exact prompt and references of every try.
- `LOG.md`: one entry per panel: the method, how many tries, what changed, the check result for every hand in the panel, and anything you could not fix.
- `DONE_HF.md` when the chapter is finished.

**Never write into `art/` itself or `art/_rejects/`, and never rename, move or delete anything there.** Some files in `art/` are hard links; Claude puts the fixed panels in place.

## Method 1: edit (the default)
Use this when the rest of the panel is fine.
1. **Crop.** Find the hand or arm in the base. Cut a crop around it, including:
   - the whole arm up to the shoulder;
   - whatever the hand holds or touches;
   - a margin.
   
   Make the crop a size the generator returns unchanged, as in your earlier patch fixes (P62's pencil, P20's sigil), so nothing is ever resized.
2. **Edit the crop.** Pass the crop as the image to edit, the hand reference, and the character's details sheet. The prompt:
   - starts with the STYLE BLOCK and the CLEAN-UP LINE;
   - then says: "Edit this image. Redraw only <the hand or arm> so that <the fix sentence>. Keep everything else exactly as it is: the face, hair, clothes, background, colours, line weight and light.";
   - ends with: "Hands and arms: follow the anatomy of the hand reference exactly (finger count, knuckles, thumb position, wrist angle); draw them in the house style."
3. **Composite.** Paste the edited crop back into a copy of the base at exactly its position, one pixel for one pixel, through a soft-edged mask.
   - The mask covers the old hand and arm as well as the new one, so no trace of the old hand is left.
   - Outside the mask the panel stays identical to the base.
   - If the edit shifted the colours, match them to the base just outside the mask before you paste.
4. **Check.** Look at the result at full size, and at every hand at 2x:
   - the lines meet at the mask edge, with no doubled outline, smear or colour step;
   - every hand in the panel passes the check below.

## Method 2: redraw
Use this when the list says so, or when an edit has failed three times.
1. Draw the whole panel again at the base's pixel size. Pass:
   - the base as the first reference;
   - the hand reference;
   - the character sheets the list names.
2. The prompt starts with the STYLE BLOCK and the CLEAN-UP LINE, then says: "Redraw this panel with the same composition, camera, characters, positions, expressions, background, colours and light; change only the arms and hands: <the fix sentence>." Then add the panel's `art:` and `acting:` lines from `scripts_v2/chNNN.yaml`, and the hand-reference line above.
3. Keep the empty areas empty: the balloons are already placed there.

## The check (every hand in the panel, not just the fixed one)
- **Count and side:**
  - five digits per hand: four fingers and a thumb, for Nib and Borro too;
  - the thumb on the correct side for a left or right hand;
  - nothing fused, extra or missing;
  - no hand that belongs to nobody.
- **Joints and proportion:**
  - every arm starts at the shoulder;
  - the upper arm and forearm are about the same length;
  - the elbows and wrists bend only the way they bend;
  - a hand is about as tall as the face.
  - Nib's and Borro's long arms, reaching their knees, are correct.
- **Grip and job:**
  - the fingers wrap what they hold, with nothing passing through or floating;
  - the hand does exactly the job in the fix sentence, on the named side.
- **Design:**
  - Jaeha's black fingerless gloves, with all ten fingertips bare;
  - bandages, sleeves and props as in the base.
- **No other change,** for an edit: compare the base and the result side by side.

Take up to three tries per method. If a panel still fails, keep the best try in `fixed/`, and write in `LOG.md` exactly what is still wrong.

## Also
- **Usage limit.** If the image tool returns a usage limit (429), stop. Write in `LOG.md` which panels are done and which are not, with the reset time, then stop.
- **Disk.** If free disk space falls below 3 GB, stop and say so in `LOG.md`.
- Don't ask questions; make the reasonable choice and note it in `LOG.md`.
