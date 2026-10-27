# Hands pass on the scripts (brief for the editors), 28 October 2026

**Why.** After watching chapters 2 and 3, the owner said the story is "amazing" and the one problem is the hands and arms: "theyre awful. sometimes the positions and everything else is awful about arms and hands." Codex draws the panels from the scripts. When a script only says "Jaeha gestures" or "hands clasped", the image model invents the hands, and invented hands are the ones that go wrong. From now on every panel tells Codex what each visible hand does, by side, before it is drawn (`codex/PANEL_BRIEF_v2.md` section 4c).

**Your job.** For every panel of your chapters that has art, decide what each visible character's hands and arms do, in one short line per character, and pick the hand reference that fits. You write a JSON file; Claude merges it into the scripts. **Don't edit the YAML scripts or any other file.**

## Read first
1. The script, `scripts_v2/chNNN.yaml`: for each panel, `art:` (what the panel shows), `camera:` (the framing: what is in frame), `acting:` (per character; some lines already mention hands), `foreground:`, `eyeline:`. Also the chapter's `continuity:` and `cast:` at the top.
2. `codex/PANEL_BRIEF_v2.md`: section 4c (hands and arms) and your chapters' "Chapter N rules" (costumes, bandages, props, who wears what).
3. `codex/CHARACTER_DESIGNS_v2.md`: the designs of the characters in your chapters (search for their names). The hand locks are listed below.

Panels with no art are skipped: `kind: caption`, `kind: title`. The END card (`kind: end`) has art (the chibi gag): include it, as `"END"`.

