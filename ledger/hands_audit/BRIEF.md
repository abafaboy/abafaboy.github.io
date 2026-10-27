# Hands and arms audit (brief for the reviewers)

**Why:** after watching chapters 2 and 3, the owner said (28 October 2026): "the only comment i have is the hands and arms. theyre awful. sometimes the positions and everything else is awful about arms and hands. everything else is amazing." Earlier reviews passed these panels, so look at the art fresh and assume nothing.

**Your job:** look at every panel image in your chapters for problems with **hands and arms only**. Ignore every other kind of problem (faces, props, backgrounds, lettering, story).

## Where things are
- Panels: `/home/claude/msgf-art/chapters_v2/chNNN/art/PNN.png` (and `END.png`). These are the current versions, the ones in the videos. Ignore `_rejects/`.
- What each panel is meant to show: `/home/claude/msgf-bible/scripts_v2/chNNN.yaml`. Find the panel by `id:`. The `art:` and `camera:` fields say who is in it and what their hands are meant to be doing.
- Left and right: a character's LEFT/RIGHT is their own, not the viewer's. Facing the viewer, their right hand is at picture-left. In a back view, picture-left is their left.

## How to look
- Open each panel with the Read tool. For any panel with a visible hand or arm, crop and enlarge the hands and arms before you judge. Write a small Python/Pillow script that saves 2x crops to your own scratch folder (`/tmp/claude-0/hands_audit/<chapter>/`) and Read the crops. A full panel viewed small hides finger and wrist errors.
- The video shows each panel at 2560x1440 with slow pans, so a viewer sees hands clearly. Judge at that size.

## What counts as a problem
1. **Count:** a hand with more or fewer than five digits (thumb included) where all of them should be visible. Fused or melted fingers. A thumb on the wrong side for a left or right hand.
2. **Limbs:** an extra or missing arm or hand. A hand that belongs to nobody. Two hands merged. An arm that starts at the chest, back or neck instead of the shoulder.
3. **Joints:** an elbow or wrist bending the wrong way, or a wrist twisted further than a wrist turns. A "rubber" arm with no elbow, or a broken-looking kink.
4. **Proportion:** forearm and upper arm very different in length. An arm too long or too short (a relaxed arm's fingertips reach about mid-thigh). A hand far too small or big (a hand is about the height of the face, chin to hairline).
5. **Grip and contact:** fingers that don't wrap what they hold. A weapon or prop passing through the hand, floating beside it, or held in a way no one holds it. A hand meant to touch a shoulder or arm that hovers or sinks into it. A two-handed grip where the hands can't both reach.
6. **Pose and acting:** arms in a position a person wouldn't take, or that doesn't read as the action in the script (for example, a "point" that reads as a wave, an arm raised from nowhere, a stiff mannequin arm, an elbow jutting at an impossible angle). Arms that make the figure look broken or puppet-like.
7. **Foreshortening:** an arm pointed at the camera that reads as a stump or a balloon.

Nib (a goblin) also has five digits on each hand (four fingers and a thumb). Borro (a stone giant) has four fingers and a thumb on each hand. Jaeha wears fingerless black gloves; his fingertips still show and still count.

## Severity
- **3:** a viewer notices at video size without looking for it (a wrong finger count on a visible hand, an extra or missing hand, a broken or impossible arm, a floating grip, a pose that reads as wrong).
- **2:** noticeable on a careful look (an odd wrist, an awkward or stiff arm, a hand the wrong size, a weak grip).
- **1:** minor. List it, but it won't be fixed.

## Suggested fix (pick one)
The owner's rule (28 October 2026, "they need to be fixed by codex, you cannot fix them"): **every hand and arm fix is drawn by Codex.** Claude does not paint hands or arms.
- **codex_edit:** Codex regenerates only the hand or arm area and keeps the rest of the panel (a wrong finger count, fused fingers, a weak grip, a hand the wrong size).
- **codex_redraw:** the pose needs a new drawing of the whole panel.
- **crop:** the panel can be cropped or reframed so the bad hand leaves the frame without losing the beat.

For codex_edit and codex_redraw, say in `redraw_note`, in one sentence, what must change, with each hand's job (for example, "his RIGHT hand grips Nib's collar; his LEFT hand braces on the floor").

## What to write
For each chapter, write `/home/claude/msgf-bible/ledger/hands_audit/chNNN.json`: a list with one entry per problem, in panel order.

```json
[{"panel": "P12", "who": "Jaeha", "where": "his RIGHT hand on the notebook, picture-left",
  "problem": "six fingers; the thumb and index are fused", "severity": 3, "fix": "paint",
  "redraw_note": ""}]
```

Also include an entry with `"problem": "clean"` and `"severity": 0` for every panel you checked that has visible hands or arms and no problem, so we can tell checked from skipped. Skip panels with no hands or arms at all, but list their ids in a final entry: `{"panel": "none_visible", "panels": ["P01", "P05"]}`.

Then reply with a short summary: how many panels you checked, how many problems at severity 3 and 2, and the five worst panels with one line each. Don't edit any images and don't change any other files.
