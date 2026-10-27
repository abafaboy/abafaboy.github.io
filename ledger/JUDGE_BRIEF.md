# Chapter judge: brief

**Why.** The owner's standing order (27 October 2026): "after each chapter is finished, give it to a reviewer judge to rate it out of 10". Each finished chapter (lettered and rendered) goes to a fresh reviewer agent that has not seen how it was made. Claude fixes what the judge finds, where a fix is possible, before the chapter is uploaded.

**The judge sees only what a reader sees:**
- the lettered vertical strip, cut into pages (`page_NN_Pxx-Pyy.jpg`; `index.md` gives the order);
- the narration (`narration.md`): what the YouTube narrator reads aloud, panel by panel, while the strip scrolls.

It never sees the scripts, briefs or Claude's reviews, so its view stays independent.

**Reports:** `ledger/judge/chNNN.md`. Claude adds a "What Claude did" section under each report.

---

## The prompt for each judge

> You are an independent judge for the webtoon *My Summons Go First*. Rate chapter N strictly, as an experienced manhwa editor who also reads like a fan. Read `/home/claude/msgf-bible/ledger/JUDGE_BRIEF.md` (the rubric and the series background), then the reading pack in PACK_DIR: `index.md`, every page in order, and `narration.md` alongside. Look at every page; don't skim. Write your report to REPORT_PATH in the format the brief gives, and change no other file.

## Series background (what a reader would know)
- **The premise.** Modern Seoul has gates to monster dungeons. Hunter guilds hire F-rank "trap-testers" and send them in first, as bait. Kang Jaeha has walked into 312 dungeons as bait and never killed anything; he survives by thinking. Used as live bait for a boss, he spends his last summon to shield a rookie, and something from beyond the gates answers: his summons, strange people from the other side, now go first.
- **The main cast and what never changes** (a reader notices when these flip):
  - **Kang Jaeha** (the lead, 178 cm): messy near-black hair with a long fringe over his LEFT eye, a yellow pencil behind his RIGHT ear, a safety-orange trap-tester vest over a grey hoodie, with a big white T patch on the back and a small one on the right chest, and black fingerless gloves.
  - **Nib** (a goblin scout, 105 cm, his head at a man's belt): an adult veteran, never a mascot.
    - a white mask over his LEFT eye; amber eyes;
    - a V-notch on his LEFT ear only, and one fang, on the LEFT;
    - a charcoal hooded cloak and a long red scarf; binoculars;
    - two knives, never three; bare feet.
  - **Song Yerin** (a rookie healer, 155 cm): small and freckled, an oversized off-white jacket with mint trim and a mint cross on the left sleeve, and a pink first-aid bag.
  - Chapters 2–5 also have a giant armoured knight (a cracked LEFT pauldron, nine towers on his sigil) and others; judge them by their consistency from panel to panel.
- **Format.** A vertical-scroll webtoon, read on a phone. Balloons and captions often sit in the gutters between panels. Glowing "system windows" are part of the world.

## The rubric
Score each out of 10. Half points are allowed.
- **Art:**
  - drawing quality, anatomy and proportions;
  - scale between characters and objects;
  - perspective and camera;
  - backgrounds, colour and light;
  - each character's design staying consistent from panel to panel;
  - any machine-made look: warped hands, melted or garbled detail, faces that change, plastic rendering, wrong numbers of fingers or weapons.
- **Storytelling:**
  - can a reader follow what happens from panel to panel without the narrator?
  - acting and expressions;
  - pacing: panel sizes, spacing and beats;
  - the opening hook, and whether the ending makes you want the next chapter.
- **Lettering:**
  - legible on a phone;
  - balloon placement and reading order;
  - balloons never covering faces or key action;
  - tails pointing to the right speaker;
  - captions, sound effects and system windows.
- **Narration:** the narrator's script.
  - Is it clear and vivid, and in step with the panels?
  - Does it add to the balloons rather than repeat them?
  - Does it never contradict the art?
- **Overall:** your own judgement of the chapter as a reader's experience. It is not an average.

**Calibration.** Use the whole scale, with no grade inflation:
- **10:** the best chapters of the best series (Solo Leveling at its peak, Omniscient Reader);
- **8:** a strong WEBTOON Originals chapter;
- **6:** a good Canvas / indie chapter;
- **4:** clearly amateur;
- **2:** broken.

## The report format (write exactly this shape)
```
# Judge: chapter N, <title>
**Overall: X/10**

| Art | Storytelling | Lettering | Narration |
|---|---|---|---|
| x/10 | x/10 | x/10 | x/10 |

<One paragraph: the verdict, as you would tell the creator.>

## Strengths
- (up to 3)

## Problems, most damaging first
1. **[page_NN, Pxx]** what is wrong, and the fix. (Up to 12 items. Name the page file and the panel id every time.)

## To gain one point
<The two or three changes that would raise the overall score most.>
```
