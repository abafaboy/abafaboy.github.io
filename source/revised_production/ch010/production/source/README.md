# Chapter 10 assembly preparation

Locked dispatch copies are unchanged. `lettering_script.json` contains all 47 exact spoken lines in 32 ordered units, including six silent units (P08/P10/P12/P19/P25/P28). Source and intake provenance are in `qa/preparation_provenance.json`. No art, final placements, visual approvals, PDF or publication is represented by this preparation.

## Arrival workflow

1. Retain each actual Library identity, delivered archive and SHA256 under intake/. Extract safely to a batch-specific raw/ directory. Verify the complete supplied manifest before use. Never replace original art with a reference or preview.
2. Independently review native art at full and phone widths, the full source acting and the continuity checklist. Bind every raw verdict to exact SHA256, panel number and crop in qa/independent_raw_review.json. A reference approval is not a raw-art approval.
3. Use pending_final_layouts.json as a required face/hand/prop protection checklist. Mark actual pixel-derived protected boxes/polygons, speaker endpoints and tail paths on the approved crop. Do not copy guessed coordinates from another panel. Complete layout_config.json only for the reviewed panel.
4. Use provisional_text_fit.json for text-only ellipse dimensions at fixed 31 master pixels (15.1125 at 390px). No font shrink. Prefer free background and extra assembly space; preserve actual acting and chronology. If a layout cannot fit, reflow preserved accepted frames or request a correctly scoped art repair, never rewrite dialogue or hide the evidence.
5. Run `python source/build_chapter.py --panels 1,2,3,4` for a scoped proof. The renderer rejects missing exact independent raw passes, missing protected geometry, extra/missing lines, wrong font, text overflow, tail self-intersections, overlaps, protected-art collisions, incorrect glyph reading order and sub-31px text. P04 CLIP VOICE is transmitted audio; its phone-source attribution needs an explicit reviewed source or tail.
6. Review full/390px proofs independently, including all protected features and spoken timing. Record immutable exact output hashes. Full render remains PROVISIONAL_FULL_Chapter_10.pdf until final reader/sequence/continuity and PDF QA plus parent delivery authorization. Do not rename a provisional proof to imply acceptance.

Inherited implementation: Chapter 11's current gated renderer, using Chapter 9 text-fit helpers. Fonts remain separately licensed local resources and must not be included in packages. Phone widths, native crops, source identities and font SHA256 are retained in output metadata. The output PDF is raster and must remain below 25 MB without embedded fonts.

## Scope boundaries

No source rewrites, invented images, story-art generation, other-chapter edits or publication. Lane A acceptance is bounded to approved support/contact/release/storage and clip reference scope, not completed story panels. Parent has eight art batches running; actual delivery identifiers are still required.
