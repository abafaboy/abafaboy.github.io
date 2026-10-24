# Manhwa craft bible: how real Korean webtoons are built

This is the rulebook for the rebuilt *My Summons Go First*. Every script, panel brief and art pass is checked against it.

## Where the rules come from

| Tag | Meaning |
|---|---|
| **[R]** | Seen directly: real episodes read slice by slice on WEBTOON (official English), Oct 2026. Notes in `MANHWA_CORPUS.md`. |
| **[K]** | Korean industry or academic source: platform data, creator surveys, PD interviews, papers. Numbered in the source list at the end of `KOREAN_CRAFT_REPORT.md`. |
| **[pacing report]** | Arc and chapter data in `PACING_REPORT.md` (partial; it says where its data is thin). |
| **[S]** | The earlier survey of 103 episode-1s (`VISUAL_SURVEY.md`). |
| **[I]** | Our own inference from the above. Treat as a default, not a law. |

**The corpus read slice by slice (13 episodes):**
- *Omniscient Reader* (ORV) eps 0, 1, 2, 3
- *The Lone Necromancer* (LN) eps 1, 2, 6
- *Eleceed* ep 1
- *The Greatest Estate Developer* (TGED) ep 1
- *I'm the Max-Level Newbie* ep 0
- *My S-Class Hunters* (MSCH) eps 1, 2
- Two Chinese manhua as genre references only: *The Summoner: Apocalypse Rewinds* ep 1, *Necromancer, the Ultimate Scourge* ep 1

Episode titles for MSCH 1–66, LN 1–7 and *Surviving the Game as a Barbarian* 1–60 were read from the official lists for arc lengths.

---

## A. The reader's contract (what a summoner/hunter manhwa promises)

1. **Danger in chapter 1.** Every Korean launch episode in the corpus puts death or a monster on the page by its last third [R: ORV1–2, LN1, MSCH1, Max-Level Newbie 0].
   - ORV's first scenario card ends on "Penalty for failure: Death" [R: ORV2].
2. **The MC's lack, then his edge, fast.** "Now the grammar demands showing character appeal and relationships within the first few scrolls of episode 1" (Kakao PD) [K47].
   - The edge arrives as a reveal at the end of ep 1 or 2:
     - LN's first summon ends ep 1;
     - MSCH's power window ends ep 2;
     - TGED's blueprint vision ends ep 1 [R].
3. **Visible growth, often.** Rewards land as UI windows every few pages in action episodes: gold, level-up, card choice, new skill, new summon [R: LN2, LN6]. Readers want growth "trackable at a glance" [K60].
4. **Summons are companions, not tools.**
   - Summons with names and personalities are the genre's heart [K42, K64].
   - LN's oldest skeleton gets a goodbye line before a sacrifice [R: LN6].
   - MSCH's "custody" power works through people the MC cares about [R: MSCH2].
5. **The underdog is underestimated in public, then proves it in public.** Bystanders and rivals voice contempt and later awe [R: MSCH2, LN6, Max-Level Newbie 0, Necromancer Scourge 1].
6. **Payoff (사이다, "cider") at least every ~3 episodes.**
   - Never 3 build-up episodes in a row [K54].
   - Readers' tolerance for frustrating build-up (고구마) "has dropped a lot" [K47].
   - One quieter episode after a big event is fine [K16].
7. **Intelligibility first.** Readers who must "study" the world leave [K53, K46]. Explain one rule at a time, at the moment it matters.

## B. Series and arc pacing (numbers)

| Measure | Real benchmark | Rule for us |
|---|---|---|
| First danger | ch 1 [R] | ch 1 |
| First fight | ch 1–3 (LN ch 1; Solo Leveling ch 3 [pacing report]) | ch 1–2 |
| First power-up | end of ch 1–2 [R] | end of ch 1 |
| First arc | LN 3 eps; ORV first block 5 releases; Solo Leveling first arc 10 chapters [R, pacing report] | 5 chapters |
| Early arc length | median about 4 episodes (ORV blocks, TGED events); LN 3 [pacing report, R] | 3–7 chapters early, 10–15 later |
| New companion | MSCH titles mark a new companion at eps 9, 14, 26, 44, 56, 57 (gaps 1–18, about 10 on average) [R titles]; LN has 4 minions by ep 6 [R] | a new summon or major ally every 8–12 chapters early |
| Big "underestimated" payoff | MSCH titles "Stronger than I look" (37), "Pro in noob's clothing" (40) [R] | a public reversal by ch 12, then one every arc |
| Season length | Solo Leveling S1 110; TGED S1 104; Barbarian S1 53 [pacing report, R] | Part One = 100 chapters |
| Prologue | 2 releases or fewer [pacing report] | a 6–10 panel flash-forward inside ch 1, no separate prologue |

