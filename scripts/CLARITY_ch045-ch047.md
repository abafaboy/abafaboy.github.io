# Clarity pass: chapters 45, 46 and 47

Scope: only scripts/ch045.yaml, scripts/ch046.yaml, scripts/ch047.yaml, and this report. Read SCRIPT_CLARITY_BRIEF.md, SCRIPT_FORMAT.md, CODEX_SCRIPT_BRIEF.md section 3, the story bible's cast and foreshadowing ledger, the three complete scripts, the last ten panels of ch044, and the chapter 45-47 beats. No images generated.

Counts compare each final line with its original source. Rewritten means the text changed; moved means the line changed panel; marked off-panel means a new `offpanel:` prefix; corrected side means an existing `side` value changed. The categories overlap. Added speaker positions in art briefs are not counted as side corrections.

| Chapter | Rewritten | Moved | Marked off-panel | Side corrections | Added lines | Panels | Tall/bleed |
|---|---:|---:|---:|---:|---:|---:|---:|
| 45 | 35 | 0 | 6 | 15 | 0 | 52 | 15/52 (28.8%) |
| 46 | 39 | 0 | 1 | 15 | 0 | 53 | 15/53 (28.3%) |
| 47 | 48 | 0 | 8 | 5 | 0 | 62 | 17/62 (27.4%) |

Before this pass each chapter had 10 tall/bleed panels. No panels were added, split, merged or renumbered, and every chapter stays inside 45-65 panels. Existing title and end cards, chibi and silent flags, SFX, UI entries, continuity notes and plant/payoff notes were preserved. Every chapter keeps its story beats and its final hook. Only the `shape`, `camera`, `art`, `calm` and `lines` fields of panels were touched (a field-by-field comparison of the originals and the finals confirms it).

## Chapter 45: Arcade Glass