## The rules
1. **By side, the character's own.** Write "RIGHT hand ...; LEFT hand ..." using the character's own right and left. (Facing the viewer, a character's RIGHT hand is at picture-left. In a back view, picture-left is their LEFT.) You don't need picture positions; their own side is enough.
2. **Only what the camera shows.** Read `camera:` and `art:`. In a face close-up where no hand is part of the beat, write `"none"` for the panel: that tells Codex to keep hands out of the frame (image models like to add a hand to a face). When a character's hands would be at the frame edge and aren't part of the beat, say "hands below the frame" or "out of frame".
3. **Keep hands simple unless the beat is the hand** (4c.3). The easiest hands to draw well: relaxed at the side, in a pocket (if the costume has one), holding a strap, resting on a surface, behind a prop, cropped by the frame. Never invent a busy gesture for a talking head. Avoid a hand or forearm pointed straight at the camera unless the art asks for it.
4. **Match the script; don't change it.** If `art:` or `acting:` names a hand action, keep it and give it a side ("points at the door" becomes "RIGHT arm extended, index finger pointing at the door; LEFT hand at his side"). Never change the story, the camera, the art, the acting or the props. If `art:` and `acting:` disagree about hands, follow `art:` and list the conflict in your report.
5. **Grips.** Say which hand holds what and how: "RIGHT hand grips the sword hilt at her hip, thumb over the guard"; "LEFT hand holds the phone upright, thumb on the screen". Fingers wrap what they hold. A two-handed action must be one both hands can reach.
6. **Continuity across panels.** A prop stays in the same hand from panel to panel unless the script moves it. A weapon is out only when the script has drawn it. Injuries, gloves and bandages stay on the same side (`continuity:` and the chapter rules). Plan whole scenes, not single panels.
7. **Contact.** A hand on a shoulder rests on it with the fingers curving over; a hand that grabs a wrist wraps it (thumb on one side, fingers on the other); a hand braced on the floor is flat with the weight on it.
8. **Non-human hands.** Use the designs (below). Claws, paws and fins are not hands: only write a line for a monster when it holds or grips something, and then name the side ("the bell ringer's RIGHT hand grips the clapper").
9. **Crowds.** For background figures add one key `"background"`: "hands relaxed or out of sight", or what the crowd does with them if it matters (phones up, pointing).
10. **Seoa (15).** Plain everyday hands only (a school bag strap, a phone, a cup, hands on her hips when she scolds). Nothing that draws the eye to her body.
11. **Plain words, one line per character, under about 30 words.** Don't write finger counts for humans (the style block covers that). Do write them for the non-human designs below, every time.

## Hand locks from the designs
- **Kang Jaeha:** black fingerless gloves with grey knuckle pads (all ten fingertips bare) in every outfit unless the chapter rules say otherwise. Exceptions (rulings of 28 October): bare hands from ch 33 P15 (hospital) to the end of ch 33, and in the training look (ch 34–40), as on its approved sheets. Right-handed: he writes with his RIGHT hand, the yellow pencil lives behind his RIGHT ear, the black notebook lives in his LEFT chest pocket and is held in his LEFT hand when open. Check the chapter rules for bandages and plasters (for example ch 13: plasters on both palms, a bite bandage on his LEFT forearm).
- **Nib:** four fingers and a thumb on each hand; long arms by design (his fingertips reach his knees); big bony hands with long fingers and dark nails. Two knives (never three), worn crossed at the small of his back; binoculars. In public he plays a husk: arms hanging stiff, hands limp.
- **Borro:** four fingers and a thumb on each hand; huge blunt-fingered hands; long thick arms reaching his knees. His heavy shield, always on his LEFT side (LEFT forearm through the strap, or his LEFT hand on its edge when it stands). Plays a husk in public like Nib.
- **The Arc 4 crew (Pyo, Dami, Woo, Ho):** bare hands, as on `crew/lineup_kit.png`; only Jaeha wears gloves.
- **Song Yerin:** a healer (glowing palms when she heals: `healing_palms.png`); the pink first-aid bag.
- **Yoo Bomi:** a streamer; her phone (`phone_hold.png`).
- **Lyra:** a right-handed archer: the white longbow in her LEFT hand, the string drawn with her RIGHT hand (a fingered leather glove on the RIGHT hand), a silver bracer on her LEFT forearm, the quiver at her RIGHT hip.
- **Han Sora:** a compact black repeating crossbow, the stock to her RIGHT shoulder, the RIGHT hand on the grip; the brass compass on a chain round her RIGHT wrist until ch 31; a bandage round her RIGHT wrist from ch 32; a new silver compass on her LEFT wrist from ch 34.
- **Moon Ahin:** white fitted gloves; the silver conductor's baton always in her RIGHT hand.
- **Auntie Geum Okran:** her LEFT arm from just above the elbow is a gunmetal prosthetic with three thick metal fingers and a thumb; the long steel ladle always in her RIGHT hand.
- **Pim:** long thin grey-lilac fingers, three and a thumb on each hand.
- **The knight commander:** armoured gauntlets.
- Anyone else: check their design entry for gloves, props and sides.

## Hand references (job H1, realistic photographs in `characters_v2/hands/`)
Pick the one that fits the panel's most demanding hand; two at most. Leave `hand_ref` out when the hands are simple (relaxed, pockets, out of frame).

| File | Pose |
|---|---|
| `grip_hilt_one_hand.png` | one gloved hand gripping a sword hilt |
| `grip_hilt_two_hands.png` | a two-handed sword grip |
| `reverse_grip_knives.png` | short knives held in reverse grip, one in each hand |
| `notebook_and_pencil.png` | notebook in the LEFT hand, writing with a pencil in the RIGHT |
| `pointing.png` | pointing, arm extended or close at the side |
| `hand_on_shoulder.png` | a hand resting on someone's shoulder; a fist gripping a collar |
| `phone_hold.png` | a phone held upright with the thumb on the screen; held sideways to film |
| `bow_draw.png` | a recurve bow at full draw |
| `crossbow_hold.png` | a compact crossbow shouldered, ready to shoot |
| `healing_palms.png` | palms held over a wound; a palm pressed flat on a shoulder |
| `shield_grip.png` | a forearm through a shield's strap; a hand on a standing shield's edge |
| `fists_and_bracing.png` | a clenched fist; a hand braced flat on the floor |
| `reaching_grabbing_wrist.png` | reaching; gripping a wrist; pulling someone up by the wrist |
| `mouth_and_strap.png` | hands over the mouth; hands on a bag strap; a hand on the chest |
| `holding_cup.png` | holding a paper cup; lifting it to drink |
| `handshake_and_peace.png` | a handshake; a peace sign |
| `arms_carry.png` | carrying someone over the shoulder; helping someone walk; holding someone from behind |
| `arms_relaxed.png` | arms relaxed at the sides; arms crossed |

If a hand action recurs in your chapters and nothing here fits (a ladle, a baton, a steering wheel, a keyboard, a gun, hands tied), list it in your report as a missing reference, with the panels.

## What to write
One file per chapter: `/home/claude/msgf-bible/ledger/hands_pass/chNNN.json`, a JSON object with one entry for **every panel that has art**, in panel order:

```json
{
  "P04": {"hands": {"assoc_guard": "only his RIGHT index finger enters from the frame edge, pressing into Nib's cheek; the rest of the hand out of frame"},
          "hand_ref": ["pointing.png"]},
  "P05": {"hands": {"assoc_guard": "RIGHT index finger pokes Nib's cheek, the other fingers curled, thumb on the middle finger; LEFT hand on his belt",
                    "kang_jaeha": "both hands hold the closed folder flat against his stomach, RIGHT hand over LEFT",
                    "choi_dongmin": "RIGHT hand lifts a paper coffee cup to his mouth, fingers round it, thumb opposite; LEFT arm across his stomach",
                    "nib": "arms hanging stiff at his sides, four-fingered hands open and limp (the husk act)"},
          "hand_ref": ["pointing.png", "holding_cup.png"]},
  "P06": "none"
}
```

- Keys inside `hands` are the script's character ids (as in `acting:`), plus `"background"` if needed.
- `"none"` means no hands in frame.
- Write valid JSON (check it with `python3 -m json.tool`). Then run `python3 /home/claude/msgf-bible/tools/merge_hands.py --check NNN` (it reads your JSON and the script and reports missing panels, unknown character ids or reference names; it changes nothing) and fix what it reports.

## Your reply
When all your chapters are done, reply in a few lines per chapter: how many panels have hands, how many are "none", any art/acting conflicts you found (panel and what), and the missing references (the action and the panels).
