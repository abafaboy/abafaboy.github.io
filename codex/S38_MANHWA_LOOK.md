# S38: the manhwa look, pushed further (2 November 2026)

**Why.** Chapters 1–10 went up on YouTube and did well. The owner, 2 November: "try to keep improving the art style so its more similar to the manhwa / manga style". Our panels read as polished anime illustrations: thin coloured lines, soft painted light, and backgrounds as busy and as sharp as the people (chapter 11 P66 and P69 are typical). Real webtoon panels read as *drawn*: bold black ink, flat cel colour, backgrounds that step back, and graphic effects at the big beats.

**When it applies.** To every new chapter panel **from chapter 12 on**, after the style test below has been approved. Chapter 11 finishes in the current V2 look so the chapter stays consistent. The V2 rules in `MANHWA_STYLE_GUIDE.md` stay in force; this brief turns four of them up and replaces the STYLE BLOCK.

## 1. The four changes

1. **Ink like a webtoon studio.**
   - Solid black G-pen lines on every figure.
   - The outer silhouette, the jaw, the hair mass and every overlap get a bold tapered contour (about 4–6 px on a 1536 px canvas). Inner lines are thin (1–2 px).
   - Spot solid blacks: the hair's dark mass, the deepest shadow under the chin, inside a sleeve, a coat's folds. A third of a dramatic panel may be near-black.
   - Hair is drawn in sharp angular clumps with two or three crisp highlight cuts, never strand-by-strand painting.
2. **Flat cel colour, no painting on figures.**
   - Each material gets one flat base colour, one hard-edged cel shadow, and at most one small crisp highlight. Glossy specular only on metal, glass and wet surfaces.
   - No soft gradients, airbrush, painted brush texture or skin texture on any figure: no pores, no painted wrinkles, no blush made of soft spray (blush is a few hatched lines).
   - Light from a glow (a summon, a system window, fire) is a flat coloured cel shape on the lit side plus a crisp rim, not a soft haze over the whole figure.
3. **Backgrounds step back, every time.**
   - Follow the density ladder in `MANHWA_STYLE_GUIDE.md` section 8 strictly.
   - **Establishing shots:** detailed, but drawn as clean line art with flat fills, never painted.
   - **Medium shots:** big simple shapes, three or four props, lower contrast and lower saturation than the people, detail fading toward the edges.
   - **Talk, reactions, close-ups and eyes:** the background drops to a flat colour, a two-colour gradient, a few soft out-of-focus shapes, sparkle dots, or speed lines. A crowd behind a talking character is drawn as simple flat silhouettes or pale shapes, not as a row of detailed people.
   - The characters always have the strongest contrast in the panel.
4. **Manga and manhwa effects at the peaks.**
   - **Shock and realisation:** radial focus lines closing in from the frame edges; the background may drop to white or black.
   - **Speed:** straight speed lines along the motion; the background turns to streaks.
   - **Impact:** a jagged flat-colour burst, faceted debris, an ink spatter; at the biggest hit, a one-panel black-and-white inverted flash frame where the script's recipe is `impact` or `splash`.
   - **Dread:** vertical gloom lines over the top of the frame and a shadowed upper face with the eyes left lit.
   - **Comedy** (recipes `tone-flip` and any `gag` beat): manhwa gag faces. Blank white eyes, a giant sweat drop, a vein mark, a tiny wobbly mouth, a squashed simple body. Only where the script asks for a joke.
   - **Screentone dots:** only in effect backgrounds (behind a reaction, inside a burst), never on skin or clothes.

## 2. The S38 STYLE BLOCK (replaces the V2 STYLE BLOCK for chapter panels from chapter 12 on)

> Korean webtoon panel, drawn and coloured by a top professional action-webtoon studio. Clean digital inking with solid black G-pen lines: bold tapered outer contours, heavier on the silhouette, the jaw, the hair mass and where forms overlap; thin inner lines; solid spotted blacks in the hair and the deepest shadows. Hair in sharp angular clumps with a few crisp highlight cuts. Flat cel colouring: one flat base colour, one hard-edged cel shadow and at most one small crisp highlight per material; no soft gradients, airbrush, painted texture or skin texture on any figure. One named key light; at dramatic beats a thin crisp rim light from behind and large near-black shadow masses. Faces in webtoon construction: a clean simple nose line, defined lips, expressive eyes with sharp catchlights. The background is clean line art with flat fills, lower in contrast and saturation than the characters, simplified for the panel type. Graphic manhwa effects at peak beats: radial focus lines, speed lines, flat jagged impact bursts. Reads instantly at phone size.

