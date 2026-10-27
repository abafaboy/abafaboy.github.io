# My Summons Go First: the V2 art (branch `msgf-art`)

This branch holds the art. The story, scripts, briefs and designs are on the `msgf-bible` branch; start with `HANDOFF_ABAFADOT.md` there.

**What is here.** Every V2 image that existed on Abafa's laptop when it crashed, copied on 25 October 2026 at about 19:40 Tashkent time. The files are byte-identical to the laptop originals: nothing was resized, converted or re-saved. Abafa chose to keep them on this public repo so Abafadot can reach them.

## The references (approved: build on these)

Use these as references for every new image. Codex drew all of them with its built-in image generation (`image_gen`). Use the same kind of model, and attach the relevant approved sheets to every generation, so the new art matches.

| Folder | What | Status |
|---|---|---|
| `style_test_v2/acting/` | The style and acting tests: the house style (line, colour, rendering, acting) | Approved, the style anchor |
| `characters_v2/<id>/` | The Arc 1 character sheets: `front.png`, `turnaround.png`, `expressions.png`, `details.png`, and where they exist `acting.png`, `talking.png`, `chibi.png` | Approved |
| `characters_v2/nib/*_seal2*` | Nib's seal 2/5 look (S2b, approved 26 Oct): `front_seal2_nomask.png`, `turnaround_seal2.png` (with the mask), `details_seal2.png`. Chapters 3 to 20 use these (he wears the seal 3/5 armour from chapter 21); his face and acting still come from his base `expressions.png` and `acting.png`, his height from the scale chart | Approved |
| `characters_v2/borro/`, `characters_v2/baek_taegun/` | Borro (S16, all five sheets) and Director Baek (S17), approved 27 Oct | Approved |
| Arc 2 sheets | `neighbourhood` (S18), `ahin_husk` (S19), `ash_rat` (M1, with the redrawn swarm), `drowned_hound` (M2), `ash_hound` (M3), `marsh_serpent` (M4), approved 27 Oct. Creatures carry Claude's `scale_card.png` (beside the standard 178 cm man) | Approved |
| Arcs 3–4 sheets | `han_sora` (S20), Nib's seal 3/5 armour `nib/*_seal3*` (S21), `oh_minseok` (S22), `crew` (S23), `geum_okran` (S24), `arc3_cast` (S25), `training_construct` (M5), `basalt_boar` (M6), `bell_ringer` (M7), `canyon_wyvern` (M8), `tide_warden` (M9) and `props_v2/arc3` (P1), approved 27 Oct, with Claude's scale cards for the monsters, Sora and Auntie Geum | Approved |
| Arc 5 sheets | Jaeha's `kang_jaeha/*_training*` (S26), `arc5_cast` (S27), Lyra's and Moon Ahin's beach looks (S30), `brine_crawler` (M10), `reef_hermit` (M11), `deep_lantern` (M12), `pim/front.png` (S29, the rest to draw) and `props_v2/arc5` (P2), approved 27 Oct | Approved |
| Arcs 3–5 keys | L13–L24 in `locations_v2/`, approved 27 Oct, except `dam_gate/key.png` and `farm_pit/key.png` and `alarm.png` (being redrawn) | Approved |
| `locations_v2/` new keys | Arc 2 keys approved 27 Oct: `sewer_gate`, `survey_gate`, `hanriver_gate`, `carpark_gate`, `call_void`, `tower_gate` (key only), `mangwon_market`, `fish_market`, `kanghan_office`, `bomi_room` (outside), `kanghan_guild_hall`, `rooftop_room/stairs_night.png` | Approved |
| `deliveries/<entry>/` | Every reviewed delivery exactly as it came in, with its rejects and notes (provenance only; build on the approved copies) | Archive |
| `characters_v2/scale_chart_v2.png` | Everyone's height side by side | Approved |
| `characters_v2/summon_silhouettes.png` | The summon silhouettes for the chapter 1 flash-forward | Approved |
| `locations_v2/<id>/` | The Arc 1 location keys | Approved |

Characters in `characters_v2/`: `kang_jaeha`, `nib`, `song_yerin`, `mok_hangyu`, `black_hound` (line-up), `husk`, `knight_commander`, `stone_lizard`, `kang_seoa`, `yoo_bomi`, `choi_dongmin`, `kett`, `lyra`, `moon_ahin`. Each sheet's design rules are in `codex/CHARACTER_DESIGNS_v2.md` on `msgf-bible`; when a sheet and the document disagree, ask Claude.

**Never use anything in a `_rejects/` folder as a reference.** Those are failed attempts kept only for the record.

## The chapters

| Folder | What | Status |
|---|---|---|
| `chapters_v2/ch001/art/` | Chapter 1's panels (P08, P25 and P59 are text panels with no art) | Published as an unlisted video. P09, P21 and P22 redrawn and approved 27 Oct (`codex/reviews/ch001-FIX.md`), for the long-form |
| `chapters_v2/ch002/art/` | Chapter 2's panels: all 60 images | Approved (P52 fixed by job ch002-R6, `codex/reviews/ch002.md`) |
| `chapters_v2/ch003/art/` | Chapter 3's panels: all 62 images | Approved (P33, P45, P49 redrawn by job ch003-R1; Claude fixed Nib's RIGHT ear and mask edge on P45; `codex/reviews/ch003.md`) |
| `chapters_v2/ch004/art/` | Chapter 4's approved panels so far: 51 of parts A–C and E–H | P03 is being redrawn (job ch004-R1); part D is being drawn |
| `chapters_v2/ch005/art/` | Chapter 5's approved panels: 58 of 59 | P35 is being redrawn (job ch005-R1) |
| `chapters_v2/ch006/art/` | Chapter 6's approved panels: 57 of 60 images | P41, P51 and P54 to be fixed (job ch006-R1, `codex/reviews/ch006.md`); P59 carries Claude's screen look |
| `chapters_v2/ch009/art/` | Chapter 9's approved panels so far: 42 (parts A, C, E, F, G; Claude fixed P09, P41, P49) | P50 to be redrawn (job ch009-R1); parts B and D still to draw (`codex/reviews/ch009.md`) |
| `chapters_v2/ch010/art/` | Chapter 10's approved panels so far: 45 (parts A, C–G; Claude fixed P20, P27, P41, P42) | P48 to be redone (job ch010-R1); part B to draw; parts H and I in progress (`codex/reviews/ch010.md`) |

## Sending new art back for review

1. Put each finished entry in its own folder under `inbox/` on this branch, named after the entry: `inbox/T1/`, `inbox/S2b/`, `inbox/ch002-B/` and so on. Include the PNGs exactly as generated plus the entry's `DONE` file, and for chapter parts the `PROMPTS_<part>.json` and `REVIEW_<part>.json`. Never resize, convert or re-save a PNG.
2. Add one line to `INBOX.md` for each entry: the entry, the date and time, and anything odd.
3. Tell Abafa. Claude reviews every image and writes the verdict to `codex/reviews/<entry>.md` on `msgf-bible`: **APPROVED**, or **REDO** with the exact redo prompt. Approved art moves into `characters_v2/`, `locations_v2/`, `chapters_v2/` and so on; nothing is built on art before its verdict.
