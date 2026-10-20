# My Summons Go First — revised Chapter 5: The Way Around

Completed private narration and Follow integration package: all 56 source
dialogue records are recorded, captioned and placed on a measured sample
timeline. Manager is new, explicitly authorized casting. The other five
voice assignments and all 55 prior recordings are unchanged.

No repository change, push, publication or deployment occurred. The existing
publisher remains the sole site writer. Sources, the previous partial package
and earlier Chapter 3/4 packages remain preserved.

## Deliverables

- `assets/series.json`: Chapter 5-only append input for the existing release tool.
- `assets/ch/005/audio.mp3`: libmp3lame 128 kbps narration.
- `assets/ch/005/audio.wav`: PCM16 mono 24 kHz master, **4,640,055 frames /
  193.335625 seconds**.
- `assets/ch/005/001.jpg`–`019.jpg`: exact approved-reader embedded JPEG bytes,
  1200 pixels wide. No artwork or lettering was regenerated.
- `recordings/`: 56 source-ordered dialogue WAVs with exact text, voice,
  declared phonemes, gain, sample count and SHA-256 evidence.
- `timing/timing.json`: 56 measured dialogue intervals and cast settings.
- `timing/dialogue.vtt`: 56 exact-source, timestamped dialogue captions.
- `timing/panels.json`, `qa/follow_geometry.json`: 38 panels, 56 dialogue boxes
  and 109 wrapped visual lines.
- `voices/cast_preview.mp3`: six existing source excerpts with a written index.
  No speaker labels are added to the speech.
- `qa/`: independent geometry, PCM/MP3, caption, preservation and browser
  evidence. Earlier partial-state reports are historical evidence under
  `qa/history_partial_preparation/`.

The **190 Follow cues** cover all 38 panels and both boundaries of all 56
utterances. Eight silent panels have explicit visual holds: 1, 2, 6, 7, 12,
16, 29 and 38. Five shared dialogue rows use clamped monotonic focus anchors.
Coordinates use the approved reader's actual JPEG dimensions, including
page-specific rounding from the 800-pixel lettering master.

Panel 11 SFX “THUP. THUP.” and panel 36 phone text remain unspoken. The spoken
record after the SFX keeps its original item index, `p011_l02`. Panel 36 has
a stationary three-second phone-reading hold with an explicit cue at both ends.

## Exact voice mapping

| Speaker | Voice | Language | Speed | Recordings | Assignment |
|---|---|---|---:|---:|---|
| TAEO | am_puck | en-us | 0.98 | 25 | Established |
| NIB | bm_fable | en-gb | 0.94 | 19 | Established |
| COWORKER | af_bella | en-us | 1.02 | 6 | Established |
| DELIVERY WORKER | bm_george | en-gb | 1.00 | 4 | Established |
| CUSTOMER | bf_emma | en-gb | 1.00 | 1 | Established |
| MANAGER | bm_lewis | en-gb | 1.00 | 1 | New, explicitly authorized |

Manager's direction is calm and practical. This new production choice makes
no claim of prior canon. Script and punctuation are unchanged. No unsupported
synthesis prosody control is invented; delivery has no subjective auditory approval.

Engine: Kokoro 82M v1.0 FP32 ONNX, `kokoro-onnx==0.6.1`,
`onnxruntime==1.31.0`, CPU. Model/voice-bank hashes and official source
references are in `voices/model_provenance.json`; model binaries are not
duplicated. Settings: trim true, sentence pause 0.25 s, clause pause 0.10 s,
gain `min(1.8, 0.15/RMS, 0.88/peak)`, no pitch shift or time stretch.

Established names remain Taeo `tˈeɪoʊ` (TAY-oh), Nib `nɪb`, and Chae
`tʃɛ` (one-syllable CHEH). This script has zero spoken occurrences of those
names. No additional spoken name test was introduced.

Pacing: 0.35 s per-panel dialogue lead, 0.45 s between dialogue records,
1.10 s final-line panel hold, 0.15 s transition and 1.25 s final tail. Silent
and phone-reading holds are explicit in `timing/pacing.json`. Utterances
total 98.385625 s; intended holds total 94.95 s.

## Validation and listening limits

Both source ZIPs and the approved PDF were materialized into this consumer's
executor and opened. Safe ZIP-member/CRC checks and all **867 indexed source
files** passed. The archived and separately approved PDFs differ in container
bytes, while all 19 embedded JPEG payloads, decoded pixels, page dimensions
and complete 390-pixel page renders are identical. The separately supplied PDF
remains authoritative. The byte mismatch and visual comparison are accurately
retained in `qa/source_integrity.json` and `qa/approved_vs_source_reader.json`.

