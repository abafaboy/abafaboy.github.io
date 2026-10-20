# STYLE FIX: make it read as Korean manhwa, not AI

The owner looked at the first character sheets and said they look **"too AI, rather than manhwa"**. That verdict overrides everything else. Until it is fixed, no more character sheets, location keys or panels.

## 1. What reads as AI in the current sheets (fix every item)
1. **Soft, airbrushed shading.** Smooth gradients on the hoodie, skin and hair. Real webtoons use flat colour plus ONE hard-edged shadow shape per material.
2. **Uniform thin lines with soft edges.** There is no visible ink stroke: no taper, no thick outer contour, no weight change. Real webtoon line art is confident G-pen ink. Outer contours are clearly heavier, inner lines thinner, and the lines are darker where forms overlap or turn away from the light.
3. **A generic "AI anime" face.** The same pretty template on everyone: glossy eyes, tiny mouth, no structure. Korean webtoon faces are constructed:
   - a defined brow ridge;
   - a nose bridge carried by one shadow shape;
   - an angular jaw and visible cheekbone planes;
   - a thick upper lash line with a single catchlight;
   - a mouth that is one expressive line.
   Each character must have their own face shape.
4. **Even studio lighting** with no light source. Cloth folds are airbrushed and generic instead of drawn as a few decisive fold lines with shadow shapes.
5. **Glowy backgrounds** (lamp bloom, haze) with photographic depth.

## 2. Step 1: look at real manhwa first (the owner approved this)
Open these episodes in your browser and study them **for style only**.
- Never copy their characters, faces, poses, compositions, panels or text.
- Never use their images as input to image generation.
- If you have to download an image to view it, keep it outside this project folder and delete it afterwards.
- If your browser cannot open webtoons.com, write that in `style_test/abcd/REPORT.md` and continue with Step 2 using the descriptions in `bible/VISUAL_SURVEY.md`.

| Episode (URL) | What to study |
|---|---|
| Questism, ep 1 · https://www.webtoons.com/en/fantasy/questism/x/viewer?title_no=3767&episode_no=1 | Line weight on faces and school uniforms; hard cel shadows on modern clothes; how a system pop-up sits in a scene |
| The Constellations Are My Disciples, ep 1 · https://www.webtoons.com/en/fantasy/the-constellations-are-my-disciples/x/viewer?title_no=5638&episode_no=1 | Flat shadow SHAPES on hair and skin; one crisp highlight band on hair; thought balloons with circle trails |
| Eleceed, ep 1 · https://www.webtoons.com/en/action/eleceed/x/viewer?title_no=1571&episode_no=1 | Clean line art, lots of white space, the switch to simplified CHIBI comedy faces |
| Lookism, ep 1 · https://www.webtoons.com/en/drama/lookism/x/viewer?title_no=1049&episode_no=1 | Korean webtoon face construction (jaw, nose, eyes); hand-lettered SFX; floating inner monologue |
| Viral Hit, ep 1 · https://www.webtoons.com/en/action/viral-hit/x/viewer?title_no=2268&episode_no=1 | Modern Seoul realism; casual clothes; phone and stream UI in panels |
| The Greatest Estate Developer, ep 1 · https://www.webtoons.com/en/fantasy/the-greatest-estate-developer/x/viewer?title_no=3596&episode_no=1 | CHIBI and gag faces mid-scene; comedic timing |
| Return of the Blossoming Blade, ep 1 · https://www.webtoons.com/en/action/return-of-the-blossoming-blade/x/viewer?title_no=2849&episode_no=1 | The jump from a tragic, dramatic prologue to slapstick chibi comedy |
| Study Group, ep 1 · https://www.webtoons.com/en/action/study-group/x/viewer?title_no=3595&episode_no=1 | Small panels, white space, bright clean colour |
| Bloodhounds, ep 1 · https://www.webtoons.com/en/action/bloodhounds/x/viewer?title_no=4000&episode_no=1 | A muted palette with ONE red accent; gritty everyday Seoul |
| Dungeon Porter, ep 1 · https://www.webtoons.com/en/fantasy/dungeon-porter/x/viewer?title_no=7914&episode_no=1 | A low-rank worker hero; campfire warmth; dungeon interiors drawn, not painted |
| Just a Goblin, ep 1 · https://www.webtoons.com/en/fantasy/just-a-goblin/x/viewer?title_no=3514&episode_no=1 | The CUTE goblin look Nib must NOT have |

