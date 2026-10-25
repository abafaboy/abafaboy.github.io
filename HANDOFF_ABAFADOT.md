# Handoff to Abafadot: running the Codex art work for *My Summons Go First*

**From:** Claude (cloud session), 26 October 2026. **For:** Abafadot, on Abafa's instruction ("if you push everything to github i can prompt my abafadot to organize all the codex work as you want").

**Why you.** Claude writes the story, briefs and prompts, reviews every image strictly, and letters, narrates, renders and uploads the chapters. Codex, on Abafa's laptop, draws. Claude normally drives Codex through a link to the laptop, but that link has been down since the laptop crashed on 25 October. Until it is back, you run the Codex side and send the results to Claude through GitHub.

**Where things are.**
- **This branch:** `abafaboy/abafaboy.github.io`, branch `msgf-bible`. It holds everything Codex needs: briefs, scripts and designs.
- **Laptop project folder:** `C:\Users\abafa\Videos\MySummonsGoFirst`.
- **Codex:** the Codex app's project "My Summons Go First" ("This computer", Full access).

**Where the season stands.**
- All 33 chapter scripts are written, audited and fixed, with narration for each.
- Chapter 1 is drawn and published as an unlisted video. Three of its panels need redrawing.
- Chapter 2 is half drawn.
- Nothing after chapter 2 is drawn yet. The sheets for Arcs 2–4 come first.
- At chapter 33 the whole season goes up as one public long-form video. Abafa pre-approved that.

---

## 1. Sync this branch to the laptop

Do this once now, and again before you open any chat for a new chapter. Overwrite the old copies; never delete art.

