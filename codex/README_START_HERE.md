# START HERE (Codex): the rebuild, 25 October 2026

## Changes on 28 October 2026: hands and arms (these override every brief below)
After watching chapters 2 and 3, the owner said the story, the plot and the characters are "amazing", and that the one problem is the hands and arms: "theyre awful. sometimes the positions and everything else is awful about arms and hands." From now on:
1. **Hands and arms are the first check on every image.** A hand or arm a viewer would notice at video size (a wrong finger count, an extra, missing or fused hand, an arm that doesn't start at the shoulder, an elbow or wrist bending wrongly, a grip that doesn't hold, a pose no body takes) fails the image, however good the rest is. Follow `PANEL_BRIEF_v2.md` section 4c.
2. **Hand references.** Job H1 (`HANDS_REFERENCE_BRIEF.md`) builds realistic hand and arm references in `characters_v2/hands/`. When a panel shows a hand gripping, pointing, touching or doing anything specific, pass the matching hand reference as one of the five references (drop the acting sheet first to make room).
3. **Codex fixes hands; Claude does not paint them.** Hand and arm fixes on existing panels come to you as jobs. A targeted edit of the hand or arm area (crop, edit, composite back at the original pixel size) is the preferred fix when the rest of the panel is approved.

## Changes on 27 October 2026 (these override every brief below)
The first cloud runs stalled on four rules. From now on:
1. **References: at most 5 images per image call** (the tool refuses a sixth). Choose them in the order of `PANEL_BRIEF_v2.md` section 2: each acting character's sheet (the turnaround when the angle matters, else `front.png`), then the location key, then one acting or face sheet if a slot is left. For a sheet entry, once your `front.png` passes, it is your first reference. A `style_test_v2/acting/` anchor is optional and comes last: the approved sheets already carry the house style. **Never hold or skip an image because more references could help.** Pick five by this order and draw.
2. **No 178 cm silhouette on sheets.** Draw every sheet (front, turnaround, views, line-ups) with the character or creature alone on the flat light-grey background, filling the canvas height, with nothing else for scale. Claude adds the silhouette at the exact ratio after review, or makes a separate scale card, so a silhouette drawn at the wrong ratio is no longer a reason to redo. Do check the body's own proportions against the design (head count, arm and leg length, the size of a prop against the body). **Scenes** (a swarm in a tunnel, a pack in an alley, a serpent beside a building) keep a person drawn into the picture for scale, like the tiny figures in location keys.
3. **Up to 5 tries per image.** If it still fails, keep your best try under the normal file name, list its faults in your `DONE` file, and go on with the rest of the job. Only a sheet entry whose `front.png` fails stops there (everything else in it is drawn from the front).
4. **Not reasons to stop or redo:** a faint tone change in a flat background; a size within about 5% of a number in the brief; a detail the brief leaves open. Something small and incidental that would need a sheet that doesn't exist yet (a framed family photo on a shelf, a poster, a crowd) is drawn small and generic, with no reference.

What counts as approved is `reviews/STATUS.md` (on GitHub: `codex/reviews/STATUS.md`) and the verdict files beside it. Never use an image that isn't approved there, and never anything in a `_rejects/` folder.

## What changed
- **A new story.** The owner rebuilt *My Summons Go First* from the ground up: a new lead (Kang Jaeha, an F-rank trap-tester), a new cast and a new plot. Only Nib carries over as a character, and he is redesigned. A few old names reappear in new roles (see `bible/NAME_SHEET.md`).
- **Retired work.** The old scripts, the art for old chapters 1–13 and every old character sheet are retired. They stay on disk, but they are never used as references.
- **A new look.** The art style was rebuilt from a direct study of real Korean webtoons. The style is chosen: **V2 · Cinematic cel**.

## Read in this order (laptop paths)

