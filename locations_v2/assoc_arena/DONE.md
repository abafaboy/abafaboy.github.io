# L13 DONE — Association test arena

Completed 27 October 2026 (Asia/Tashkent). L13 covers this arena plus assoc_lobby and assoc_hearing_room, each with its own DONE.md.

## Delivered
- key.png — retained attempt 3 of 5, 1536×1024: round basement arena at 30 m scale, padded grey perimeter, high observation window on the right, blank green wall screen on the left, paired inlaid white light rails, cold-white attached floodlights, two tiny staff on the floor plane. No construct or summon.
- notes.md — layout, scale, dormant lighting and later-panel continuity.
- prompts.json — full five-call prompt record, references, source/saved files, decisions and disk checks.
- _rejects/ — attempts 1, 2, 4 and 5, ordinary full-size PNGs. Attempts 1–2 also have an oversized visible service door; the retained layout keeps the service entry behind camera.

## Remaining fault in the best try
The blank screen is near-green, not exact and perfectly uniform #00FF00. Kept-image interior samples: (180,160) = RGB (6,255,3); (250,160) = (7,254,5); (330,180) = (7,253,4). Five calls did not obtain exact screen pixels. Per the 27 October override, keep the best under key.png and stop at five. No recolouring or pixel alteration was performed. Screen-colour correction remains for review; no further drawing is left.

No other material layout, text, scale or rendering fault found in the retained key.

## Verification and limits
- Built-in image_gen.imagegen used; exact prompts and per-call references/free-space checks are in prompts.json. At most one approved image reference per call; none from retired or reject folders.
- Every retained and rejected image is a full-size 1536×1024 generator PNG copied byte-for-byte. All 11 entry PNG copies passed SHA-256 source equality, had exactly one NTFS hard-link name, and had no reparse-point attribute: ordinary files, no hard links or shortcuts.
- Kept images inspected full size, at 200 px wide, and with 200% source-pixel crops. QA images stayed in memory; no extra previews or temporary images were saved in the project.
- C: checked with Get-PSDrive C before every image call. Lowest reading was 39,557,664,768 bytes (36.84 GiB), above the 3 GiB drawing-stop threshold; final reading 45,154,938,880 bytes (42.05 GiB).
- Project writes were confined to locations_v2/assoc_lobby/, locations_v2/assoc_hearing_room/ and locations_v2/assoc_arena/. Other chats' folders, briefs and review state were not modified.
- Entry L13 drawing is finished. Pending Claude review; this is not an approval verdict. No other L13 deliverables remain undrawn. Stop here.

