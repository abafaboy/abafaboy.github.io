# L17 — DONE

Completed 27 October 2026. All seven images requested by entry L17 of `ASSETS_ARC3_BRIEF.md` are saved. No drawing remains. New assets await Claude's review; no review-board approval is claimed or changed.

| Kept file | Attempts | Result |
|---|---:|---|
| `locations_v2/columbarium/key.png` | 1 | White corridor, eight niche rows, chrysanthemums, long bars of sun, two distant visitors for scale. |
| `locations_v2/columbarium/niche.png` | 1 | Straight-on niche with urn, thumbs-up photo, toy husk, coffee can and blank brass plate. |
| `locations_v2/hanriver_gate/pier7.png` | 1 | Open slit, cracked orange lamp and blank faded-yellow area for the letterer's pier numeral. |
| `locations_v2/hanriver_gate/inside_fence.png` | 1 | Open fence, crane truck, open box truck and faint violet cargo crates. |
| `locations_v2/hanriver_gate/sealed.png` | 2 | Fully closed, dark steel iris behind plain yellow police cordon. |
| `locations_v2/rooftop_room/party_dusk.png` | 1 | Approved roof layout, warm bulbs above the laundry, exactly two folding dinner tables. |
| `locations_v2/kanghan_office/day.png` | 1 | Approved office layout in hard daylight, blinds raised, no people. |

One reject is preserved as an ordinary PNG: `locations_v2/hanriver_gate/_rejects/L17_sealed_try01_wrong_emblem.png`. Its generated emblem used adjacent hexagons instead of nested hexagons; the replacement has no optional emblem. Do not use the reject as a reference.

The full exact prompt set, all eight attempts, approved input paths, generator source paths and free-space checks are in [prompts.json](prompts.json). Generation used the built-in image tool. Layout and light continuity for all seven images are in [notes.md](notes.md). Existing location notes, prompts, completion files, review files and all other chats' folders were left untouched. Only L17's new view PNGs and its location-local reject were added outside this folder.

Validation: every kept PNG and the reject is 1536×1024, matches its original generator file byte for byte by SHA-256, has no reparse-point attribute, and has exactly one filesystem hard-link entry. All were saved with ordinary `Copy-Item`, with no resizing, conversion, sharpening or recompression. Full images, 200-pixel-wide thumbnails and 200% detail crops were inspected. Inspection images existed only in memory; no extra previews or temporary images were kept in the project.

`Get-PSDrive C` was checked before every image call. The eight pre-call checks ranged from approximately 39.98 to 41.98 GB free; the final verification found approximately 37.08 GB free. The 3 GB stop condition never occurred.

No known retained-image faults require another drawing pass. Under the overriding no-text rule, the scripted pier **7**, niche inscription and police wording remain for the letterer. The small incidental Minseok photo was drawn from the written design, as allowed by the 27 October README; no unapproved character sheet was used. Only approved river, rooftop and office images were passed as image references, with at most two references in a call. No new output or reject was reused as a reference. Nothing was uploaded or published.
