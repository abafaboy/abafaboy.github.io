# My Summons Go First — Chapter 2: A Place to Sit

61-panel source and artwork production. Script is approved for the complete first meeting in Taeo's apartment. The approved larger Nib reference is included as approved_model.png. The chapter-specific dialogue correction is “I saw a summon at work.”

## Art and continuity

See ART_BRIEF.md. Script and character model are the shared authority for all art batches. Original generation outputs, prompt records, revisions, and final crop manifests are retained. Layout uses actual artwork and separately rendered lettering. The final publication is a raster-page PDF: it contains no embedded font program. No font files are included in the source package.

## Font and rebuilding

The user's licensed Anime Ace font must be supplied privately through ANIME_ACE_FONT. See FONT_LICENSE_AND_REBUILD.txt. The editable script, prompts, original art, layout geometry, source code, QA records and reader render files are retained for rebuilding. A complete render requires current independently reviewed art SHA-256 entries in qa/independent_raw_review.json.

## Final reader and review

The completed reader has 61 panels on 31 raster pages. All 58 script lettering items are retained. Independent source-resolution and actual 390-pixel reader checks are recorded by source/page SHA-256 under qa. The final technical audit verifies the exact current art and page hashes, canonical text, PDF size, page count and absence of embedded fonts.

Run build_chapter.py to rebuild all panels and pages, then audit_final_reader.py to verify the current output. package_source.py preserves every original artwork revision, prompt, final crop/layout and review record. The source archive contains no font binaries. Source_File_Index.json provides per-file sizes and SHA-256 values.
