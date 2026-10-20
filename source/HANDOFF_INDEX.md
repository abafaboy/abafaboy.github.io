# Source entry points and omissions

This is the owner-approved public source handoff on `msgf-source`, under `source/`. It contains major spoilers. Production and live publishing remain paused. It is based on existing repository commit `fb4b585a8fb47f24b2d98b7d0122b4f7ac12f9a1`; no live site files were changed.

## Story authority

- [Original 44-page development bible text](historical_original_bible/ORIGINAL_DEVELOPMENT_BIBLE_TEXT.md): complete recovered text, historical/superseded. PDF pagination markers are preserved.
- [Current architecture v3](revised_production/planning/PRIVATE_story_architecture_v3.md): the full 224-chapter plan, world/power rules, characters, arcs, mysteries, foreshadowing and setup/payoff ledgers. It separates established constraints from proposed events. The original `PRIVATE_` filename is retained for provenance; its inclusion here is intentional and owner-approved.
- [Planning directory](revised_production/planning/): earlier architecture versions and developmental material remain historical. A planned spine is not a set of finished chapter scripts. Approved revised scripts take precedence where they differ.
- [Generated reference collection](original_generated_references/) and [revised production references](revised_production/references/): original generated model/style/continuity references; approved and historical usage is described by neighboring production files.

## Chapters 1–10

Chapter folders preserve scripts, panel/batch briefs, prompt text, dialogue/lettering JSON, layout preparation and reference material wherever recovered. Files named `raw/` in this curated collection mainly preserve prompts and source records; they do not imply that all raw image variants are included. Earlier candidates, repair prompts, backups and dispatch materials remain historical and must not override the reviewed/current sources listed here.

| Chapter | Script entry point | Production collection | Status at handoff |
| --- | --- | --- | --- |
| 1 | [script_v2.md](revised_production/ch001/script_v2.md) | [revised_production/ch001/](revised_production/ch001/) | Published revised edition; frozen settings in publisher snapshot |
| 2 | [script_v2.md](revised_production/ch002/script_v2.md) | [revised_production/ch002/](revised_production/ch002/) | Published revised edition; frozen settings in publisher snapshot |
| 3 | [script_v1.md](revised_production/ch003/script_v1.md) | [revised_production/ch003/](revised_production/ch003/) | Published revised edition; frozen settings in publisher snapshot |
| 4 | [script_v1.md](revised_production/ch004/script_v1.md) | [revised_production/ch004/](revised_production/ch004/) | Published revised edition; frozen settings in publisher snapshot |
| 5 | [script_v1.md](revised_production/ch005/script_v1.md) | [revised_production/ch005/](revised_production/ch005/) | Published revised edition; frozen settings in publisher snapshot |
| 6 | [script_v1.md](revised_production/ch006/script_v1.md) | [revised_production/ch006/](revised_production/ch006/) | Published revised edition; frozen settings in publisher snapshot |
| 7 | [script_v1.md](revised_production/ch007/script_v1.md) | [revised_production/ch007/](revised_production/ch007/) | Published revised edition; frozen settings in publisher snapshot |
| 8 | [script_v1.md](revised_production/ch008/script_v1.md) | [revised_production/ch008/](revised_production/ch008/) | Incomplete; P01–33 cleared, P34–36 held at interruption |
| 9 | [CH009_script.md](revised_production/ch009/reviewed_source/Chapter9_Reconciled/CH009_script.md) | [revised_production/ch009/](revised_production/ch009/) | Finished reader held for story order; unpublished |
| 10 | [CH010_script.md](revised_production/ch010/production/source/CH010_script.md) | [revised_production/ch010/](revised_production/ch010/) | Reviewed script/briefs/layout preparation; finished art not established |

Chapter 9's reconciled authority folder and Chapter 10's active production source take precedence over their earlier dispatch materials. Chapter 1–2 v1 scripts are historical; v2 is current. No missing chapter, art, voice or future event was invented for this handoff.

## Lettering, narration and release

- [Publisher snapshot](publisher_snapshot/README.md): final published Chapter 1–7 geometry/settings, selected-art hashes for Chapter 7, actual narration recipes/cast/pronunciations, final public manifest and current release-helper documentation.
- [Recovered narration/release sources](narration_and_release/): earlier tooling, pronunciation/timing settings and production preparation. The folder names do not establish publication status; in particular Chapter 10 narration preparation is not a finished chapter release.
- [Font acquisition and licensing](README.md#fonts-and-licensing): Anime Ace 2 BB and DejaVu Sans binaries are omitted; obtain appropriate licensed copies through the official sources listed there.

## Deliberate omissions

The curated input contains 1,755 files, including 1,752 manifest-listed production files plus its README, input manifest and exclusion list. The handoff adds existing publisher settings and documentation; `HANDOFF_MANIFEST.json` gives the final file list, byte counts and SHA-256 hashes (excluding itself).

Bulk native finished-panel variants, duplicate rendered readers/PDFs, narration WAV/MP3 binaries, model/voice weights, caches and redundant QA renders are omitted from this source tree. The existing repository retains the published reader/PDF/audio assets for Chapters 1–7 under `manhwa/series/my-summons-go-first/`. The source tree alone cannot reconstruct every final pixel or recording without the exact accepted external native inputs. No completeness claim is made for those omitted binaries or interrupted Chapters 8–10.

All font programs are omitted, including the restricted Anime Ace 2 BB files and the DejaVu Sans fallback. Commercial-comic screenshots/reproductions, secrets, transfer receipts/signed URLs, unrelated private data and internal coordination/memory notes are excluded. [EXCLUDED_FILES.json](EXCLUDED_FILES.json) records the original collection's file-level exclusions. The publisher supplement also omits cast coordination evidence and private Library lookup identifiers; archive filenames/member names and source hashes remain where useful for recovery. Production prompts, layouts and authored continuity/story documents are retained.

No blanket license is added to the author's story/art or the recovered source collection. Research links in planning files grant no rights to reproduce third-party art. Respect the respective tool, model and font licenses before any later redistribution or rebuild.
