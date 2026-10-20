# My Summons Go First — Chapter 4: Something There

This source collection preserves the reviewed 55-panel script, native image-generation artwork and revisions, exact prompts, crop manifests, editable dialogue layouts, rendered lettering, and inspection evidence. It does not contain font software. Chapter 1–3 files were not modified. No website publication is part of this package.

## Reading and editing

- `script_v1.md` and `lettering_script.json`: exact reviewed story and 76 dialogue records, plus three art-owned text records.
- `layout_config.json`: authoritative selected source and crop for every panel, protected artwork, balloon boxes, line breaks and tails. Coordinates use an 800-pixel-wide master.
- `../raw/`: retained artist packages, original native outputs, selected sources, rejected/replaced versions and prompts. Folder names such as `provisional` describe the intake location, not the final verdict. Only the selected source hashes in the final review receipts are approved for the reader.
- `../qa/`: exact-hash independent raw-art and compressed-reader reviews. Older rejected receipts are retained for provenance; later passing receipts apply only to their named hashes.
- `../lettered/placement_manifest.json`: final panel/page mapping and exact lettering geometry.
- `../lettered/My_Summons_Go_First_Chapter_4.pdf`: flattened-image reader. It embeds no font program.

## Rebuilding

Supply your own properly licensed Anime Ace 2.0 BB Regular font through the `ANIME_ACE_FONT` environment variable. The original font binary is deliberately omitted. See `FONT_LICENSE_AND_REBUILD.txt`. DejaVu Sans is used for the title/footer and the exact U+2014 em dash absent from Anime Ace; the approved dash is rasterized, not silently rewritten.

Run `python source/build_chapter.py` from the production directory after installing Pillow, PyMuPDF and fontTools. The renderer refuses selected art without a matching passing review hash and crop. Then run `python source/export_pdf390.py` to render the actual compressed PDF at 390 pixels wide. Final visual QA and `python source/audit_final_reader.py` are required before release.

The native text in panels 37, 40 and 51 belongs to the generated artwork and has no separate lettering overlay. Dialogue lives in editable layout records and is composited separately. `ALLOW_PROVISIONAL=1` exists solely for explicitly authorized partial working proofs and must not be used for final release.

Final archive file hashes are listed in `Source_File_Index.json` at the package root. Intermediate compressed transport ZIPs are omitted where their extracted files are retained. No generation is implied by a rebuild; artwork is read from preserved native image files.

The complete source is delivered as three ordinary ZIP parts to respect Library’s 512 MiB per-file limit. Extract all parts into one directory; no special split-archive utility is required. Each part contains the shared full file index with its archive-part mapping. These are preservation parts, not alternative editions.
