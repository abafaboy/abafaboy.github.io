# When the laptop comes back: the checklist

The laptop (device "abafaboy", Tashkent) crashed on 25 October 2026. Abafa is away until 2 November and asked a colleague to switch it back on. Everything that didn't need the laptop was finished while it was off. This is the order of work once the bridge answers again.

**Update, 26 October, 03:00 Dubai:** Abafa expects the laptop to work again on **27 October** ("lets just wait till my latop works tomorrow"). He found the cloud relay too much hassle, so from then on Claude drives Codex on the laptop directly through the bridge and asks him to pass nothing on. Done meanwhile: S2b (Nib's seal 2/5) came in from the cloud Codex session and is **APPROVED** (`codex/reviews/S2b.md`; the files are in `characters_v2/nib/` on `msgf-art`); the 34 audit findings on chapters 34-40 are fixed (commit a08b14f), so every script changed since the laptop's copy.

**Earlier update, 26 October:** Abafadot now draws in the cloud (`HANDOFF_ABAFADOT.md`), with the laptop's V2 art copied to the `msgf-art` branch. When the laptop returns, first pull `msgf-art` and `codex/reviews/STATUS.md` to see what Abafadot has drawn and what is approved; only restart Codex on the laptop for entries nobody has drawn yet, and copy any approved art from `msgf-art` into the laptop's art folders.

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
| `scripts_v2/ch001.yaml` to `ch040.yaml` (all of them: the audits changed most) | `scripts_v2/` |
| `ARC5_BEATS.md`, `ARC6_BEATS.md`, `ART_BIBLE.md`, `SCRIPT_FORMAT_v2.md` | `bible/` |
| `codex/reviews/` (the verdicts and `STATUS.md`) | `reviews\` |
| from `msgf-art`: `characters_v2/nib/*_seal2*` (S2b) and anything else newly approved | the same paths in the laptop's art folders |

## 3. Restart the stalled Codex work
- First check `inbox/` on `msgf-art` and `codex/reviews/STATUS.md`: draw only what nobody has delivered.
- Chapter 2 parts A to I (only P01, P08, P16, P23 and P30 survived; keep them) and the chapter 1 fix chat (`CH001_FIXES.md`: P09, P21, P22).
- Then, with the prompts in `SESSIONS_TO_OPEN_5.md`: S2b is done, so the rest of Wave A (S16-S19, M1-M4, L6-L12), then Wave B, then Wave C; T1 last, once S21 is approved. Check each chat's first image before opening more of the same kind.
- Chapter 3 can start as soon as its sheets are approved (S2b is; check `PANEL_BRIEF_v2.md` section 9 for the rest).

## 4. Review every image strictly
- Chapter 1 P45: if the drawn notebook flies out of his hand, chapter 2 (which keeps it in his LEFT chest pocket until P25) needs one line in its continuity block saying he snatched it back off the floor as he landed.
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
