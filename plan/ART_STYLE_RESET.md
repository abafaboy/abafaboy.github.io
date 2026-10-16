# Art style reset (Abafa, 17 Oct 2026): top priority

Abafa: "the images look too ai again. make it research manhwa style and go back to manhwa style."

Pause all new panel generation in the current look until steps 1–3 are done.

## 1. Research real manhwa first
Study real panels from Korean fantasy webtoons with a similar tone. Use them for style only and never copy their characters:
- The Greatest Estate Developer
- Trash of the Count's Family
- Solo Leveling
- Omniscient Reader's Viewpoint
- Return of the Mount Hua Sect

Note how they handle line art, shading, backgrounds, close-ups and comedy beats.

Then:
- Write your findings to `plan/STYLE_GUIDE.md`.
- Rewrite the STYLE section of `plan/brief_head.txt` from that guide. The current one already says "flat cel shading", but the images ignore it, so it must be far more specific.
- Replace `style_refs\ref1-8` if they look like AI illustrations rather than real webtoon panels.

## 2. What makes the current art look AI
This starts around Ch 24 and is worst from Ch 29.
- Painterly, soft rendering everywhere, with glossy skin and hair.
- Warm bloom, god rays, glowing dust motes, haze and depth-of-field blur.
- Every surface over-detailed: props, papers, fabric folds, jewellery, clutter.
- Nearly every panel is a cinematic "key art" shot with a full background.

## 3. Target look
Chapters 1–20 were closer to this.
- **Line art:** clean, confident digital line art with darker outer contours.
- **Shading:** flat cel shading. Use a base colour plus one or two hard-edged shadow tones and small crisp highlights. Gradients only for skies and magic glow.
- **Backgrounds:** detailed only in establishing shots. Dialogue and reaction panels get simple, faded, or flat-colour/gradient backgrounds.
- **Framing:** webtoon framing, with close-ups and extreme close-ups (eyes, hands) for emotion. Also use reaction shots, low and high angles, and figures cropped by the panel edge.
- **Comedy beats:** simplified or chibi faces and plain backgrounds, for example Tamsin's "always cold" joke and Tobin's harpoon.
- **Effects:** use sparingly. Focus lines for shock; glow only for aether and rimeglass.
- **Colour:** a limited palette per scene, with strong value contrast.
- **Characters:** every design stays exactly as on the sheets.
  - Bram has one arm; the LEFT is missing and the sleeve is pinned.
  - Ash is horse-sized, black, with amber eyes and a torn ear.
- **Text:** none in the art.

## 4. Style test before redrawing
Draw three Ch 29 panels in the new style:
- p07: Tamsin writing
- p12: Tobin unveiling the harpoon
- p17: the green ending at the white

Compare them side by side with Ch 1–16 panels. Show the three to Abafa in this chat. If he doesn't answer within an hour, continue.

## 5. Scope
- **Volume 1 (Ch 1–28)** stays as it is.
- **Ch 29 onward** is redrawn in the new style. Ch 29–35 and 46 already have art in the old look.
  - Rebuild each one, reusing the layout files and updating the face boxes for the new panels.
  - Replace the live Ch 29, 30, 31, 32 and 46 on the site.
- **All future chapters** use the new style.

## Website
Claude fixed the reader's Follow mode on main (`read.html`, commit 731052a). Run `git pull --rebase` in `VID\site` before your next push, and don't overwrite `read.html`.
