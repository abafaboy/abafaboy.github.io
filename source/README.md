# My Summons Go First: source handoff

This is a recovery of existing production sources, not a new draft, remake, or release. Production and publishing are paused for takeover. The requested destination is the `msgf-source` branch under `source/`; do not merge this material into the live reader. The archive contains major future-story spoilers.

## Authority and status

- Chapters 1–7 were the last verified published revised edition. Chapter 8 is incomplete: P01–33 had cleared review, with P34–36 still held at the usage interruption. Chapter 9 has a finished reader but was held for story-order publication. Chapter 10 has its reviewed script, briefs, layout preparation and references; finished art is not established. Do not call 8–10 published or final.
- Current long-range planning is `revised_production/planning/PRIVATE_story_architecture_v3.md`. It explicitly distinguishes established constraints from proposed future events. Its 224-chapter spine is a plan, not 224 completed scripts. V1 and V2 are historical revisions.
- Approved chapter scripts take precedence over the planning document. Revised chapters 1 and 2 use `script_v2.md`; their `script_v1.md` files are retained for history, not current authority.
- Chapter 9's reconciled source is in `revised_production/ch009/reviewed_source/Chapter9_Reconciled/`. Chapter 10's active source is `revised_production/ch010/production/source/`. Earlier dispatch materials remain developmental history and should not silently override these sources.
- The original pre-reset story bible is included in [`historical_original_bible/ORIGINAL_DEVELOPMENT_BIBLE_TEXT.md`](historical_original_bible/ORIGINAL_DEVELOPMENT_BIBLE_TEXT.md). It is historical and superseded wherever revised scripts/planning differ. Do not import its rejected opening into the current version.

## Contents

`revised_production/` preserves scripts, panel and batch briefs, generation/edit prompts, original generated character/prop/style references, layout configurations, lettering dialogue and rendering scripts, continuity locks, and longer-range planning. Future chapter preparation beyond 10 is retained where available but is not finished publication.

`narration_and_release/` contains actual voice IDs, pronunciation/timing settings, narration and Follow tools, plus the recovered `series_release.py` implementation. `original_generated_references/` contains approved generated style-source images rather than reproduced pages from commercial comics.

`SOURCE_MANIFEST.json` records the original relative source path, bytes and SHA256 for the 1,752 recovered input files. It is preserved as the original collection manifest. `HANDOFF_MANIFEST.json` inventories every final handoff file except itself, including publisher supplements and updated documentation. Some historical files reference other original locations. They have been preserved without rewriting history; use the package paths and manifest when resolving them.

## Fonts and licensing

No font binaries are included. Comic dialogue uses Anime Ace 2.0 BB Regular by Blambot: https://blambot.com/products/anime-ace-2 ; license https://blambot.com/pages/licenses . Obtain your own appropriate licence. Existing scripts commonly use `ANIME_ACE_FONT` to select the local font. Flattened lettering is distinct from font redistribution or webfont embedding. Neutral sans-serif UI font choices are recorded in per-chapter configuration/placement manifests. DejaVu Sans, used for UI/fallback text, is also omitted; legitimate downloads and licensing are available at https://dejavu-fonts.github.io/Download.html and https://dejavu-fonts.github.io/License.html . Do not assume a font licence transfers with this archive.

No third-party comic page reproductions are included. Research links and observations in the authored planning documents are references, not licences to copy another work's artwork or dialogue.

## Publisher supplement

[`publisher_snapshot/README.md`](publisher_snapshot/README.md) documents the frozen published Chapter 1–7 placements, narration settings, final public manifest and current `series_release.py`. [`HANDOFF_INDEX.md`](HANDOFF_INDEX.md) gives entry points and chapter status. The original recovered collection remains separate from this supplement.

## Release build

The recovered `narration_and_release/chapter5_reference/tools/series_release.py` validates a finished chapter bundle and stages an append-only site release. Its commands are:

    python series_release.py validate PATH_TO_SERIES_MANIFEST.json
    python series_release.py prepare PATH_TO_SERIES_MANIFEST.json --output-root PATH_TO_SITE/manhwa/series

It checks the series/chapters/assets manifest, allowed keys, safe filenames, asset integrity and timing before staging. It never invokes Git or generates art, and it does not copy unreferenced source files. A Git push and successful Pages deployment are separate steps. The later publisher version is included at `publisher_snapshot/tools/series_release.py`; its README documents the added edition/top-mask support and a read-only validation command against existing repository assets. Do not feed this entire source archive into the public-release tool.

Lettering `build_chapter.py` scripts are chapter-specific. Preserve script/lettering IDs, accepted raw art, face-safe placements and timeline mappings; install only properly licensed fonts. The source package does not substitute for the exact referenced art/audio assets when rebuilding a complete reader.

## Deliberate exclusions and limitations

This is the text/configuration/reference source package, not a duplicate of every finished-page rendition. It excludes redundant QA renders, caches, ZIP-in-ZIP duplicates, temporary transfer helpers, all font binaries, model weights, and bulk raw panel variants / narration recordings. Those already-produced assets can be preserved separately from the publishing workspace and existing chapter archives. No missing art, voices, chapters, or storyline have been invented to fill gaps. `EXCLUDED_FILES.json` records any additional filtered source files.
