# Chapter 1 production sources

## Checkpoint status

All 64 panels are lettered with the licensed Anime Ace 2.0 BB Regular font. The final renderer passed real-glyph ellipse containment, reading-order, source-hash, full-shape protection and pairwise balloon/tail checks. The 71 canonical text records are unchanged; seven separately tagged prop/continuity records add the Sunday schedule, grandmother transfer, approved fictional small balance, and persistent interface labels. The flattened 32-page PDF, 390-pixel reader images and placement manifest are in `lettered/`. Independent visual review passed all 32 actual 390-pixel reader pages, with exact text and source mappings verified; see `qa/independent_final_visual_review.json` and `qa/independent_final_integrity.json`. Older geometry proofs are diagnostic checkpoints, not the final reader.

Canonical story: `script_v2.md` (One More Shift). `lettering_script.json` preserves the exact spoken, message, interface and sound-effect text by script-panel number.

`raw/p01.png` through `p32.png` are untouched illustrated source pages, each containing two script panels. Raw page 11 contains script panels 21 and 22. Art manifests describe original-image pixel coordinates, with rectangles in x0, y0, x1, y1 format.

`layout_config.json` uses an 800-pixel-wide logical lettering canvas. Its crop rectangles refer to original-image pixels. Its balloon boxes are x, y, width, height in logical output pixels. Mouth locations and protection boxes are transformed into the same logical coordinate system, including any intentional white breathing space. Smaller quiet inserts may preserve the complete artwork at a reduced width. No stretching or content-aware alteration is used.

## Rebuild

Install Pillow, fontTools and PyMuPDF in your Python environment. Set `UI_FONT` if DejaVu Sans is not installed at the system default path. Supply a properly licensed Anime Ace 2.0 BB Regular font locally. Font files are intentionally excluded from this source package.

Set `ANIME_ACE_FONT` to your font path, then run:

    python source/build_chapter.py

The renderer preserves original text in the placement manifest. The comic font's keyboard-case convention is applied for rendering. A fallback is used only for individual punctuation glyphs missing from the main font, and is explicitly recorded per glyph. UI and phone-message text use a neutral sans serif.

`check_geometry.py` creates text-free placement previews and checks complete balloon/tail polygons against protected artwork. All multi-balloon dialogue has explicit line breaks and a checked first-line ordering plan. Distinct filled balloon/tail shapes are checked pairwise for intersections. The final renderer additionally checks actual first-glyph reading order, glyph containment and spacing within the balloon ellipse. Dialogue uses 29 logical pixels, equivalent to 14.14 pixels at phone width. `placement_manifest.json` records input hashes, crop transforms, full balloon geometry and per-character bounds.

Final PDFs contain flattened page images only. They do not embed or distribute editable font programs.