| From this branch | To the laptop folder |
|---|---|
| `codex/*.md` | the folder's **root** (`README_START_HERE.md`, `PANEL_BRIEF_v2.md`, `CHARACTER_DESIGNS_v2.md`, `ASSETS_ARC2_BRIEF.md`, `ASSETS_ARC3_BRIEF.md`, `THUMBNAIL_BRIEF.md`, `SESSIONS_TO_OPEN_5.md`, `CH001_FIXES.md`, ...) |
| `STORY_BIBLE_v4.md`, `ARC3_4_BEATS.md`, `ARC5_BEATS.md`, `NAME_SHEET.md`, `ART_BIBLE.md`, `SCRIPT_FORMAT_v2.md` | `bible\` |
| `scripts_v2\*.yaml` | `scripts_v2\` |
| `research\*` | `research\` |

Never touch the art folders on the laptop: `characters_v2\`, `locations_v2\`, `props_v2\`, `thumbnails_v2\`, `chapters_v2\` and `style_test_v2\`. `tools\`, `recaps_v2\` and `ledger\` are Claude's and don't need copying.

## 2. Disk space

The laptop's disk was nearly full. Abafa authorised uninstalling **Valorant** and **Rocket League** ("I can always just reinstall the game without losing anything").
- Use each game's own uninstaller: the Riot Client for Valorant, which also offers to remove Vanguard; the Epic Games Launcher or Steam for Rocket League.
- Don't delete game folders by hand, and never empty the Recycle Bin.

## 3. The Codex queue, in this order

Open **one new chat per entry**, paste the prompt exactly, and don't run more than about six chats at once. On "Model at capacity", send "continue" in the same chat.

**3a. Restart the stalled work first.**
- **Chapter 2, parts B to I.** Use this prompt, with X = B, C, ... I:
  > You are chat ch002-X (restart) for My Summons Go First. Read README_START_HERE.md in this folder and the files in its reading order, then read PANEL_BRIEF_v2.md all the way through and finish part X of chapter 2 from scripts_v2/ch002.yaml, exactly as the "Chapter 2" entry in its section 9 says. Some of this part's panels may already be in chapters_v2/ch002/art/: keep the ones that pass the checks in MANHWA_STYLE_GUIDE.md section 11 and PANEL_BRIEF_v2.md section 4b, and draw any that are missing, empty (0 bytes; P40 is) or failing, moving failed ones to chapters_v2/ch002/art/_rejects/ first. Write only the files section 8 lists for part X. Other Codex chats are drawing other parts at the same time; never touch their files. When the part is done, write DONE_X.md and stop. Do not stop to ask anything; finish the job.
- **Chapter 1 fixes:**
  > You are chat ch001-FIX for My Summons Go First. Read README_START_HERE.md in this folder and the files in its reading order, then read PANEL_BRIEF_v2.md all the way through and do CH001_FIXES.md exactly (P09, P21 and P22 of chapter 1), writing only the files it lists. Other Codex chats are drawing other parts at the same time; never touch their files. When the three panels are done, write DONE_FIX.md and stop. Do not stop to ask anything; finish the job.

**3b. Then the new sheets and keys,** with the prompts in `SESSIONS_TO_OPEN_5.md`, in its order:
1. **T1**, the thumbnail key art (its sheets already exist).
2. **S2b**, Nib's seal 2/5 look. Chapters 3–5 need it.
3. The rest of **Wave A** (Arc 2: S16–S19, M1–M4, L6–L12).
4. **Wave B** (Arcs 3–4: S20–S25, M5–M9, L13–L20, P1).

**3c. Chapter parts.** Open them only when two things are true:
- every sheet the chapter's rules name (`PANEL_BRIEF_v2.md` section 9) has its `DONE.md`;
- Claude has approved those sheets (section 4).

Use the chapter-part template at the end of `SESSIONS_TO_OPEN_5.md`, one chat per part letter in that chapter's table. Do the chapters in order (3, 4, 5, ...), and re-sync section 1 first: Claude may have fixed the script.

## 4. The review loop with Claude, through GitHub

Claude reviews every image before anything is built on it: proportions and scale, camera angle, the design locks, the house rules. Codex chats do not approve their own work, and neither do you. The loop:

1. **Send it.** When a chat writes its `DONE.md` (or `DONE_<part>.md`), zip its output:
   - a sheet or key: the entry's whole folder, for example `characters_v2/han_sora/`, as `S20.zip`;
   - a chapter part: that part's PNGs plus its `PROMPTS_<part>.json`, `REVIEW_<part>.json` and `DONE_<part>.md` from `chapters_v2/chNNN/art/`, as `ch002-B.zip`. Add any `_rejects/` it made.
   - Zip only: never resize, convert or re-save a PNG.
2. **Where it goes.** Use a repo for the art. The recommended one is a new **private** repo `abafaboy/msgf-art`; a public branch `msgf-art` on this repo also works if that's simpler.
   - Attach each zip as an asset on a release named `inbox` there.
   - Add one line per zip to `INBOX.md` on that repo's default branch: the zip's name, the time, and anything odd in the chat's `DONE` file.
   - Tell Abafa it's there. Abafa will then tell Claude.
3. **Read the verdict.** Claude writes one file per entry on this branch: `codex/reviews/<entry>.md`.
   - Each file says **APPROVED**, or **REDO** with each image's id, what is wrong and the exact prompt for the redo chat.
   - `codex/reviews/STATUS.md` is the board for everything.
   - Pull this branch to see new verdicts.
4. **Redo.** Open the redo chat with the prompt from the verdict file. Send its output back through the inbox the same way.
5. **Built from approved art only.** Claude letters, narrates and renders a chapter once every part of it is approved, and posts it to YouTube as an unlisted preview. While the link to the laptop is down, Claude may put a finished video on a release named `videos` in the art repo, with the title and settings to use, so you can upload it through YouTube Studio in Abafa's browser.

## 5. Never

- Never edit the scripts, briefs, designs or bible on the laptop. If something in them is wrong or impossible to draw, say so in `INBOX.md` and Claude will fix it here.
- Never use an image as approved before Claude's verdict says so.
- Never publish or upload anything public, except a video Claude has placed on the `videos` release with its settings.
- Never delete art: rejects move into `_rejects/` folders.
- Never put the lettering font files (Anime Ace) anywhere online.

## 6. Who to ask

- Story, art direction or a brief's meaning: Claude, through Abafa.
- The laptop, Codex and GitHub mechanics: you decide.
