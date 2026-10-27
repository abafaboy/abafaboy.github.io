# H1: hand and arm references (realistic), 28 October 2026

**Why.** After chapters 2 and 3 the owner said the story is "amazing" and the one problem is the hands and arms ("theyre awful"). He asked for "different hand references if needed for realism". This job builds a library of realistic hand and arm references. From now on every panel with a hand doing something specific passes the matching reference (`PANEL_BRIEF_v2.md` section 4c), and every hand fix is drawn against one.

**What these images are.** Anatomy references only. They are realistic on purpose and are never pasted into a panel, so the NEGATIVE BLOCK's "not a photograph" does not apply here. Use no character sheets as references; describe the hands in words.

## Every image
- **1536×1024 PNG, three views of ONE pose side by side:** a three-quarter front view, a side view, and the view a comic panel most often uses for that pose (named per entry).
- **Look:** a realistic studio photograph. Plain mid-grey seamless background, soft even light from the upper left, natural matte skin, short clean nails, no jewellery, no rings, no tattoos. Sleeves pushed above the elbow so the whole forearm shows; show the arm up to the shoulder whenever the arm's position is part of the pose. No faces; crop at the shoulder or chin.
- **Adults only.** A man's hands (lean, about 25) unless the entry says a woman's (slimmer, about 25).
- **Jaeha's gloves:** where the entry says "gloved", the hands wear plain black fingerless gloves that end at the middle knuckle, with all five fingertips bare.

## Check before you keep (up to 3 tries per image)
Crop each hand at 2x and count: five digits per hand, the thumb on the correct side (a RIGHT hand seen palm-down has the thumb on the viewer's left), every knuckle bending the right way, the wrist continuous with the forearm, the elbow where it should be, the upper arm and forearm about the same length, the grip actually wrapping the object, and all three views showing the same pose. No extra, missing or fused fingers anywhere.

## Job H1-A (one chat)
1. `grip_hilt_one_hand.png`: a gloved RIGHT hand gripping a long sword's hilt, blade pointing down and slightly forward; thumb wrapped over the fingers, wrist straight; third view from below, looking up at the fist and guard.
2. `grip_hilt_two_hands.png`: two gloved hands on a two-handed hilt, RIGHT hand just under the guard, LEFT hand below it near the pommel, both forearms in line with the blade, the blade raised across the body; third view over the shoulder.
3. `reverse_grip_knives.png`: a lean man's hands each holding a short knife in reverse grip (blade running down along the outside of the forearm, thumb capping the pommel), elbows bent, fists at chest height; third view from the front at chest height.
4. `notebook_and_pencil.png`: gloved hands. The LEFT hand holds a small open notebook (A6, black cover) at chest height, thumb across the pages; the RIGHT hand writes in it with a yellow pencil held in a normal tripod grip; third view over the writer's right shoulder.
5. `pointing.png`: a RIGHT arm fully extended, pointing with the index finger, the other fingers curled and the thumb resting on the middle finger; third view: pointing at something close, elbow bent at the side.
6. `hand_on_shoulder.png`: one man's RIGHT hand resting on another man's LEFT shoulder from behind, fingers curving over the top of the shoulder; second view from the side; third view: a fist gripping the collar of a hooded jacket at the nape.
7. `phone_hold.png`: a woman's RIGHT hand holding a phone upright, thumb on the screen, little finger under the phone's bottom edge; second view from the side; third view: both hands holding the phone sideways to film.
8. `bow_draw.png`: a woman drawing a recurve bow at full draw. The LEFT arm extended, the hand closed around the grip with the knuckles at about 45 degrees and the wrist straight; the RIGHT hand's first three fingers hook the string at the corner of her jaw, the RIGHT elbow raised level with the shoulder behind her; third view from the front, the bow arm toward the camera.
9. `crossbow_hold.png`: a woman holding a compact black crossbow ready to shoot: the stock against her RIGHT shoulder, the RIGHT hand on the pistol grip with the index finger lying straight along the side above the trigger, the LEFT hand under the fore-end; third view from her LEFT side.

## Job H1-B (one chat)
10. `healing_palms.png`: a woman's two hands held a few centimetres above a man's wounded shoulder, palms toward it, fingers relaxed and slightly apart; second view from the side; third view: one palm pressed flat on the shoulder, fingers curving over it.
11. `shield_grip.png`: a man's LEFT forearm through the arm strap of a heavy rectangular shield, the hand closed on the inner grip, seen from inside the shield; second view from the side; third view: a RIGHT hand resting on the top edge of a tower shield standing on the ground.
12. `fists_and_bracing.png`: a clenched gloved RIGHT fist from the front and from the side (thumb outside the fingers); third view: a hand braced flat on a stone floor with weight on it, fingers spread, elbow slightly bent.
13. `reaching_grabbing_wrist.png`: a RIGHT hand reaching out with the fingers open; second view: that hand gripping another person's wrist (thumb on one side, fingers wrapped on the other); third view: two hands clasped wrist to wrist, one pulling the other up.
14. `mouth_and_strap.png`: a woman's hands: both hands over her mouth in shock (fingertips at the cheekbones); second view: both hands gripping a cross-body bag strap at her chest; third view: one hand pressed to her chest.
15. `holding_cup.png`: a man's RIGHT hand holding a paper coffee cup (fingers around it, thumb opposite); second view from the side; third view: the hand lifting it to the mouth (cup and hand only, no face).
16. `handshake_and_peace.png`: a firm handshake between a man's RIGHT hand and a woman's RIGHT hand; second view from above; third view: a woman's RIGHT hand making a peace sign beside her cheek (no face).
17. `arms_carry.png`: arms only, from the side: one man carrying another over his shoulder (the carrier's arm across the back of the carried man's knees); second view: a man helping an injured man walk, the injured man's arm across his shoulders and the helper's arm around his waist; third view: arms holding a person across the chest from behind.
18. `arms_relaxed.png`: a standing man's arms relaxed at his sides, front and side view, fingertips reaching mid-thigh (a length reference); third view: arms crossed over the chest.

## Files
- `characters_v2/hands/<name>.png` (exactly the names above).
- `characters_v2/hands/prompts.json`: the exact prompt for every kept image and try.
- `characters_v2/hands/INDEX.md`: one line per file: the pose, which characters it serves (Jaeha: 1, 2, 4, 5, 6, 12, 13; Nib: 3; Lyra: 8; Bomi: 5, 7, 8, 16; Sora: 9; Yerin: 7, 10, 14; Mok and Borro: 11, 17; Choi: 15), and how many tries it took.
- `characters_v2/hands/DONE_H1A.md` or `DONE_H1B.md` when your half is finished. Then STOP.

Rejects go to `characters_v2/_rejects/hands_<name>_<try>_<reason>.png`.
