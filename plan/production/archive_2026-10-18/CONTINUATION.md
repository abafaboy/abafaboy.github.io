# The Lord Who Measured Zero: final paused archive

Status date: 18 October 2026 UTC. Production stopped at the user's change of direction. This package preserves existing work. It does not authorize resuming generation, rendering or publishing.

## What is finished

- 82 chapters have complete art reported: 35–105, 107–110, 113–115, 119–120 and 125–126.
- Complete art is separate from independent visual QA, Windows adoption, video rendering and live website publication.
- Last verified new-style live chapters: 35–37, 39–40, 43–44 and 51. Chapter 38 was rendered but unpublished. This archive did not independently recheck the live site or publish anything.
- Chapters 1–34 and Volume1 remain preserved without changes.

## Exact stop points

- Chapter106: 16 producer-accepted finals; p17 raw held for glossy floor; p18 ungenerated.
- Chapter111: 16 producer-accepted finals; p17–19 unstarted; no raw-only held panel.
- Chapter116: 7 producer-accepted finals; p08–19 unproduced. The p08 pre-call record was cancelled without invocation.
- Chapter121: 17 producer-accepted finals; p18 raw withheld for exposed fingertip/bandage continuity and minor wall texture. The chapter has 18 expected panels.
- Chapter127: 12 producer-accepted finals; p13–19 unstarted.
- Chapters112,117–118,122–124,128–130 and131–222 unstarted. Source plans may exist; this does not mean art production started.
- Independent QA of these five partial chapters remains pending. All five final-stop ZIP byte counts and SHA-256 hashes were verified locally by this packager.

## How to read the archive

1. ARCHIVE_MANIFEST.json is the current status overlay: chapter groups, exact stop receipts, candidate-specific correction order, quarantines and known gaps.
2. EVIDENCE_INDEX.json preserves project QA/receipt snapshots. Earlier HOLD or PARTIAL wording remains historical; named later clearance applies only to the exact corrected panel. It is not a blanket chapter adoption grant.
3. FINAL_PNG_INVENTORY.json enumerates recent local finalized PNGs, their exact hashes/byte counts and proposed non-live Git archive destinations. It is not a complete inventory of every historic panel.
4. The original full handoff remains unchanged in Library: libfile_fb79d31539a481918b719ac831604203, Windows_Coordinator_QA_Handoff_2026-10-17.zip, 26,317,135 bytes, SHA256 118a31459ed94021f450c946d29fb1773af34d4d92c702abd0ea92d5258c456f.
5. Latest durable QA delta: libfile_042d1995806c8191b3f78f0c371d0aba (Chapter126), linking Chapter115 libfile_ddd545dee66c819190f3d8a7c88a1760 and Chapter110 libfile_e0324a48c70481919e83beac8a3c7b40, then the older chain.

## Correction and quarantine rules

Load the base first, then source corrections and named art supplements in the manifest's order. Verify exact candidate hashes; similarly named files are insufficient. Retain old bytes for provenance without treating them as production.

Important multi-step chains include Ch70 finish then leaf correction; Ch76 review then foreground corrections; Ch80 candidate v2 then supplement v3 then final p18 v4; Ch86 seven-panel then p09/p12 finish supplement; Ch89 finish v2 then hand v4; Ch107 p09 five-digit v2; Ch108 p11/p16 v2; Ch98 p14 carving correction. The full list and receipts are in the manifest/evidence.

Never adopt the accidental incomplete Ch89 hand v3 (libfile_4fd7f37ffb588191b6445ed90b8c279a) or the 19 superseded Ch49–50 intermediates (libfile_b6815d1a63548191afdd9e6a6510fc51). Do not silently mix raw-held art, rejected variants or old partial checkpoints into a complete chapter.

## Evidence limits

- Ch66 p01–05 original prompt revision was overwritten; no reconstruction is claimed.
- Ch95 p13 lacks historic reference hashes after workspace loss. Visual clearance does not repair that gap.
- Ch101 was partially lost then rebuilt; inaccessible earlier attempts were not used. Ch102–106 were later new production. Current prompts, ordered reference hashes and raw originals were preserved.
- Early receipt IDs supplied by the parent are historical evidence; missing size/hash fields are explicit nulls.
- Recent reviewer files confirm bounded passes for Ch101–105,109–110,113–115,119–120,125–126; Ch107/108 passes require their corrections. Producer stop notes saying completed Ch113–115 QA is pending are stale relative to the reviewer deltas.
- Bounded art passes do not certify face boxes, lettering, strip overlaps, audio, full decode or deployment.

## Git preservation proposal

Source branch: manhwa-pipeline in abafaboy/abafaboy.github.io. Read-only observed head: 5cf600334c4ebba4aa8b6445ea3043274f88324e. Existing source conventions store chapter scripts, briefs, layouts and QA; the inspected source chapters do not store final panel PNGs. A separate plan/production/archive_2026-10-18/ directory avoids implying production adoption.

Proposed first actual-art batch: Ch113's 17 final PNGs, 29,098,045 bytes total, under plan/production/archive_2026-10-18/art/ch113/p01.png through p17.png. Each PNG is 1,211,967–2,205,883 bytes. The local recent complete-chapter PNG inventory totals 544,373,996 bytes; partials are listed separately. This first batch is preservation only and is not a website or video release. The archive metadata must not be described as an asset upload before actual blobs and a commit are verified.

Keep full raw/reference ZIPs in Library. They are large and may contain private staging/reference assets or third-party comic references unsuitable for public Git. Do not upload them blindly. A branch commit should preserve all existing entries and use a checked expected head, never force-reset; no read.html or deployed chapter metadata changes are proposed.

## If work is explicitly resumed later

Resolve the named Library files, verify hashes/bytes, and select only independently cleared final candidates. Reconfirm current repository and computer state rather than assuming this date's status. Follow plan/production/redraw_adoption_contract_v1.json: backups before overwrite, independent production-size pixel review, fresh face measurements, strip/manual overlap QA, canonical natural-speed voice validation, full decode and encoded-frame checks, then separate deployment verification. Never claim listening when unavailable.

The cloud Ch100 experiment remains feasibility-only. Missing canonical end-card/SFX/model/dependencies and blocked Chromium launch prevented any strip/audio/video render. Its provisional layout/config/tool edits must not be published or adopted as a finished chapter.

## GitHub attempt outcome

The one permitted unreferenced-blob test for Ch113 p12.png (1,211,967 bytes; 1,615,956 base64 characters) returned GitHub 403 FORBIDDEN: “Resource not accessible by integration.” No blob SHA was created, no branch was changed, and no metadata or PNG assets were pushed. This is an integration permission rejection, not evidence of a payload size limit. No alternate write route or retry was attempted. The preservation proposal above remains unexecuted; resolve repository integration access before any separately authorized push.
