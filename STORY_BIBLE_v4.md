# STORY BIBLE v4: My Summons Go First (the rebuild)

**Canon.** This is the approved story, copied from the owner's storyboard doc *My Summons Go First: rebuild story board and characters*, approved on 25 October 2026 with every recommended option. If this file and the doc ever differ, ask; update both together.

**Replaces.**
- `STORY_BIBLE.md` (v3, the Yoon Taeo story).
- `PART_ONE_BEATS.md`.
- The old scripts `scripts/ch001–ch100.yaml`.

All of those are retired and kept for history only.

**Related files.**
- Names and spellings: `NAME_SHEET.md`.
- How it looks: `codex/MANHWA_STYLE_GUIDE.md` and `codex/CHARACTER_DESIGNS_v2.md`.

---

## The pitch

*My Summons Go First* becomes a summoner action manhwa. An F-rank "trap-tester" lets his summons do the fighting while he out-thinks everyone, until he is strong enough to go first himself. The owner approved this direction on 25 October, with every recommended option.

- **Title.** *My Summons Go First* (kept).
- **Logline.**
  - In Seoul, summoners are hired as human trap-testers, and "summons go first" is the raid rule.
  - Kang Jaeha has walked into 312 dungeons and never killed anything.
  - Used as live bait for a boss, he survives by being the smartest person in the room.
  - When he spends his last husk to shield a rookie, a broken protocol from beyond the gates answers through it.
- **The promise.**
  - A smart underdog commander.
  - Summons who are strange, funny, deadly people from the other side of the gates.
  - A power that turns every hit he takes for them into his own strength.
  - The day he goes first himself.
- **The question.** In a world that sends the weakest in first, can the man who was always sent first build a team where everyone comes back?
- **Feels like:**
  - *Omniscient Reader*: the smart lead and the dread.
  - *Solo Leveling*: dungeon tension and visible growth.
  - *Eleceed*: a deadly creature in a small, funny body.
  - *My S-Class Hunters*: a weak lead whose power works through others.
- **Tone.** Danger on the page from chapter 1, a short laugh in every chapter, and no paperwork plots.
- **Format.** Part One is 100 chapters (still one YouTube video). Each chapter is 60–75 panels; climax chapters run up to 90.

## Why we rebuilt

Our chapters 1–13 broke the genre's promise. There is no monster fight until chapter 10, 69% of panels are talk, and the stakes are paperwork.

The benchmark is 14 real episodes Claude read slice by slice: 12 Korean ones and 2 Chinese titles as genre references. They come from *Omniscient Reader*, *The Lone Necromancer*, *My S-Class Hunters*, *Eleceed*, *The Greatest Estate Developer* and *Max-Level Newbie*, plus Korean industry sources and reader research.

| Measure | Ours (ch 1–13) | Real manhwa | New rule |
| --- | --- | --- | --- |
| Monster fight on the page | none in ch 1–9 | danger in ch 1 of every Korean launch read | danger in ch 1, a fight by ch 2 |
| Talk-only panels | 69% | fight episodes are mostly action | 50% or less |
| System windows | 8 in 13 chapters | every rule and reward shown | a window for every rule, reward and limit |
| Words per bubble | 5.3 (clipped) | about 8–9, full sentences | complete sentences averaging 7–10 words |
| Summons in Part One | 5 | a new companion about every 10 episodes | 7 summons, the first in ch 1 |
| End hooks | admin lines ("It says I have three days") | threat, mystery, system message, arrival | rotate the hook types |
| Money amounts in scripts | 122 | one number when it matters | one number when it matters |

What survives from the old version:

- the power ideas;
- the first summon appearing at the end of chapter 1;
- Nib and his deadpan "You first." running gag;
- the art pipeline.

Research files (public repo):

