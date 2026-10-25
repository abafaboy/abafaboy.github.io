# ACTING TEST BRIEF: three chapter 1 talk panels in style V2 (one Codex chat)

**Why.** The owner's verdict on the last manhwa was that body positions, emotions and dialogue panels looked unnatural and AI-made. Claude studied a real summoner manhwa (`research/ACTING_STUDY.md`) and wrote acting rules (`MANHWA_STYLE_GUIDE.md` 6b, 10.5 and 11c). The chapter 1 script now names the acting for every panel. This test checks that the rules produce panels that act like real manhwa before the whole chapter is drawn.

**When.** Start only when `characters_v2/kang_jaeha/DONE.md` has a "Round 1 fixes" section. Jaeha's corrected sheet is a reference here.

## Read first
- `README_START_HERE.md`.
- `MANHWA_STYLE_GUIDE.md`:
  - 6b (acting and staging);
  - 10 (prompt order) with 10.1 the STYLE BLOCK, 10.2 the recipe lines, 10.3 the NEGATIVE BLOCK, 10.4 the CLEAN-UP LINE and 10.5 the ACTING LINES;
  - 11, 11b and 11c (the checks).
- `CHARACTER_DESIGNS_v2.md`: the prompt snippets in section 8, word for word.
- `SCRIPT_FORMAT_v2.md`: what `acting`, `eyeline` and `foreground` mean.
- `scripts_v2/ch001.yaml`: panels P11, P23 and P28.

## References you may pass
- **Characters:** `characters_v2/<id>/front.png` and `expressions.png` for each character in the panel. For the two background hunters in A2, use `black_hound/lineup.png`.
- **Places:** `locations_v2/gate0912_site/key.png` (A1), `locations_v2/boss_room/door.png` (A2) and `locations_v2/gate0912_fortress/key.png` (A3).
- **Never:** anything in the old `characters/` folder, or any real webtoon image.

## The three panels (all 1536×1024)

| File | Panel | What it tests |
|---|---|---|
| `A1_P11.png` | P11, `talk`: over Jaeha's shoulder toward Mok | the over-the-shoulder crop, Mok's weight shift and his shooing hand, a lazy grin with cold eyes, two hunters busy with their own gear |
| `A2_P28.png` | P28, `talk`: Mok's shield nudging Jaeha toward the door | bodies touching and pushing, Jaeha's placating hands and his eyes sliding up to the lamp, two hunters sharing a look behind |
| `A3_P23.png` | P23, `name-card`: Yerin against the cracked wall | shock in the whole body, eyeline to someone off-panel, the right third left calm for the name card |

## How to build each prompt
Follow the order in style guide section 10:
1. the STYLE BLOCK, then the CLEAN-UP LINE;
2. the recipe line;
3. the panel's `camera`, `light` and `art`;
4. its `acting`, `eyeline` and `foreground`, word for word, then the reference sentence from 10.5;
5. the snippet of every character in the panel;
6. the NEGATIVE BLOCK.

Two further rules:
- **No lettering.** Draw no bubbles or text; leave the `calm` area empty. The T on Jaeha's vest patch is the only letter allowed.
- **Locks.** Keep every lock from `CHARACTER_DESIGNS_v2.md`: Jaeha's fringe over his LEFT eye, the pencil behind his RIGHT ear, the notebook in his LEFT chest pocket.

## Checks
- Run sections 11, 11b and 11c on every image. Redo an image up to 3 times.
- Put each reject in `style_test_v2/acting/_rejects/` with the reason in its file name.

## Deliverables (in `style_test_v2/acting/`)
- `A1_P11.png`, `A2_P28.png` and `A3_P23.png`.
- `PROMPTS.json`: the exact prompt and reference files for every kept image and every reject.
- `REPORT.md`. For each panel:
  - which 11c checks passed on the kept image;
  - what failed in each reject;
  - whether any character drifted toward their model sheet's standing pose (11c.8), and what fixed it.

