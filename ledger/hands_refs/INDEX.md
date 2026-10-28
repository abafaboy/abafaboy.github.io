# Hand and arm references (index)

Realistic references for hands and arms (`HANDS_REFERENCE_BRIEF.md`, jobs H1 and H2). Pass the matching file as a hand reference whenever a hand grips, points, holds or touches (`PANEL_BRIEF_v2.md` 4c). Take anatomy, grip and pose from them; draw the hand in the house style.

## H1A
Delivered 28 October 2026. Each file is a 1536×1024 PNG with three studio-photograph views. “Calls” counts every tool attempt, including calls that produced no image.
| File | Pose / three views | Serves | Tries |
| --- | --- | --- | --- |
| grip_hilt_one_hand.png | Gloved right hand on downward sword hilt; three-quarter front, side, from below | Jaeha | Kept call 3; 2 images generated; earlier call 1 returned HTTP 429 |
| grip_hilt_two_hands.png | Gloved two-handed raised sword; right hand at guard, left near pommel; three-quarter front, side, over shoulder | Jaeha | Kept call 1; 1 image generated |
| reverse_grip_knives.png | Bare hands on short knives in reverse grip, thumbs over pommels; three-quarter front, side, chest-height front | Nib | Kept call 3; 1 image generated; first 2 calls blocked before output |
| notebook_and_pencil.png | Gloved left hand holds open black A6 notebook with thumb on page; right hand writes with yellow pencil in tripod grip; front three-quarter, side, over right shoulder | Jaeha | Kept call 3; 3 images generated |
| pointing.png | Bare right arm pointing; extended three-quarter front, extended side, close-target bent elbow | Jaeha, Bomi | Kept call 2; 2 images generated |
Every kept hand was cropped at 2× and inspected. The knife study has a minor framing limit: outer elbows meet the frame edges in the front views; the side view shows the full bent elbow. Exact prompts, disk checks, crop coordinates and verdicts are in `prompts_H1A.json`. These are delivered for review; approval remains governed by `reviews/STATUS.md`.

## H1B
Best attempts saved at the three-call limit under README_START_HERE.md, 27 October rule 3. All four need review; none is a complete brief pass. See DONE_H1B.md for exact faults.
- hand_on_shoulder.png — man's right-hand shoulder-rest request, side view and nape collar grip; Jaeha; 3 tries, kept try 3; 1536x1024; resting-hand handedness and arm/idle-hand framing faults.
- phone_hold.png — woman's right-hand upright phone hold, side view and two-hand landscape filming; Bomi, Yerin; 3 tries, kept try 1; 1536x1024; little finger rests on side rather than underneath bottom edge.
- bow_draw.png — woman's left bow arm/right three-finger recurve draw, three-quarter/side/front; Lyra, Bomi; 3 calls, kept try 2 (try 3 HTTP 400); 1536x1024; middle bow hand absent, first bow hand and drawing elbow clipped.
- crossbow_hold.png — woman's right-hand pistol grip and left support, three-quarter/right-side/left-side; Sora; 3 calls, kept try 1 (tries 2–3 HTTP 400); native 1881x836; wrong size, low stock, third-view right index in guard.

## H1C
Five generator-original PNGs, 1536×1024, drawn in order 10–14. Built-in image_gen; no input references. Every kept hand inspected in an individual 2× in-memory crop. Delivery notes and limitations: DONE_H1C.md. Exact prompts, calls, rejection reasons and crop boxes: prompts_H1C.json.
- `healing_palms.png` — Woman's two palms hovering above a wounded shoulder, side view, one palm pressed on shoulder; Yerin; 3 calls (first HTTP 429, then 2 generated tries), kept try 3. Side-view forearm framing limitation noted.
- `shield_grip.png` — LEFT arm strapped into shield and hand on inside grip, side view, RIGHT hand resting on grounded tower shield; Mok and Borro; 2 tries, kept try 2.
- `fists_and_bracing.png` — Gloved RIGHT fist front and side, RIGHT hand braced on stone floor; Jaeha; 2 tries, kept try 2.
- `reaching_grabbing_wrist.png` — RIGHT hand reaching, gripping another wrist, reciprocal wrist grip for pull-up; Jaeha; 2 tries, kept try 2.
- `mouth_and_strap.png` — Woman's two hands over mouth, two hands gripping cross-body strap, RIGHT palm on chest; Yerin; 3 tries, kept try 3. Small centre-view lower-lip/chin edge noted.

## H1D
- `holding_cup.png` — 15: man's right-hand paper-cup grip, side view, lifting to mouth off-frame; Choi; 1 try; 2x hand crops checked.
- `handshake_and_peace.png` — 16: man's/woman's right handshake, steep downward view, woman's right peace sign; Bomi; 3 tries; best retained, center view is oblique rather than perfectly vertical overhead; 2x hand crops checked.
- `arms_carry.png` — 17: shoulder carry, assisted walking, rear chest hold; Mok and Borro; 3 tries; best retained, carry grip sits just above knees and rear hold crosses lower chest/upper abdomen; all seven visible hands checked at 2x.
- `arms_relaxed.png` — 18: front/profile relaxed arms with mid-thigh fingertips, arms crossed with hands on opposite biceps; general adult male arm-length reference (no character assigned in brief); 2 tries; all five visible hands checked at 2x.

## Claude's review (28 October)

All eighteen H1 files are APPROVED as references. Take each one's anatomy and grip; draw the hand in the house style. Notes on six of them:
- `hand_on_shoulder.png`: in the first view the resting hand reads as a LEFT hand. For a RIGHT hand on a shoulder, use the side view (centre) and the collar grip (right).
- `phone_hold.png`: the little finger rests on the side of the phone, not under its bottom edge. Either is fine in a panel.
- `bow_draw.png`: the centre view has no bow hand. Take the bow hand from the left and right views, and the three-finger draw from all three.
- `crossbow_hold.png` (1881×836, a wrong size; kept as drawn): use it for the hands only: the RIGHT hand on the pistol grip, the index finger straight along the side, the LEFT hand under the fore-end. The stock goes into the pocket of her RIGHT shoulder, not low at the chest.
- `handshake_and_peace.png`: the centre view looks down steeply; the handshake itself is the left view.
- `arms_carry.png`: in the shoulder carry the carrier's forearm wraps the thighs just above the knees, which is fine. The rear hold crosses the lower chest.
