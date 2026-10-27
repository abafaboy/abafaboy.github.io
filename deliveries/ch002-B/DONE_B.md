# ch002-B — INCOMPLETE / BLOCKED, pending Claude

Recorded: 2026-10-25 22:56:54 UTC. Assigned range: **P08–P14** (PANEL_BRIEF_v2 section 9, Chapter 2). No art for P15. **This is a partial delivery, not a completion or approval marker.** Stop at this entry and await Claude verdict.

Bible source: `4515a815d802a726b48b374ee344808eed635144`; art source: `79d12395969c5a57cfbdfdfeb328e7dffe573855`. Fresh remote recheck confirms the same bible; art advanced independently to `a8af66ec8a8a2587d050642426018d8b97fb25bb`. No ch002-B verdict exists. Read HANDOFF, art README, README_START_HERE reading order, full PANEL_BRIEF_v2, relevant character/location designs and verbatim snippets, script through neighbouring P07/P15/P16, SCRIPT_FORMAT_v2, acting-test Round 2 and REPORT, current review board/S2b verdict, and session template. All Nib inputs are approved **base seal1**; no seal2 or retired inputs.

| Panel | New tries | Result |
|---|---:|---|
| P08 | 0 | Protected survivor copied byte-for-byte, review-only. Fragmented garment shadows raise 11b.1; redraw held on references. Canonical original untouched. |
| P09 | 1 | Candidate; first-image technical/style checkpoint satisfactory before any other generation. Pending Claude. |
| P10 | 2 | Candidate, pale reaction background corrected. Pending Claude. |
| P11 | 3 | FAILED / review-only: near foreground paving still defocused. Final also archived in rejects. |
| P12 | 0 | HELD, 7 required references exceed max5. |
| P13 | 3 | FAILED / review-only: unclear reverse grips/hilt construction. Final also archived in rejects. |
| P14 | 0 | HELD, 7 required references exceed max5. |

## Exact reference conflicts (pending, never called)

HANDOFF section 1 requires approved fronts and relevant turnarounds for each character, plus face/acting sheet for a readable face, location key and 1–2 approved acting anchors. The masked base turnaround satisfies Nib’s required mask/turnaround input. Here is one mandatory anchor per set; still seven paths each. No priority waiver is in the current verdicts. No required input was silently dropped, combined, transformed or passed as a sixth/seventh path. PANEL_BRIEF section 2 has a lighter priority list, but it cannot waive the current handoff and user’s explicit full-input rule.

**P08 redraw: 7 vs runtime max5.**
- `characters_v2/kang_jaeha/front.png`
- `characters_v2/kang_jaeha/turnaround.png`
- `characters_v2/kang_jaeha/talking.png`
- `characters_v2/nib/front.png`
- `characters_v2/nib/turnaround_mask.png`
- `locations_v2/boss_room/key.png`
- `style_test_v2/acting/A3_P23.png`

**P12: 7 vs runtime max5.**
- `characters_v2/kang_jaeha/front.png`
- `characters_v2/kang_jaeha/turnaround.png`
- `characters_v2/kang_jaeha/talking.png`
- `characters_v2/nib/front.png`
- `characters_v2/nib/turnaround_mask.png`
- `locations_v2/boss_room/key.png`
- `style_test_v2/acting/A3_P23.png`

**P14: 7 vs runtime max5.**
- `characters_v2/nib/front.png`
- `characters_v2/nib/turnaround_mask.png`
- `characters_v2/nib/expressions.png`
- `characters_v2/knight_commander/front.png`
- `characters_v2/knight_commander/turnaround.png`
- `locations_v2/boss_room/key.png`
- `style_test_v2/acting/A3_P23.png`

P08 remains in its original home and its byte-identical inbox copy is review-only. P12/P14 have no PNG. These holds need Claude’s reference-priority rule before any generation.

## Remaining failed checks

- **P11, 3/3:** The final near pillar edge is sharp, but full-size and 200% inspection of the bottom paving shows photographic defocus. Background detail also remains higher than the simplified anticipation recipe. No full strict-check pass.
- **P13, 3/3:** Mask coverage, fang side and open mouth are fixed in the final candidate, but the picture-left hilt/guard construction and both blades’ reverse-grip alignment remain unclear. Small angular skin-shadow shapes also need strict review. No full strict-check pass.
- **P09/P10:** These are self-checked candidates only. Full-body standing height cannot be measured in the close crops; Claude still reviews exact locks, shadow shapes, hands, camera and acting.

