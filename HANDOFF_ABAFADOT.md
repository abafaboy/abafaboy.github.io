# Handoff to Abafadot: drawing the art for *My Summons Go First*

**From:** Claude (cloud session), 26 October 2026. **For:** Abafadot, on Abafa's instruction ("if you push everything to github i can prompt my abafadot to organize all the codex work as you want").

**Update, 27 October:** Abafa's laptop works again, so Claude runs Codex there directly and the cloud route is paused. Don't start new entries unless Abafa asks. Everything already delivered to `inbox/` has a verdict in `codex/reviews/`.

**Why you.** Claude writes the story, briefs and prompts, reviews every image strictly, and letters, narrates, renders and uploads the chapters. Codex, on Abafa's laptop, used to draw. The laptop crashed on 25 October and is off until Abafa is back (2 November), so you draw in the cloud and send the results to Claude through GitHub.

**Where things are.**
- **The writing (this branch):** `abafaboy/abafaboy.github.io`, branch `msgf-bible`: briefs (`codex/`), scripts (`scripts_v2/`), designs, bible.
- **The art: branch `msgf-art`** on the same repo. It holds every V2 image from the laptop (copied on 25 October, byte-identical): the approved style tests, the Arc 1 character sheets and location keys, chapter 1's panels and the five surviving chapter 2 panels. Its `README.md` says what each folder is and what is approved. New art comes back through its `inbox/` folder (section 4).
- **The briefs speak of a laptop folder.** Read "this folder" in any brief or prompt as the two branches: `codex/*.md` is what the laptop root held; `STORY_BIBLE_v4.md`, `ARC3_4_BEATS.md`, `ARC5_BEATS.md`, `NAME_SHEET.md`, `ART_BIBLE.md` and `SCRIPT_FORMAT_v2.md` are the laptop's `bible\`; `scripts_v2/` and `research/` are the same; the art folders (`characters_v2/`, `locations_v2/`, `style_test_v2/`, `chapters_v2/`, and later `props_v2/`, `thumbnails_v2/`) are on `msgf-art`.

**Where the season stands.**
- All 40 chapter scripts are written, with narration for each: season one (chapters 1–33, audited and fixed) and Arc 5 (chapters 34–40).
- Chapter 1 is drawn and published as an unlisted video. Three of its panels need redrawing.
- Chapter 2: only P01, P08, P16, P23 and P30 survived. The rest is to be drawn.
- Nothing after chapter 2 is drawn yet. The sheets for Arcs 2–4 come first.
- At chapter 33 the whole season goes up as one public long-form video. Abafa pre-approved that.

---

## 1. Matching the style (the most important rule)

Every new image must look like the approved art, as if the same artist drew it.
- **Same model.** Codex drew everything with its built-in image generation (`image_gen`). Use the same kind of model.
- **Always attach references, at most five per call** (the tool refuses a sixth). Choose them in the order of `codex/PANEL_BRIEF_v2.md` section 2: each acting character's approved sheet, then the location key, then one face or acting sheet if a slot is left; a `style_test_v2/acting/` anchor only if a slot is still free. Never hold an image back because more references could help. The 27 October changes at the top of `codex/README_START_HERE.md` override this file and every brief (no silhouettes on sheets; up to five tries).
- **Never draw from a written brief alone**, and never use anything in a `_rejects/` folder as a reference.
- **Check before you send.** Run each image against `codex/MANHWA_STYLE_GUIDE.md` section 11 and `codex/PANEL_BRIEF_v2.md` section 4b (proportions, scale, camera angle). Claude rejects compressed or small-looking bodies, wrong scale and camera angles that don't match the description.

## 2. The laptop steps don't apply in the cloud

The old instructions to copy files to the laptop and to uninstall Valorant and Rocket League are only for when Codex runs on the laptop again. Skip them.

## 3. The queue, in this order

Work one entry at a time, or several in parallel. Each entry's prompt is written for "one Codex chat per entry"; give the same prompt to whatever runs the drawing.