Then STOP. Write only in `style_test_v2/acting/`.

---

## Round 2 (25 October, night): Claude's review and the next test

**The owner's words, the same night:** "remember about the faces and emotions and body language and dialog face movements." The style guide now has three more face rules (6b Faces 8–10: talking mouths, the face moves with every line, listeners react), a left/right rule (11b.10) and three more acting checks (11c.9–11). Read them first.

### Claude's verdict on round 1
- **A3 / P23 passes.** Keep it as it is.
- **A1 / P11 fails three strict checks**, although the acting itself is good (keep the poses, the crop, the shooing hand, the grin and both hunters):
  1. 11b.1: Jaeha's orange vest and grey hoodie sleeve are covered in translucent diagonal shards. Repaint them flat, with a few large opaque shadow shapes, as clean as `kang_jaeha/front.png`.
  2. 11c.11: Mok's tower shield floats behind him. It is slung on his back: show a thick black strap running diagonally across his chest from his right shoulder to his left hip, and the top of the shield behind his right shoulder.
  3. 11b.4: Mok's sword is a bare blade dangling from a thigh strap. It is sheathed in its black scabbard with the steel tip, hanging from his belt, as in `mok_hangyu/details.png`.

  Make one targeted edit of the kept `A1_P11.png` (pass it as the edit target) and change only those three things.
- **A2 / P28 is restaged.** The shield-nudge grip failed four times, so the script changed (`scripts_v2/ch001.yaml`, P28, re-read it): the door is at picture-right; Mok steps in behind Jaeha and steers him with his right hand clamped on Jaeha's near shoulder, leaning over him, chin jerked at the door, camera smile with the mouth open mid-line; his tower shield stands on its bottom edge at his left side with his left hand resting on its top. Jaeha faces the door, so we see his RIGHT side: the pencil behind his right ear shows and the fringe hides his far (left) eye. He leans back against the push with his palms out, head tipped back so his visible right eye rolls up to the red lamp, a strained smile and a sweat drop. Draw it fresh.

### New: a dialogue run, P27 to P32 (faces that move with the talk)
This tests what the owner asked for: faces, emotions, body language and the face changing line by line across one conversation. Draw these five panels in script order, at the sizes below, as one continuous exchange in the same light and on the same side of the action (the door always at picture-right):

| File | Panel | Size | What it tests |
|---|---|---|---|
| `B1_P27.png` | P27, low angle on Mok, his name-card panel | 1536×1024 | Mok's big fake camera smile, mouth open mid-line, thumb jabbing at the door; the left third calm |
| `B2_P28.png` | P28 as restaged (the same image as the new A2) | 1536×1024 | the push, Jaeha's placating hands and eyes up, Mok talking, the listeners' shared look |
| `B3_P29.png` | P29, close on Jaeha | 1024×1024 | the frozen polite smile with one corner twitching, sweat, eyes rolled up to the lamp; mouth open on his line |
| `B4_P31.png` | P31, low, Mok shoving with the shield | 1536×1024 | Mok's smile gone, flat dead eyes, the shield lifted on his arm and driven into Jaeha's back; Jaeha stumbling |
| `B5_P32.png` | P32, extreme close-up of Jaeha's eyes in profile | 1536×512 | the polite mask gone: narrowed eyes measuring the door (his right eye; the fringe stays over his left) |

Then stack the five, in order, into one vertical strip, `B_sequence.png`, 800 px wide with 40 px white gaps, so the run can be read like a phone scroll. Across the run, check that each character's face and head angle change from panel to panel (11c.10) and that the speaker's mouth is open on every line (11c.9).

### Checks and limits
- Run 11, 11b and 11c on every image; up to 3 tries per image.
- Rejects go to `style_test_v2/acting/_rejects/` with the reason in the file name.
- Update `PROMPTS.json`, `REPORT.md` (add a "Round 2" section with the same per-panel tables) and `PROGRESS.md`.

Then STOP. Write only in `style_test_v2/acting/`.
