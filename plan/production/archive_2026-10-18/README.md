# The Lord Who Measured Zero: records checkpoint

This branch preserves production records for the paused series. It does not
publish chapters, resume production, or establish that all original artwork has
been backed up to Git. The initial records checkpoint contained no final panel
PNGs. Subsequent recovery totals and outstanding chapters are recorded in
`RECOVERY_STATUS.json`; each recovered chapter has per-panel `PROVENANCE.json`.

The five original records are copied unchanged from
`LWMZ_Final_Paused_Archive_2026-10-18.zip`, Library item
`libfile_e57f713ba45c8191a456d6c4b04f36ac`, version 1. The source ZIP was downloaded
and verified locally: 120,653 bytes, SHA-256
`5bc95b4b978f78e1b9ede67c4743ec5585d3838e0c5eb2332a6853833743cb36`.
The four checksums in `SHA256SUMS.txt` also match the archived records.

- `ARCHIVE_MANIFEST.json`: coverage, stopped partials, correction order,
  quarantines, provenance gaps, and Library recovery identities.
- `CONTINUATION.md`: the original handoff and its historical status statements.
- `EVIDENCE_INDEX.json`: project QA and receipt snapshots.
- `FINAL_PNG_INVENTORY.json`: exact expected PNG hashes, sizes, and proposed
  archive paths for subsequent recovery. An inventory entry is not a stored PNG.
- `SHA256SUMS.txt`: checksums for the four original records above.

The original handoff describes earlier failed integration writes. Those are
historical evidence. This checkpoint uses the environment's existing native
Git origin under the user's later explicit archive authorization, without
changing credentials or network settings.

This branch starts at main commit
`8a20ca5a59315db8b79b16c9e1276151dc617564`. The source branch and observed source
head recorded inside the manifest remain historical references; this checkpoint
does not assert that it contains all files from that source branch.

All existing repository files are retained. Main, the live reader, chapter
manifests, website assets, and new-series preparation are unchanged. Raw bundles,
reference artwork, and rejected candidates remain outside this branch. Use the
manifest's exact Library identities and correction order for later final-PNG
recovery, and verify actual committed blobs before reporting artwork backed up.
