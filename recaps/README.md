# Narrator recaps

One file per chapter: a JSON list of `{"panel": "<id>", "text": "<narration>"}` in reading order, read by `tools/recap_video.py` (voice am_michael, speed 1.3, gap 0.08).

- ch001–ch005: written by Claude at the pace the owner approved (about 500–700 words).
- ch006–ch013: Codex's first recaps tightened to the same pace (about 600–800 words for 55–60 panels).
- **ch006.json is a stopgap.** Chapter 6 art stops at P35, so its last four entries summarise P36–P55 over P35. Rewrite it when P36–P55 are drawn; `ch006_full_codex.json` is Codex's full-length version to start from.
- Panel ids must have art in the chapter's `art/` folder, and the order must never go backwards (the camera only scrolls down).