Named what the crew holds and why: the three Sinjeong fragments were taken before the ceiling fell and not from the abandoned cluster; a repeat stone kind gives zero; arcade glass is the new kind; the contact window is something the crew can use to invite someone. Wrote out the rules dialogue so each rule line names its subject (Sejin's "RULE ONE COVERS MEDICAL HELP TOO. WE ASK BEFORE WE OFFER.", Nib's "ANYONE CAN LEAVE. EVEN WHEN WE NEED THEM.", Orrin's "THE THIRD RULE SHOULD BE: EVERYONE COMES BACK."). Restated Grandpa's promise in full ("REMEMBER YOUR PROMISE. YOU TELL US EVERY TIME YOU CARRY."). Sera's questions through the seam are now short, complete questions.

Kept the ₩60,000,000 cluster left behind, both PAYOFF P11 notes, the window 4 arithmetic (horn 34 + exchange sample 33 + arcade glass 33 = 100, UI untouched), the three-rule wall labels, Taeo's invitation ("MY NAME IS YOON TAEO." / "I'M ASKING IF YOU'D COME. YOU CAN SAY NO."), Sera's "WHO'S ASKING?" and "WHAT'S THE PAY?", the equal-share terms at P43 and the unchanged bleed hook (accepted notice, drawn bow in the seam).

No lines moved. No lines added. Sera is never drawn before the hook, so all of her seam lines are marked off-panel, with `side` set to the side of the seam. P47:2 went the other way: Nib is now drawn in the widened panel, so his "YES." is a normal line.

**Off-panel attribution:** P37:1, P40:1, P43:3, P45:1, P45:3, P47:1.

**Side corrections:** P06:1, P06:2, P09:1, P14:2, P19:1, P28:1, P32:1, P37:1, P38:1, P38:2, P41:1, P43:3, P44:1, P44:2, P47:1.

References use panel ID and one-based line number in the revised script.

**Reshaped panels:**

- `wide` → `tall`: P14, P16, P18, P23, P30.
- `inset-l` → `wide`: P15, P47.
- `wide` → `full`: P37.

**Camera and calm changes:** P15 and P47 (cameras no longer promise a close-up of several speakers; `calm` moved from right to top with the new wide shape) and P23 (restaged over Taeo's shoulder so the speaker is drawn).

**Framing and placement:** Added explicit left/middle/right positions for visible speakers in 30 art briefs, left room for standing or full figures, and cropped the remaining wide conversation shots at the waist. Detail shots keep the relevant hands, faces or objects. A close-up carries at most one off-panel line. Floats: 2 (limit 10).

**NEEDS REDRAW**

None. No `chapters/ch045/art/<id>.png` panel art existed for this chapter when checked; revised art/framing fields were unlocked.

**Validation:** `python3 codex/laptop_tools/validate_script.py scripts/ch045.yaml` → **OK**, 52 panels, 11 silent, 2 chibi, no warnings.

## Chapter 46: Who's Paying?

Said what is being lowered in the stand-off ("POINT THE ARROW DOWN." / "AND YOU PUT THE KNIFE AWAY."), what Taeo pays for ("I PAY FOR THE ROOM. WE AGREE ON JOB FEES TOGETHER."), what Sera praises on Orrin ("YOUR SHELL MAKES AN EXCELLENT ROOF."), and what the phone does ("THE PHONE ALSO SHOUTS." / "IT ONLY SHOUTS WHEN I OWE SOMEONE MONEY."). Replaced bare "him", "it" and "that" with names (Ilan, the sky, the request, Dr. Pyo). Made Chae's registration questions, Pyo's lobbying and Sera's conditions complete sentences, and let Sera say "AND TAEO DOESN'T ANSWER FOR ME." Fixed the typo "IM SEJIN" and made Sejin's consent request plain.

Kept Sera's entrance ("FAST. GOOD. I'M SERA. WHO'S PAYING?"), the cup runner ("YOU FIRST." and the water joke), Pyo's required "THREE ARRIVALS, MR. YOON. THE ASSEMBLY WILL WANT A WORD.", Sera's registration under the existing arrival route, Ilan's "for responsibilities" with no proof of where he is, the PAYOFF P07 notes, and the exact hook line "THAT'S THE WHITE BIT."

No lines moved. No lines added. P44 was a close-up on Taeo that also carried Sera's reply; her reply is now off-panel, which keeps the close-up to one drawn speaker and one off-panel line.

**Off-panel attribution:** P44:2.

**Side corrections:** P04:1, P06:1, P06:2, P07:1, P18:1, P26:1, P26:3, P33:1, P35:3, P37:1, P40:1, P40:2, P43:1, P43:2, P44:1.

References use panel ID and one-based line number in the revised script.

**Reshaped panels:**

- `wide` → `tall`: P03, P09, P15, P20, P23.
- `wide` → `full`: P35, P45.

**Framing and placement:** Added explicit left/middle/right positions for visible speakers in 31 art briefs, centred the single-subject close-ups (their `side` is now `c`), left room for standing or full figures, and cropped the remaining wide conversation shots at the waist. Detail shots keep the relevant hands, faces or objects. A close-up carries at most one off-panel line. Floats: 1 (limit 10).

**NEEDS REDRAW**

None. No `chapters/ch046/art/<id>.png` panel art existed for this chapter when checked; revised art/framing fields were unlocked.

**Validation:** `python3 codex/laptop_tools/validate_script.py scripts/ch046.yaml` → **OK**, 53 panels, 12 silent, 2 chibi, no warnings.

## Chapter 47: Not for Free

Made the emergency readable from the first call: "A FILM CREW IS STUCK IN A D-GRADE GATE.", the crew "WENT PAST THE WARNING SIGN", and the production company is arguing about "THE RESCUE FEE" (Minho's "THE BILL" was changed so it cannot be mistaken for the rescue-network bill later). Turned Taeo's cut-off "I CAN COVER—" into a finished offer ("I CAN COVER YOUR PAY."), made "I DID IT AGAIN" say what he did ("I DECIDED FOR YOU AGAIN."), and made the money readable in order: the fee, what it pays for, who gets what ("EACH OF US GETS EIGHT HUNDRED THOUSAND WON AFTER COSTS."). Named the equipment Nib orders left behind, Sera's "THREE STEPS LEFT" order now ends "FOLLOW NIB", and Sera's radio report says what is needed ("THE CAMERA OPERATOR NEEDS HELP WALKING."). After the rescue, the news voices name the bidding system and Han Seoryun's bill, Sejin answers Sera's question plainly ("THE RESCUE-NETWORK BILL WAS THE ANSWER."), Taeo names Ryu Survey and the licence, and Sera's "AS LONG AS EVERY JOB IS ON PAID TERMS." is a full condition.

Kept every money figure (₩3,000,000 prepaid, ₩600,000 costs, ₩800,000 × 3 shares, ₩500,000,000 equipment-grant pool in the poster UI only), the two-knock and three-knock signals (no dialogue, SFX untouched), Sera's "I DON'T WORK FOR FREE." / "AND I DON'T DIE FOR STRANGERS WHO IGNORED A SIGN.", Nib's "ASK. DON'T SEND.", Baek's "BIDDING FUNDS THE EQUIPMENT THAT SAVES LIVES.", Taeo's "ONE DAY WE'RE A GUILD. OURS.", the cake and open-door beats, and the unchanged tall hook "...REMOTE OPERATIONS." (the only ellipsis in the chapter, a real pause at the poster).

No lines moved. No lines added. Voices heard only through a phone, call or broadcast, with no speaker drawn, are marked off-panel; Minho at the gate (P06, P15) is drawn, so he stays on-panel. Minho's last line (P60) is off-panel because the strip shows only his hand.

**Off-panel attribution:** P03:1, P12:1, P13:3, P16:1, P37:1, P44:1, P46:1, P60:1.

**Side corrections:** P01:2, P04:1, P07:1, P09:1, P14:1.

References use panel ID and one-based line number in the revised script.

**Reshaped panels:**

- `wide` → `tall`: P01, P08, P11, P24, P30, P55, P59.
- `strip` → `wide`: P02, P23.
- `wide` → `full`: P35, P41.

**Camera changes:** P02 (overhead strip → waist-up two-shot, because Sera and Nib both speak), P20 (no longer says "close") and P23 (close on the route sketch → waist-up briefing with Minho and Sejin both visible).

**Framing and placement:** Added explicit left/middle/right positions for visible speakers in 26 art briefs, left room for standing or full figures, and cropped the remaining wide conversation shots at the waist. The strips that remain are details or single faces (P10, P14, P26, P29, P32, P33, P38, P42, P46, P49, P52, P60). A close-up carries at most one off-panel line. KIT HAND panels P03, P12, P16, P19 and P51 keep their art and UI; only the lines of P03, P12, P16 and P51 changed. Floats: 2 (limit 10).

**NEEDS REDRAW**

None. No `chapters/ch047/art/<id>.png` panel art existed for this chapter when checked; revised art/framing fields were unlocked.

**Validation:** `python3 codex/laptop_tools/validate_script.py scripts/ch047.yaml` → **OK**, 62 panels, 6 silent, 1 chibi, no warnings.

## Final checks

Each chapter passed the validator before work started on the next one, and all three were revalidated at the end. The three target files were mode 444; they were written as root and left at 444.

Compared the originals with the final scripts: existing IDs, chapter metadata, gaps, backgrounds, UI entries, SFX, notes, plants/payoffs, title and end cards, and silent/chibi flags are unchanged. Spoken lines all have a `side`; every drawn speaker is named in the art brief; no panel has more than three lines; no panel mixes three speakers with an off-panel line; bubbles meet the word limits (18, and 12 beside inset or narrow shapes); dialogue is in capitals; no interruption dashes remain; no run of more than two panels shares a camera; no chapter uses more than two bleed panels; and every chapter is above the quarter tall/bleed target.
