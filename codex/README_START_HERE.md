# START HERE (Codex): the rebuild, 25 October 2026

## What changed
- **A new story.** The owner rebuilt *My Summons Go First* from the ground up: a new lead (Kang Jaeha, an F-rank trap-tester), a new cast and a new plot. Only Nib carries over as a character, and he is redesigned. A few old names reappear in new roles (see `bible/NAME_SHEET.md`).
- **Retired work.** The old scripts, the art for old chapters 1–13 and every old character sheet are retired. They stay on disk, but they are never used as references.
- **A new look.** The art style was rebuilt from a direct study of real Korean webtoons. The style is chosen: **V2 · Cinematic cel**.

## Read in this order (laptop paths)

| # | File | What it gives you |
|---|---|---|
| 1 | `bible/STORY_BIBLE_v4.md` | The story: world, powers, cast, arcs, chapters 1–12 |
| 2 | `bible/NAME_SHEET.md` | Exact spellings, file ids, retired names |
| 3 | `MANHWA_STYLE_GUIDE.md` | **The look:** line, light, colour, effects, the V2 style block, the image check |
| 4 | `MANHWA_ART_DIRECTION.md` | **Staging:** panel recipes, action grammar, colour flips, summon colours |
| 5 | `CHARACTER_DESIGNS_v2.md` | **Who looks like what:** cast, monsters, locations, props, all approved by the owner. |
| 6 | `STYLE_TEST_BRIEF.md`, `MODEL_SHEETS_BRIEF.md` or `LOCATION_KEYS_BRIEF.md` | **Your job:** the entry your chat was given |

**Reference, when you need it:**
- `research/RENDERING_STUDY.md`: what real webtoons do, panel by panel.
- `research/ACTING_STUDY.md`: how a real summoner manhwa poses bodies, acts faces and stages talk. Its rules are in the style guide, 6b and 11c.
- `REVIEW_FIXES.md`: Claude's strict review of the first sheets, entry by entry.
- `research/MANHWA_CRAFT_BIBLE.md`: the chapter-writing rules.
- `bible/VISUAL_SURVEY.md`: 103 episode-1s.
- `bible/ART_BIBLE.md`: A5b chibi, A6, A7, A9 (no text in art), A10 (continuity) and Parts B and C still apply.
- `PANEL_BRIEF.md`: sizes by shape, file naming and the anatomy checks still apply.

**Ignore (retired, history only):**
- `bible/STORY_BIBLE.md`, `bible/PART_ONE_BEATS.md`;
- `scripts/`, the old ch001–ch100;
- `chapters/`, the old art;
- everything in `characters/`, including the old `nib/`, `kett/`, `baek/` and `ilan/`;
- `CHARACTER_BRIEF*.md`, `LOCATION_BRIEF.md`;
- `CODEX_SCRIPT_BRIEF.md`, `SCRIPT_WRITER_BRIEF.md`, `SCRIPT_CLARITY_BRIEF.md`, `RECAP_BRIEF.md`, `PANEL_REVIEW_BRIEF.md` and `UI_KIT_BRIEF.md` (written for the old story; new versions will come);
- `STYLE_FIX_BRIEF.md` (its method B choice is folded into the style guide);
- the `SESSIONS_*` and `*_STATE.json` files.

## The job queue

Claude opens the Codex chats on the owner's computer and checks every result. Each chat does one entry and writes only in its own folders.

1. **Now, in parallel chats:**
   - **C1:** two V2 check panels (`STYLE_TEST_BRIEF.md`);
   - **S1–S12:** the model sheets, one chat per character (`MODEL_SHEETS_BRIEF.md`), in a NEW folder `characters_v2/`, never in the old `characters/`;
   - **L1–L5:** the location keys (`LOCATION_KEYS_BRIEF.md`), in `locations_v2/`.
2. **Last:** S13, the scale chart, once S1–S11 are done.
3. **Acting test (A1):** three chapter 1 talk panels (`ACTING_TEST_BRIEF.md`), in `style_test_v2/acting/`, once Jaeha's round 1 fixes are done. Round 2 adds a five-panel dialogue run, P27–P32.
4. **Round 2 fixes** (`REVIEW_FIXES.md`, "Round 2") and **S15, Moon Ahin** (`MODEL_SHEETS_BRIEF.md`), drawn early for the owner's sheets.
5. **Chapter panels:** only after the owner approves the new chapter 1 script. A v2 panel brief comes with it.

## Hard rules for every job
- **No text in the art,** except the single block letter T on Jaeha's vest patch. Emblems without letters are fine; brand logos and wordmarks are not. The letterer adds every word, sound effect and window. Screens that need content are flat #00FF00.
- **No outside images.** Never use real webtoon images as inputs, and never put a real title, studio, artist or character name in a prompt.
- **No old references.** Never use the old cast's sheets or old panels as references.
- **Write only in your job's folder.** Do not edit `bible/`, `research/`, `scripts/` or the briefs.
- **Nothing public.** Do not publish or upload anything.

## Where these files also live
Claude keeps the same files in the GitHub repo `abafaboy/abafaboy.github.io`, branch `msgf-bible`:

| Repo | Laptop |
|---|---|
| `codex/*.md` (the briefs) | the laptop folder's root |
| `STORY_BIBLE_v4.md`, `NAME_SHEET.md`, `ART_BIBLE.md`, `SCRIPT_FORMAT_v2.md` (repo root) | `bible/` |
| `scripts_v2/` (the rebuilt chapter scripts) | `scripts_v2/` |
| `research/` | `research/` (but `VISUAL_SURVEY.md` is in the laptop's `bible/`) |

When a brief names a path like `codex/MANHWA_STYLE_GUIDE.md`, look for the same file name in the laptop folder.
