# Clarity pass: chapters 1–4

Completed against `SCRIPT_CLARITY_BRIEF.md`, the script format, section 3 of the script brief, and the story bible. Existing drawings were checked for speaker positions. Chapter 1 has no preceding chapter; subsequent chapters were checked against the preceding chapter's ending.

Only `ch001.yaml`–`ch004.yaml` and this report were edited in the project. Original panel IDs, order, story events, hooks, money, deadlines, and plant/payoff notes remain. Every protected field on all 224 locked story panels is unchanged, as are the UI entries. No chapter artwork was changed.

## Line counts

Counts refer to original line entries. Categories overlap: a rewritten line may also have moved or had its side corrected. When original lines were combined, each original whose wording changed counts as rewritten. “Newly off-panel” excludes lines already marked off-panel.

| Chapter | Rewritten | Moved | Newly off-panel | Side corrected | Panels | Taeo floats |
|---|---:|---:|---:|---:|---:|---:|
| ch001 | 27 | 0 | 7 | 29 | 55 | 8 |
| ch002 | 30 | 0 | 3 | 24 | 61 | 4 |
| ch003 | 35 | 5 | 6 | 41 | 61 | 5 |
| ch004 | 70 | 3 | 4 | 58 | 62 | 6 |

No panels were added, split, merged, removed, or renumbered.

## Chapter 1

Named the sale, shifts, golem, aisle crack, baskets, and eggs where the original wording left the referent uncertain. Combined the manager's introduction and stocker announcement to fit three lines. Matched sides to the actual drawings, including the manager/courier exchanges and Eunchae/Taeo outside. Marked the absent speakers in the video-call panels and Taeo's foreground-hand shot. Urgent inset dialogue now uses permitted bubble types.

Unlocked framing: P54 keeps its bleed shape; its brief now places Nib in the centre and Taeo on the right, with room for both bodies.

### NEEDS REDRAW

No remaining speaker-identification blocker requires new art. Locked body-layout problems remain: P09 and P41 put full chibi figures in insets; P16 fits the departing courier and golem into a narrow panel; P17 shows too much of Eunchae's standing body in an inset; P37 uses a strip for a conversation between two torsos; P40 crowds two standing figures into an inset. These require a new frame/crop or a full/tall composition in the art pass.

## Chapter 2

Made the return request, name card, mug placement, phone, command comparison, and Kett's empty post explicit. Kept the open-door choice, cup test, “YOU FIRST,” “I'M NOT THAT ONE,” apology, glitch, and three-day hook. Hand-only and kit-phone speech is marked off-panel; close-up replies have at most one off-panel line.

Unlocked framing: P21 changed from strip to tall. Nib now stands centrally at the door with his entire adult figure given space.

### NEEDS REDRAW

No remaining speaker-identification blocker. P19 compresses Taeo's seated figure into an inset; P23 uses a narrow frame for his full seated figure; P24 places two full chibi figures in an inset; P50 crowds the kneeling/seated blanket exchange into an inset. Give those bodies a full/tall frame or a closer crop.

## Chapter 3

Kept the receptionist's correction from “it” to “him,” the Sunline/Haneul Air plant, Seoryun's rescue line, patch reveal, Kett plant, and Kanghan hook. Clarified the fan ranking and assessment language.

Five original lines moved to adjacent panels: the appointment instruction P13 → P12; Taeo's surprise P12 → P13, combined with his correction; Nib's screen question P29 → P28; Nib's counting question P29 → P30; Chae's “GOOD” P43 → P44, combined with her test instruction. The screen insert now has only one off-panel reply.

Unlocked framing: P39 changed from wide to tall, showing Nib's full figure while he recalls his post. P40 retains its vignette and P41 its inset; their briefs now specify centred portraits and clear off-panel geography.

### NEEDS REDRAW

No remaining speaker-identification blocker. P22 crowds the two figures in the recessed doorway into an inset; P26 fits Nib and the standing schoolgirls into an inset; P32 contains full chibi figures in the revolving-door inset; P33 shows Nib's standing figure in an inset; P46 puts Taeo's full leaning chibi figure into an inset. The standing groups in wide P16, P18, P25, P31, P42, and P49 also need the room required by the new body-framing rule.

## Chapter 4

Explained the arrival category, thirty-day protection, pressure test, survey search, written assessment, and observation offer. Kept the first amber pulse and two-successes/one-miss sequence. Corrected P29's “MY LEFT” to “MY RIGHT,” matching the art brief, notes, and canon. Pyo's offer now makes the proposed living arrangement explicit; Taeo still fails to refuse and the lunch-count hook remains.

Three original lines moved to adjacent panels: Chae's 1995 explanation P07 → P06; her arrival definition P08 → P09, combined with the existing explanation; Taeo's apology P09 → P08, where he is visible. P02 and P40 each combine their insert speech into one off-panel spoken line.

Unlocked framing: P21 changed from wide to tall and reconciles the camera with the right-shoulder art description. P41 changed from inset-r to full, with Taeo left, Nib right, and Chae in the centre background.

### NEEDS REDRAW

No remaining speaker-identification blocker. P15 and P31 use narrow frames for full standing figures; P19 puts two full chibi figures in an inset; P51 draws Nib's whole body inside a nominal close-up inset. The standing/full-body groups in wide P08, P12, P18, P35, P36, P42, P47, P48, P52, and P58 need a full/tall composition under the new framing rule. Locked Chae/Pyo nameplates sometimes share their speaker's centre position; their sides were kept truthful to the drawing rather than moved to the right for the nameplate convention.

## Validation and limits

Each chapter returned **OK** from `python tools/validate_script.py` before the next chapter's revision began. The completed files also pass together without warnings. Additional checks found no changed protected fields, changed panel IDs/order, panels with more than three total lines, missing spoken-line sides, or close-ups/inserts with more than one off-panel spoken line.

Tall/bleed counts are 4/55, 5/61, 6/61, and 3/62 respectively. The quarter-chapter target remains unmet because nearly all framing is locked; reaching it requires the art/layout pass. Existing locked art briefs and notes retain their original wording, including historical dialogue quotations. Only the performable lines and the identified unlocked framing were revised.
