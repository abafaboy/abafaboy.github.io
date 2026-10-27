# L13 DONE — Association lobby

Completed 27 October 2026 (Asia/Tashkent). L13 covers this lobby plus assoc_hearing_room and assoc_arena, each with its own DONE.md.

## Delivered
- key.png — retained attempt 3 of 5, 1536×1024: five-storey glass atrium, morning glass-roof light, grey/white floor with a five-point star inside a shield inlay, three blank green screens, security arch and desk, two tiny generic staff.
- notes.md — layout, scale, light and later-panel continuity.
- prompts.json — full five-call prompt record, source files, references, saved files, decisions and disk checks.
- _rejects/ — attempts 1, 2, 4 and 5, each saved as an ordinary full-size PNG.

## Remaining fault in the best try
The screens are visibly blank green but not exact uniform #00FF00. Kept-image interior samples: (320,260) = RGB (2,252,2); (840,310) = (3,253,3); (1300,280) = (2,253,1). Five calls did not obtain exact screen pixels. Per the 27 October override, the best image is retained under key.png and generation stops at five. No recolouring, re-encoding or other pixel edit was performed. This screen-colour correction remains for review; no further drawing is left.

No other material layout, text, scale or rendering fault found in the retained key.

## Verification and limits
- Built-in image_gen.imagegen used; exact prompts and per-call references/free-space checks are in prompts.json. At most one approved image reference per call; none from retired or reject folders.
- Every retained and rejected image is a full-size 1536×1024 generator PNG copied byte-for-byte. All 11 entry PNG copies passed SHA-256 source equality, had exactly one NTFS hard-link name, and had no reparse-point attribute: ordinary files, no hard links or shortcuts.
- Kept images inspected full size, at 200 px wide, and with 200% source-pixel crops. QA images stayed in memory; no extra previews or temporary images were saved in the project.
- C: checked with Get-PSDrive C before every image call. Lowest reading was 39,557,664,768 bytes (36.84 GiB), above the 3 GiB drawing-stop threshold; final reading 45,154,938,880 bytes (42.05 GiB).
- Project writes were confined to locations_v2/assoc_lobby/, locations_v2/assoc_hearing_room/ and locations_v2/assoc_arena/. Other chats' folders, briefs and review state were not modified.
- Entry L13 drawing is finished. Pending Claude review; this is not an approval verdict. No other L13 deliverables remain undrawn. Stop here.

