# Hands and arms fixes: chapter 10

From Claude's audit of 28 October 2026 (`ledger/hands_audit/ch010.json`). **3 panels to fix** (1 problems at severity 3, 1 at severity 2, 1 at severity 1). How to fix them: `codex/HANDS_FIX_BRIEF.md`. Base images: `chapters_v2/ch010/art/hands_fix/base/`.

## P17: edit (severity 1)
- **Jaeha**, his LEFT (bandaged) hand presenting the tarp palm up, picture-right (x 1000-1110, y 410-490 of 1536x1024): only the thumb and three thin stacked fingers show; it still reads as an open presenting hand at video size. His RIGHT hand on the cup and Borro's hanging hands are fine
  - **Fix:** Jaeha's LEFT hand presents the tarp palm up with four fingers and the thumb visible, while his RIGHT hand holds the coffee cup at his mouth.
- **References:** `characters_v2/hands/reaching_grabbing_wrist.png`, `characters_v2/kang_jaeha/details.png`

## P36: edit (severity 3)
- **Jaeha**, his second arm, the one with its hand on Borro's arm, picture centre-left (x 470-640, y 370-430 of 1536x1024): seen from behind, both of his arms grow out of his RIGHT side: the pencil arm from his right shoulder and a second arm from under his right armpit at mid-ribs, stacked like two right arms, with no arm on his LEFT side; read as his LEFT arm reaching across his chest it would be about one and a half times too long (shoulder to wrist ~265 px against a head ~69 px tall). The hands themselves (pencil hand, flat hand on Borro's arm) and everyone else's hands (Yerin's two glowing hands, Borro's fists, Nib's hands on his knife) are fine
  - **Fix:** Jaeha's RIGHT arm keeps pointing the pencil along the beam from his right shoulder; remove the arm growing from under his right armpit and draw his LEFT arm from his LEFT shoulder (picture-left side of his back), reaching across in front of his chest so his LEFT hand rests on Borro's forearm at a normal arm's length, with Borro's forearm close beside him.
- **References:** `characters_v2/hands/pointing.png`, `characters_v2/hands/hand_on_shoulder.png`, `characters_v2/kang_jaeha/details.png`

## P41: edit (severity 2)
- **Nib**, his RIGHT hand stretched out for balance, picture-left edge (x 10-165, y 250-370 of 1536x1024): the clawed hand shows only two fingertips and the thumb; the other two fingers are hidden behind the top finger with only knuckle ridges showing, so on a careful look it reads as a three-digit claw. His LEFT hand (picture-right) and both arms are fine
  - **Fix:** Nib's RIGHT hand stays spread like a claw for balance with all four long fingers and the thumb clearly visible, matching his LEFT hand.
- **References:** `characters_v2/hands/reaching_grabbing_wrist.png`, `characters_v2/nib/details.png`

## Left out of this job (redrawn by another job, or judged not worth a fix): P38

Panels that passed: P01, P03, P05, P07, P09, P15, P16, P18, P19, P20, P22, P23, P24, P25, P26, P27, P28, P30, P34, P35, P37, P39, P40, P42, P43, P44, P45, P46, P47, P49, P50, P51, P52, P53, P54, P55.
