# Narrator recaps for the rebuilt story (v2)

One file per chapter: a JSON list of `{"panel": "<id>", "text": "<narration>"}` in reading order, read by `tools/recap_video.py` (voice am_michael, speed 1.2, gap 0.08, 2560x1440 at 30 fps).

- One narrator, recap-channel pace: about 800–900 words for a 60-panel chapter.
- Every panel id must have art. Never use caption or title panels (P08, P25 and P59 in chapter 1).
- The order never goes backwards: the camera only scrolls down.
- The old story's recaps stay in `recaps/` and are not used for the rebuild.