- [Measured diagnosis](https://github.com/abafaboy/abafaboy.github.io/blob/msgf-bible/research/DIAGNOSIS.md)
- [Craft bible: the rules every script will follow](https://github.com/abafaboy/abafaboy.github.io/blob/msgf-bible/research/MANHWA_CRAFT_BIBLE.md)
- [Episode-by-episode reading notes](https://github.com/abafaboy/abafaboy.github.io/blob/msgf-bible/research/MANHWA_CORPUS.md)

## The world in nine rules

Ten years after the gates opened, Seoul runs on what hunters bring out of them. Summoners are the class everyone sends in first.

1. **The Opening.** Ten years ago, gates opened across the world in one night. Inside each one is a dungeon: a broken piece of somewhere else, under a sky of the wrong colour.
2. **Grades and breaks.** Gates are graded F to S. A gate closes when its boss dies. A gate nobody clears in time *breaks*, and its monsters spill into the street.
3. **Cores.** Small monsters drop small cores, which power Seoul's hospitals, trains and lights. A boss drops one big core worth a fortune.
4. **Hunters.** About one person in five hundred awakens. The Hunter Association ranks them F to S. Guilds hire them, and streamers broadcast their raids.
5. **Summoners are the bottom of the ladder.** A normal summoner calls a *husk*, a faceless white doll that falls apart after one hit.
   - Guilds hire summoners as trap-testers: the husk walks in first to set off the traps, and the summoner is paid per trap.
   - "Summons go first" is the raid rule.
6. **Jaeha's summons are different.** His are people from the other side of the gates, with names, voices and opinions. They can refuse an order, and they can refuse to come at all. In public they wear white husk masks, and the Association files them as "unusual husks".
7. **Kept gates (the secret of Arc 4).** A gate stays open as long as its boss lives. The Kanghan Group chains bosses alive inside unregistered gates and drains them for years. They call these gates core farms.
8. **What bosses are (the secret of Arc 6).** The dungeons are pieces of a dying world, the Far Side, eaten by a corruption called the Hush.
   - Every boss is one of its fallen heroes, hushed, and a boss core is what is left of them.
   - Small monsters are only Hush-spawn, so their cores are just fuel.
   - Kanghan has known this for years.
9. **The Operator protocol.** The Far Side's last defenders built a protocol that lets a commander outside the Hush's reach call their fighters and send them in first.
   - It binds to one living, willing Operator. If he is forced, the protocol ends.
   - Operator #1 was the first person on Earth it chose, ten years ago. He sent his fighters first until none came back, and the Hush took him. The night he fell was the night the gates opened.

## The power system

Jaeha keeps the old power, now made visible: he calls fighters from the Far Side, links to them, carries their pain, and turns what he carries into his own strength.

| Skill | Levels (chapter) | What it does | Limit or cost |
| --- | --- | --- | --- |
| CALL | ch 1 | Calls the Far Side. A fighter sees Jaeha, hears his offer and decides whether to answer. | Needs Route Alignment at 100%. The window stays open 60 seconds; if nobody accepts, the call is wasted. |
| LINK | ch 2 | Feel and see through a summon, and give silent orders. | Their pain comes through too. |
| CARRY | ch 2 | Take part of a summon's damage into his own body so they keep fighting. | It hurts. Overload means nosebleeds, then collapse. |
| PASS | I ch 15 (between two summons) · II ch 60 (a chain through many) · III ch 70 (everyone on the field) | Move force between linked bodies: a blocked hit becomes an arrow's power. | Each hand-off loses some force. |
| STORE / RELEASE | I ch 40 (one stored strike) · II ch 55 (chained strikes) · III ch 80 (through a weapon) | Keep the force he carried and use it himself. This is how he becomes strong. | Too much at once breaks his bones. |
| CONTRACT | ch 48 | Free a hushed boss instead of killing it. If the hero agrees, they join. | No core, so no money. They can say no. |
| VANGUARD | ch 97 | Go in first, ahead of his summons, and release everything he has stored. | One use at first. |
| UNISON | Part Two | Fuse with a summon. | Can't be undone. |

**How summons live on Earth.**

- **Field form.** Full power (as far as their seal allows) for a timed call: 5 minutes at first, longer as Jaeha levels.
- **Rest form.** Between calls they stay with him, visible and able to walk and talk, but no stronger than an ordinary person. They must stay within a set distance of him.
- **Cooldown.** The wait between calls is about a minute inside a gate, where mana is thick, and several hours outside. A dungeon break floods the street with gate mana, so summons can fight in a break.
- **In public.** Summons wear white husk masks. Nib wears the cracked face of the husk he came through.

**Meters the reader can track.**

- **Route Alignment (%).** It fills each time Jaeha deals with a new kind of boss, whether he harvests it or releases it. At 100% he can CALL. When his summon slots are full, a full meter breaks a seal or adds a slot instead.
- **Operator level and summon slots.** Slots are how many summons he can keep: 1 in chapter 1, 7 by chapter 100.
- **Seals.** Every summon arrives at a fraction of their old power (Nib at 1/5). A seal break is a big power-up and changes how the summon looks.

**The rule that protects Jaeha.** A chapter 4 window reads: [OPERATOR AUTHORITY CANNOT BE TRANSFERRED. IF THE OPERATOR IS FORCED, THE PROTOCOL ENDS.] So nobody can simply seize him; they have to recruit him, test him or trick him.

**Fight rules (how "summons go first" works on the page).**

1. Summons take the front. Jaeha reads the fight, calls the enemy's tells and carries hits.
2. Every win needs one smart move by Jaeha: a pattern he read, a trap he used, a rule he bent or a combo.
3. Summons can lose, and they can refuse. They get hurt, their field time runs out, or they say no, and Jaeha has to think fast.
4. Every reward and every limit appears as a window with numbers.

**What came from the old version.** LOAD SHARE becomes CARRY, and the reservoir becomes STORE / RELEASE. Relay and lattice become PASS II and III. Fusion becomes UNISON, draws become CALL, and summons can still say no.

## The main character: Kang Jaeha

Kang Jaeha (24) is an F-rank summoner who has survived 312 raids as bait by watching everything and writing it down.

- **Name card in chapter 1.** KANG JAEHA (24) · F-RANK SUMMONER · TRAP-TESTER, 4 YEARS · 312 RAIDS · 0 KILLS
- **Look.**
  - Lean, 178 cm, with tired eyes and messy black hair falling over one eye.
  - A grey hoodie under an orange trap-tester vest with a white "T" patch, and fingerless gloves.
  - A battered black notebook in his chest pocket and a pencil behind his ear.
  - Later: a black field coat from Arc 5, and the Ninth Wall blade from chapter 97.
- **His signature: the notebook.**
  - Four years of monster patterns, trap types and every raid leader's bad habits.
  - When he is planning, he writes. When the plan is ready, he closes the notebook.
  - Readers learn that the closing notebook means somebody is about to lose.
- **Outside and inside.** Outside he is quiet, polite and easy to overlook. Inside he is cold, funny and counting everyone's mistakes.
- **How he is smart.**
  - He remembers patterns from 312 raids.
  - He reads system windows like contracts and finds the loopholes.
  - He predicts things and is proven right.
  - He turns traps and terrain into weapons, and he plans combos.
- **Home.** A rooftop room in Mangwon-dong with his sister Seoa (15). Their parents died on the night of the Opening. The rent is late, and her school trip isn't paid.
- **Ghost.** Four years ago his mentor Oh Minseok, another trap-tester, pushed him out of a sealed room and died inside. Jaeha tried to go back in and was dragged away. The guild called it an accident. Minseok's rule was "Everyone comes back."
- **Want.** Money and safety for Seoa, and never to be bait again.
- **Flaw.** He trusts nobody, keeps secrets and carries everything himself. CARRY is his flaw turned into a power.
- **Need.** To let others choose to go first, and to step forward himself.
- **Part One arc.**
  1. Bait (ch 1).
  2. Commander of his own small team (ch 12).
  3. Exposes the guild that killed Minseok (ch 21).
  4. Survives the kept gate beside his rival, and his body breaks (ch 33).
  5. Makes his first kill with his own hands (ch 40).
  6. Learns he has been harvesting people, and stops (ch 50).
  7. Wins his first fight against a boss alone (ch 55).
  8. Fights on the front line in the Seoul Break (ch 70–72).
  9. Founds GO FIRST (ch 75) and beats the Collector one-on-one (ch 84).
  10. Goes in ahead of his summons for the first time: "Today, I go first" (ch 97).
- **Voice.**
  - In public: "Of course, sir. My husk is ready, and it's a very brave husk."
  - Inner voice: "Its left shoulder drops before every sweep. Three, two..."
  - To Nib: "I'm not in charge because I'm strong. I'm in charge because I read the manual."

## The summons

Seven summons join in Part One: the first in chapter 1, then one every 8–20 chapters. Each is a Far Side hero with a legend, a want and a running joke.

| Summon | Role | Arrives | How |
| --- | --- | --- | --- |
| Nib | scout and knife-fighter | ch 1 | emergency CALL, through Jaeha's last husk |
| Borro | tank and carrier | ch 10 | CALL, won with a promise |
| Lyra | archer | ch 18 | CALL in the middle of a raid |
| Pim | signals and detection | ch 36 | CALL |
| Maud | field surgeon | ch 48 | first CONTRACT (a freed boss) |
| Caldric, the Bell General | heavy fighter | ch 68 | CONTRACT (the Seoul Break's boss) |
| Kett | young scout | ch 88 | freed from Kanghan's Annex |

**Nib, goblin scout, "the last scout of the Ninth Wall".** The one name kept from the old version, redesigned.

- **Look.**
  - 105 cm (his head reaches Jaeha's belt) and wiry, with grey-green skin and yellow eyes.
  - Long ears (the left one notched) and one small fang.
  - A charcoal hooded scout cloak with too many pockets, a red scarf, two short knives and brass binoculars.
  - Barefoot until he chooses his own boots.
  - In public, he wears the cracked white face of the husk he came through.
- **Personality.** Few words, but always whole sentences. Deadpan, suspicious of doors and food, and quietly kind.
- **Running gag.** "You first." He makes everyone else go through doors and taste food first. It's a scout's habit and the title turned upside down.
- **Want.** To find his apprentice Kett, missing since the Ninth Wall fell.
- **Seal breaks.** Each one changes his look.
  - ch 3: the Ninth Wall's colours return to his cloak.
  - ch 20: scout-captain armour.
  - ch 55: shadow-step (his outline smokes when he moves).
  - ch 88: his full form, with the nine-tower crest.
- **Voice.** "Who's in charge here?" ... "Then why are you the one bleeding?" ... "I won't kill him. But I'll hold him for you."

**Borro, stoneback carrier.**

- **Look.** 2.4 m and slow-eyed, with slate-grey skin and a shell of stacked slate plates with moss and tiny flowers growing on it. He carries a door-sized iron shield.
- **Personality.** Gentle, slow-talking and dryly funny. He gardens and hates being called equipment.
- **Legend.** He carried a whole village across a collapsing bridge.
- **How he joins.** Jaeha's pitch: "I can't promise you a garden. I can promise you a roof, and I'll carry what hits you." He lives under a tarp on the rooftop: technically, a roof. In public he is "the biggest husk anyone has ever seen".
- **Voice.** "I'm slow on purpose. Slow things arrive."

**Lyra, river archer.**

- **Look.** Tall, with blue-grey skin and silver freckles, a long braid strung with river beads, a white longbow and a flute at her belt.
- **Personality.** Vain, competitive and musical. She loves applause and money and says so, and she is brave.
- **Want.** To find her little brother Ilan, who left their river home.
- **Signature combo, "Borrowed Thunder" (first at ch 19).** Borro blocks a hit, Jaeha PASSes the impact, and Lyra fires it.
- **Loss.** In Arc 7 the Collector breaks her bow, and she has to win her aim back.
- **Voice.** "Count the arrows if you want. I only need the one."

**Pim, moth-folk signal keeper.**

- **Look.** 1.4 m of fluffy cream fur, with huge black eyes, feathery antennae and soft wings folded like a cape. He wears a headset "borrowed" from a PC bang.
- **Personality.** Loves gossip, festivals and K-dramas, even though loud places hurt his antennae. Dramatic, and brave when it counts.
- **Job in the story.** He hears signals across the gates: the failing Busan seal (Arc 5), Kett's call sign (ch 40) and the fall of Caldric's fortress (Arc 6).
- **Voice.** "Shh! Someone on the other side is calling. And they're whispering YOUR name, boss."

**Maud, armoured field surgeon.**

- **Look.** 1.9 m and broad, with a burn-scarred face and cropped white hair. She wears surgeon's plate over stitched leather aprons and carries a bone saw and a needle case.
- **Story.** While hushed, she was the boss "Butcher of Ward Nine". Freed, she wants to save more people than she killed.
- **Limit.** Her healing closes wounds but can't replace blood or erase exhaustion.
- **Voice.** "Hold still. This will hurt, and then you'll live. That's the deal."

**Caldric, the Bell General.**

- **Look.** 2.1 m in cracked bronze armour shaped like a great bell. He fights with a bell-headed mace whose every hit rings. While hushed, the bell is silent.
- **Personality.** Formal, honourable and hopeless with vending machines and phones.
- **Buried conflict.** His bell rang the retreat that left Nib's wall alone for nine days. He is also the caller who refused Jaeha in chapter 9; his fortress fell afterwards.
- **Running gag with Nib.** "A general goes first." / "A scout goes first. Generals go second. That's why they live."

**Kett, young goblin scout.**

- **Story.** Nib's apprentice, held in Kanghan's Annex. He is freed half-hushed in chapter 88, and Maud and a CONTRACT bring him back.
- **Personality.** He talks too much: the opposite of Nib.

## Allies and rivals

The human cast gives Jaeha a family, a team, a crowd, a rival and a teacher. Each one arrives at a turning point and wants something of their own.

| Character | Who they are | Wants | Arrives | Look |
| --- | --- | --- | --- | --- |
| Kang Seoa (15) | His sister. Sharp-tongued, she runs the household budget in a spreadsheet and runs the market evacuation in ch 11. Never a damsel, never kidnapped. | Her brother home for dinner, and a place at an art high school | ch 5 | short bob, school uniform, round glasses, calculator keychain |
| Song Yerin (20) | E-rank healer. She froze on her first raid in ch 1, then quits Black Hound in ch 5 and becomes the team's medic. | To prove she won't freeze again | ch 1 | small and freckled, oversized healer's jacket, pink first-aid bag |
| Yoo Bomi (21) | E-rank ranger and streamer ("BomBom TV"). Loud, nosy and funny. Her live chat is the crowd, and part of it never believes anything. | 100,000 subscribers, to save her parents' restaurant | ch 5 | neon-yellow jacket, camera drone, a bow she rarely hits with |
| Choi Dongmin (34) | Gate Rescue Corps responder who finds Jaeha at the gate exit. Chatty, sarcastic and kind, living on kimbap and coffee. He testifies at Jaeha's re-test and keeps a copy of the buried proof. | One week without a break killing someone in his district | ch 4 | rescue jacket, reflective stripes, permanent eye bags |
| Moon Ahin (22) | A-rank summoner, "the Puppeteer". Director Baek's niece and heir to Kanghan's guild. She commands 40 flawless husks like an orchestra and despises trap-testers. Rival, then friend, and she funds GO FIRST. | To prove husks are an art, and to get out of her uncle's shadow | ch 12 (meets him in Arc 4) | white coat, silver hair ribbon, conductor's baton |
| Auntie Geum Okran (62) | Retired S-rank, "the Wall of Busan". Runs a 24-hour tteokbokki stall and trains Jaeha's body so it can hold what he stores. | One student who doesn't die | ch 33 | apron over a tracksuit, one prosthetic arm, a ladle she fights with |
| Oh Minseok (died 4 years ago) | Jaeha's mentor, another trap-tester. His recording is found in ch 21; its last seconds are the ch 22 hook. | (in flashbacks) everyone home | flashbacks | the same orange vest, a kind grin |

**Running jokes.**

- Seoa pays Nib in snacks for chores.
- Bomi films everything and can't hit anything.
- Choi turns up with kimbap whenever Jaeha least wants a witness.
- Geum's training is always "just one more".

## Villains and the long mystery

Part One climbs a ladder of villains, each one working for the next: a guild bully who serves a corporation without knowing why, the corporate director, the monster he thinks he controls, and the series villain behind them all.

**Mok Hangyu (38): Black Hound Guild raid leader, B-rank tank (Arcs 1–3).**

- **Who he is.** Charming on camera and ruthless off it. Black Hound is Kanghan's contractor, and Mok does its dirty work.
- **What he did.** Four years ago, on Kanghan's orders, he sealed Minseok inside the Han River gate.
- **Role in the story.**
  - He sends Jaeha in as live bait in chapter 1, then blames him for four dead hunters.
  - He is exposed in chapter 21.
- **Look.** Big, with a gold chain, a black guild jacket with a hound's head on it, and a tower shield.

**Director Baek Taegun (54): Kanghan Group Core Division (Part One main villain).**

- **His argument.** "Korea runs on cores. Do you want the hospitals dark?"
- **His secret.** He runs the kept gates, where chained bosses are drained for years. He also runs the Annex, where Far Side beings are held, Kett among them.
- **What he wants.** He wants the Operator alive and willing, because forcing an Operator ends the protocol.
  - His signal in chapter 5 names the gate, not the person, so he starts by investigating the survivors.
  - From then on he tests, tempts and squeezes Jaeha instead of grabbing him.
- **Look.** Grey suit, silver glasses, and a cane with a core in the handle. Name card in chapter 12.

**The Collector (Arcs 7–8).**

- **Who he is.** A masked hunter of Far Side heroes who wears the badges of those he has taken.
- **Who he serves.** Baek thinks he controls him. He serves the Hush King.
- **His record.** He beats Jaeha's whole linked team once (Arc 7). Jaeha beats him one-on-one in chapter 84.

**Operator #1, the Hush King (series villain).**

- **Who he was.** The first person on Earth the protocol chose. He sent his fighters first until none came back, and the Hush took him on the night the gates opened.
- **What he wants now.** Jaeha's protocol, so he can open every gate.
- **In Part One.** Only interface glitches ("OPERATOR #1 — STATUS: HUSHED") and the last page of chapter 100: "Operator #2. You're late."

**Mysteries, planted and paid off.**

| Mystery | Planted | Paid off |
| --- | --- | --- |
| Why the protocol chose Jaeha: "Sent first: 312 times. Left someone behind: 0 times." | ch 1 | ch 100: Operator #1's record was the reverse |
| The broken chains around the first boss | ch 1 | Arc 4: Kanghan chains bosses to keep gates open |
| The Ninth Wall blade, too heavy for Jaeha to lift | ch 4 | ch 97: he lifts it with stored force |
| "That's what Dad said, the night of the Opening." | ch 7 | Part Two: the night Operator #1 fell |
| The Kanghan guards at a gate under the Han River | ch 8 | Arc 4: the gate where Minseok died, kept open for four years |
| Bosses whose window offers only HARVEST | ch 8 | ch 50: they were people too; his level hid the RELEASE option |
| The first caller who refuses: "Not yet, Operator. My wall still stands." | ch 9 | ch 68: Caldric, the Bell General |
| Kett's call sign in Pim's signals | ch 40 | ch 88: Kett is freed from the Annex |

## Series storyboard

Part One runs nine arcs over 100 chapters. The summons carry the fights until chapter 40, when Jaeha starts fighting with his own hands. In chapter 97 he finally goes in ahead of them.

| Arc | Chapters | Summon joins | Power and seal milestones |
| --- | --- | --- | --- |
| 1. Bait | 1–5 | Nib (1) | CALL (1); LINK and CARRY (2); Nib's seal 2/5 (3) |
| 2. The Trap Rats | 6–12 | Borro (10) | first CALL by choice (9–10) |
| 3. Black Hound | 13–22 | Lyra (18) | PASS I (15); Nib's seal 3/5 (20) |
| 4. The Kept Gate | 23–33 | — | his body breaks under CARRY (33) |
| 5. The Wall of Busan | 34–40 | Pim (36) | STORE / RELEASE I and his first kill (40) |
| 6. The Hushed | 41–55 | Maud (48) | CONTRACT (48); RELEASE II and Nib's seal 4/5 (55) |
| 7. Seoul Break | 56–72 | Caldric (68) | PASS II (60); PASS III (70) |
| 8. Go First | 73–86 | — | RELEASE III (80) |
| 9. Gwanghwamun | 87–100 | Kett (88) | Nib's seal 5/5 (88); VANGUARD (97) |

1. **Bait (1–5).** Live bait, Nib, the release and the funeral he walks into.
   - **Ends:** Kanghan hunts for the Operator among the survivors.
2. **The Trap Rats (6–12).** Money, the team, Borro and the Market Break.
   - **Ends:** Jaeha accepts Black Hound's invitation and decides to set his own trap.
3. **Black Hound (13–22).** Justice for Minseok.
   - After the viral clip, the Association orders a re-test, and Choi testifies.
   - PASS I unlocks in training (15).
   - The B-grade raid is a trap. Mok wants Jaeha dead, and Kanghan's man inside Black Hound turns it into a test of the Operator. Jaeha sets his own trap first.
   - Lyra joins mid-raid (18). "Borrowed Thunder" kills the boss (19), and Nib's seal reaches 3/5 (20).
   - Mok's confession and Minseok's recording go out on Bomi's stream (21).
   - **Ends (22):** the recording's last seconds point to the Han River gate Jaeha saw in chapter 8, still open after four years.
4. **The Kept Gate (23–33).** Inside, Kanghan keeps a boss chained alive and drains it: a core farm.
   - Moon Ahin has come in on her own to find out why her family's guild hires trap-testers for an unregistered gate, so the rivals have to work together.
   - They escape with proof. Kanghan's people inside the Association bury it, but Choi keeps a copy.
   - **Ends:** Jaeha's body breaks under CARRY. Auntie Geum: "Your head is S-rank. Your body is garbage."
5. **The Wall of Busan (34–40).** Pim joins (36) and hears the Busan sea gate's seal failing: 72 hours left.
   - Jaeha trains against that clock while Kanghan watches him.
   - The sea gate breaks, and he makes his first kill with STORE / RELEASE I (40).
   - **Ends:** Pim hears a call sign from inside a gate. It is Kett's.
6. **The Hushed (41–55).** An A-grade boss turns out to be a hushed field surgeon. Jaeha's first CONTRACT frees her, and Maud joins (48).
   - The reveal (50): every boss was a person, including the ones he harvested in chapters 8 and 12. His level hid the RELEASE option, and Kanghan knew. He stops harvesting boss cores and earns from clear contracts instead.
   - Pim hears the fall of a fortress with a great bell.
   - **Ends (55):** Jaeha beats a boss alone for the first time (RELEASE II). Kett is a prisoner in Kanghan's Annex, and Nib's seal reaches 4/5.
7. **Seoul Break (56–72).** The Han River farm ruptures, and gates break across Seoul.
   - The Collector beats the whole linked team once and breaks Lyra's bow.
   - The break's boss is Caldric, the Bell General, hushed: the caller who refused in chapter 9.
   - Jaeha links everyone (PASS II at 60, PASS III at 70), fights on the front line, and frees Caldric (68).
   - **Ends (72):** the government moves to register his summons as "strategic assets".
8. **Go First (73–86).** Jaeha founds the guild GO FIRST with former trap-testers (75), funded by Moon Ahin, who breaks with her uncle.
   - The Collector leads a Kanghan strike on the GO FIRST depot, and Jaeha beats him one-on-one with RELEASE III (84).
   - **Ends (86):** Baek's plan is revealed: force open an S-grade gate at Gwanghwamun.
9. **Gwanghwamun (87–100).** A raid on the Annex frees Kett, who becomes the seventh summon, and Nib's seal reaches 5/5 (88).
   - The S-grade gate opens over Gwanghwamun, the scene from chapter 1's flash-forward.
   - The summons go first and fall back one by one. Jaeha lifts the Ninth Wall blade and, for the first time, goes in ahead of them: "Today, I go first." (97)
   - **Ends (100):** through the gate, the Far Side's sky, and Operator #1: "Operator #2. You're late."

**After Part One.**

- **Part Two, The Far Side (about ch 101–200).**
  - Crossing over to the Ninth Wall.
  - Operator #1's story, a dark mirror of Jaeha's.
  - UNISON and its permanent cost.
  - Jaeha reaches S-rank.
- **Part Three, Everyone Comes Back (about ch 201–260).**
  - War across both worlds and the final battle with Operator #1.
  - The old doctrine reversed: Operators go first.
  - The gates end as doors instead of wounds.

## Arc 1 (chapters 1–5): Bait, beat by beat

Arc 1 takes Jaeha from bait to Operator in five chapters. Every chapter from 2 on has a payoff, a smart move and a short laugh.

### Chapter 1: Bait (about 70 panels)

1. **Flash-forward (8 panels).**
   - A red sky over Gwanghwamun and an S-grade gate like a wound.
   - A livestream chat scrolls: "A SUMMONER is going in first??", "Summoners are bait, everyone knows that."
   - Behind a man in a black coat stands a line of strange silhouettes; the smallest, a cloaked goblin, is at the front.
   - Nib: "You first?" Jaeha: "Not yet. My summons go first."
   - Caption: "Six months earlier, I was the bait."
2. **The trap-tester (14 panels).**
   - A C-grade gate in a subway construction site, raided by the Black Hound Guild.
   - Raid leader Mok: "Summoner, you know the rule." Jaeha: "Yes, sir. Summons go first."
   - His faceless white husk walks ahead. CLICK. Spikes shred it, and the hunters laugh.
   - Name card: KANG JAEHA (24) · F-RANK SUMMONER · TRAP-TESTER, 4 YEARS · 312 RAIDS · 0 KILLS.
   - "Why do we even bring a trap rat along?" "Because a trap rat is cheaper than a healing potion."
   - In his notebook: "Stone lizards. Tail sweep after the third bite. Blind on the left."
   - He tells the rookie healer, "Take one step to your left, please." A tail misses her by an inch, and she stares at him (name card: SONG YERIN (20) · E-RANK HEALER · FIRST RAID).
   - The title card lands here, about a fifth of the way in.
3. **Live bait (12 panels).**
   - The boss room has an iron door with a red lamp.
   - Mok (name card): "The boss in there only wakes for something alive. Husks don't count. So you walk in, it comes for you, and we kill it from behind. Summons go first. Then summoners."
   - Jaeha, polite: "Sir, that lamp is red. On every survey I've seen, red means the grade is wrong." Mok: "Then you'd better run fast."
   - Inside, a giant knight kneels in broken chains. There is a dark hole where its face should be.
   - Jaeha takes one step, and the hole lights up red.
4. **The ambush fails (12 panels).**
   - Black Hound attacks from behind, but the knight is far stronger than C-grade and cuts through them (shown in silhouettes and splashes).
   - Behind a pillar, Jaeha reads it: "It's slow to turn in that armour, and it always hits whatever is in front of it." He pulls the frozen Yerin out of its path: "Stay behind me and keep your back to the pillar."
   - Mok retreats through the door with two hunters: "Shut it! The trap rat will keep it busy!" The door slams, and the red lamp locks.
5. **The last husk (10 panels).**
   - Jaeha has one husk left in him today. The knight's blade rises over Yerin.
   - "Go first. One more time." He pours everything into the husk, and it stands in front of her, glowing the wrong colour.
   - Old, glitching windows appear one by one:
     - [OPERATOR CANDIDATE DETECTED]
     - [SENT FIRST: 312 TIMES]
     - [LEFT SOMEONE BEHIND: 0 TIMES]
     - [EMERGENCY CALL: 1 · THE HUSK WILL BE USED AS A DOOR]
   - The blade comes down. [SOMEONE ANSWERED.]
6. **The answer (4 panels).**
   - The husk's white shell cracks open. A small cloaked figure inside it has caught the giant blade an inch from Yerin's face with two crossed knives. Half of the husk's cracked face still covers his own, like a mask.
   - He looks back: "Who's in charge here?" Jaeha: "I think... it's me?"
   - **Hook:** the first summon arrives.

### Chapter 2: Who's in Charge (about 65 panels)

1. **Back in.** Nib: "Then why are you the one bleeding?" He kicks the blade aside and drags them both behind a pillar.
2. **Nib's window.** [NIB · FAR SIDE SCOUT · SEAL 1/5 · FIELD FORM 05:00]. The countdown keeps returning.
3. **First words.**
   - Nib: "Tell me quickly. What is that thing, and what are you?"
   - Jaeha: "It's a boss. I'm a trap-tester. I walk in first so other people don't have to."
   - Nib: "Then we do the same job. Mine paid better."
4. **Summons go first.** Nib is fast, but the knight's reach is huge and the seal holds him back. He is thrown across the hall.
5. **LINK unlocks.**
   - Jaeha sees through Nib's eyes in a split view.
   - From his notebook he calls the tells: "Its left shoulder drops before every sweep. Wait for it... now!"
   - Nib ducks, and his knives open a seam in the armour. **Payoff: the smart MC.**
6. **CARRY unlocks.**
   - The counter-blow comes for Nib. A window asks [CARRY?], and Jaeha takes the hit in his own body.
   - Nib: "You took my hit. Why would you do that?" Jaeha: "Because you're the one who can actually hurt it."
7. **Yerin.** Shaking, she heals him: "I froze before. I'm not going to freeze again."
8. **Hook.** With 40 seconds left, the knight roars in an old language. Nib stares at the sigil on its chest, a wall with nine towers: "That's the sigil of the Ninth Wall. That knight was my commander."

### Chapter 3: The Ninth Wall (about 65 panels)

1. **Flashback (8 grey panels).** Nib held the Ninth Wall alone for nine days and sent his apprentice Kett back with a message. A bell rang the retreat in the distance. "Nobody came back for me."
2. **Nib refuses.**
   - Jaeha: "Nib, take its legs." Nib: "No. Not him. I won't."
   - The timer hits zero, and Nib drops into rest form: [FIELD FORM ENDED · COOLDOWN 01:00].
3. **The trap-tester's plan.**
   - Jaeha reads the floor, the old fortress's pressure plates, and sketches which plate fires which spikes.
   - He closes the notebook. Then he stands in front on purpose to draw the knight onto the plates, and spikes and a portcullis pin it.
   - "Three hundred and twelve raids. I know a trap when I see one." **Payoff.**
4. **Survive the cooldown.**
   - The knight starts tearing free. Jaeha and Yerin take turns standing in front of it, using her healing flares as bait.
   - Yerin: "Is this what you do every single day?" Jaeha: "Usually there's less screaming."
5. **The second call.**
   - Nib returns to field form: "You called me back." "I told you. Everyone comes back."
   - [SEAL 1/5 → 2/5]: a power-up splash, and his cloak takes the Ninth Wall's colours.
   - Nib: "I still won't kill him. But I'll hold him for you."
6. **Hook.** Through the hole in its face, the knight speaks clearly: "Nib... end it... before the Hush takes you too."

### Chapter 4: Harvest or Release (about 70 panels)

1. **The last exchange.**
   - Nib holds the knight. Jaeha carries the counter until his nose bleeds, and Yerin heals him.
   - Through LINK, Jaeha sees a red crack in the rim of the hole: the weak point.
   - Nib gives his consent: "Do it. He asked us to." Jaeha: "Then we do it together." Nib's knives go in on Jaeha's call.
2. [BOSS DEFEATED: HUSHED KNIGHT-COMMANDER]
3. **The choice.**
   - Two options: [HARVEST CORE · EST. ₩400,000,000] or [RELEASE].
   - For one panel, Jaeha remembers the rent and Seoa's school trip.
   - "What does release do?" [THE REMAINS RETURN TO THEIR OWN.]
   - He looks at Nib, and he picks RELEASE.
4. **The release.**
   - For one panel the knight has a real face, an old soldier's: "Nib. You found an Operator. Go first for him, and make sure he comes back." Then he turns to ash.
   - His chains crumble. One link carries a stamped mark, unreadable for now.
5. **The blade.**
   - The knight's blade goes into Jaeha's inventory: [NINTH WALL BLADE · STRENGTH REQUIRED 90 · YOUR STRENGTH 7].
   - He can draw it into his hands, but he can't lift it.
6. **Reward cascade.**
   - [OPERATOR LV. 1 → 3], [LINK LV. 2], [CARRY LV. 2], [ROUTE ALIGNMENT 30%].
   - Title: "The One Who Went Back".
   - Status window: CLASS: OPERATOR (shown to others as Summoner (F)).
   - The rule: [OPERATOR AUTHORITY CANNOT BE TRANSFERRED. IF THE OPERATOR IS FORCED, THE PROTOCOL ENDS.]
7. **Outside.**
   - [GATE CLOSING · 30s]. They dive out into the night.
   - A Gate Rescue responder wraps them in blankets (name card: CHOI DONGMIN (34) · GATE RESCUE CORPS).
   - Choi: "An F-rank and a rookie walked out of a gate that killed four B-ranks? I'm going to need a lot more coffee for this report."
   - He points at the masked Nib, now in rest form: "And what's the little guy?" Jaeha: "He's my husk, sir. A very unusual husk."
8. **Hook.** A billboard across the street shows Black Hound's live press conference. Mok, solemn: "Our trap-tester set off a hidden boss. Four of our hunters died. Kang Jaeha is presumed dead."

### Chapter 5: A Few Words at My Memorial (about 65 panels)

1. **The memorial.** Black Hound holds a memorial press event. Outside, the streamer Bomi broadcasts for clout (name card). Her chat: "rip trap rat", "F".
2. **The return.**
   - Jaeha walks into the shot behind Mok, bandaged, with Yerin and a small masked "husk": "Sorry I'm late, sir. Could I say a few words at my memorial?"
   - Viewers jump from 412 to 9,870. The chat splits: "HE'S ALIVE??", "this is staged", "summoners are still bait lol".
3. **Mok's offer.**
   - Mok hugs him for the cameras. In a back room: "Sign a statement that you set off the trap, and this ten million is yours."
   - Jaeha, polite: "That's very generous, sir. Could I think about it until tomorrow?" In his pocket, his phone is recording. "Not yet."
   - Yerin refuses to sign and quits on the spot: "I watched you close that door." She leaves with Jaeha.
4. **Home.**
   - Seoa (name card) is furious and crying with relief: "You said this was your last month of trap-testing."
   - Nib, in rest form, meets instant ramen. "You first." Seoa: "Is your husk... eating?" Nib: "I am not a husk. I am hungry."
   - Jaeha draws the blade from his inventory to show them. It drops and cracks the floor. Nib: "You're weak." Jaeha: "I'm aware."
   - Rent of ₩300,000 is due Friday, and his savings are ₩0.
5. **Hook.**
   - Kanghan Tower. A monitor reads: [GATE 0912 · BOSS CORE NOT HARVESTED · SIGNAL: OPERATOR PROTOCOL].
   - A man in silver glasses: "The survivors were Mok, two of his hunters, a rookie healer, and a trap-tester who should be dead. Find out which one of them it is."

## Arc 2 (chapters 6–12): The Trap Rats, chapter by chapter

Arc 2 gives Jaeha money trouble, a team, a second summon and his first public win. Every chapter has a smart move by Jaeha and an enemy that can really hurt them.

**Ch 6, Trap Rats.**

- To pay the rent, Jaeha takes an E-grade sewer gate as a trap-tester, with Nib posing as his husk. Bomi tags along to film "the trap-tester who came back".
- Nib is supposed to stay silent in public. He fails at once: "Your grip on that sword is wrong. You'll lose a finger."
- **Smart move.** Jaeha steers Bomi's drone toward a decoy tunnel on purpose, so it films nothing while Nib clears a rat swarm in field form.
- Bomi's chat calls the team "the Trap Rats" as an insult. Bomi likes it.
- **Hook (mystery).** At home, Bomi freezes her footage on one frame: a small masked shape moving faster than any husk. "Husks don't move like that."

**Ch 7, Ten Thousand Won a Trap.**

- Choi drops by the rooftop with kimbap and questions. Jaeha answers every one without saying anything.
- Black Hound rigs a trap on Jaeha's next survey job. He predicted it from his notebook page on Mok's men, and the saboteurs walk into their own trap. "Who sets a trap for a trap-tester?"
- Bomi shows him her frozen frame. They make a deal: she films, she never shows Nib's face, and she gets the full story when it's safe.
- **Hook (personal).** Seoa finds his torn vest: "You promised you'd quit." "After one more gate." "That's what Dad said, the night of the Opening."

**Ch 8, Eyes.**

- Jaeha trains LINK range by seeing through Nib from rooftops across Mangwon. A street cat chases Nib, who is in rest form, the whole way.
- Through Nib's eyes he spots an unregistered gate under a Han River bridge, guarded by men with Kanghan badges.
- **The first team job.** The Trap Rats take a D-grade gate in a flooded car park.
  - Nib can't fight in deep water, so Jaeha lures the boss, a drowned hound, up the dry ramp, and it bites him.
  - Its window offers only HARVEST, so they harvest it. The rent is paid.
- **Hook.** [ROUTE ALIGNMENT 100%] [A CALL IS AVAILABLE].

**Ch 9, Not Yet, Operator.**

- **The CALL is a conversation.** Whoever answers sees Jaeha and hears his offer.
- **The refusal.** A silhouette ringing a bell in a burning fortress answers first: "Not yet, Operator. My wall still stands." [DECLINED] at 00:41.
- **Smart move.** Jaeha reads the window's fine print and learns the call is wasted if nobody accepts in time. He rewrites his offer while the clock runs down.
- **Hook (countdown).** 00:03, and something huge and slow stirs under a mossy sky.

**Ch 10, A Roof, Not a Garden.**

- **Borro answers.** He asks what Jaeha can offer. "I can't promise you a garden. I can promise you a roof, and I'll carry what hits you."
- **Borro arrives.** He comes through the window and crushes the bed. He moves in under a tarp on the rooftop. "You promised me a roof." "You're on a roof." "...Technically."
- **The first two-summon fight.** A D-grade job in a half-built tower, kept quiet.
  - **Smart move.** The floor is collapsing, so Jaeha sets Borro on the load-bearing beam and sends Nib around the edge.
  - **Cost.** CARRY for two leaves him bleeding.
- **Hook (threat).** Emergency alerts across Mapo: a dungeon break at Mangwon Market.

**Ch 11, Market Break.**

- **Seoa takes charge.** She is at the market, but she doesn't wait to be rescued. She knows every alley, runs the evacuation with the market grannies, and phones Jaeha with directions.
- **The rule.** A window explains it: gate mana floods the street during a break, so the summons' cooldown is short.
- **Smart move.** The narrow alleys funnel the monsters to Borro.
- **Impact panel.** Borro holds up a collapsing footbridge with people still on it. Jaeha CARRIES for both summons until his nose bleeds.
- A market granny hits a monster with a radish.
- **Hook.** The break's boss, a huge cold-blooded serpent, bursts up from under the footbridge.

**Ch 12, His Summons Go First.**

- **Smart move.** Cold slows the serpent, so Jaeha herds it into the fish market's freezer lane, and Nib and Borro finish it. Its window, again, offers only HARVEST.
- **The viral clip.** Bomi's clip "HIS SUMMONS GO FIRST!" goes viral. Most of the chat flips to awe, some still shout "CGI", and the old insult becomes a chant.
- Nib refuses to pose for the thumbnail. "One smile?" "No."
- **Kanghan.** A file updates: "Gate 0912 survivor Kang Jaeha. Operator probability 91%." Name card: DIRECTOR BAEK TAEGUN (54) · KANGHAN GROUP CORE DIVISION. Moon Ahin watches the clip: "Husks don't move like that."
- **Hook (decision).** Black Hound invites Jaeha on a B-grade raid "for heroes". He closes his notebook. "This time, I'm the one setting the trap."

## How every chapter will be built

Every script must pass a 14-point check before any art starts. The rules come from the episodes Claude read and from Korean industry sources.

1. **Something dangerous, funny or strange happens in the first 5 panels:** a cold open, a flash-forward, or a jump straight back into the last cliffhanger.
2. **The title card comes after the hook,** 15–40% of the way in. It is never parked at panel 5.
3. **The chapter turns at least twice** and ends in a different situation from where it started.
4. **A payoff at least every 3 chapters:** a win, a power-up, a reveal, or an enemy humbled.
5. **Talk-only panels stay at or below 50%.** Our old chapters were at 69%.
6. **Bubbles are complete sentences averaging 7–10 words.** One or two sentences per bubble, no more than 3 bubbles per panel, and the lines make sense without the art. One-word reactions are fine; clipped fragments are not.
7. **Every important new character gets a name card:** NAME (age) · rank or role · one line.
8. **Every rule, reward and limit appears as a system window with numbers.**
9. **Action is one beat per panel** with a big SFX, at least one impact panel, angles that change every panel, and colour flips for hits.
10. **The last 1–3 panels open a question:** a threat, a mystery, a system message, an arrival, a power or a countdown. The hook type changes from one chapter to the next.
11. **Jaeha does something smart on the page.** He predicts, plans, reads a rule or sets up a combo.
12. **One or two short laughs per chapter,** from character or premise, never breaking a tense beat.
13. **Every fight adds something new** (a rule, a mechanic, a terrain trick or a reveal), and the enemy can really win.
14. **Power is shown through bodies.** Bystanders step back, drop weapons or freeze; nobody makes speeches of praise.

What readers complain about most is fights with no challenge, forgettable side characters, filler, the "everyone is shocked" formula and jokes that break the plot. Rules 4, 11, 12, 13 and 14 exist to prevent those. Full sources are in the [craft bible](https://github.com/abafaboy/abafaboy.github.io/blob/msgf-bible/research/MANHWA_CRAFT_BIBLE.md).

## Decisions (approved 25 October)

The owner chose the recommended option for all six decisions.

| Decision | Approved |
| --- | --- |
| Names | New names (Kang Jaeha, Seoa and the rest), keeping only Nib |
| Jaeha's starting job | Trap-tester |
| Tone | Real danger, with deaths shown through silhouettes and splashes, and short character comedy |
| When Jaeha fights himself | First kill at ch 40, front line from ch 70, "Today, I go first" at ch 97 |
| Real-world themes | Background texture only |
| Part One length | 100 chapters, one YouTube video; the old scripts and the 13 drawn chapters are retired and kept in the repo |
