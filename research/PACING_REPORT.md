# First-arc pacing of hit manhwa: research report (PARTIAL)

Delivered by a research agent, Oct 2026. Chapter-level data was thin because wiki chapter pages could not be fetched; see section 0. MANHWA_CRAFT_BIBLE.md cites it as [pacing report].

# Manhwa pacing dataset: PARTIAL (read section 0 first)

No files were written. Every event cell below is paraphrased from a cited page, not from memory. "NS" means no source. The chapter-level data I could source is thin, so most of what follows is block or arc structure from reliable pages, labelled as such.

## 0. Status, limits, legend

**What is and isn't delivered**
- True per-chapter text exists only for The Greatest Estate Developer (TGED) Ep 2, plus low-reliability fan recaps for Solo Leveling ch 2-10.
- Everything else is block/arc-level, or NS.
- The summoner/necromancer pair is not delivered (section 5).

**Why it is partial (observed in this session)**
1. Fandom per-chapter pages all failed in WebFetch with `client_error`, on repeated tries at different times:
   - Solo Leveling wiki: `Chapter_1`, `Chapter_2`, `Chapter_10`, `Volumes_and_Chapters`.
   - ORV wiki: `Episode_1`, `Chapter_1_(webtoon)`, `Prologue_(webtoon)`, `Story_Arcs`, `Kim_Dokja/Synopsis`.
   - SSS wiki: `Episode_1`, `Chapter_1`.
   - dragonschef wiki (TGED): `Episode_1_(TGED)`, `Episode_2_(TGED)`, `Episode_3`, `Episode_3_(TGED)`, `Chapter_1_(TGED)`, and its main page.
   - TGED wiki: `Episode_2_(TGED)`. Only `the-greatest-estate-developer.fandom.com/wiki/Episode_2` worked.
   - Also blocked: the CBR guide (robots_disallowed) and koreawebtoon.fandom.com.
2. WebSearch hit the shared cap of 200 calls per turn after about 40 of my calls. WebFetch only accepts URLs already surfaced by search or fetch results, so I could not guess other chapter URLs. One request through a translate proxy was denied by the permission classifier as bot-check circumvention. I did not retry or work around it.
3. Reading-site recaps are unreliable:
   - The readsololevelingmanga.us "Chapter 5" recap describes an E-rank dungeon with item drops. That contradicts [5][6] and is excluded.
   - On solomangahub.com the `...solo-leveling-chapter-1/` URL serves a Chapter 10 recap.
   - Its ch 2-10 recaps are vague but consistent with [5][6], so I use them as [L] only.
   - Ch 11-20 pages on that site failed the provenance check.

**Legend**
- Flags: F fight, P power-up/level-up, S system/status window, R reveal, N new major character, C comedic beat, L location change.
- Flag values: Y = source states it; N = source implies none (inferred); ? = source silent.
- Reliability tags:
  - [H] structural fact from a wiki or index.
  - [M] second-hand mapping, e.g. anime synopsis mapped to manhwa chapters.
  - [L] fan-site recap.
- Numbers in brackets are source numbers from section 9.

## 1. Solo Leveling (webtoon; Fandom numbering, Prologue = ch 0)

The print chapters differ from release chapters. Yen Press Vol. 1 prints "Prologue / Ch 1 Double Dungeon / Ch 2 Three Commandments / Ch 3 Quest" [8]. Those are the Kakao arc names, not release numbers. Kakao blocks per NamuWiki [3]:
- Double Dungeon = ch 1-4.
- Three Rules = ch 4-10 (ch 4 overlaps both blocks).
- Quest and Boss Battle follow, with end points not given.
- Lizards runs to ch 27.
- B-Rank Kang Tae-sik starts at ch 27.