| # | File | What it gives you |
|---|---|---|
| 1 | `bible/STORY_BIBLE_v4.md` | The story: world, powers, cast, arcs, chapters 1–12 |
| 1b | `bible/ARC3_4_BEATS.md` | Chapters 13–33, beat by beat (read it for any Arc 3–4 entry or chapter) |
| 1c | `bible/ARC5_BEATS.md` | Chapters 34–40, beat by beat (read it for any Arc 5 entry or chapter) |
| 2 | `bible/NAME_SHEET.md` | Exact spellings, file ids, retired names |
| 3 | `MANHWA_STYLE_GUIDE.md` | **The look:** line, light, colour, effects, the V2 style block, the image check |
| 4 | `MANHWA_ART_DIRECTION.md` | **Staging:** panel recipes, action grammar, colour flips, summon colours |
| 5 | `CHARACTER_DESIGNS_v2.md` | **Who looks like what:** cast, monsters, locations, props, all approved by the owner. |
| 6 | The brief your prompt names: `MODEL_SHEETS_BRIEF.md`, `LOCATION_KEYS_BRIEF.md`, `ASSETS_ARC2_BRIEF.md`, `ASSETS_ARC3_BRIEF.md`, `ASSETS_ARC5_BRIEF.md`, `THUMBNAIL_BRIEF.md` or `PANEL_BRIEF_v2.md` | **Your job:** the entry or chapter part your chat was given |

**Reference, when you need it:**
- `research/RENDERING_STUDY.md`: what real webtoons do, panel by panel.
- `research/ACTING_STUDY.md`: how a real summoner manhwa poses bodies, acts faces and stages talk. Its rules are in the style guide, 6b and 11c.
- `REVIEW_FIXES.md`: Claude's strict review of the first sheets, entry by entry.
- `research/MANHWA_CRAFT_BIBLE.md`: the chapter-writing rules.
- `bible/VISUAL_SURVEY.md`: 103 episode-1s.
- `bible/ART_BIBLE.md`: A5b chibi, A6, A7, A9 (no text in art), A10 (continuity) and Parts B and C still apply.
- `PANEL_BRIEF_v2.md`: how chapter panels are drawn (it replaces `PANEL_BRIEF.md`).

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
5. **Acting sheets P1–P6** (`ACTING_SHEETS_BRIEF.md`): body-language poses and dialogue faces for Jaeha, Nib, Yerin, Mok, Lyra and Bomi.
6. **Chapter panels (now):** chapter 1 is finished and the owner approved it. Chapter 2 is drawn in nine parallel parts (`PANEL_BRIEF_v2.md` section 9), into `chapters_v2/ch002/art/`, and every later chapter the same way. Read `PANEL_BRIEF_v2.md` section 4b first: the owner asked for much stricter proportions, scale and perspective.
7. **Arc 2 sheets and keys** (`ASSETS_ARC2_BRIEF.md`: S2b, S16–S19, M1–M4, L6–L12), then **Arcs 3–4 sheets and keys** (`ASSETS_ARC3_BRIEF.md`: S20–S25, M5–M9, L13–L20, P1), then **Arc 5 sheets and keys** (`ASSETS_ARC5_BRIEF.md`: S26–S31, M10–M12, L21–L24, P2). Chapters 3–5 need S2b; chapters 6–12 need the Arc 2 entries; chapters 13–33 need the Arcs 3–4 entries; chapters 34–40 need the Arc 5 entries. A chapter's parts open only when the sheets its rules name are done.

## Hard rules for every job
- **No text in the art,** except the single block letter T on Jaeha's vest patch. Emblems without letters are fine; brand logos and wordmarks are not. The letterer adds every word, sound effect and window. Screens that need content are flat #00FF00.
- **No outside images.** Never use real webtoon images as inputs, and never put a real title, studio, artist or character name in a prompt.
- **No old references.** Never use the old cast's sheets or old panels as references.
- **PNG only, nothing compressed.** Save every image as a PNG straight from the generator, at full size; never JPEG or WebP, never shrink-and-enlarge (`MANHWA_STYLE_GUIDE.md` section 13, check 11b.11).
- **Write only in your job's folder.** Do not edit `bible/`, `research/`, `scripts/` or the briefs.
- **Nothing public.** Do not publish or upload anything.

## Where these files also live
Claude keeps the same files in the GitHub repo `abafaboy/abafaboy.github.io`, branch `msgf-bible`:

| Repo | Laptop |
|---|---|
| `codex/*.md` (the briefs) | the laptop folder's root |
| `STORY_BIBLE_v4.md`, `ARC3_4_BEATS.md`, `ARC5_BEATS.md`, `NAME_SHEET.md`, `ART_BIBLE.md`, `SCRIPT_FORMAT_v2.md` (repo root) | `bible/` |
| `scripts_v2/` (the rebuilt chapter scripts) | `scripts_v2/` |
| `research/` | `research/` (but `VISUAL_SURVEY.md` is in the laptop's `bible/`) |

When a brief names a path like `codex/MANHWA_STYLE_GUIDE.md`, look for the same file name in the laptop folder.
