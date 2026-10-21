# Clarity pass: chapters 034–037

Revised only `ch034.yaml`, `ch035.yaml`, `ch036.yaml`, `ch037.yaml`, and this report. No images were generated. Read the clarity brief, script format including Letterer features, script-brief requirements, story bible and foreshadowing ledger, all four original scripts, and chapter 033's last ten panels. Checked the arc's chapter beats for continuity.

Counts compare the original scripts with the completed pass. **Rewritten** means an existing line's text changed, including float narration. **Moved** means an existing line changed panels. **Off-panel** means a line newly received `offpanel:<id>`. **Side corrected** counts changes to the actual `side` field; added art staging that makes an existing side explicit is not counted. Categories overlap.

| Chapter | Lines rewritten | Lines moved | Newly off-panel | Sides corrected | Final panels | Tall/bleed |
|---|---:|---:|---:|---:|---:|---:|
| 034 | 29 | 2 | 13 | 2 | 49 | 13 |
| 035 | 23 | 0 | 8 | 1 | 46 | 13 |
| 036 | 36 | 0 | 11 | 0 | 46 | 15 |
| 037 | 26 | 2 | 11 | 1 | 48 | 14 |
| Total | 114 | 4 | 43 | 4 | 189 | 55 |

## Chapter 034 — Surge

Made the capped contract, additional dispatch fees, departure delays, and uncertain travel time explicit. Named the seven gates and pharmacy route. Kept Taeo's dry nervousness, the radio gag, Seoryun's unasked arrival, the silent first sight of her, the consenting links, and the shoe hook.

- **Added/split:** split the exchange in P12 across P12 and new **P12a**. The GMA lead's travel-time question and bidder two's answer move to P12a. The officer reads the two quotes in P12. No existing ID was renumbered.
- **Reshaped to tall:** P07, P16, P19, P22, P23, P25, P30, P34, P36, P40, P43.
- **Reshaped to full:** P08, P11, P12, P14, P20, P26, P28, P33, P46.
- **Framing and speakers:** P11 becomes a table scene rather than an insert containing two unseen callers. P20 shows both map speakers' faces. P26 shows all three people agreeing to the assignment. P31 becomes a head-and-hand crop. Added explicit positions and waist-up crops where needed. Corrected the GMA lead's off-panel side in P10 and Orrin's side in P26.
- **Validation:** ran `python tools/validate_script.py scripts/ch034.yaml` and obtained **OK before starting chapter 035**. Final validation also reports OK with no warnings.

### NEEDS REDRAW

None. No locked panel PNGs were present under `chapters/ch034/art/`; the framing changes are instructions for undrawn panels.

## Chapter 035 — Passage F

Clarified the eight-out/ten-remaining evacuation count, the return turn at the T, the displaced stone obstruction, and the intact cable beneath it. Named the stockrooms and blocked corridor instead of relying on ambiguous references. Preserved the elderly passengers, Orrin's seating jokes, the knock code, Baek's useful intervention, Nib's hurt, the shoe's move to the trestle, and Taeo's exact final admission.

- **Added/split/moved:** none.
- **Reshaped to tall:** P02, P05, P07, P11, P16, P17, P22, P25, P31, P34, P38.
- **Reshaped to full:** P06, P09, P10, P12, P14, P20, P26, P28, P29, P35, P40, P43.
- **Framing and speakers:** P06 shows both seated-conversation faces. The elder woman is visibly included in P07. P15 stays a hand/eye detail; P44 stays a head-and-shoulders reaction. Marked Minho's correction in P26 as off-panel and placed the office man and Nib clearly. Corrected Baek to the left in P19, with Taeo's answering bubble on the right beneath the nameplate.
- **Validation:** ran `python tools/validate_script.py scripts/ch035.yaml` and obtained **OK before starting chapter 036**. Final validation also reports OK with no warnings.

### NEEDS REDRAW

None. No locked panel PNGs were present under `chapters/ch035/art/`.

## Chapter 036 — My Map Is Wrong

Clarified Nib's physical smoke-and-tapping clues, the small key, the bypass route, the replacement cable loop, the lost shoes, and which girl must stay close. Kept the sixteen-person total, four-person medical handoff, twelve held below, street breach, connected cable, door wedge, Taeo's fear, and Seoryun's shield hook.

- **Added/split/moved:** none.
- **Reshaped to tall:** P01, P08, P11, P16, P18, P21, P28, P30, P31, P32, P35, P39.
- **Reshaped to full:** P04, P09, P12, P13, P19, P20, P23, P26, P37, P44.
- **Framing and speakers:** P11 gives Nib and the sock-footed boy room. P17 marks Nib's reply outside the pharmacist's close-up. P25 explicitly draws Minho with his radio, so all three speakers are visible. Radio replies and voices over object details are marked off-panel. Added clear speaker positions throughout.
- **Foreshadowing:** PLANT P12 remains in P21–P23. The vice-captain receives command at **00:24**, acts at **00:30**, and loses command at **00:34**, exactly ten seconds after the handoff. The deputy remains unnamed and is not identified as Kang.
- **Validation:** ran `python tools/validate_script.py scripts/ch036.yaml` and obtained **OK before starting chapter 037**. Final validation also reports OK with no warnings.

### NEEDS REDRAW

None. No locked panel PNGs were present under `chapters/ch036/art/`.

## Chapter 037 — Down

Clarified the outside radio role, the whole-cluster valuation, the cost to Minho's family, the remaining civilians, the lintel load, the tested 21% limit, and the child's question about Orrin. Preserved the single barrier defeating three hounds, the untouched ₩60,000,000 cluster, Minho's angry compliance, Dami's unfilmed work, the eight/four count, willing load sharing, recoil injuries, and the shell-crack hook.

- **Moved:** Minho's valuation transmission moves **P18 → P17**, where his face and raised radio are visible. Nib's promise to stay with the boy moves **P34 → P37**, immediately before Orrin's count. This leaves P34 with one off-panel question and Orrin's answer; P37 visibly contains all three speakers.
- **Added/split:** none. Existing **P32a** is retained.
- **Reshaped to tall:** P01, P06, P11, P12, P13, P21, P23, P27, P30, P32a, P37.
- **Reshaped to full:** P05, P09, P10, P14, P18, P20, P25, P28, P33, P34, P36, P40, P41, P42, P44.
- **Reshaped to wide:** P17, a waist-up view of Minho and his radio.
- **Framing and speakers:** P27 explicitly shows Minho transmitting and marks Taeo's street-side answer as an off-panel phone/radio line. P28 and P41 become medium two-shots. Marked voices outside face/detail crops and added speaker positions. Corrected Minho's side to centre in P37.
- **Validation:** `python tools/validate_script.py scripts/ch037.yaml` reports **OK**, with no warnings.

### NEEDS REDRAW

None. No locked panel PNGs were present under `chapters/ch037/art/`.

## Final checks

All four chapters pass the validator without errors or warnings. Additional checks confirmed at most three lines per panel, a side on every spoken line, no close-up with multiple off-panel voices, no three-speaker panel with an absent speaker, and at least one quarter tall/bleed panels in every chapter. Manual review checked speaker visibility and staging.

Compared every original panel against the completed scripts: existing IDs, chapter metadata, UI, SFX, gaps, backgrounds, calm zones, style, silent flags, continuity/plant notes, title cards, and end cards are unchanged. Only shape, camera, art instructions, and lines changed in existing panels; P12a is the sole added panel. No fragment is collected, no new return mark appears, and no rescue is completed ahead of its existing hook.