**Arc shape [I, from R + K].**
- Each arc has:
  - a concrete noun title, like "Double Dungeon", "Three Rules", "Fire horn lion" [K, R];
  - a local antagonist or obstacle;
  - a new rule, reward or companion;
  - a public payoff.
- New named cast arrives at arc starts.

## C. Chapter anatomy

**Size.**
- Korean weekly episodes run 60–80 cuts (panels): average 64.6 actual vs 53.9 "ideal" in the creator survey; 70 in the Hanyang study [K2, K3]. Platforms floor at 50 [K1].
- Our corpus ranges from 52 slices (MSCH 2) to 239 (LN 3).
- **Our rule:**
  - 60–75 panels;
  - action-climax chapters up to ~90;
  - quiet chapters no fewer than 55.

**The shape of one chapter** [R, all corpus episodes]:
1. **Cold open, panels 1–5.**
   - Use one of these:
     - in medias res (LN6 opens mid-fight);
     - a flash-forward (ORV0, TGED1);
     - a hook fact or number (ORV0 "1 view"; Max-Level Newbie "70 attempts, 315,850 casualties");
     - a re-entry into last chapter's cliffhanger (ORV3, LN2).
   - Never open on a calm establishing shot of an ordinary place unless the next 2 panels break it.
2. **Title card at 15–40% of the chapter, after the hook is re-established.**
   - ORV: slice 25–30 of 112–141. MSCH2: slice 22 of 52. Eleceed1: slice 43 of 107. TGED1: about slice 30 [R].
   - It may also sit at the very end of a launch chapter (MSCH1) or work as a scene break (LN6 at slice 123).
   - **Never at a fixed panel number.** (Ours was always P05.)
3. **The body turns at least twice.** Something changes the situation: a reveal, a rule, an arrival, a betrayal or a reward.
   - Each chapter "starts in one situation and ends in another" [K18, K48].
4. **The last 1–3 panels open a question that grows out of the scene** [K37, K48].
   - Observed hook types:
     - new threat (ORV2 quest card, LN6 rival scene);
     - mystery line (MSCH1 "My baby brother...");
     - system message (MSCH2 "...has come under your custody!");
     - someone arrives (TGED2);
     - relationship turn (Eleceed1: the cat talks);
     - countdown (ORV3).
   - Rotate them. Never end on an admin notice or a polite line.

**Per-chapter minimums [I, from R].**
- Action-arc chapters: one dangerous moment or one fight. Quiet chapters: at least one turn and one laugh.
- At least one impact panel (full width, bleed or extra tall), plus one system window or reward wherever the system is involved.
- **Talk-only panels ≤ 50%** of the chapter, and never 3 talk-heavy chapters in a row (our old ch 1–13 averaged 69%; see `DIAGNOSIS.md`).

## D. Scene patterns (the device library)

Each pattern is named so a script can call it ("use NAME CARD", "SPEECH IN BITES").

