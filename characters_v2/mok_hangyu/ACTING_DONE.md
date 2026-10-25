# P4 — Mok Hangyu acting sheets

R2 phone correction completed 25 October 2026.

The user reports Claude's strict review passed `talking.png` and all six acting poses, including shield support, sheathed sword and the left-chest hound emblem. The sole requested correction was the branded-looking camera module in the selfie pose.

Patched `acting.png` by cropping the phone, editing the crop with built-in imagegen, then compositing only a small mask on the phone's back. It is now a plain black rounded-corner phone with one small round camera lens and no other marks. The original outline, hand and grip were retained.

**Pixel verification:** 278 phone pixels changed, within x=193–216 and y=8–26 (zero-based). All other 1,572,586 pixels are identical; zero pixels outside the phone mask changed. `talking.png` is unchanged. Both sheets remain 1536×1024.

The old acting sheet was moved intact to `characters_v2/_rejects/mok_hangyu_acting_r2_branded_phone.png`; its SHA-256 matches the original. `acting_prompts.json` retains the original generation history and adds the exact R2 prompt, crop reference, mask, output hashes and pixel-difference results.

Initial generation: three tries per sheet; acting used attempt 3 and talking used attempt 2. R2 used one local crop edit, with no sheet regeneration. No other sheets, `prompts.json`, `DONE.md` or `card.json` were edited.
