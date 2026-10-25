# When the laptop comes back: the checklist

The laptop (device "abafaboy", Tashkent) crashed on 25 October 2026. Abafa is away until 2 November and asked a colleague to switch it back on. Everything that didn't need the laptop was finished while it was off. This is the order of work once the bridge answers again.

## 0. Check the bridge
- `device_list_dir C:\Users\abafa\Videos\MySummonsGoFirst`. If it fails, try again later; a reminder fires on 2 November.
- This session now has a shell on the laptop (`device_bash`) when it is connected: use it for listing, copying and checking files there.

## 1. Free disk space (authorised by Abafa: "uninstall valorant to free up space. you can uninstall rocket league too", "because i can always just reinstall the game without losing anythung")
- Use each game's own uninstaller (Riot Client for Valorant, which also offers to remove Vanguard; the Epic Games Launcher or Steam for Rocket League), never a raw delete. Never empty the Recycle Bin.
- Check the free space afterwards and note it here.

## 2. Put the new files on the laptop (then check each with a re-stage and `cmp`)
| Repo (`msgf-bible`) | Laptop folder |
|---|---|
| `codex/*.md` | the root (`README_START_HERE.md`, `ASSETS_ARC2_BRIEF.md`, `ASSETS_ARC3_BRIEF.md`, `THUMBNAIL_BRIEF.md`, `PANEL_BRIEF_v2.md`, `CHARACTER_DESIGNS_v2.md`, `SESSIONS_TO_OPEN_5.md`, ...) |
| `STORY_BIBLE_v4.md`, `ARC3_4_BEATS.md`, `NAME_SHEET.md` | `bible/` |
| `scripts_v2/ch001.yaml` to `ch033.yaml` (ch007, ch008 and any audit fixes changed) | `scripts_v2/` |

## 3. Restart the stalled Codex work
- Chapter 2 parts B to I (redraw P40, which was saved as 0 bytes) and the chapter 1 fix chat (`CH001_FIXES.md`: P09, P21, P22).
- Then open, in this order (`SESSIONS_TO_OPEN_5.md`): T1 (thumbnail key art), S2b, the rest of Wave A, then Wave B. Check each chat's first image before opening more of the same kind.

## 4. Review every image strictly
- Proportions, scale and camera angle first (`PANEL_BRIEF_v2.md` 4b; `tools/head_ruler.py`, `tools/check_art_v2.py`). Known issue to re-check: chapter 2 P08.
- Fan service only on adults; never Seoa; Yerin covered; nothing explicit, no angle up a skirt or at a crotch.

## 5. Each approved chapter
1. Stage its art into `/home/claude/work/chNNN/art/`.
2. Letter: `python3 tools/autostrip2.py scripts_v2/chNNN.yaml /home/claude/work/chNNN/art /home/claude/work/chNNN/out --dpr 2`.
3. Render with the season settings in `ledger/PUBLISHING.md` ("Encode settings").
4. Upload as Unlisted (`My Summons Go First · Chapter N: <title>`) and log the link in `ledger/PUBLISHING.md`.
- The container has little disk (about 6 GB free on 25 October): keep each chapter's `recap.mp4` and `recap.wav` (the long-form joins them), and delete its lettering work folder (`out/_work`) once the video is checked.

## 6. At chapter 33
`ledger/PUBLISHING.md`, "Steps, at chapter 33": redo chapter 1 with the fixes, join with `tools/longform_build.py`, make the thumbnail with `tools/thumbnail_text.py`, upload as Public, send Abafa the link.
