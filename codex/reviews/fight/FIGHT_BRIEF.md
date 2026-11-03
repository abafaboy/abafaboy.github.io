# Fight-scene audit and re-storyboard: My Summons Go First

## Why
"My Summons Go First" (MSGF) is the owner's manhwa, published as a recap video on YouTube (16:9, one narrator, the lettered strip scrolling past; each panel is on screen for about 3–6 seconds). An image model (Codex) draws every panel from a script. The owner, a long-time manhwa reader, watched the chapters 1–20 video and said: **"the plot is good, but the fight scenes, body positions are pretty trash ... the fight scenes are especially awful as a manhwa reader."** He wants the fights fixed for the next long video (chapters 1–30).

A separate review already listed broken anatomy panel by panel (extra limbs, wrong sizes); a fix job is repairing those. **Your job is different: judge each FIGHT SEQUENCE as a whole, the way a reader of Solo Leveling, Omniscient Reader's Viewpoint, Eleceed or The Breaker would, then re-storyboard it** so the fight can be redrawn properly.

## What I (the main session) already saw in chapter 11 (Market Break), as a calibration
- Bodies are posed, not fighting: stiff standing or crouching "for the camera", no line of action, no wind-up, no follow-through.
- The camera stays at eye level and medium or wide distance; little foreshortening; the action is small and far away.
- Hits never visibly land: the moment of contact is replaced by debris and a giant SFX.
- SFX do the work the drawing should do: huge identical white letters (KRASH KRASH KRASH, SHK SHK SHRAKK, BOOM BOOM BOOM) laid across the action, often covering the fighter.
- Few speed lines or impact bursts in the art itself; the detailed background stays during the hit.
- Choreography doesn't read: wide establishing shots in the middle of the action, cuts between characters with no action-reaction chain, tangled bodies (P51 "WHAM": Nib flat on his back under a hound, unreadable).
- System windows (cooldown timers) sit on top of the action beats.
Confirm or correct this for your chapters; do not assume it.

## The standard (a manhwa reader's checklist for a fight)
1. **Choreography reads as cause and effect.** Every panel shows ONE action; the next shows its result. A reader can narrate every beat ("Nib ducks under the claw / his knife flashes up / the jaw snaps on air / the hound crashes past him").
2. **Beat rhythm.** Anticipation (small or thin panel) → strike (big) → impact (biggest, tilted) → reaction → aftermath. Quick beats get small panels; key blows get large or tall panels. 1–3 peak panels per chapter.
3. **Camera changes every panel.** Low angle for power, high angle for a fighter in trouble, dutch tilt for chaos, over-the-shoulder for a face-off, extreme close-ups (eyes, fist, blade edge, a foot planting). Foreshortening toward the camera: a fist, blade, claw or arrow coming AT the reader.
4. **Bodies have a line of action and weight.** A strong C or S curve through the body; the weight shifted onto a planted foot or clearly airborne; follow-through after every strike; balance obeys gravity. Never a straight, vertical, square-to-camera body in an action panel.
5. **Contact is shown.** In the impact panel the blow connects: blade sparks on a claw, a fist meets a shield, a shoulder slams into a chest, an arrow punches through armour. Platform-safe: no gore close-ups; blood is a spray or a splash.
6. **Effects are drawn into the art.** Speed lines along the motion, radial impact bursts at the contact point, the background dropped to speed lines, a flat colour or a gradient at the peak of a move, debris, sparks, motion smears, afterimages.
7. **Clarity.** At most two fighters in focus in an action panel; readable silhouettes; no tangles; consistent screen direction (180-degree rule) within an exchange.
8. **SFX support, never cover.** One SFX per impact, angled along the motion, placed beside the contact point, never over a face or the key limb. Most drawn beats need a small SFX or none.
9. **No system windows on top of key action beats**: put them on a reaction or a quiet panel before or after.
10. **The MC reads the fight.** Jaeha (F-rank, the summons fight for him) gets short reaction or eyes panels between beats, showing calculation, not just fear.
11. **Video format.** The strip is scaled to fit a 1920x1080 frame, so a wide panel shows its figures small. A fight needs tall panels, close-ups and large figures; long wide shots belong only at the start (geography) or the end (aftermath).

