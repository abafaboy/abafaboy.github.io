# S39 — Fights that read like a real manhwa (4 November 2026)

## Why this exists
The owner reads action manhwa. After watching the chapters 1–20 video he said: "the plot is good, but the fight scenes, body positions are pretty trash ... the fight scenes are especially awful as a manhwa reader." He wants every fight fixed for the chapters 1–30 video.

Five strict audits of every fight in chapters 1–22 found the same faults again and again:
- **Posed bodies.** Fighters stand or crouch square to the camera, symmetrical, with no wind-up and no follow-through. Nib has two stock poses that must never come back: "airplane arms" (both arms flung out sideways) and the "frog jump" (both knees up, fists by his shoulders).
- **The same camera.** Eye level, medium or wide, side-on. Borro's shield block was drawn about eight times from the same side-on spot. Nothing ever comes toward the camera.
- **Small fighters.** The striker is an eighth of the panel at the frame edge. In a 16:9 video he is a few dozen pixels.
- **Crammed beats.** Two or three actions in one panel, so one of them gets lost.
- **Results instead of contact.** Scripts wrote "bursts into ash" and the art drew the aftermath, not the hit.
- **Monsters pose instead of attacking.** Hounds walk in lines and stand on their hind legs at the shield "like dogs at a door".
- **Peaks no bigger than anything else.** `full` came out 1536x1024, the same as `wide`.
- **The lettering hid the hits the art did draw.** XL sound effects sat on the contact point, and system windows sat on action panels. (That part is fixed in the lettering, not by you.)

These rules apply to every fight or action panel you draw from now on: remaster redraws, NEW panels and new chapters. They come on top of the chapter's own style lock: V2 for chapters 1–11, S38 for chapter 12 onward.

## The rules for a fight panel
1. **One action per panel.** At most two figures in focus. A pack or a crowd may stay as dark silhouettes behind them.
2. **A line of action through every fighting body.**
   - Use a strong C or S curve.
   - The weight sits on a named planted foot, or the body is clearly airborne.
   - Every strike gets follow-through.
   - Never square to the camera, never symmetrical, never a vertical straight body.
   - Knees bent in every fighting, landing or bracing pose. Legs follow S36 (the eight leg lines).
3. **Contact is shown; gore is not.**
   - The blow connects on-panel: knife points sparking on stone, a skull hitting the shield's face, jaws closing on a sleeve or on a blade, an arrow punching through a plate.
   - Monsters burst into ash or violet smoke outward from the contact point.
   - People: blood only as a small spray or splash. No wound close-ups, no severed parts. Human deaths stay off-panel or in silhouette.
4. **Change the camera every panel**, never two panels in a row from the same spot.
   - Low or worm's-eye for power, high for a fighter in trouble, over-the-shoulder for a face-off.
   - Extreme close-ups: an eye, a planted foot, a blade edge, a claw.
   - At least one shot per exchange foreshortens something toward the camera (a blade, fist, tusk, claw or arrow). Use a wide lens (18–28 mm) for action.
   - The dutch tilt (10–20°) is drawn INSIDE the picture; the panel frame stays square.
5. **Effects are drawn into the art.**
   - Speed lines along the motion. A radial burst at the contact point.
   - At the peak of a move, drop the background to speed lines, a flat colour or a gradient.
   - Debris and sparks at impacts; a smear or afterimage on the fastest limb.
   - Crisp tapered ink lines, never airbrush blur.
6. **Size.**
   - The figure in focus fills at least a third of the panel height in an action panel, and 60% or more in a peak.
   - Peaks are `tall` (1024x1536) or `bleed`; a peak is never a 1536x1024 wide.
   - Wide shots only at the start of an exchange (geography) or at its end (aftermath).
7. **True heights in every shot.**
   - Nib: 105 cm; his head reaches Jaeha's belt; his head is about 0.74 of Jaeha's.
   - Borro: 2.4 m; Jaeha reaches his chest.
   - Lyra: 182 cm.
   - Monsters keep the size set in their first panel. Put a scale object in monster shots (a door, a car, a person).
8. **Screen direction.** Each fight's board names who stays on the image-left and who on the image-right. Keep it inside the exchange; flip only where the board says.
9. **Borro.**
   - The shield is on his LEFT forearm, always ACROSS the line of the threat (between the attacker and whoever he protects), never standing beside him like a door.
   - In a rear view it is on the IMAGE-LEFT; write "seen from behind, the shield on his LEFT forearm, image-left" in your prompt.
   - Vary his shots: under the shield, over his shoulder, from behind the attacker.
10. **Nib.**
    - Reverse grip on both knives, bare feet; wears his mask where the chapter says.
    - Strikes are a lunge, a dive, a backhand or a cross-slash, with the planted foot named.
    - Show him large enough to read: at least a third of the panel height in his own strikes.
11. **Lyra.**
    - Right-handed: the bow in her LEFT hand, the gloved RIGHT hand drawing to her RIGHT jaw. Facing the camera, she aims image-right.
    - The camera is never aimed up her skirt.
12. **Monsters attack with their whole body:** a stretched leap, a crumple on impact, a recoil, a thrash. Never a line of walkers, never upright on their hind legs at a shield.
13. **Leave the SFX space the row names** (beside the contact, never on it). No text, letters or numbers in the image.
14. **Kang Seoa is 15.** No fan service, no kicks in a skirt, nothing that frames her body.

## How to work a fight panel
1. **Sketch the pose first.** Draw a grey pose sketch of the action (a plain grey mannequin or a sketch in the panel's camera) and check it before you paint:
   - the joints;
   - the limb lengths;
   - the weight and balance;
   - the contact point;
   - the true heights.
   Save the sketch as `chapters_v2/<ch>/art/_pose/<panel>_pose.png`.
2. **Paint the panel from the sketch** in the chapter's style lock, at the row's shape: tall 1024x1536, wide 1536x1024, inset 1254x1254.
3. **Check at 2x:**
   - five digits on every hand (Nib's: four fingers and a thumb);
   - the correct hand holds each weapon;
   - the eight leg lines;
   - the contact is visible;
   - the figure in focus is big enough;
   - nothing is tangled;
   - no text in the image.
4. **In your REVIEW json entry for the panel, record:**
   - `heads`: one box per speaking or important character, in fractions, as before;
   - `contact`: a box `[x0, y0, x1, y1]` around the contact point, in fractions, so the letterer can keep the SFX off it.
