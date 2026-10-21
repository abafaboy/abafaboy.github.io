# CODEX SCRIPT BRIEF: write chapter scripts for "My Summons Go First"

Claude wrote chapters 1–22 (`scripts/ch001.yaml` … `scripts/ch022.yaml`). You write the rest of Part One, in batches, one Codex chat per batch. Several chats work at the same time, each on its own chapters, so write only the files your task names.

## 1. Read first, completely
- `bible/STORY_BIBLE.md`: canon (world rules, cast and voices, motifs, the foreshadowing ledger in section 8, chapter craft in section 10).
- `bible/PART_ONE_BEATS.md`: your arc's header, and the sections for your chapters plus the chapter before and after. Deliver every beat listed for your chapters, in order.
- `bible/SCRIPT_FORMAT.md`: the YAML format, including "Letterer features". Follow it exactly.
- `bible/ART_BIBLE.md`: Part A (art briefs, the A4 colour script, A5b chibi), B3 bubble types, B4 system windows, B5 phones, and Part C.
- `scripts/ch001.yaml` (the gold standard) and at least two of Claude's later scripts (for example `scripts/ch013.yaml` and `scripts/ch019.yaml`): match their detail in art briefs, their lettering and their voice.
- `ledger/CONTINUITY_TODO.md`: rulings already made and open issues.
- `world/LOCATIONS.md` (partial) and `locations/<id>/notes.md` with the key images: the drawn location keys are canonical for how a place looks. Use those ids in `locations:`.
- `characters/<id>/`: the model sheets. Use these ids in `who:` and in art briefs.
- The previous chapter's script, if it exists when you start: its last 10 panels and its end card. It may still be being written by another chat; if it is missing, work from the beats.

## 2. Write `scripts/chNNN.yaml` (three digits) for each chapter in your task, in order, and no other file except your report

## 3. Requirements (checked)
- 45–65 panels, including the title card (`kind: title`, after a 2–6 panel cold open) and the end card (`kind: end`, with a `chibi_gag` and the next-chapter teaser).
- Every beat for the chapter, with the HOOK as the final story panel (shape tall or bleed).
- At least 3 `silent: true` panels, 1–3 `style: chibi` panels on comedy beats, at least one extreme close-up, at least one big reaction, never more than two consecutive panels from the same camera position, and a varied mix of shapes.
- Each bubble at most 18 words; split and chain longer lines. All dialogue in CAPS. Taeo's floating narration (`type: float`) at most 6–10 lines per chapter, short and honest, never explaining what the art shows.
- Voices: Nib speaks in short declaratives, deadpan, no small talk. Taeo is polite, tired and dry, and says sorry too much. Everyone else keeps the voice the bible gives them.
- Art briefs: model-sheet ids and outfits, pose and ACTING (the emotion on the face), location id, light source, palette (A4), props, and what must not appear. NEVER ask for text, bubbles or SFX in the art; signs, tags and boards stay blank (the letterer writes any story-critical word with a `label` ui entry).
- Keep Nib adult and never cute outside chibi: the V-notch in his LEFT ear, one lower fang on the left, brown rope belt, pouch on the RIGHT hip, brown wooden sheath on the LEFT hip, barefoot until he buys boots in ch 43.
- Screens: write "screen: green" in an art brief ONLY when the same panel has a `ui` entry with `on: screen` that fills it. Any other screen is dark or plain shapes. For a plain "reads his phone" beat, prefer a kit phone hand (`art: "KIT HAND"` plus `hand:` in the ui entry).
- Lettering placement: at most 3 lines per panel. Lines on inset-l, inset-r, narrow-l and narrow-r panels sit in a column beside the panel: keep those at most 12 words and never use shout or intense there. On a panel with an `intro:` nameplate, keep the lower-left corner of the art plain and put the speaker whose line falls below the panel on the right (`side: r`).
- System windows use the kit kinds (system.notice, system.notice_small, system.window, system.summon_card, system.warning, system.log, system.glitch). Phone screens use phone.* kinds; TV uses tv.lowerthird.
- Foreshadowing: place every ledger plant and payoff due in your chapters (section 6). Log each in that panel's notes as "PLANT Pxx" or "PAYOFF Pxx". Keep the motifs (bible section 7) alive without explaining them.
- Continuity: start where the previous chapter's hook leaves off and end on your chapter's hook. Times, prices, counts and ages must match the bible and earlier chapters.
- Make it genuinely good: real laughs, real ache, natural dialogue, stakes, and a hook that makes the next chapter unmissable.

## 3b. Clarity rules (from the owner's feedback on chapters 1–4)
Follow every rule in `SCRIPT_CLARITY_BRIEF.md` section 3. In short:
- every spoken line comes from someone drawn in that panel, or is marked `offpanel:<id>` with the side they stand on;
- in a close-up, only the person shown speaks, plus at most one off-panel line;
- the dialogue is plain enough to follow at scroll speed;
- full bodies go in tall, bleed or full panels, never in strips.