## First-image checkpoint and provenance

P09 try1 was saved and inspected before P10/P11/P13 calls: native **1254×1254**, SHA-256 `c78a0ac22a250cdb0827332ab24a08665cd894d098dab859d9155383738c7ce8`. Full-size, 200px and 200% face detail were satisfactory for technical/style self-check; this is not a Claude verdict.

Nine completed built-in image_gen calls, all with **exactly five inspected approved local references**, including approved Arc1 character sheets, boss-room key and `style_test_v2/acting/A3_P23.png`. No failed candidate used as a generation reference or edit target. No duplicate/uncertain calls; all results known. Three total tries per panel cap respected.

Every PNG is an untouched byte copy of a native generator source, or the protected P08 survivor. No resize, conversion, re-save, compositing or code retouch. Inspection-only derivatives in `/tmp` are neither generation inputs nor deliverables. `PROMPTS_B.json` contains exact prompts, ordered paths and hashes, source fields, generator source paths, outcomes and PNG inventory. `REVIEW_B.json` records head boxes and candid checks.

Inventory: **5 main PNGs**, **7 reject PNGs**, **10 unique PNG byte streams** (the survivor + 9 generated attempts), and the four part metadata files. Final failed P11/P13 are duplicated in `_rejects/` so their status is explicit. P15 has no image.

| PNG | Native dimensions | Bytes | SHA-256 |
|---|---|---:|---|
| P08.png | 1536×1024 | 1862040 | `8acbcd211854fc9a66736e8a3a1b87284c74b074055434e737a31da0d438bda7` |
| P09.png | 1254×1254 | 1933590 | `c78a0ac22a250cdb0827332ab24a08665cd894d098dab859d9155383738c7ce8` |
| P10.png | 1254×1254 | 1895486 | `22740e3633795906c9c2687677f9d4729a03773be12d74a4224287a043c507ee` |
| P11.png | 1536×1024 | 2057609 | `bf7c20406bb9250f219915225a094cec92fd5d45fd1007eed3ed777c536052c2` |
| P13.png | 1254×1254 | 2003341 | `91a1236afe02db273d890c1246692e3aefa7667794161b4f926cb61b81cbef6d` |
| _rejects/P10_01_dark_background_fragmented_sleeve_shadows.png | 1254×1254 | 1887121 | `b3cc75741d756c6b599198aed6ae24e04dcec0bc2b9ad053bc267d9d6d54888e` |
| _rejects/P11_01_foreground_depth_blur_busy_background.png | 1536×1024 | 2266168 | `cefba3ccd342eb9c34d24fdb118ab44f42fe203a5c36dc32d8d54f1d32d26616` |
| _rejects/P11_02_persistent_foreground_depth_blur.png | 1536×1024 | 2068625 | `a6798415a55b199da2f5a51237eba1a081e7de0e0e0e0c7abb3d80d34f95eb2e` |
| _rejects/P11_03_final_foreground_paving_depth_blur.png | 1536×1024 | 2057609 | `bf7c20406bb9250f219915225a094cec92fd5d45fd1007eed3ed777c536052c2` |
| _rejects/P13_01_closed_speaking_mouth.png | 1254×1254 | 1912380 | `89a962265ec39cc8e5895c5e8139a13805d0bfca6f7593a6f84289f65fa3ddb3` |
| _rejects/P13_02_mask_exposes_left_eye_fang_upper_wrong_head_angle.png | 1254×1254 | 1989129 | `495400a60dd4115242c47ff17497bdaf2515aba2354c2946c8c881e853c5c5f9` |
| _rejects/P13_03_final_knife_grips_unclear.png | 1254×1254 | 2003341 | `91a1236afe02db273d890c1246692e3aefa7667794161b4f926cb61b81cbef6d` |

Only `inbox/ch002-B/` and one line in `INBOX.md` are submitted on `msgf-art`. No canonical art, other part, main, bible, brief, script, font or secret changes. Native fetch/rebase preserves concurrent entries; no force push. Delivery verification checks remote commit ancestry and output hashes. **Stop here and await Claude verdict/reference-priority resolution.**
