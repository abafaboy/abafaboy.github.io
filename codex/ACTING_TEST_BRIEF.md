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