## What you have
- **The lettered pages as the video shows them:** `/home/claude/work/judge/chNNN_final/page_NN_Pxx-Pyy.jpg` (1080 px wide), with `index.md` mapping pages to panels. Look at every page of each fight in order. Make your own contact sheets with Python/PIL (for example 4–6 pages side by side at about 360 px wide) in your own folder `/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/fight/<your range>/`; read crops of the originals when you need detail.
- **Original art (read-only):** `/mnt/user-data/uploads/Videos/MySummonsGoFirst/chapters_v2/chNNN/art/PNN.png`.
- **Scripts:** `/home/claude/msgf-bible/scripts_v2/chNNN.yaml`. Each panel has `recipe` (talk, impact, anticipation, splash, aftermath, reaction, insert...), `shape` (wide, tall, inset-l/r, strip, full), `camera`, `art`, `acting`, `hands`, `lines` (dialogue), `sfx`, `ui` (system windows). Use these to find the fights and to keep the story and dialogue.
- **Designs and rules:** `/home/claude/msgf-bible/codex/CHARACTER_DESIGNS_v2.md` (looks, heights, weapons) and `/home/claude/msgf-bible/codex/MANHWA_ART_DIRECTION.md` (the recipe table and the existing action rules; note its rule 7 "violence happens between panels", which may be one reason the fights never show a hit; say whether to drop it).
- Fixed facts: Nib is a 105 cm wiry goblin, two knives, arms to his knees, barefoot; Borro a 2.4 m giant with a stone shell, a blank mask and a shield on his LEFT arm (Jaeha reaches his chest); Lyra 182 cm, right-handed archer (bow in her LEFT hand, gloved RIGHT hand draws to her RIGHT jaw; facing the camera she aims image-right; the camera is never aimed up her skirt); Jaeha 178 cm, F-rank trap-tester, barely fights early. Kang Seoa is 15: never fan service.

## Deliverable, per chapter
1. **The fight sequences** in the chapter: each with its panel range, one line on what happens, and a **grade out of 10** as a seasoned manhwa reader would give it.
2. **For each sequence, what is wrong**, panel by panel where it matters (cite what you saw: "P51: Nib flat on his back, the hound on top, limbs tangled; you cannot tell who is biting whom").
3. **A new storyboard for each sequence graded below 8**, as a table:
   `| new | replaces | shape | camera | action (who does what: line of action, weight, which hand/foot, the contact point) | effects in the art | SFX (text, where) | dialogue kept |`
   - Keep the same story events, outcome and dialogue lines (you may move a line to a better panel). You may add or cut panels, at most about 30% more than now.
   - Write every panel so an AI image model can draw it: ONE clear action; at most two figures in focus (a crowd or a pack can stay a blurred silhouette behind); explicit camera and lens (for example "worm's-eye, wide lens, Nib's knife hand foreshortened toward the camera"); explicit limbs (which hand holds which knife, which foot is planted); the contact point; the background treatment (speed lines / flat red / detailed). Avoid what image models fail at: tangles of bodies, interlocking hands, more than three figures doing different actions, text in the image.
   - Mark panels to KEEP as they are (good enough), REDRAW, CUT or NEW.
4. **Patterns** across your chapters (for example "every impact is a wide shot", "Borro is always drawn standing square").

## Rules
Read-only: do not modify, move or delete anything outside your own folder. Do not use remote-device, computer-use, browser or network tools; do not contact anyone. Writing markdown files may be refused for subagents: **return your whole deliverable as text in your final reply** (that is what gets used), and keep it complete: every sequence, every storyboard row. Delete your contact sheets when you finish.