Write `style_test/abcd/STUDY_NOTES.md` with 10–20 concrete technique notes in your own words. For example: "outer contour about 3× the inner line", "shadow edge always hard, shadow colour cooler", "no gradient on skin except a blush". Then use them in Step 2.

## 3. Step 2: a four-way style test (then STOP and report)
Draw the SAME two images four ways.
- **Image 1, wide.** Hanbit Mart counter at night, fluorescent light. Taeo in his work vest rings up a customer, tired. The customer is a middle-aged woman in a beige cardigan, arguing. Nib is not in it.
- **Image 2, close-up.** Nib's face and shoulders, wary, hand at his knife hilt, lit from the side by cyan summon light.

| Method | How |
|---|---|
| **A · baseline** | Your current method, for comparison. |
| **B · technique prompt** | One pass with the TECHNIQUE BLOCK below plus your study notes. |
| **C · ink first** | Pass 1: generate ONLY black ink line art on pure white (G-pen, varied weight, no grey, no shading, no text). Pass 2: an image EDIT of that exact line art: flat colours, one hard shadow tone, small sharp highlights, keep every line. Then, with Python, check the alignment of pass 1 against pass 2 (for example, phase correlation). If they align within 2 px, multiply the pass-1 ink layer over the colour result so the lines stay crisp ink. Report the alignment you measured. |
| **D · ink first + finishing** | C, plus light webtoon finishing in Python: replace pure black lines with warm near-black #2B2523, and add a very light screentone dot pattern ONLY inside background shadow areas (never on faces). |

**TECHNIQUE BLOCK** (use it in B, C and D):
> Korean webtoon (manhwa) panel drawn by a professional webtoon artist in Clip Studio Paint. Digital ink line art with a G-pen brush: confident tapered strokes, thick outer contours, thin inner lines, heavier line weight on the shadow side. Flat colour fills. ONE hard-edged cel shadow tone per material, with no gradients, no airbrush and no soft blending on skin, hair or clothes. Small sharp white highlights on hair and eyes only. Korean webtoon face construction: defined brow, a single shadow shape along the nose bridge, angular jaw, thick upper lash line with one catchlight, the mouth as one expressive line. Clothes with a few decisive fold lines and shadow shapes. A simplified drawn background. No bloom, no haze, no glow, no depth-of-field blur. Not 3D, not painterly, not a glossy anime illustration.

**Deliverables**
- `style_test/abcd/img1_A.png` … `img1_D.png` and `img2_A.png` … `img2_D.png`.
- `style_test/abcd/compare.png`: two rows (image 1, image 2), four columns (A–D), each labelled.
- `style_test/abcd/REPORT.md`: what each method did well and badly, honestly, plus which one YOU think looks most like the real episodes and why.

Then **stop** and wait. The owner chooses the method.

## 4. Step 3 (only after the owner picks): chibi
The owner asked for chibi. For taeo, nib, eunchae, haru and grandma, make `characters/<id>/chibi.png`:
- 2.5 heads tall;
- the same colours, hair and props as the full sheet (Nib's ear notch, belt, pouch and sheath; Taeo's backpack patch);
- 8 gag poses:
  1. panic, with sweat drops flying;
  2. deadpan stare (dot eyes, flat line mouth);
  3. waterfall crying;
  4. rage, with steam from the head;
  5. sparkling pride;
  6. asleep with a snot bubble;
  7. shocked, turned to white stone;
  8. eating with a full mouth.

Chibi is for comedy beats only. Every chapter will use 1–3 chibi panels or insets, plus a small chibi gag on the end card.

## 5. Step 4 (after the owner picks): redo the model sheets
Redo every turnaround, expressions sheet and details sheet in the chosen method. Do the same for the location keys and the original style-test panels. Keep the earlier sheets in `characters/_v1/` for reference; do not delete them.
