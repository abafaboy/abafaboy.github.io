# Chapter 6 production sources

Complete 41-unit assembly of the unmodified reviewed script, using the Chapter 5 renderer. The 70 exact text records include 65 dialogue lines, one SFX and four verified native phone messages/notes. All story sources have independent SHA-256/crop-specific acceptance. Rejected prior candidates remain identified in provenance records and their upstream Library packages.

## Rendering

Set `ANIME_ACE_FONT` to your licensed Anime Ace 2.0 BB font, then run `python source/build_chapter.py`. No font binaries are supplied. Dialogue/SFX use rasterized Anime Ace; PDF pages are compressed images with zero font resources. The build enforces under 25,000,000 bytes, exact text, natural ellipse padding, ordered dialogue, separate balloon/tail shapes, and protected face/action/UI regions. P1/P41 phone text remains native imagegen pixels. No System window appears in this script.

Geometry in `lettered/placement_manifest.json` uses an 800px master. Full panel PNGs are 1600px wide; phone proofs are 390px. Page mappings supply panel offsets. Individual glyph bounds and balloon outlines support narration highlighting. The complete reader uses 21 pages. `export_pdf390.py` rasterizes the actual compressed PDF; `verify_complete_chapter.py` checks the final 70 text records, all 41 assets, 21 pages, PDF size, zero fonts and hashes. Final visual acceptance is a separate required gate recorded under `qa`.

## Provenance

P20 is an independently accepted composited imagegen radio repair. It is not described as a wholly native generated frame. P14 v5/P41 v4 are native full-image repairs with surrounding resampling; their visual acceptance does not claim byte-unchanged surroundings. P22 uses the full new 1214×1295 framing. P30 uses its full native repaired source; the producer selected file is a normalized resize.

Selected native sources, exact crops, complete script, layout/text sources, generation metadata, original/rejected-source hashes and Library provenance are included in the source handoff. Duplicate upstream ZIPs and font binaries are excluded. Only final accepted sources should be used for the reader; prior rejected versions are historical records, not approved alternatives.
