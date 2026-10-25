# D2 handoff — chapter 1

25 October 2026, Asia/Tashkent.

**Production pass finished within the three-total-tries cap. Four panels are accepted; P43 remains unresolved. No P43.png was written.**

| Panel | Tries | Result | Native PNG size |
|---|---:|---|---|
| P39 | 1 | Kept | 1024×1536 |
| P40 | 2 | Kept | 1536×1024 |
| P41 | 1 | Kept | 1536×1024 |
| P42 | 3 | Kept | 1536×1024 |
| P43 | 3 | Rejected, no final | Every output was 1254×1254; required 1024×1024 |

P39 is the empty black/red sword-path tone flip. P40's first draft was rejected for foreground depth blur and excessive background detail; the second has crisp near edges and quieter architecture. P41 keeps the low shield-impact camera, supported two-hand grip, braced skid, clenched teeth and white contact flash. P42's edits removed the blurred background, simplified the bent-knee shading and corrected the golden cheek light to green dusk while preserving the calculating face, right-hand pencil, one open notebook and empty left chest pocket.

**P43:** all three built-in imagegen calls returned native 1254×1254 despite repeated explicit 1024×1024 requests. No resizing, re-saving or fourth try was performed. The best visual candidate is `_rejects/P43_2_native_1254_square.png`; its head box is recorded for review only. It shows the nine-tower badge, cracked anatomical left pauldron, frontal sword sweep, dropped buckler, red face-light and green shafts. Try 1 also crowded the calm zone; try 3 has excessive cloak-edge wear and an unclear right-hand hilt connection. This part does **not** claim a complete strict pass for all five panels.

All images were visually checked full size and at 200 px width; native-edge, face/hand/prop areas were also inspected at 200 percent. `REVIEW_D2.json` records checks 11, 11b and 11c, every candidate verdict, and normalized head boxes. P39 has no heads; P40 has the two fallen silhouettes; P41 has Mok; P42 has Jaeha. P43's box explicitly points to the rejected try-2 candidate.

`PROMPTS_D2.json` contains every exact prompt, ordered reference paths and hashes, native dimensions, generated source paths, output hashes and rejection reasons. Ten generated candidates total: four kept and six rejects. No call used more than five reference images. All ten saved candidate files are byte-identical to their generator sources. Accepted sizes match the brief. No art was re-encoded, sharpened or resized; inspection derivatives existed only in memory.

Only D2's four accepted panel PNGs, six rejects, `PROMPTS_D2.json`, `REVIEW_D2.json`, `PROGRESS_D2.md` and this handoff were intentionally written in the project. Shared scripts, briefs, sheets and other parts were untouched. Built-in imagegen was used throughout.

Stopped here as instructed.

