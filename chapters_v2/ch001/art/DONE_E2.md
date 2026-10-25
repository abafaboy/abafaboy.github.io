# E2 finished — chapter 1, 25 October 2026

The authorized drawing and strict-review run is finished. **Three panels are accepted; two remain review-only after the three-total-try cap. This is not an all-panel quality pass.**

| Panel | Size | Tries | Result |
|---|---|---|---|
| P50.png | 1024×1536 | 2 | Accepted. Green backlight/red face-hole, nine-tower badge, left cracked pauldron and protective left arm checked. |
| P51.png | 1536×1024 | 3 | REVIEW ONLY. Final hand fits the middle third, but the sleeve ends at an unnatural internal vertical cutoff. Also archived as a reject. |
| P52.png | 1024×1536 | 2 | Accepted. Red overhead face-light, raised two-handed sword, Yerin's fear pose/left hand/strap tangle, supported gear and crisp foreground checked. |
| P53.png | 1536×1024 | 1 | Accepted. Hard decision in visible right eye, left-eye fringe, red eye-line light. Eye/brow remain inside middle-third crop; expendable hair/pencil margins may be cropped. |
| P54.png | 1024×1536 | 3 | REVIEW ONLY. Protective staging works, but husk rear foot still has a shoe-like heel block, Yerin's cyan face-light is weak, vest fragments remain and Jaeha's iris reads too light/gold. Also archived as a reject. |

## Records

- PROMPTS_E2.json: exact prompts and ordered references for all 11 calls, original source fields, rejection reasons, source/output SHA-256, reference hashes at final audit, native dimensions and prompt validation.
- REVIEW_E2.json: normalized head boxes for every visible character, all numbered checks 11, 11b and 11c, kept/review candidate numbers and explicit failures. P51 has no visible head.
- PROGRESS_E2.md: one line after each panel.
- Eight E2 rejects are in _rejects/ with panel/try/reason names. P51/P54 final files are preserved for review, not accepted production art.

## Verification

All five main PNGs and all eight reject files are byte-identical copies of generator PNGs. All eleven generator candidates have the brief's exact native dimensions. No image was resized, re-saved, sharpened, recompressed or composited. The full native images, 200 px-wide previews and 200% diagnostic details were inspected; inspection derivatives existed only in memory. No JPEG/WebP or extra QA files were written.

The file audit returned no errors: JSON parses; source/reference/output files exist; PNG headers and dimensions match; source/copy hashes match; prompts contain the exact V2 style, cleanup, negative and reference blocks, verbatim camera/light/art/acting/eyeline/foreground text where present; no call exceeds five references and no panel exceeds three tries. The husk's arms-hanging default in its snippet is overridden by the scripted arms-spread stance, as the prompt-kit permits. The special husk front_reference.png is used instead of a nonexistent front.png.

Reads completed: README_START_HERE.md; PANEL_BRIEF_v2.md all and section 9 E2; MANHWA_STYLE_GUIDE.md all; MANHWA_ART_DIRECTION.md; required character, husk, knight, location and prop designs plus section 8 snippets; bible/SCRIPT_FORMAT_v2.md; scripts_v2/ch001.yaml P49–P55; ACTING_TEST_BRIEF.md Round 2; style_test_v2/acting/REPORT.md; boss-room location notes. Only current V2 reference images were used.

Intentional project writes were confined to P50–P54, their named rejects, and these four E2 record files. Shared briefs, scripts, model sheets and other parts' files were not edited. Nothing was published or uploaded. No fourth attempts were made. E2 stops here.
