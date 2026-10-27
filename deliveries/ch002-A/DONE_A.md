# ch002-A — INCOMPLETE / BLOCKED, pending Claude

Recorded: 2026-10-25 22:37:09 UTC. Exact assigned range: **P01–P07**, from PANEL_BRIEF_v2 section 9, Chapter 2. Stop here for Claude’s verdict/reference-priority resolution. No self-approval.

Read the fresh handoff and art README, README_START_HERE reading order and relevant designs, complete PANEL_BRIEF_v2, script fields through P08, and acting REPORT. Bible source: `a11411c68427faeea4945302d15ea5917e598ce3`; original art source: `f4ebd472e3795a719dc4aa63b34cf558b5b528fa`. S2b is now marked approved in the fetched README; it was **never used**. All Nib references are base seal 1/5.

| Panel | New tries | Result |
|---|---:|---|
| P01 | 0 | Protected survivor copied byte-for-byte; no new approval. Original remains untouched. |
| P02 | 2 | Second attempt is a review candidate; first archived for depth blur. |
| P03 | 0 | Pending six-reference conflict described below. |
| P04 | 0 | Pending minimum six-reference conflict described below. |
| P05 | 0 | Pending minimum six-reference conflict described below. |
| P06 | 3 | **FAILED, review-only** final candidate; upper window zone still occupied by head. Final also archived in rejects. No fourth call. |
| P07 | 2 | Second attempt is a review candidate; first archived for closed speaking mouth and shredded hem. |

## Exact blockers and remaining work

- **P04 and P05: pending, never attempted.** Three hero fronts (`nib/front.png`, `kang_jaeha/front.png`, `song_yerin/front.png`) + `nib/turnaround_mask.png` + `boss_room/key.png` + one approved `style_test_v2/acting/` anchor = **six PNG paths minimum**, while the backend permits five. This already leaves out the extra per-character turnaround/face sheets in HANDOFF section 1. No critical reference was silently omitted; no approved image was transformed or combined; no brief-only call was made.
- **P03: pending, never attempted.** Nib front + mask turnaround + expressions (the handoff face set), approved knight sword detail, boss-room key and an approved acting anchor = **six paths**. PANEL_BRIEF section 2 prioritizes front/location and treats extra acting as room permits, while HANDOFF section 1 names the full face/turnaround set. The sword-contact beat requires a decision about which reference requirement may be relaxed. Exact paths are in PROMPTS_A.json. No six-path probe was sent.
- **P06: failed after three completed calls.** The generator repeatedly places the head in the required empty upper half. P06.png is a review-only last attempt, not acceptable chapter art. A new brief/verdict is needed before further tries.
- P01 has no prior verdict; perspective and crouching make exact scale measurement uncertain. It stays unchanged under the explicit keep instruction. P02/P07 still need Claude’s independent art verdict, including strict clothing-shadow and hand-contact review.

## Saved checkpoint and provenance

The first P02 candidate was copied and reported before bulk continuation: native 1254 square, SHA-256 `643d6cf26e182facac2daf5660b021fbd3c7cf73a656fcbc207173c72cd1dc9a`; then archived for depth blur. Seven completed built-in imagegen calls total, each using exactly five locally inspected approved references including the location and one approved acting anchor. No rejected image was a reference. Every exact request, ordered reference hash, generator source path, result and rejection is in PROMPTS_A.json.

All output PNGs are untouched byte copies of native generator sources or the protected survivor. No resizing, conversion, re-saving, compositing or pixel/code patching. Temporary 200 px/200% inspection derivatives stayed in `/tmp` and were never generation inputs or deliverables. Native PNG decode and source-byte equality checked. Head boxes and candid self-check observations are in REVIEW_A.json; they do not confer approval.

Inventory: **4 main PNGs** (P01, P02, P06 review-only, P07), **5 reject PNGs** (including the duplicate final P06), and PROMPTS_A.json, REVIEW_A.json, PROGRESS_A.md, DONE_A.md. Eight unique PNG byte streams: the protected original plus seven generated attempts. No P03/P04/P05 image exists.

| PNG | Native dimensions | Bytes | SHA-256 |
|---|---|---:|---|
| P01.png | 1536×1024 | 2267185 | `aa5575cfd80a980d804c56bd5bcec8b90415125c7b25c079d41058687b6d5dc5` |
| P02.png | 1254×1254 | 1998740 | `1b5790eaadec95928c4f356df9e31e7c7bd0d9711659e635d5cca6affed1389b` |
| P06.png | 1536×1024 | 2245432 | `22d994236fcd82b5d9901d2e91563d83758c64a1d6a392547c28ac389da76332` |
| P07.png | 1024×1536 | 1875258 | `aa48d5c655e8ea7a0b54366853a64c6734defbb0c14abd71fa2bf7a39b2573f7` |
| _rejects/P02_01_background_depth_blur.png | 1254×1254 | 2061308 | `643d6cf26e182facac2daf5660b021fbd3c7cf73a656fcbc207173c72cd1dc9a` |
| _rejects/P06_01_window_space_head_too_high_depth_blur.png | 1536×1024 | 1939296 | `51d044f61afd2aef7bf39054a23a7e66f876c4d81449503a0af1d5cae6aa1391` |
| _rejects/P06_02_head_still_inside_window_zone.png | 1536×1024 | 2045143 | `5a112e0c071df866b5e9460a02c89e14dfd761c72d22dbaf6510fdcb9f5d3d40` |
| _rejects/P06_03_final_window_zone_still_occupied.png | 1536×1024 | 2245432 | `22d994236fcd82b5d9901d2e91563d83758c64a1d6a392547c28ac389da76332` |
| _rejects/P07_01_closed_speaking_mouth_shredded_hem.png | 1024×1536 | 1995985 | `e34260a653f172d740f9ee17e8f4feb20e984ed0783e47bf18f3ede2e693da12` |

Only `inbox/ch002-A/` and the single INBOX.md entry are submitted. Canonical art, other parts, main, bible/scripts/briefs, fonts and secrets are unchanged. This delivery is **incomplete** and stops for Claude’s verdict; nothing is built or published from it.
