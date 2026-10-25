# My Summons Go First: the V2 art (branch `msgf-art`)

This branch holds the art. The story, scripts, briefs and designs are on the `msgf-bible` branch; start with `HANDOFF_ABAFADOT.md` there.

**What is here.** Every V2 image that existed on Abafa's laptop when it crashed, copied on 25 October 2026 at about 19:40 Tashkent time. The files are byte-identical to the laptop originals: nothing was resized, converted or re-saved. Abafa chose to keep them on this public repo so Abafadot can reach them.

## The references (approved: build on these)

Use these as references for every new image. Codex drew all of them with its built-in image generation (`image_gen`). Use the same kind of model, and attach the relevant approved sheets to every generation, so the new art matches.

| Folder | What | Status |
|---|---|---|
| `style_test_v2/acting/` | The style and acting tests: the house style (line, colour, rendering, acting) | Approved, the style anchor |
| `characters_v2/<id>/` | The Arc 1 character sheets: `front.png`, `turnaround.png`, `expressions.png`, `details.png`, and where they exist `acting.png`, `talking.png`, `chibi.png` | Approved |
| `characters_v2/scale_chart_v2.png` | Everyone's height side by side | Approved |
| `characters_v2/summon_silhouettes.png` | The summon silhouettes for the chapter 1 flash-forward | Approved |
| `locations_v2/<id>/` | The Arc 1 location keys | Approved |

Characters in `characters_v2/`: `kang_jaeha`, `nib`, `song_yerin`, `mok_hangyu`, `black_hound` (line-up), `husk`, `knight_commander`, `stone_lizard`, `kang_seoa`, `yoo_bomi`, `choi_dongmin`, `kett`, `lyra`, `moon_ahin`. Each sheet's design rules are in `codex/CHARACTER_DESIGNS_v2.md` on `msgf-bible`; when a sheet and the document disagree, ask Claude.

**Never use anything in a `_rejects/` folder as a reference.** Those are failed attempts kept only for the record.

## The chapters

| Folder | What | Status |
|---|---|---|
| `chapters_v2/ch001/art/` | Chapter 1's panels (P08, P25 and P59 are text panels with no art) | Published as an unlisted video. P09, P21 and P22 are to be redrawn: `codex/CH001_FIXES.md` on `msgf-bible` |
| `chapters_v2/ch002/art/` | The only five chapter 2 panels that survived: P01, P08, P16, P23, P30 | Not reviewed yet. Everything else in chapter 2 is still to be drawn |

## Sending new art back for review

1. Put each finished entry in its own folder under `inbox/` on this branch, named after the entry: `inbox/T1/`, `inbox/S2b/`, `inbox/ch002-B/` and so on. Include the PNGs exactly as generated plus the entry's `DONE` file, and for chapter parts the `PROMPTS_<part>.json` and `REVIEW_<part>.json`. Never resize, convert or re-save a PNG.
2. Add one line to `INBOX.md` for each entry: the entry, the date and time, and anything odd.
3. Tell Abafa. Claude reviews every image and writes the verdict to `codex/reviews/<entry>.md` on `msgf-bible`: **APPROVED**, or **REDO** with the exact redo prompt. Approved art moves into `characters_v2/`, `locations_v2/`, `chapters_v2/` and so on; nothing is built on art before its verdict.