Keep the rest of the prompt kit exactly as `MANHWA_STYLE_GUIDE.md` section 10 says: the CLEAN-UP LINE (10.4) after the style block, the recipe line, the ACTING LINES, the reference sentence, and the NEGATIVE BLOCK (10.3) with this sentence added at its start:

> Not a painting and not a semi-realistic illustration: no painterly brushwork or soft rendering on figures, no photo-textured or painted backgrounds, no anime key-visual lighting haze.

## 3. The S38 check (add it to every panel's REVIEW entry, after hands and legs)
1. Are the figure outlines solid black and bold on the silhouette, thin inside?
2. Is every figure flat cel colour with hard-edged shadows (no soft painting, no skin texture)?
3. Is the background simpler, paler or darker and lower in contrast than the characters, as the density ladder says for this recipe?
4. If the beat is a peak (shock, speed, impact, dread, gag), is the effect drawn as graphic shapes?
5. Does it read in one second at phone size (about 400 px wide)?

## 4. Job S38-T: the style test (do this first, before any chapter 12 panel)
Redraw four approved panels with **exactly** their script text and their references from the chapter 11 `PROMPTS_<letter>.json` files. The only change is the S38 STYLE BLOCK and the extra negative sentence:

| Test | Panel | What it tests |
|---|---|---|
| T1 | `chapters_v2/ch011/art/P67.png` | Emotional close-up: face, hand, ink, a background that drops to flat colour |
| T2 | `chapters_v2/ch011/art/P66.png` | Medium shot with a crowd: the background steps back, the crowd as simple shapes |
| T3 | `chapters_v2/ch011/art/P53.png` | Action: Nib's lunge, speed lines, an impact burst |
| T4 | `chapters_v2/ch011/art/P70.png` | Eyes and dread: spotted blacks, a flat violet up-light and rim, focus lines |

- Save each as `style_test_v3/<test>_<panel>.png` (for example `style_test_v3/T1_P67.png`) at the original panel's size.
- Next to each, save `style_test_v3/<test>_compare.png`: the original on the left and the S38 version on the right, each 768 px wide.
- Up to 3 tries per test. Run the hand check, the leg check and the S38 check on each, and write `style_test_v3/REVIEW.json` and `style_test_v3/DONE.md`.
- Never overwrite or move anything in `chapters_v2/`: the test only writes in `style_test_v3/`.
- Claude reviews the test. The approved tests become the **style keys**: from chapter 12 on, pass the closest style key as one of the five references whenever a slot is free after the characters, the location and the pose sketch.

## 5. Job S38-K: the style keys (added 2 November after the S38-T review)
The S38-T test changed the look only a little: the reference images carry their V2 rendering into each new image. Make three **style keys** that show the S38 look clearly, then pass the closest one as a reference on every chapter panel from chapter 12 on.

| Key | Scene (script text from chapter 11) | Shows |
|---|---|---|
| K1 | P70: the extreme close-up of Jaeha's eyes with the violet up-light | Face and hair: bold ink, hard cel shadows, flat glow shapes |
| K2 | P66: Seoa holding up the rice-cake bag with the crowd behind her | A character against a background that steps back: the crowd as flat, pale, simple shapes |
| K3 | P53: Nib's lunge on the top step sweeping a hound off in a burst of ash | Action: speed lines, a flat jagged burst, spotted blacks |

- Put the S38 STYLE BLOCK at the very start of the prompt, before the scene.
- Pass only the character's sheet (turnaround or front) and its expressions sheet: no location key, no earlier panel.
- Add: "The reference images show only the character's design (face, hair, clothes, colours). Ignore their rendering, shading and line style; draw everything in the style described above."
- Push it further than T1-T4: thick black outer contours, flat colour with one hard shadow, no painted smoke or sky (smoke and sky are flat shapes or a two-colour gradient), the crowd in K2 as simple flat shapes with no faces drawn in detail.
- Save `style_keys/K1.png`, `style_keys/K2.png` and `style_keys/K3.png` at the panel sizes (K1 and K2 wide 1536×1024, K3 wide 1536×1024), with `style_keys/K<n>_compare.png` (the V2 panel left, the key right, 768 px each). Up to 4 tries each. Write `style_keys/DONE.md`.
- From chapter 12 on, every panel prompt adds the design-only sentence above, and passes the closest style key as one reference when a slot is free (K1 for close-ups and reactions, K2 for talk and medium shots, K3 for action), once `reviews/S38.md` approves the keys.