## 4. Validate
After each chapter run `python tools/validate_script.py scripts/chNNN.yaml` and fix every ERROR (and every warning you sensibly can) before you start the next chapter. If PyYAML is missing, install it with pip.

## 5. Rulings and locked details (from chapters 1–22)
- The calendar: ch 1 is Tuesday 14 March; the classification review is Saturday 8 April (ch 9); ch 10 is Monday 10 April.
- The link: the amber pulse always shows in Taeo's RIGHT palm. Orrin's pulse (from ch 25) is slate-green. Give Sera, Kesh and Dara their own colours when they link, and record them in the notes.
- The knock: two knocks from outside mean "come back", three from inside mean "coming" (lettered TTOK TTOK). Radios die at a threshold unless Ryu's survey line is intact (a white cable with a blue band every metre and a grey relay tripod every 50 m).
- Return marks: a thin cold-white ring with a violet edge on the wrist inside a gate; it fades outside.
- Nib's props: the pale-blue ID card (ch 9), his folded PAPER drawing of his watch post, Eunchae's cobalt-blue pencil with Kett's mark (a little three-line fork) carved near the eraser, a small green dinosaur sticker on his pouch flap (from ch 8), matte black 8x30 binoculars on a black woven strap knotted at the LEFT side of his neck (from ch 19, Kett's mark scratched on the hinge). From ch 43 he wears the boots he chose (describe them precisely in ch 43 and keep them identical after).
- Taeo's props: the olive backpack with the faded orange shield-and-open-door patch, a knock-off of the OLD design of Han Seoryun's team patch; the dark grey phone with a hairline crack in the top-left corner and a green dinosaur sticker; one mole under his RIGHT eye. Recoil from carrying shows as bruising on his forearms and nosebleeds.
- Seoryun's current team patch has a redesigned door ("THAT'S FROM BEFORE WE CHANGED THE DOOR", ch 39).
- Places: Taeo moves from his flat to a container home at the Ryu yard in ch 28 (location id `ryu_practice_yard`; `ryu_yard` is an alias). The crew's first base is an old tyre-shop compound in a Mapo gate zone (ch 33).
- Characters without a finished model sheet (sheets are being drawn): `seonhee` (Ryu Seonhee, about 55, Minho's mother, runs Ryu Survey's books), `dongsik` (Ryu Dongsik, about 58, Minho's father, uses a wheelchair since a survey accident), `bluebird_collector`, `meridian_officer`, `baek` (Director Baek Hojin of Seoul Meridian Guild, about 55, tall, silver at the temples, navy field-command coat over a dark suit, calm and reasonable), `yeo_ara` (Seoryun's new vice-captain, about 30), `kang` (Seoryun's former vice-captain, memory only), `taeo_young` (Taeo at 14), `taeo_father`, `taeo_mother`, `do_gangjin` (Iron Vow's elite junior captain, about 22), `ironvow_captain`, `coop_chairman` (Haeseong fisheries co-op, about 72), `ilan` (Sera's younger brother, about 19), `aao_supervisor` (Chae's unnamed supervisor). Kesh, Dara and Kett sheets are still being drawn. Describe any of these fully in the art brief of their first panel in each chapter.

