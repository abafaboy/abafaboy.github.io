# M3 — Ash hounds — DONE

27 October 2026. Entry finished and ready for Claude's review. No remaining deliverables.

## Kept files

- `front.png` — the checked front anchor, attempt 3.
- `turnaround.png` — side, front and back views, attempt 1.
- `details.png` — eyeless/noseless head, open split jaw, cracked back and four-toed paw, attempt 1.
- `pack.png` — exactly six running normal hounds in a narrow market alley, with an actual generic 178 cm adult silhouette for scale, attempt 4.
- `alpha.png` — the 1.6 m shoulder-height alpha, side and howling three-quarter views, with heavier neck and flaring violet fissures, attempt 1.
- `card.json` — sizes, palette, design locks, alpha tell, references and review notes.
- `prompts.json` — the exact built-in image_gen.imagegen prompt and reference paths for all 10 calls, every source/destination, verdict, rejection reason and free-space reading.

All five kept PNGs are native 1536×1024 generator files. Every kept image and reject was copied byte-for-byte to an ordinary file. SHA-256 comparisons against the generator originals passed for all ten files; no hard links, shortcuts, resizing, retouching, compositing or re-encoding were used.

## Review and overrides

Read README_START_HERE.md and its applicable reading sequence, the M3 entry, MODEL_SHEETS_BRIEF.md sections 1–3, PANEL_BRIEF_v2.md reference/scale rules, and the style-test report. The 27 October README changes take precedence.

The front passed the internal drawing check before being used as the first reference for every remaining image. The only additional image input was the Mangwon Market key, approved as L9 in reviews/STATUS.md, used for the pack scene. No rejected, retired or outside image was used as a reference.

Sheets have no person, scale silhouette, height marker, label or text. The alley scene retains its human scale figure. The alpha's 160 cm shoulder height is recorded in metadata, following the no-silhouette override.

Inspected the full-size images, 200 px thumbnails and 200% ink/anatomy spot checks. Six pack heads/bodies are countable, the leaders sit near half the adult's height at their shoulders, and their paws share the alley floor. Front, views, details and alpha retain the smooth black eyeless/noseless skull, split white-toothed jaw, long canine legs and dorsal violet cracks.

Minor review notes: the generated sheet backgrounds are slightly cooler/darker than exact #E9E9EC and have faint tone variation, allowed by the 27 October override. Scene scale is a visual comparison rather than an exact scale card. No other unresolved fault was identified. Final approval remains with Claude; shared review files were not changed.

## Rejected ordinary PNGs

Saved in `characters_v2/_rejects/`:

- `ash_hound_front_01_eye_socket_shapes_extra_toes.png` — socket-like facial shadows and extra weight-bearing toes.
- `ash_hound_front_02_three_quarter_body.png` — body turned into three-quarter rather than front; ambiguous skull modelling.
- `ash_hound_pack_01_overscale_foreground.png` — leading hounds too large against the adult; busy floor.
- `ash_hound_pack_02_seven_hounds.png` — seven hounds instead of six.
- `ash_hound_pack_03_blurred_foreground_tubs.png` — optical blur on the nearest tubs.

No image reached the five-try limit. No inspection previews or temporary images were saved in the project.

## Disk and write scope

Checked C: with Get-PSDrive C before every generation call. Available space ranged from about 42.23 GiB to 40.23 GiB before calls, always above 3 GB; exact byte readings are in prompts.json.

Project writes were confined to characters_v2/ash_hound/ and the five M3-prefixed reject files in characters_v2/_rejects/. Other chats' folders were not modified. Built-in generator originals remain in its application-managed generated_images folder.

Stopped after writing this DONE.md.
