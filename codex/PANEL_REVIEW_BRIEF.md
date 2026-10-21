# PANEL REVIEW BRIEF: check drawn panels and mark where each character is

This is a looking task. Do NOT generate, edit or move any image. You look at every panel PNG of the chapter named in your task and write two files.
- The letterer uses `REVIEW.json` to point speech-bubble tails at the right character.
- The art chats use `REDRAW.md` to fix broken panels.

Other Codex chats are working at the same time: write only your chapter's `REVIEW.json` and `REDRAW.md`.

## 1. Read first
- `PANEL_BRIEF.md` section 5 (the locks for Nib and Taeo).
- `scripts/chNNN.yaml`: for each panel, its `camera`, `art` and `lines` (who speaks).
- `characters/<id>/turnaround.png` for each character, so you can tell them apart.

## 2. For each `chapters/chNNN/art/P*.png` (skip `END.png`), in order
1. **heads.** For every character whose head is at least partly visible, give a box around the head as `[left, top, right, bottom]`, in fractions of the image width and height, to 2 decimals (0.00 is the left or top edge, 1.00 the right or bottom edge).
   - Key each box by the cast id the script uses in `who` (taeo, nib, chae, minho, and so on).
   - Use `unknown` for a figure you can't identify.
   - Skip background extras unless they speak in that panel.
2. **verdict.** `redraw` if any of these is true, otherwise `ok`:
   - **Anatomy.** A body that couldn't exist: extra or missing arms, legs or fingers that a reader would notice; limbs coming from the wrong place; joints bending the wrong way; a torso or legs far too long or too short; a squashed or stretched figure; a head far too big or too small for the body; bodies merged with each other or with furniture.
   - **Off model.** The wrong character, or a character clearly off model. Check the locks in PANEL_BRIEF section 5: Nib's notched LEFT ear, lower fang, pouch and sheath; Taeo's mole under his RIGHT eye, the olive backpack with the orange patch, and the dark grey phone with the cracked top-left corner.
   - **Text.** Letters, numbers, bubbles or interface drawn into the art.
   - **Wrong content.** The panel doesn't show what the script needs: the wrong action or place, or a speaker the script needs visible is missing.
   Note minor issues in `problems` but keep the verdict `ok`.
3. **problems.** A short list of what is wrong. Leave it empty if nothing is.

## 3. Output
`chapters/chNNN/art/REVIEW.json`, valid JSON, one entry per panel:
```json
{
  "P01": {"heads": {"taeo": [0.42, 0.18, 0.55, 0.40]}, "verdict": "ok", "problems": []},
  "P02": {"heads": {"taeo": [0.10, 0.05, 0.45, 0.60], "nib": [0.62, 0.30, 0.80, 0.55]}, "verdict": "redraw",
          "problems": ["Taeo's left arm comes out of his chest", "torso far too long"]}
}
```
Save it after every 10 panels or so, so a restart can carry on from where it stopped.

`chapters/chNNN/art/REDRAW.md`, one line per panel with verdict `redraw`:
`P02: Taeo's left arm comes out of his chest and his torso is far too long. Redraw: same pose and framing, correct anatomy.`
Write `none` if no panel needs a redraw.

Do not stop to ask anything; finish the chapter.
