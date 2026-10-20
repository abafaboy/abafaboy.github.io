# Chapter 7 assembly readiness

Prepared from the reviewed Chapter 7 script and dialogue JSON, with Chapter 6 renderer lineage. No art was generated, no reader rendered, and nothing was uploaded or published. All files created by this preparation are inside ch007.

## Ready
- Exact records: 34 acting units, 70 spoken lines and four native phone-screen rows (P16–17). P6 and P24 are silent. No thought dialogue or SFX is scripted; none is invented.
- Organic continuous-outline speech balloons, separately placed transmitted-phone/radio dialogue, protected-art masks and tail collisions inherited from the accepted renderer. All ordinary speech requires a reviewed speaker tail. Transmitted lines may be tailless only with reviewed transmission-source attribution. Grandmother remains a remote voice, not a visible/video-call speaker.
- Text-only candidate sizes at 31px master / 15.11px at 390px; no provisional candidates are treated as actual layout coordinates.
- Local Anime Ace 2.0 BB identity and hash checks. Font programs remain outside this tree. Raster-only PDF inserts; final export asserts zero PDF fonts. No font programs may be included in delivered archives.
- Complete export requires all 34 panels. Exact raw source SHA-256 + panel number + crop must match independent PASS. No provisional-art bypass.
- Source/continuity copies and reference hashes, preflight, native screen-text gates, actual compressed PDF 390px export for final QA.

## Required inputs before rendering
1. Incoming original source PNGs with source provenance and approved exact crop coordinates. Store under production/raw; preserve originals unchanged.
2. Independent raw review records under production/qa/independent_raw_review.json. Format: {"panels":[1],"sha256":"...","crop_xyxy":[0,0,width,height],"verdict":"pass"}. An existing pass for a different source or crop does not transfer.
3. Approved P4 exit-corner anchor and P24 table anchor; reconcile subsequent panels against both. P16 screen must contain exact native “GATE STATUS: CLOSED” / “Recording retained.” P17 uses the same words if readable. Do not manufacture device text in assembly.
4. Per-art protected faces, hands, prop/action paths, native text, and visible handoffs, plus suitable balloon/tail positions. Set protection_reviewed only after pixel inspection. Longer lines may require restrained canvas extensions; do not put balloons over protected action.
5. Exact final-reader independent QA after compression at 390px, including actual glyph ordering, organic contours, distinct balloons, reading clarity, and no overlap with faces/hands/action. Raw-art approval does not replace reader approval.

## Commands after inputs are ready
Set ANIME_ACE_FONT to the existing local licensed font if relocating this work. Run preflight.py first. build_chapter.py --panels accepts a subset for a visibly provisional proof, but raw sources still require full independent PASS. build_chapter.py without a subset requires all 34. Then export_pdf390.py exports the actual final PDF pixels for review. No publication commands are included.

prepare_assembly.py is an initializer, not an update tool: do not rerun it after incoming art, layouts or review records are registered, because it writes empty initial gates.