| Pattern | What it is | Seen in |
|---|---|---|
| **HOOK FACT** | Open on one strange number or fact, lettered big. | ORV0 ("1 view"), Max-Level Newbie 0 ("315,850 casualties") |
| **FLASH-FORWARD** | 6–20 panels of the epic future, then "Back then, I had no idea" or "Six months earlier". | ORV0, TGED1 |
| **NAME CARD** | A new important character gets a caption: NAME (age) · rank/role · one-line bio or epithet. Half-page portrait for big ones ("STEEL BLADE / HYEONSEONG LEE / ROK ARMY LIEUTENANT"). | ORV1, ORV3, MSCH2 ("YOOJIN HAN, F-RANK HUNTER. TITLE: CUSTODIAN."), TGED1 |
| **CONTEMPT CHORUS** | Party members or bystanders mock the MC in 1-bubble panels. One mocking line also plants the mystery ("he survived every raid even when the rest of the party got wiped out"). | MSCH2 |
| **DENIAL CHORUS** | When the world breaks, 5–8 bystanders each get one line showing a type ("Are you filming a movie? I have audition", a child: "Is it a cartoon?"). | ORV2 |
| **HIDDEN CALCULATION** | The MC smiles or fawns outwardly; a GRIN panel or one inner line shows the plan. | MSCH2 |
| **FRAME THE CHAOS** | The smart MC explains the new reality to a companion with an analogy: "Think of it this way. We're part of that game now. Every game has rules." | ORV3 |
| **PREDICT, THEN CONFIRM** | The MC predicts ("And soon...") and the next panel proves it (BANG). This is how foreknowledge or expertise reads as power. | ORV3 |
| **RULES BY FAILED EXAMPLE** | A side character breaks a rule and pays (a bribe is burned; someone who tries to leave dies). No lecture needed. | ORV2, Solo Leveling ch 3 [pacing report] |
| **SHOW FAILURE ELSEWHERE** | Cut to another group failing the same test, to show the cost. | ORV3 (the girls' school channel) |
| **TONE FLIP** | Comedy to horror in one beat: a line split over 3 panels ("I..." / "...told you..." / "...to be quiet!"), an extreme close-up of an eye, then a full-height SFX. The violence happens between panels; show before and after. | ORV2 |
| **SPEECH IN BITES** | A villain's or herald's speech is cut into 5–15-word bubbles, one per panel, with reactions between them. | ORV2, ORV3 |
| **TONAL WHIPLASH** | A cheerful side character's hope, then the news of their death on the next panel. Stakes in 2 panels. | MSCH2 |
| **LORE DURING CHAOS** | World history is narrated as retrospective captions over the disaster panels ("It was later revealed..."), so action never stops for exposition. | MSCH1 |
| **RULES SHOWN ON SOMEONE ELSE FIRST** | A side character awakens or uses the power before the MC does, so the reader learns the rule by watching. | MSCH1 |
| **DIEGETIC EXPLAINER** | A TV show, news ticker, livestream or app explains the world in a light, comic register. | MSCH2 ("Hunter Files"), ORV3 (PM broadcast), Max-Level Newbie 0 (livestream chat) |
| **CROWD METER** | A livestream chat or viewer counter rises with the MC's feat: doubt first, then "Wait a sec...", then awe. | Max-Level Newbie 0 |
| **TIMED CHOICE** | A visible countdown forces a decision; the MC reasons out loud and picks right. | LN1 (class cards, "8 seconds"), ORV3 |
| **VILLAIN CHANGES THE RULES** | Mid-episode the antagonist tightens the rule: timer cut, "30 minutes" struck through, "10 minutes" added. | ORV3 |
| **MID-FIGHT SYSTEM SURPRISE** | A new mechanic triggers mid-fight. The MC reads the card and decides on the spot: mechanic → decision → action in under 10 panels. | LN6 (Synergy Effect) |
| **SACRIFICE THAT BECOMES EVOLUTION** | The MC orders a cold, smart sacrifice with a feeling line ("Thank you for everything"); the summon survives the kill and evolves from the boss's power. | LN6 |
| **REWARD CASCADE** | After a big win, 5–10 small UI cards in a row (gold, level, card choice, skill, cap +1), plus party banter comparing loot. | LN6 |
| **DOUBTERS' PAYOFF** | A rival tells others the MC is dead or useless; the MC walks in on that exact line: "Who did you say died?" | LN6 |
| **FUTURE ALLY ON A SCREEN** | A future companion is first shown elsewhere (broadcast, rumour, silhouette) with a caption card, chapters before they meet. | ORV3 (Jihye Lee), ORV3 silhouette |
| **VISUALISED THINKING** | The MC's plan or knowledge appears as a holographic overlay (blueprint, tactical map), so being smart reads as spectacle. | TGED1 |
| **SMALL BODY, BIG POWER** | A strong creature in a small, funny body beside a kind MC. | Eleceed1 (Kayden the cat) |

## E. Dialogue

**What the numbers say.**
- Real bubbles in the corpus average **~8–9 words**. In 60 lines transcribed in order (a line split across two panels counted once): ORV2 7.8 words over 31 lines, MSCH1 9.0 over 29 lines [R].
- Our old chapters averaged **5.3** (ch 2: 4.0) [measured].
- Real lines are complete, natural sentences ("Are you filming a movie? I have to go to my audition."). Ours were clipped fragments ("I'M TWO MONTHS OF MULE."), which the owner found confusing.

**Rules.**
1. **Bubble size.** 1–2 sentences per bubble, about 6–14 words, never more than about 25. Split longer speech into linked bubbles or across panels [K23, K18, R].
2. **≤ 3 bubbles per panel**, counting thought bubbles and narration boxes [K12].
3. **Every line does something:** asks, refuses, threatens, mocks, bargains, jokes or reveals. Delete lines that only restate the image [K58].
4. **Short must stay clear.** Each line names or implies who does what. Test: read the dialogue without the art; it must still make sense [K53, I].
5. **Exposition rides on motive.** Backstory comes out because someone asks for a reason ("Why are you working so hard? Saving for college?" "Yes, but not mine. It's for my younger brother.") [R: MSCH1]. Use an object instead of a speech where possible: a phone photo, a gate stone handed over [R: MSCH1; K46].
6. **Never two explanation-only bubbles in a row** [I].
7. **Banter is ping-pong.** Exchanges go A–B–A–B with a turn on the last line, usually a joke or a sting (TGED: "You may be a hooligan, but you are his son.") [R, K58].
8. **Give each character a register:** formal, deadpan, slangy, archaic or childish. The voice should be recognisable without the name [K58, R].
9. **No childish lines.** Characters can be silly, but the writing can't [K55, K59].
10. **Rhythm in fights:** short command lines ("Both of you, charge!"), one-word reactions ("?!", "Huh?"), then one longer line at the turn ("With this synergy effect and weapon... I can win!") [R: LN6].

## F. Narration and inner voice

- **The MC's inner voice** sits in black or white boxes, 5–15 words each, 2–3 per beat at most [R: ORV1–3]. It carries:
  - fear and humour;
  - plans (HIDDEN CALCULATION);
  - foreshadowing ("Back then, I had no idea.").
- **Key nouns in red** inside narration (ORV: TWSA, PROTAGONIST) [R].
- Narration and monologue lines stay **fewer than dialogue lines** in every chapter. Frequent narration breaks immersion [K33, K25].
- **Retrospective narration** ("It was later revealed...") is allowed for world history during action (LORE DURING CHAOS) [R: MSCH1].
- **Quote boxes** (a distinct box style) for prophecy or source-text the MC knows: ORV uses orange-bordered black boxes with quote marks [R].

## G. System windows

- **What windows do.** They show every rule, reward, penalty and limit, with numbers [R: all hunter titles; K41]. The penalty can be severe ("Penalty for failure: Death") [R: ORV2].
- **Quest card fields:** title, objective, category, difficulty, time limit, reward, penalty [R: ORV2].
- **Status window:**
  - fields: name, level, HP/MP, class, stats, skills;
  - only the MC sees it [K41, R: LN2];
  - first appears at the turning point after a near-death moment [I, from the five openings reviewed in K60–64].
- **Rhythm.** Show one window per beat, not a wall. Reveal fields one panel at a time when they matter (LN6 shows a SKILL INFO card, then its effect) [R].
- **The system can have a personality.**
  - TGED's system cheers ("CLAP CLAP CLAP") and mocks ("(LAUGH)") [R].
  - Ours: the Operator interface is an old military protocol. It is formal, glitchy and literal, and that is funny.
- **SFX for windows:** DING, VOOM, CRACKLE when glitching [R].

## H. Action staging

1. **One beat per panel.** Each action panel carries one big SFX lettered into the art, angled, often breaking the frame: STAB, CLANG, SLASH, WHAM, SKREEE [R: LN2, LN6, MSCH1]. The SFX sits on the thing making the sound [K20].
2. **Three beats:** anticipation, action, reaction or outcome. Add panels only where time should slow [K17, K20].
3. **Narrow gutters for speed, wide gutters before a reveal** [K15, K17]. Benchmarks at 800 px width:
   - ≥200 px between beats;
   - ~400 px standard;
   - 600–1,000 px at a scene change [K12, K13, K19].
4. **Angles change every panel:**
   - extreme low angle on the monster;
   - eye-level close-up on the MC's eyes;
   - overhead on the battlefield;
   - Dutch-tilted frames for chaos [R].
5. **Colour flips for impact.**
   - Hot orange or yellow for hits (LN6);
   - black and red for horror (ORV2);
   - cyan for system light on faces (ORV2 slice 99);
   - white flash panels between hits (Max-Level Newbie 0) [R].
6. **Show the MC reading the fight** in close-ups between hits: sweat, eyes, a short inner line ("Tiny, child-sized bodies. Not difficult opponents.") [R: LN2].
7. **Monster reveal over the MC's back.** The creature fills the panel and the MC is small in the foreground [R: MSCH1].
8. **Violence between panels:** before, a full-height SFX, after. Gore is kept to silhouettes and splashes [R: ORV2, LN1].
9. **Quick battle resolution** is a core engagement strategy: an enemy falls within 3–4 episodes [K37].

## I. Comedy

- **Comedy and danger share a page** [R: LN1, LN6 ("Have a taste of this solid desk from hell!"), ORV2]. A gag right before a tone flip makes the flip hit harder.
- **SD/chibi reaction panels** for embarrassment and shock: sparkle eyes, sweat drops, dark auras [R: ORV1, Eleceed1, our old ch 1]. Use 1–3 per chapter.
- **Running gags** belong to characters (Nib's "You first."). The pattern is: set it up, repeat it, then subvert it [I].
- **Deadpan straight man plus exasperated MC** (TGED Javier/Lloyd) [R].
- **Lettering density as a joke:** a run-on bubble of tiny text when someone gushes (MSCH1) [R].

## J. Lettering language (bubble types)

| Type | Look | Use | Seen in |
|---|---|---|---|
| Speech | white oval | normal talk | all |
| Shout | white, jagged edge | shouting, shock | all |
| Thought | cloud with trailing circles | private thought | ORV0 |
| Strained | spiky inner border | panic, pain | ORV0, Eleceed1 |
| Whisper | dashed outline | whispers | common |
| Monster/herald voice | black hexagon, RED text | non-human speakers | ORV2 dokkaebi |
| Command | thick black fuzzy border | the MC's orders to summons | LN6 |
| Inner voice | black or white box | MC narration | ORV1–3 |
| Quote box | black box, orange text, quote marks | prophecy or source text | ORV3 |
| Broadcast | box with border, TV-style | TV, PA, phone audio | ORV3, MSCH2 |
| System window | cyan glowing UI frame | system messages | all |
| Chat | dark comment boxes "[user]: text" | livestream chorus | Max-Level Newbie 0 |

- **SFX are drawn into the art,** large and angled, coloured to the scene.
- **Text sizes:** typically 12–30 px on an 800 px canvas, larger than print [K12, K17].
- Keep bubbles in gutters and negative space, never over faces or hands. Read top-left to bottom-right [K23, K24].

## K. Chapter checklist (a script fails if any answer is no)

1. Does something dangerous, funny or strange happen in the first 5 panels?
2. Is the title card placed after the hook (15–40%), not at a fixed panel?
3. Does the chapter turn at least twice, and does it end in a different situation from where it began?
4. Is there a payoff in this chapter or one of the two before it?
5. Are talk-only panels ≤ 50%?
6. Do bubbles average 6–14 words and read clearly without the art?
7. Does every important new character get a NAME CARD?
8. Is every rule and reward shown as a system window with numbers?
9. Are there SFX on every action beat, and at least one impact panel?
10. Do the last 1–3 panels open a question (threat, mystery, system, arrival, power, countdown), different in type from the last chapter's hook?
11. Does the MC do something smart on the page (predict, plan, read a rule, combo), not just react?
12. Did someone laugh?