Ten builder/pronunciation tests passed, including stationary phone-hold
endpoints, source/voice completeness, placeholder rejection, preservation of
output, MP3 decoded frame count and established name phonemes. Test tones
remain temporary and are absent from release assets. All 56 caption records
match source text and measured boundaries within half a millisecond.
All 55 earlier WAV hashes and five prior cast entries are unchanged.

The independent audit reconstructs all 56 unique dialogue payloads exactly
once in source order and all 142 intended zero-hold events. The reconstructed
master matches sample for sample. Master and gapless MP3 decode both contain
4,640,055 frames, with zero clipped master samples. FFprobe's MP3 container
duration is 193.392 s due to frame padding; gapless decoded and native browser
duration is 193.335625 s.

Actual MP3 and all 19 JPEGs passed private Chromium checks at 390×844 and
1440×900: 224 dialogue start/end observations, 436 wrapped-text rectangles,
224 full balloon boxes, all five shared/clamped rows, native playback/seek/pause,
manual Follow off, Follow-on realignment, sticky controls, no autoplay, silent
panel visibility, final panel 38 and the stationary phone-reading hold.
Browser screenshots are not included.

**No audio was subjectively heard.** Unprompted local `small.en` recognition
matched 48/56 isolated clips after case/punctuation normalization. `medium.en`
reviewed the eight baseline flags without source prompts or hotwords. Manager
matched exactly. Recognition of the actual full MP3 differed from the normalized
script only at “There”/“They're”; full output and isolated clip uncertainties
remain in `qa/content_audio/`.

Recognition differences are not confirmed spoken errors. No approved recording
was changed on ASR evidence alone. ASR, phoneme input and signal checks do not
approve acting, pronunciation, prosody or intelligibility. Headless playback
checks native decoding and clock behavior without an auditory assessment or
a claim about a deployed website.

## Publisher integration

Validate the append input in the publisher's own checkout:

```bash
python3 /path/to/repository/tools/series_release.py validate /path/to/package/assets/series.json
```

Use the established append workflow to preserve Chapters 1–4, synopsis and
cover. Only referenced public assets belong in the site. The audio field
references `audio.mp3`. Keep the WAV master, recordings, sources, captions,
voice preview, tooling and QA private. The approved PDF remains in Library.

Regeneration uses the exact models, `tools/requirements-lock.txt` and fresh
output locations. FFmpeg/libmp3lame and local Chromium are required. Build,
browser and optional ASR dependencies are listed separately. Tools do not
invoke Git mutation, deployment or paid APIs.

```bash
python tools/synthesize_kokoro.py --model /path/to/kokoro-v1.0.onnx --voices /path/to/voices-v1.0.bin --recordings-directory /path/to/new_recordings
python tools/build_narration.py --cast voices/cast.json --recordings /path/to/new_recordings/recordings.json --pacing timing/pacing.json --output /path/to/new_build
python tools/write_vtt.py --timing /path/to/new_build/timing.private.json --output /path/to/new_build/dialogue.vtt
python tools/audit_pcm_timeline.py --package /path/to/package_with_these_recordings --build /path/to/new_build --output-directory /path/to/new_qa
python tools/run_browser_qa.py --repository /path/to/publisher_checkout --manifest /path/to/new_build/series.json --geometry qa/follow_geometry.json --output /path/to/new_qa/browser_results.json
python tools/run_visual_hold_browser_qa.py --repository /path/to/publisher_checkout --manifest /path/to/new_build/series.json --geometry qa/follow_geometry.json --output /path/to/new_qa/browser_visual_holds_results.json
```

## Authoritative sources

| Input | Library ID | Bytes |
|---|---|---:|
| Approved reader | libfile_32d4dc8d04e48191beb29e6fc3cd80b9 | 10,427,729 |
| Source part 1 | libfile_30bb7cea50008191acdfbb4869860665 | 333,591,751 |
| Source part 2 | libfile_1c0e64b8ed348191a5be9c8d9fb07c46 | 268,742,841 |

Reader SHA-256:
`06d8f954dd19514efcda363c9a267da1de6737e7c78177b08a1d9ac2b15a70b4`.
Input hashes, file/version identities and repository provenance are in
`provenance.json`. The original source index describes the full preserved
source tree; raw artwork is not all duplicated here. Narration uses only the
approved final script and final placement manifest.