## 6. Chapter facts (plants and payoffs due, and key details)
- 23 "Same Kind": PLANT P11 (two fragments of the same kind add 0%); route-alignment window 3 opens (terrace clay + copper moss); hook: Orrin's invitation [ACCEPTED].
- 24 "Too Big for the Door": Orrin arrives (adult stoneback carrier, `characters/orrin`); he pins the bed and cracks the window of the 18 m² flat (see `locations/taeo_flat/`: window centred opposite the door, a narrow balcony outside it); the ladder truck lowers him from the balcony at night; give him an `intro:`; "YOU FIRST." with a bucket of water.
- 25 "I Am Not Equipment": Orrin's registration (Dr. Pyo again); hook: [LINK: 2], two pulses, amber and slate-green.
- 26 "Fair and Square": Minho beats Taeo fairly at the AAO practical; Minho's ₩310,000,000 Bluebird debt; Taeo must vacate in 30 days.
- 27 "Sandbags": [LOAD SHARE] named (15%, control test); purple forearm; Sejin becomes paid safety officer.
- 28 "Moving Day": packing the family photo, the patch and the ch 2 mug; the container home; the first found-family dinner; Eunchae fails her practical by 2 points.
- 29 "Paperwork": the Bluebird standoff over Orrin; Dami's porters form a human wall; PAYOFF P04 (Granny Moon mends Nib's shorts in silence; he carves Kett's mark on her counter; she goes very still).
- 30 "The Rim": "YOU MEASURED ME. YOU DIDN'T ASK ME."; the rim brace; contracts at Terrace Gate; Nib pays part of the ₩2,000,000 entry fee; hook "KNOCK WHEN YOU WANT ME BACK."
- 31 "Two Pulses": inside Terrace Gate under a green dusk sky; the dreams at the ledge rest (Nib: "ONE DAY I WALK HOME ON MY OWN FEET. THROUGH A DOOR I CHOSE."; Orrin: "A GARDEN ON A ROOF. PEOPLE UNDER IT ARGUING ABOUT DINNER."); Nib carves Kett's mark.
- 32 "Change the Angle": [LOAD SHARE 21%]; the bridge-boss falls into the void; "EAST TERRACE. CLEAN."; the horn is window 4's first fragment.
- 33 "Surplus" (ARC III FINALE): ₩38,000,000 in equal thirds; the tyre-shop base; Eunchae passes; Seonhee cries; PLANT P22 continued (a Sunline billboard changed with her sponsors; ch 3 P27 showed a Haneul Air banner on a World Cup-ro building); hook: the Sinjeong Station underground-arcade surge alert.
- 34 "Surge" to 37 "Down": the Sinjeong arcade surge, the bidding system, Seoryun arriving unasked, Side Passage F, Baek, the wrong map, the ₩60,000,000 cluster left behind, Orrin's shell cracking. PLANT P12 in ch 36 (an old Seoryun clip: she hands command to her vice-captain and takes it back 10 seconds later).
- 38 "The Last Person Out": Seoryun's famous image, live; Dami unfilmed.
- 39 "Good Work": PAYOFF P03 begins ("NIB, WAS IT? GOOD WORK."; "THAT'S FROM BEFORE WE CHANGED THE DOOR."; "WHY THE PATCH?").
- 40 "Why the Patch": PAYOFF P03 and P06 (the Seogang camp collapse; "YOU WENT BACK FOR PEOPLE LIKE HIM. NOBODY WENT BACK FOR HIM."; Kang; the rescue-network bill); hook: the Thursday training exchange.
- 41 "Exchange": Yeo Ara; online hate ("GOBLIN SMUGGLING PEOPLE?"); an exchange-gate sample (window 4); hook: Grandpa at the yard gate.
- 42 "The Plaque": PLANT P13 (the Long Night plaque, "ANOMALOUS ENTITIES: 0", lettered with a `label`; Granny Moon's flower); hook: the fresh bruises.
- 43 "The Year the Door Didn't Open" (FLASHBACK, muted palette): Taeo at 14, baby Haru, the funeral, the broadcast on the grandparents' old TV, the knock-off patch from a market stall; present day: Nib buys boots ("IF YOU'RE CARRYING, I'LL WALK PROPERLY."); PAYOFF P06; hook "SHOW ME YOUR ARMS."
- 44 "Not Fine": the promise ("TELL US. EVERY TIME."); "HE STAYS OUTSIDE. I BRING ME BACK. HE BRINGS THE REST."; hook: the father's porter ID ("Day 3. Foreman says we go in first. Taeo's birthday next week.", a `label`).
- 45 "Arcade Glass": PAYOFF P11 (a new kind drives the adventure); [ROUTE ALIGNMENT 100%]; the crew rules on the container wall ("1. ASK FIRST." / "2. ANYONE CAN LEAVE." / "3. EVERYONE COMES BACK."); "WHO'S ASKING?" / "WHAT'S THE PAY?"; hook: [ACCEPTED] and a drawn bow.
- 46 "Who's Paying?": Sera arrives (`characters/sera`, give her an `intro:`); PAYOFF P07 ("THAT'S THE WHITE BIT.").
- 47 "Not for Free" (ARC IV FINALE): the paid emergency rate; the bill fails in committee; Taeo registers for the operator licence exam; Minho's cake; hook: the exhibition poster (REMOTE OPERATIONS).
- 48–51: exam culture, Park Doyun the examiner (`characters/park_doyun`), the bracket draw, Sunline and BangBang (`characters/sunline`, `characters/bangbang`), the loss and the viral clip. PLANT P14 across 50–52 (Haein's reservoir prototype leaks; `characters/haein`).
- 52 "Leaks": "0.8 SECONDS IS ENOUGH. IF I KNOW WHERE THE HIT COMES FROM."
- 53–59: bank-and-release drills, Iron Vow (`do_gangjin`), "LIKE BEING PICKED UP BY THE NECK.", Sunline's record and "GOOD ANSWER.", the semifinal, the chant, the 0.8-second win, Haru's missed presentation.
- 60 "Saturation": PAYOFF P14 (the device saturates and breaks while cushioning a fall).
- 61 "Yes": "YES. MY SUMMONS GO FIRST. THEY'RE BETTER AT IT THAN ME. AND I MAKE SURE THEY COME BACK."; #MYSUMMONSGOFIRST; PLANT P22 (a third Sunline billboard).
- 62 "The Photograph" (ARC V FINALE): hook: the Chungju river gate and the carved settlement sign.
- 63–67: PLANT P15 across 63–67 (a repeating warning from a team that denies sending it); 64: the porters' fund ("NOBODY SIGNS A DRAW LOAN ALONE."), echo coral, [ROUTE ALIGNMENT 100%]; 65: Kesh arrives (PAYOFF P11); 66: PLANT P16 (Kesh recognises a relay "style") and the Arrival Work Permit Bill; 67: the echo of Taeo's own voice.
- 68–69: the clock tests, "IT'S A LOOP.", the river predator, [ROUTE: CHANNEL B CLEAR].
- 70 "Sponsor": PAYOFF P05 (the Arrival Work Permit passes its first reading); "GO B. THE SYSTEM SAYS IT'S CLEAR."
- 71–73: Sera dragged and nearly loses the arm; PLANT P17 in 72 (the predator mimics voices but never knocks); "YOU TRUSTED A WINDOW OVER MY EYES."; "YOU CAN BE SORRY AND STILL BE USEFUL."
- 74 "There Was No Knock": PAYOFF P17.
- 75 "Sorry Properly". 76 "One Word": PAYOFF P04 (Granny Moon speaks the scouts' word for "watchman"; the older carved mark on her counter). 77 "The Loop": PAYOFF P15 (a delayed relay loop, not time travel).
- 78 "The Shot": the river battle; "THEY'LL SING THAT ONE." 79 "Aftermath": the public test record; Chae's cooperative path; the message cylinder.
- 80 "Responsibilities" (ARC VI FINALE): PLANT P18 (Ilan's dated message); "GUILD CHARTER. RULE 1: ANYONE CAN LEAVE."
- 81–84: the licence requirements; Baek's offer; the Yeoju anchor field; the Haeseong fisheries co-op (`coop_chairman`); field ore and [ROUTE ALIGNMENT 100%].
- 85 "Dara": Dara arrives (PAYOFF P11). 86 "Field Practice": Taeo's irregular heart rhythm; Iron Vow's captain at the gate.
- 87 "Dialysis": PLANT P19 (a clinic's dialysis machines run on processed fragments); hook: VENN LOGISTICS on the canisters.
- 88 "Fault": PLANT P20 (a modified anchor fails with a strange pulse fault; Haein logs it).
- 89 "Two Thresholds": Doyun's apology; "ACCEPTED. YOU FIRST."
- 90 "Minho's Deal": PLANT P21 (Minho refuses Baek and still promises a support crew); ₩210,000,000 committed; "NEXT TIME, ASK ME BEFORE YOU BET MY LIFE TOO."
- 91–93: the crew-vote rule (bets over ₩50,000,000); Chae's promotion; Haru's re-run date; Iron Vow's displacement; dawn at Yeoju, two knocks and three.
- 94 "Yeoju, Day One": PLANT P20 again (a second Venn anchor, "SAME FAULT.").
- 95–96: "NIB. WHEN I KNOCK, YOU JUMP."; the re-run in Haeseong; "GOOD. NOW WIN."
- 97 "Counterstroke": PAYOFF P21 (Minho's coalition crew arrives as promised).
- 98 "Everyone Comes Back": WINNER: YOON TAEO'S CREW.
- 99 "Fair Rent": the four-storey building in the Hapjeong gate zone (Eunchae's at fair rent, Sejin and Dara's clinic, rooms, Orrin's roof garden); PAYOFF P10 begins (coalition members say no and nothing breaks); hook: Dr. Pyo with a plant.
- 100 "Their Name Over the Door" (PART ONE FINALE): the GO FIRST sign; the welcome cup (Taeo drinks first); Dami and two young porters with GO FIRST patches; Seoryun's wreath; the family; PAYOFF P02 and P04 (Granny Moon hands Nib a cloth embroidered with Kett's mark: "SOMEONE IS ASKING ON THE OLD LINE FOR THE SCOUT WHO LEFT HIS POST."); P10, P19 and P20 hooks into Part Two (the clinic's dialysis machines fail on Venn fuel); last panel: the open door at night, TO BE CONTINUED — PART TWO: THE OTHER BANK.

## 7. Report
When your batch is done, write `scripts/REPORT_chAAA-chBBB.md`: for each chapter the panel count, silent and chibi counts, bubble-type counts and any beat you could not fit; then every continuity fact the next writer needs (time, place, props, injuries, money, who is where). Do not stop to ask questions; finish the batch.
