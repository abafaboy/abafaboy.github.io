# Chapter 6: The Person Outside — Audio and Follow candidate

Private handoff, not yet release-cleared. No site publication occurred.

## Prepared
- All 65 dialogue recordings match the final lettering script exactly, in source order and with original speakers. Four phone-text records and the graphic SFX remain unspoken.
- 24 kHz mono PCM master, 128 kb/s MP3, 65 WebVTT captions, and 221 measured Follow cues. Duration: 243.078625 seconds.
- 21 JPEG segments converted from the accepted, lettered 800 px reader PNGs. Actual image dimensions and final placement geometry were used. Character artwork and dialogue were unchanged.
- Opening phone-message reading hold: 14 seconds. Final phone-note hold: 5 seconds. Six other silent panels receive 3-second holds. Every silent hold has identical-position endpoint cues.
- P17 cutoff to P18 interruption: 0.10 seconds between original clips, without extra dialogue or radio echoes.
- Established continuing voices retained. Minho remains bm_daniel / en-gb / 1.00 from the prepared source clips.

## Still required before release
Actual MP3 seek-and-Follow tests in the unchanged reader at phone and desktop sizes could not start because this execution environment blocked Chromium process sockets; an authorized retry failed during environment startup. No browser pass is claimed. The full runnable tools/test_browser.py harness and four byte-verified GitHub reader runtime files are included. Run with Python, Playwright, and Chromium in a functioning environment; it checks all 65 lines at start/middle/end, silent holds, final-panel edges, native MP3 duration, manual scrolling, Follow switching, and end navigation.

No subjective listening occurred. Existing unprompted ASR evidence and its limitations are retained under qa/preparation. In particular, “Chae sent you?” and “Left?” remain priority listening-review clips. Technical signal checks and recognition do not establish performance or pronunciation approval.

## Layout
assets/series.json is the publisher-compatible chapter entry. assets/ch/006 contains the audio, captions, and reader images. assets/timing.private.json retains sample-accurate clip intervals and visual holds. recordings preserves all original source WAVs. timing preserves exact dialogue, final lettering, and placement. qa contains independent checks and explicit pending-browser status. runtime contains fetched reader files and Git blob IDs.

The publisher must integrate the Chapter 6 entry into its current series manifest rather than replace a multichapter manifest with this private single-chapter fixture. Existing chapters and prior sources must remain intact. This package authorizes no publication.
