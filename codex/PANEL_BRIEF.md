# PANEL BRIEF: draw one chapter of "My Summons Go First" (method B)

You draw every panel of ONE chapter from its script. Several Codex sessions run at the same time, one per chapter, so touch only your own chapter's folder.

The owner chose **method B**: one image-generation pass per panel, using the TECHNIQUE BLOCK below plus `style_test/abcd/STUDY_NOTES.md`.

## 1. Read first
- `scripts/chNNN.yaml`: your job list. Each panel has `id`, `shape`, `camera`, `art`, `calm`, and sometimes `style`, `silent` and `notes`.
- `bible/ART_BIBLE.md`: Part A (drawing rules, the A4 colour script, proportions, continuity locks, A5b chibi) and Part C (the anti-AI checklist).
- `style_test/abcd/STUDY_NOTES.md` and the TECHNIQUE BLOCK in section 7.
- `characters/<id>/`: `turnaround.png`, `expressions.png`, `details.png` and `chibi.png`, whichever exist. **Pass the sheet of every character in the panel as a reference image**, so faces, hair, colours and props stay on model.
- `locations/<id>/` and `world/floorplans/<id>.png`, when they exist. Pass the location key as a reference image for every panel set there. Read the floor plan as a layout note only, and never pass a floor plan to image generation. Where a floor plan and a location key disagree, follow the key.
- `world/LOCATIONS.md`, when it exists, for location details.

If a character or location has no sheet yet, follow the description in the script and the bible, and note it in PROGRESS.md.

## 2. What to draw
For each panel in the script, in order. Skip `kind: title`; for `kind: end`, see section 3.
- **Size by shape.**
  - `full`, `wide`, `vignette`: 1536×1024.
  - `strip`: 1536×1024, with the subject inside the middle third of the height (the letterer crops a band).
  - `tall`, `narrow-l`, `narrow-r`, `bleed`: 1024×1536.
  - `inset-l`, `inset-r`: 1024×1024.
- **Follow `camera` and `art` exactly**: who, outfit, pose, ACTING (the emotion on the face), location, light source, palette, props.
- **`calm`** names the region where the letterer puts bubbles (top, top-left, bottom, and so on). Keep it simple (wall, sky, floor, plain background) and free of faces and important action.
- **`style: chibi`**: draw in the chibi style of `characters/<id>/chibi.png` (2.5 heads tall, gag faces) on a simple flat background.
- **"screen: green"**: that screen is a flat, evenly lit, pure **#00FF00** area with crisp edges. No reflections, no glare, no UI; fingers may cover part of it. Never put green on any other screen.
- **Never draw text**: no letters, numbers, words, logos with words, speech bubbles, SFX lettering or interface windows. Signs, name tags and screens without "screen: green" stay blank or abstract.
- **`silent: true`** panels are acting beats: the faces and bodies must carry the moment.

## 3. The end card
The `kind: end` panel has a `chibi_gag`. Draw it as `END.png`: 1024×1024, chibi style, plain white background, no text.

## 4. Files
- Save each panel as `chapters/chNNN/art/<id>.png` (for example `P07.png`, or `P12a.png` for an insert).
- Nothing else goes in that folder except `PROGRESS.md` and `DONE.md`. Put rejects in `chapters/chNNN/_rejects/`.
- Do not modify scripts, bible, characters, locations, world, kit or any other chapter's files.

## 5. Check every image before you save it
Redo an image up to 2 times if it fails any of these:
1. The right characters, outfits and props, and every character matches their sheet (face shape, hair, colours).
2. The locks:
   - **Nib**: a clear V-notch in the top edge of his LEFT ear; one small lower fang on his LEFT; leather pouch on the RIGHT hip; brown wooden knife sheath on the LEFT hip; barefoot; adult and never cute (except in chibi panels); 105 cm, his head at Taeo's belt.
   - **Taeo**: exactly one small mole, under his RIGHT eye; the olive backpack with the faded orange shield-and-open-door patch; the dark grey phone with a hairline crack in the top-left corner of the glass.
3. No text, no bubbles, no SFX.
4. The calm region is clear.
5. The method B look: flat colour, one hard-edged shadow tone per material, crisp tapered lines; no airbrush, haze, bloom or glow fog.
6. The right size and orientation for the shape.

## 6. Progress and finishing
- After every panel, append one line to `chapters/chNNN/art/PROGRESS.md`: `P07 done`, or `P07 redo: <reason>`.
- If you are restarted, read PROGRESS.md and continue from the first panel not marked done.
- When every panel and `END.png` exist, write `chapters/chNNN/art/DONE.md` with the panel count and any panels you are unsure about.
- Do not stop to ask questions. Finish the chapter.

## 7. TECHNIQUE BLOCK (put it in every prompt)
> Korean webtoon (manhwa) panel drawn by a professional webtoon artist in Clip Studio Paint. Digital ink line art with a G-pen brush: confident tapered strokes, thick outer contours, thin inner lines, heavier line weight on the shadow side. Flat colour fills. ONE hard-edged cel shadow tone per material, with no gradients, no airbrush and no soft blending on skin, hair or clothes. Small sharp white highlights on hair and eyes only. Korean webtoon face construction: defined brow, a single shadow shape along the nose bridge, angular jaw, thick upper lash line with one catchlight, the mouth as one expressive line. Clothes with a few decisive fold lines and shadow shapes. A simplified drawn background. No bloom, no haze, no glow, no depth-of-field blur. Not 3D, not painterly, not a glossy anime illustration.