**3a. The keys and sheets first,** with the prompts in `codex/SESSIONS_TO_OPEN_5.md` (decided 26 October; this order replaces the one in that file):
1. **S2b**, Nib's seal 2/5 look, first. Chapters 3 onward need it. Send it in and wait for Claude's verdict before anything uses it.
2. The rest of **Wave A** (Arc 2: S16–S19, M1–M4, L6–L12; `codex/ASSETS_ARC2_BRIEF.md`). These don't depend on S2b: run them while S2b waits for review.
3. **Wave B** (Arcs 3–4: S20–S25, M5–M9, L13–L20, P1; `codex/ASSETS_ARC3_BRIEF.md`).
4. **Wave C** (Arc 5: S26–S31, M10–M12, L21–L24, P2; `codex/ASSETS_ARC5_BRIEF.md`). S28 needs S24 (Geum) approved and S31 needs S20 (Han Sora) approved.
5. **T1**, the thumbnail key art (`codex/THUMBNAIL_BRIEF.md`), last: it is only needed when the season goes up as one video after chapter 33. Draw it once S21 (Nib's seal 3/5 armour) is approved, with `nib/turnaround_seal3.png`. Never draw Nib for T1 from his base (seal 1/5) sheets.

**3b. The two chapter jobs** (they need only the art already on `msgf-art`):
- **Chapter 1 fixes:**
  > You are chat ch001-FIX for My Summons Go First. Read README_START_HERE.md in this folder and the files in its reading order, then read PANEL_BRIEF_v2.md all the way through and do CH001_FIXES.md exactly (P09, P21 and P22 of chapter 1), writing only the files it lists. Match the surrounding chapter 1 panels in chapters_v2/ch001/art/. When the three panels are done, write DONE_FIX.md and stop. Do not stop to ask anything; finish the job.
- **Chapter 2, parts A to I.** Use this prompt, with X = A, B, C, ... I:
  > You are chat ch002-X for My Summons Go First. Read README_START_HERE.md in this folder and the files in its reading order, then read PANEL_BRIEF_v2.md all the way through and draw part X of chapter 2 from scripts_v2/ch002.yaml, exactly as the "Chapter 2" entry in its section 9 says. P01, P08, P16, P23 and P30 already exist in chapters_v2/ch002/art/: keep them, match them, and do not redraw them unless they fail the checks in MANHWA_STYLE_GUIDE.md section 11 and PANEL_BRIEF_v2.md section 4b. Write only the files section 8 lists for part X. When the part is done, write DONE_X.md and stop. Do not stop to ask anything; finish the job.

**3c. Chapter parts from chapter 3 on.** Start a chapter only when every sheet its rules name (`codex/PANEL_BRIEF_v2.md` section 9) is **APPROVED** in `codex/reviews/`. Use the chapter-part template at the end of `codex/SESSIONS_TO_OPEN_5.md`, one job per part letter. Do the chapters in order (3, 4, 5, ...), and pull `msgf-bible` first: Claude may have fixed the script.

## 4. The review loop with Claude, through GitHub

Claude reviews every image before anything is built on it: proportions and scale, camera angle, the design locks, the house rules. Neither the drawing jobs nor you approve their own work.

1. **Send it.** When an entry is done, commit its output to the `msgf-art` branch in its own folder under `inbox/`:
   - a sheet or key: the entry's whole output folder, as `inbox/S20/` (for example);
   - a chapter part: that part's PNGs plus its `PROMPTS_<part>.json`, `REVIEW_<part>.json` and `DONE_<part>.md`, as `inbox/ch002-B/`. Add any rejects it made in an `_rejects/` subfolder.
   - Never resize, convert or re-save a PNG.
2. **Log it.** Add one line per entry to `INBOX.md` on `msgf-art`: the entry, the time, and anything odd in its `DONE` file. Then tell Abafa; Abafa tells Claude.
3. **Read the verdict.** Claude writes one file per entry on `msgf-bible`: `codex/reviews/<entry>.md`.
   - Each file says **APPROVED**, or **REDO** with each image's id, what is wrong and the exact prompt for the redo job.
   - `codex/reviews/STATUS.md` is the board for everything. Pull `msgf-bible` to see new verdicts.
   - Approved art moves from `inbox/` into its home folder on `msgf-art` (`characters_v2/<id>/`, `chapters_v2/chNNN/art/` and so on). Claude does that, or tells you to.
4. **Redo.** Run the redo job with the prompt from the verdict file and send its output back through `inbox/` the same way.
5. **Built from approved art only.** Claude letters, narrates and renders a chapter once every part of it is approved, and posts it to YouTube as an unlisted preview through Abafa's browser.

## 5. Never

- Never edit the scripts, briefs, designs or bible. If something in them is wrong or impossible to draw, say so in `INBOX.md` and Claude will fix it on `msgf-bible`.
- Never use an image as approved before Claude's verdict says so.
- Never publish or upload anything public beyond the `msgf-art` branch.
- Never delete art: rejects move into `_rejects/` folders.
- Never put the lettering font files (Anime Ace) anywhere online.
- Fan service only ever on adults, never on Kang Seoa (15); Song Yerin stays covered; nothing explicit, and no camera angle up a skirt or at a crotch.

## 6. Who to ask

- Story, art direction or a brief's meaning: Claude, through Abafa.
- The drawing setup and GitHub mechanics: you decide.