| Ch | Events (paraphrased) | F | P | S | R | N | C | L | End hook | Rel/Src |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Prologue (introductory chapter); no event detail | ? | ? | ? | ? | ? | ? | ? | ? | NS [1] |
| 1 | NS (Fandom cites ch 1 for Jinwoo's debut; chapter sits in the 1-4 "Double Dungeon" block) | ? | ? | ? | ? | ? | ? | ? | ? | NS [14] |
| 2 | Healer Joohee treats Jinwoo's wounds; leader announces essence-stone rewards; after the clear the party finds a second entrance (double dungeon with a boss); leader Song wants in before the Association rules; vote splits 6-6 and Jinwoo breaks it in favour (family needs money) | ? | N | N | Y (double dungeon) | ? | ? | Y | decision to enter | [L] [9], matches [6] Ep1 |
| 3 | 40-minute tunnel to the gate; Song says anyone may turn back; inside: torches, divination circle, rune inscription (worship god / praise god / prove thy faith), statues whose eyes follow them; door shuts; a hunter who tries to leave is beheaded; statues start moving and the hunters must fight | Y | N | N | Y (commandments) | ? | ? | Y | new threat | [L] [9], matches [6] |
| 4 | Boss statue's eyes light; Jinwoo shouts to duck, beam kills those who moved; he links the inscription's "boss" to this statue; he and Song judge the dungeon far above B-rank | Y | N | N | Y | ? | ? | N | NS | [L] [9] |
| 5 | Song has lost an arm; healers' spells fail; B-rank healer Joohee is frightened; another hunter dies; Jinwoo sees the statues' attacks follow rules tied to the commandments | Y | N | N | Y (rules) | ? | ? | N | mystery line (recap says chapter ends there) | [L] [9], matches [6] |
| 6 | Jinwoo, calm, studies a statue, cracks hidden rules and takes the lead; survivors live but cannot leave | Y | N | N | Y | ? | ? | N | trapped (stakes) | [L] [9] |
| 7 | Team survives only by following Jinwoo; he uncovers the rules one by one (recap vague) | ? | N | N | Y | ? | ? | N | NS | [L] [9] |
| 8 | Chaos around the raid leader; Jinwoo takes the blame, puts others first; badly hurt, he focuses on the secret rules and how to open the gate (vague) | ? | N | N | ? | ? | ? | N | NS | [L] [9] |
| 9 | Jinwoo commands; recap says the statues' behaviour changes and he responds (vague) | ? | N | N | ? | ? | ? | N | NS | [L] [9] |
| 10 | Near death; tells teammates to leave; resolves to kill one monster; a strange message appears in his blurred vision (recap also mentions a "daily quest") | Y | ? (Player offer) | Y | Y | ? | ? | N | status-window message | [L] [9]; anime Ep2 ends on the Player offer at death [6] |
| 11-12 | Reawakening Arc: wakes in hospital after three days; Association members question him and tell him what happened; after they leave he finds a game-like system only he sees [1]. Anime Ep3 adds: thinks it was a dream; Joohee traumatised; Song lost an arm; second-awakening test negative; system lists daily goals and penalties; skipping day one nearly kills him in a penalty quest; completing goals gives stat bonuses and loot boxes [6] | Y (penalty quest) | Y (stat bonus) | Y | Y | ? | ? | Y | NS | [H] arc, [M] detail; split inside block NS |
| 13-17 | Instant Dungeon Arc: daily quests earn an E-rank instant-dungeon key; he enters alone [1]. Anime: faces a wolf monster stronger than any before; kills it and levels up; clears more wolves and the boss; a dungeon break puts a golem in the city; arriving hunters (incl. traumatised Joohee) do no damage; Jinwoo throws his broken sword into the golem, shattering its defence; leaves thinking it must have been more hurt than he expected [6][5] | Y | Y (level-up) | Y | N | ? | ? | Y | understated exit / hidden power | [H] arc, [M] detail; split NS |
| 18-20 | Dungeon & Lizards Arc (18-24): joins a C-rank raid; friendly party members "not what they seem" [1]. Anime Ep5 (ch 18-21): pick-up group of C-rank Hwang Dongsuk; contract says Jinwoo won't fight and gets no battle drops; he grows suspicious; newcomer Yoo Jinho completes the party; ants, then a sleeping giant spider guarding mana crystals; Jinho notes crystals aren't battle drops; party traps both in the boss room and the spider wakes [6][5] | Y | ? | ? | ? | Y (Dongsuk, Jinho) | ? | Y | trap / new threat (ch ~21) | [H] arc, [M] detail |
| 21-24 (outside window) | Anime Ep6: Jinwoo kills the boss, surprising Jinho; Dongsuk's group tries to pressure Jinho into killing him; Jinho refuses; Jinwoo gets a kill-or-die quest, kills the group, and claims monsters did it [6][5] | Y | ? | Y | Y (first sourced "stronger than they think" beat) | ? | ? | Y | cover-up | [M] |

**Derived numbers (Solo Leveling)**
- **Inciting incident:** ch 2 (second entrance found, vote) to ch 3 (entry) [L]. The whole block is ch 1-4 [H].
- **First fight:** ch 3 [L], no later than ch 4 [M]. Any fighting before the vote is NS.
- **First power-up:**
  - The Player offer comes at the near-death moment in ch 10 [L/M].
  - First stat bonus and loot come in ch 11-13 [M].
  - First explicit level-up comes in ch 13-17 [M].
- **First "stronger than people think" reveal:** none in ch 1-20. The first sourced beat is ch 21-24 [M].
- **First summon:** the first shadow soldier appears in ch 41-45 [5]. That is the Job Change Arc, 38-45 [1] (anime Ep12 "Arise" = ch 41-45).
- **First arc ends:** ch 10 [H] (D-Rank Dungeon Arc 1-10).
- **Action vs talk (ch 1-20, block-level estimate, plus or minus 3):** about 16 danger/combat chapters (3-10, 13-20) vs about 4 talk/exposition (1-2, 11-12).
- **Cliffhangers (n=6 sourced endings in ch 1-24):**
  - new threat x3 (ch 3, ~13, ~21);
  - mystery line x2 (ch 5, ~17);
  - status-window message x1 (ch 10).
- **Scene length and locations:**
  - The statue-room sequence runs ch 3-10 (8 chapters, one room).
  - There are about 6 location changes in ch 1-24 (about 1 per 4 chapters): gate to double dungeon, hospital, instance dungeon, dungeon-break site, C-rank dungeon, exit. This is inferred from the blocks.
- **Arc lengths (14 arcs, ch 1-111):**
  - Lengths: 10, 2, 5, 7, 10, 3, 8, 10, 6, 4, 11, 14, 18, 4. Median 7.5.
  - First five arcs: 10, 2, 5, 7, 10. Median 7.
  - The later arcs trend longer.
- **Season 1** = ch 1-110 [3].
- **Source discrepancy:** [1] and [2] disagree by 1 on a few later boundaries (Retesting Rank 61 vs 62; Recruitment end 111 vs 110). Arcs 1-61 agree.

## 2. Omniscient Reader's Viewpoint (webtoon)

Numbering: English Webtoons shows "Episode 0 - Prologue" and Episodes 1-308 [16]. NamuWiki uses Korean release numbers (000 Intro, 001 Prologue) [15]. The requested "ch 1-15" is probably Korean releases 002-016; the offset is unverified.

| Release | Block (NamuWiki, machine-translated titles) | Chapter-level events | Notes |
|---|---|---|---|
| 000-001 | Intro, Prologue "3 ways to survive in a ruined world" | NS | Prologue + 001 drew >10,000 comments [15] |
| 002-006 | Ep.1 "Start paid service" (5) | NS | Opening episodes contain the grandmother's assault and a head-explosion scene, both softened for the webtoon, plus a Jung Heewon convenience-store scene (releases not given) [15] |
| 007-012 | Ep.2 "Hero" (6) | NS | |
| 013-015 | Ep.3 "Contract" (3) | NS | Release 015: comedic beat, a Constellation gag aimed at readers (C=Y) [15] |
| 016-018 | Ep.4 "Hypocrisy is also good" (3) | NS | |
| 019-021 | Ep.5 "Dark Sentinel" (3) | NS | Ratings reportedly start falling from 020 [15] |

All F/P/S/R/N/L flags and end hooks for individual webtoon releases are NS.

**Novel proxy, not webtoon (flagged).** A Korean structure analysis covers the web novel's Prologue and Ep.1 (chapters 2-6) [18]. Beats:
- Prologue: the author promises a "gift"; teaser for the next day.
- 1-1: the subway stops at 7pm and the main scenario is announced; the scene cuts before the cause is shown.
- 1-2: monsters kill people; main quest is to kill a living being.
- 1-3: a text file arrives from the author; Kim asks why "that guy" hasn't appeared.
- 1-4: Kim gets a trait/skill but cannot open the trait window; a crowd beats an old woman; Kim says insects count as living beings and frees them.
- 1-5: Kim refuses an alliance, stops an attack and wins by boosting HP with gold from grasshopper eggs; he glimpses a ruined Seoul (a bigger threat).

Novel-side cliffhanger tally: mystery/teaser x4, new bigger threat x1. The webtoon's Ep.1 block also spans five releases, but nothing confirms a 1:1 mapping.

**Derived numbers (ORV)**
- **Inciting incident, first fight, first power-up, first reveal (webtoon release numbers):** NS.
  - The webtoon opening contains violence (the grandmother scene) within the first block [15].
  - The first arc is Scenario #1 "Proof of Value", releases 002-021 (20 releases) [15].
- **First mini-arc ends:** release 006 [H]. Scenario #1 ends at release 021 [H].
- **Mini-episode lengths (first 15 blocks, releases 2-72):**
  - Lengths: 5, 6, 3, 3, 3, 5, 6, 4, 7, 5, 4, 4, 4, 4, 8. Median 4, mean 4.7.
  - Blocks grow to 9 releases each by releases 99-152 [15].
- **Reception:**
  - Ranked 2nd on its Wednesday chart by release 003 and 1st by 004 [15].
  - Ratings reportedly fell from 020, with the page citing episode length and slow progress [15].
- **Action vs talk, cliffhanger counts, scene and location frequency:** NS for the webtoon.

## 3. SSS-Class Suicide Hunter / Revival Hunter (webtoon)

No chapter-level source was obtainable: the SSS Fandom pages failed, NamuWiki has no episode summaries [20], and Daum gives no episode numbers [21].

| Eps | Events | Source |
|---|---|---|
| 1-10 | NS per episode. Unplaced opening beats: low-rank F-class hunter Gong-ja envies the top hunter Flame Emperor; gets a skill that copies one skill from his opponent but only triggers when he dies; witnesses the Flame Emperor kill the "Saint"; is chased and killed; rewinds 24 hours [21]. Webtoon specifics [20]: first death is a stab to the solar plexus; about 30 deaths (novel: 40); a green-slime test; the past Flame Emperor wields a spear | [20][21] |

**Derived numbers (SSS)**
- All chapter-level metrics: NS.
- **Seasons:** S1 = eps 1-40 (Dec 31 2020 to May 28 2021); S2 = 41-80; S3 = 81-115 (35 eps); S4 = 116-151; S5 began Sep 25 2026 [20]. English Tapas shows 154 episodes [23].
- **Cadence:** weekly, with one week off after every five [20].
- **Reception [20]:**
  - The floor 10 boss stage is where readers became enthusiastic.
  - Readers disliked the 40-episode seasons.
  - Gaps ran about 8 months (S2 to S3), 9 months (S3 to S4) and 10 months (ep 80 to 81).

## 4. The Greatest Estate Developer (webtoon, episodes)

| Ep | Events | Flags | Source |
|---|---|---|---|
| 1 | Suho, a civil-engineering student, wakes in Lloyd Frontera's body, face-down on the street (novel: in bed) [27]; per a blog, he knows the novel's plot, aims to clear the family debt and has the ondol (heated-floor) idea [29] | inciting incident Y; rest ? | [M/L] |
| 2 | RP System popup appears; Javier's approval is -30 and a flattery attempt fails; Lloyd bullies a pub owner into a construction contract; tells Javier that his experience is also "past"; a week later builds the house with Javier's help and nearly collapses; the owner's mother loves the ondol floor and approval goes -31 to -29 (+36 RP); days later villagers queue and Lloyd sets up a sales table; his father Arcos arrives with Neumann | F N; P N (RP gain); S Y; R small (Javier notes Lloyd has changed); N ? (Arcos/Neumann); C Y (5 beats); L Y (about 3 settings, 2 time skips); end hook: someone arrives | [M] [26]; 9 beats |
| 3 | NS | ? | NS |
| 4-7 | Duel with Neumann after a month of preparation [25]; the giant hamster Ppodong crushes him as a comic payoff, and Javier notes technique too refined for a month of training [28] | F Y; R Y; C Y; per-episode split NS | [H] range, [M] detail |
| 8-9 | Ondol floors and road development [25] | ? | [H] range |
| 10 | NS | ? | NS |

**Derived numbers (TGED)**
- **Inciting incident:** ep 1 [25].
- **First fight:** the Neumann duel, eps 4-7 [25].
- **First power-up/system:** the RP system at ep 2 [26]. A second "praise/achievement" system activates at ep 46 [27].
- **First "more than they think" reveal:** doubt at ep 2 [26]; duel reveal at eps 4-7 [28].
- **First arc ends:** the "Year 1 Winter" block eps 1-9 [25]. Sub-arcs: eps 1-4 and eps 4-7.
- **Action vs talk (eps 1-10):** Ep 2 has zero combat. The only fight block in eps 1-10 is eps 4-7. Per-episode counts are NS.
- **Event/project lengths (18 timeline events):** 4, 4, 2, 3, 2, 12, 7, 4, 1, 2, 6, 1, 4, 10, 1, 3, 4, 5. Median 4 [25].
- **Compression:** the webtoon compresses 2-4 novel chapters into one episode, and fans praised the tight pacing [27].
- **Seasons:** S1 = eps 1-104 (Aug 5 2021 to Jul 27 2023), weekly on Fridays; S2 = 105-182; S3 = 183-211 [25][27].

## 5. Summoner / necromancer pair: NOT delivered

- **Candidates checked:**
  - The Lone Necromancer: Naver, 223 chapters per MAL [33]; the Webtoon Wiki lists eps 1-56 with no summaries [32].
  - Necromancer: KakaoPage, Erik and Moll, 2 volumes [34].
- **No fetchable chapter-summary source** for either, and my search budget ended before I could look for others. ChapterBrief's 16-title "like Solo Leveling" list contains no summoner, necromancer or tamer titles [23].
- **Only summoner-type data in hand:**
  - Solo Leveling's first summon at ch 41-45 (section 1).
  - An AI-generated summary of a recap video of an unidentified necromancer manhwa [35]. It has no chapter numbers and the page itself warns of errors. Runtime offsets, usable only as relative positions:
    - first clash at 2:10;
    - first summon (a skeleton that collapses after four swings) at 6:44, about 11% of the 60:10 runtime;
    - a "key" power-up at 12:07, about 20%;
    - a duel at 34:51, about 58%;
    - a skeleton-army battle at 54:48, about 91%;
    - a "Part Two" cliffhanger at the end.

## 6. Cross-series comparison

| Metric | Solo Leveling | ORV | SSS | TGED |
|---|---|---|---|---|
| Inciting incident | ch 2-3 [L] | NS (block 002-006) | NS | ep 1 |
| First fight | ch 3 [L], no later than 4 | NS | NS | eps 4-7 |
| First power-up / system | ch 10 offer; 11-13 stat; 13-17 level-up | NS | NS | ep 2 (RP system) |
| First "stronger than thought" | ch 21-24 [M] | NS | NS | ep 2 doubt; eps 4-7 |
| First arc ends | ch 10 | release 006 / 021 | NS | ep 4 / 7 / 9 |
| Typical arc/block length | 7.5 (n=14) | 4 (n=15) | NS | 4 (n=18) |
| Season 1 length | 110 | NS | 40 | 104 |
| First summon | ch 41-45 | n/a | n/a | n/a |

- **Medians:** only two series have values, so these are ranges.
  - First fight: ch 3-4 (Solo Leveling) and eps 4-7 (TGED), median about 4.5 (n=2).
  - First power-up/system: ch 10-13 and ep 2.
  - First reveal: ch 21-24 and eps 2-7.
- **Cliffhanger shares (n=7 sourced endings, illustrative only):**
  - new threat 3 (43%);
  - mystery line 2 (29%);
  - status-window message 1 (14%);
  - someone arrives 1 (14%).
  - Power reveal and countdown: 0 observed.

## 7. Pacing rules

Each rule is followed by evidence and confidence.

1. Make releases 1-4 carry the full premise promise. ORV's Prologue + 001 drew >10,000 comments; it was 2nd on its weekday chart by 003 and 1st by 004 [15]. (M)
2. Put the inciting incident by ch 3, with at most 2 setup chapters before it. Solo Leveling ch 2-3 [9]; TGED ep 1 [25]; ORV has a 2-release prologue then Scenario #1 at 002 [15]. (M)
3. Fight for the first time by ch 3-7. Solo Leveling ch 3 [9] (no later than 4 [5]); TGED eps 4-7 [25]. (M)
4. Make the first fight a rules or preparation fight, not a power display. Solo Leveling's commandments puzzle runs ch 3-10 [9][6]; TGED's duel follows a month of preparation and a trick [25][28]. (M)
5. Keep a sealed-room sequence to about 8 chapters or fewer before payoff. Solo Leveling ch 3-10. (L-M)
6. Close the first arc by ch 10, ending on the interface/near-death beat. Solo Leveling ch 10 [1][9][6]. TGED's mini-arcs end at eps 4 and 7 [25]; ORV's first block ends at 006 [15]. (M)
7. Keep aftermath to 2 chapters. Solo Leveling's Reawakening Arc is ch 11-12 [1]. (M)
8. Start the first solo power loop in the chapter after the aftermath, with a level-up and boss kill within 5 chapters. Solo Leveling ch 13-17 [1][6]. (M)
9. Run opening mini-arcs at 3-7 chapters, median about 4. ORV blocks median 4 [15]; TGED events median 4 [25]; Solo Leveling's first five arcs median 7 [1]. (M-H)
10. Do not lengthen arcs until the audience is locked in. ORV blocks went from 3-8 releases to 9 by releases 99-152, and ratings reportedly fell from 020 citing episode length and slow progress [15]. This is correlation only. (L-M)
11. Alternate solo and group arcs. Solo Leveling runs 10 (group trap), 2 (aftermath), 5 (solo), 7 (party), 10 (party with antagonists) [1]. (L-M)
12. Give a visible numeric metric that moves every episode. Solo Leveling's daily quests and penalties [13]; TGED ep 2: approval -31 to -29 and +36 RP [26]. (M)
13. Fit about 9 beats and 1-2 time skips into one build or training episode, and compress source material. TGED ep 2 [26]; the webtoon compresses 2-4 novel chapters per episode and is praised for tight pacing [27]. (M)
14. Put a comic beat in every episode of a comedic premise, but vary the gag. TGED ep 2 has 5 comic beats [26]; fans praised the facial comedy but some found it overused from about ep 18 [27]; ORV has reader-gag beats at 015, 022 and 025 [15]. (M)
15. Seed doubt early and pay the big reveal after the first solo loop. TGED doubt at ep 2, duel reveal at eps 4-7 [26][28]; Solo Leveling's first sourced surprised witness is ch 21-24 [6][5]. (L-M)
16. If the summon is the hook, do not copy Solo Leveling's wait. Its first shadow soldier is at ch 41-45 [5], bridged by the daily-quest loop [13]. The only other necromancer data, an unidentified recap, puts the first summon at about 11% of runtime [35]. (M for Solo Leveling, L for the recap)
17. Rotate cliffhanger types: new threat, mystery line, status-window message, someone arrives. Observed n=7 [9][6][26]. (L)
18. Introduce new named cast at arc starts. Solo Leveling ch 1-4 (Song, Joohee), ch 18-21 (Dongsuk, Jinho), ch 25-34 (Kang Taeshik) [1][5][6]. (L-M)
19. Plan platform-safe versions of shock beats in the first 6 releases. ORV softened the grandmother assault and head-explosion in its opening episodes [15]. (M)
20. Size the first season at about 100 chapters, and keep gaps short. TGED S1 is 104 and Solo Leveling S1 is 110 [25][3]. SSS's 40-episode seasons and 8-10 month gaps drew reader complaints [20]. (M)
21. Name blocks with a concrete noun that promises the content: Double Dungeon, Three Rules, Quest, Boss Battle, Lizards [3][8]. (M)
22. Keep the prologue to 2 releases or fewer. ORV 000-001 [15]; Solo Leveling ch 0 [1]. (M)

## 8. To finish the dataset

- **Per-chapter Fandom pages.** Solo Leveling `Chapter_0`-`Chapter_20`, ORV `Prologue_(webtoon)` and `Chapter_N_(webtoon)`, SSS `Episode_N`, and TGED `Episode_N` all need a retrieval method that WebFetch cannot provide, or a browser-capable agent. Only Chapter_1, Chapter_2 and Chapter_10 (Solo Leveling), Chapter_1_(webtoon) and Prologue_(webtoon) (ORV), Episode_1 and Chapter_1 (SSS) and the TGED variants named in section 0 were surfaced by search, so the other N values are an unverified URL pattern.
- **Search budget.** After the cap resets: look for per-chapter text from sources other than Fandom (Korean blogs, other-language wikis), and pick two summoner/tamer titles that have such text.

## 9. Sources

**Solo Leveling**
1. https://solo-leveling.fandom.com/wiki/Story_Arcs
2. https://solo-leveling.fandom.com/wiki/Solo_Leveling_(webtoon)
3. https://namu.wiki/w/%EB%82%98%20%ED%98%BC%EC%9E%90%EB%A7%8C%20%EB%A0%88%EB%B2%A8%EC%97%85(%EC%9B%B9%ED%88%B0)
4. https://namu.wiki/w/%EB%82%98%20%ED%98%BC%EC%9E%90%EB%A7%8C%20%EB%A0%88%EB%B2%A8%EC%97%85/%EC%A4%84%EA%B1%B0%EB%A6%AC
5. https://esports.gg/news/entertainment/solo-leveling-story-guide-anime-episode-to-manhwa-chapters/
6. https://en.wikipedia.org/wiki/Solo_Leveling_season_1
7. https://en.wikipedia.org/wiki/Solo_Leveling
8. https://yenpress.com/titles/9781975319434-solo-leveling-vol-1-comic
9. solomangahub recaps, [L]: https://solomangahub.com/manga/solo-leveling-chapter-2/ , .../solo-leveling-chapter-3/ , .../solo-leveling-chapter-4/ , .../solo-leveling-chapter-5/ , .../solo-leveling-chapter-6/ , .../solo-levelling-chapter-7/ , .../solo-levelling-chapter-8/ , .../solo-leveling-chapter-9/ , .../solo-leveling-chapter-10/
10. https://www.vinitnair.com/post/solo-leveling-volume-1-manhwa-review-a-must-read-for-fans-who-can-t-wait-for-more
11. https://www.theouterhaven.net/2021/03/solo-leveling-vol-1-review/
12. https://medium.com/@20mafultz/manhwa-synopsis-1-solo-leveling-volume-1-spoilers-93664c856c2d
13. https://v.daum.net/v/20260406093744951
14. https://solo-leveling.fandom.com/wiki/Sung_Jinwoo , https://solo-leveling.fandom.com/wiki/Dungeons , https://solo-leveling.fandom.com/wiki/Statue_of_God

**ORV**
15. https://en.namu.wiki/w/%EC%A0%84%EC%A7%80%EC%A0%81%20%EB%8F%85%EC%9E%90%20%EC%8B%9C%EC%A0%90(%EC%9B%B9%ED%88%B0)
16. https://www.webtoons.com/en/action/omniscient-reader/episode-1/viewer?title_no=2154&episode_no=2
17. https://en.wikipedia.org/wiki/Omniscient_Reader%27s_Viewpoint
18. https://www.postype.com/en/@paby1123/post/9823873 (NOVEL analysis)
19. https://www.graphiclibrary.org/reviews/omniscient-readers-viewpoint-vol-1-by-singnsong

**SSS**
20. https://namu.wiki/w/SSS%EA%B8%89%20%EC%A3%BD%EC%96%B4%EC%95%BC%20%EC%82%AC%EB%8A%94%20%ED%97%8C%ED%84%B0(%EC%9B%B9%ED%88%B0)
21. https://v.daum.net/v/20210821060016084
22. https://tvtropes.org/pmwiki/pmwiki.php/Literature/SSSClassSuicideHunter (novel)
23. https://www.chapterbrief.net/blog/sss-class-suicide-hunter-character-guide , https://www.chapterbrief.net/blog/manhwa-like-solo-leveling
24. https://wikikai.com/wiki/sss-class-suicide-hunter/ (novel arcs; not used for webtoon numbers)

**TGED**
25. https://the-greatest-estate-developer.fandom.com/wiki/The_Greatest_Estate_Developer
26. https://the-greatest-estate-developer.fandom.com/wiki/Episode_2
27. https://namu.wiki/w/%EC%97%AD%EB%8C%80%EA%B8%89%20%EC%98%81%EC%A7%80%20%EC%84%A4%EA%B3%84%EC%82%AC(%EC%9B%B9%ED%88%B0)?uuid=1aa3b269-fdb8-4b12-a3f2-e8167387a8d3
28. https://tvtropes.org/pmwiki/pmwiki.php/Webcomic/TheGreatestEstateDeveloper
29. https://thedailyfandom.org/lloyd-frontera-greatest-estate-developer-2021/
30. https://en.wikipedia.org/wiki/The_Greatest_Estate_Developer
31. https://www.webtoons.com/en/fantasy/the-greatest-estate-developer/episode-1/viewer?title_no=3596&episode_no=1 (images only)

**Necromancer candidates**
32. https://webtoon.fandom.com/wiki/The_Lone_Necromancer
33. https://myanimelist.net/manga/147450
34. https://myanimelist.net/manga/139467/Necromancer
35. https://videohighlight.com/v/BJK7uAO1uNg (AI summary of a recap video; unidentified title)

**Excluded as unreliable**
- https://readsololevelingmanga.us/solo-leveling-manga-chapter-5/ (contradicts [5][6])

## 10. Notes for the main session

- WebFetch cannot read Fandom chapter pages (`client_error`). NamuWiki (EN and KR), Wikipedia, MAL, Webtoon Wiki, TV Tropes, Daum and Postype all worked. Official Webtoons episode pages return no text.
- WebSearch is capped at 200 calls per turn, shared across agents. "Extended" mode surfaced the target wiki pages far better than "standard".
- Link-walking only works on sites whose hrefs survive page conversion. The summarizer sometimes prints guessed URLs, which then fail the provenance check.