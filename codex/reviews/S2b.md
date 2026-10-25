# S2b: Nib's seal 2/5 look

**Verdict: APPROVED** (Claude, 26 October 2026), after a small cleanup by Claude. Build chapters 3 to 20 on these.

**Delivered by:** the Codex cloud session, commit `fed6a41` on `msgf-art` (`inbox/S2b/`), 25 October 2026, 22:10 UTC.
**Now at:** `characters_v2/nib/` on `msgf-art`:
- `front_seal2_nomask.png`: front view, no mask. His look in the chapter 3 flashback, at home and wherever the script says "no mask".
- `turnaround_seal2.png`: the masked front, left three-quarter and back views.
- `details_seal2.png`: the clasp, the hood lining, the hem with the front opening, and the armhole.
- The entry's notes, renamed: `card_seal2.json`, `prompts_seal2.json`, `DONE_seal2.md`, `SELF_CHECK_seal2.json`, `DELIVERY_MANIFEST_seal2.json`.
- The four rejects are in `characters_v2/_rejects/nib_S2b/`. Never use them.

## What passes
- **Proportions:** they match his approved base sheet (`nib/front.png`) when both are scaled to the same height: head size, belt at 0.42 of his height, hem at 0.70, long arms, long bare feet.
- **Costume:**
  - Every seal-2 change is right: the wall-blue lining #2F4A6E at the open front, the armholes and inside the hood; bronze trim; the bronze clasp disc with the nine-tower sigil (nine towers countable in the detail).
  - Everything else is unchanged: the charcoal sleeveless belted cloak with its pockets, the red scarf, the brass binoculars, the two short knives crossed at the small of his back, bare feet, the arm scars.
- **Side locks:** checked in every view by the house rule (MANHWA_STYLE_GUIDE item 10):
  - the ear notch is on his LEFT ear in the front, three-quarter and back views;
  - the husk mask is over his LEFT eye;
  - the single fang is on his LEFT (picture-right in a front view);
  - his eyes are amber.
- **Style:** it matches the house style and the base sheets: the same line, the same flat colour with one cel shadow.

## What Claude fixed (no redo needed)
1. **The scale silhouettes are gone.** Both full-body sheets had a grey 178 cm man drawn beside Nib at the wrong ratio: 0.70 (front) and 0.67 (turnaround) of the man's height, instead of 105/178 = 0.59. The S2b brief did not ask for a silhouette (his base sheets have none). If left in, a wrong silhouette teaches every later panel to draw Nib about 125 cm tall.
   - Claude painted them out with the sheet's own background colour and grain; nothing else on the sheets changed.
   - **For Nib's height, always use `characters_v2/scale_chart_v2.png`**: his head reaches a 178 cm man's belt.
2. **One stray pixel at the picture-left corner of his mouth** on `front_seal2_nomask.png` (it read as a second fang) was removed. He has one fang, on his LEFT.

The native generator files are kept in git history at `fed6a41`.

## Locked by this sheet (added to `CHARACTER_DESIGNS_v2.md` 2.2)
- The bronze trim runs along the hood edge, the armholes and both edges of the front opening down to the hem.
- The hem itself stays torn and scorched as at seal 1/5: no trim survives on the torn edge. Match this in every panel.
- His face and acting still come from his base `expressions.png`, `acting.png` and `talking.png`. Only the cloak changed.

## How to use it
- With the mask (most of chapters 3 to 20): attach `turnaround_seal2.png`, `details_seal2.png` when the clasp or lining shows, and the base `expressions.png` for the face.
- Without the mask: attach `front_seal2_nomask.png` and the base `expressions.png`.
- He wears the seal 3/5 armour (S21) from chapter 21. Never mix the two looks.
