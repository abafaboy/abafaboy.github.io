"""Fresh final-PNG face protection; unchanged script text, with retained raw and visual QA."""
FACES = {'p01': [[290, 170, 520, 405], [760, 325, 945, 495], [730, 480, 885, 645], [840, 550, 990, 715], [960, 610, 1120, 765], [1280, 575, 1495, 785]], 'p02': [[0, 650, 750, 1024], [805, 710, 975, 895], [745, 20, 1070, 330], [65, 195, 235, 540]], 'p03': [[255, 200, 605, 585]], 'p04': [[110, 325, 365, 590], [545, 305, 895, 670]], 'p05': [[350, 145, 590, 375]], 'p06': [[620, 105, 985, 560], [1235, 250, 1470, 445]], 'p07': [[130, 270, 800, 1025], [355, 940, 490, 1065]], 'p08': [[590, 100, 915, 410]], 'p09': [[100, 300, 320, 505], [235, 495, 1335, 730], [1305, 235, 1525, 420]], 'p10': [], 'p11': [[165, 140, 405, 350], [440, 175, 665, 375], [295, 340, 1490, 780]], 'p12': [[210, 310, 825, 725]], 'p13': [[95, 170, 790, 780], [785, 75, 945, 250]], 'p14': [[285, 355, 640, 670], [560, 600, 845, 935]], 'p15': [[340, 130, 635, 425], [65, 290, 1480, 875]], 'p16': [[725, 180, 825, 295], [90, 645, 1445, 880]], 'p17': [[195, 560, 520, 835], [605, 780, 865, 1045], [710, 295, 985, 570]], 'p18': [[290, 425, 590, 715]], 'end': []}
TEXT = ['The far wall exploded.', 'It was a dragon. A dragon made of ice, long as a river, with no wings at all, and eyes like two cold moons.', "That's it! That's the thing that took my eye!", 'Children behind me! Wren, go for its eyes!', "Oswin's sword blazed with frost. It did nothing. You can't freeze a thing made of winter.", "Wren's arrows bounced off its scales like hail off a roof. Ash leapt for its throat, and it flung him across the hall.", "And it wasn't interested in any of them. It was coming for me.", 'It wants your warmth! Warm One, run!', 'I ran, with eleven children and a blind old woman. The wyrm hit the pillars behind us. And the ceiling came down.', 'When the dust settled, it was dark. And very quiet.', 'A pocket in the rubble, no bigger than a cottage. Yrsa, the children, and me. Somewhere beyond the stones, the wyrm was screaming.', "Its breath had frozen the very air. Frost crept over the children's furs while I watched.", 'The ground melted around me, the way it always did. But only around me. A circle the size of a blanket. Not enough for twelve.', "You're warm.", 'Rune crawled into my lap, as if that were the best news in the world.', "Children. Don't sleep. I will tell you the oldest story, and you must stay awake for the end.", 'Once, the White was green. A queen lived under the mountain, and everything she loved grew.', 'Then men came from the south. Men with lenses. They killed her, and the whole world went cold.', "But she's sleeping. You always say she's sleeping.", 'Her body died, little one. Her heart only sleeps.', 'Men with lenses. Somewhere very far away, a thought tried to reach me. The cold got there first.', "Then the smallest girl stopped shivering. Bram told me once, that's when you should be most afraid.", 'There was one thing I could try. I had never done it to strangers.', 'The Lord Who Measured Zero. Chapter thirty-eight, coming soon.']

def build():
 return f"""
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 37</div><div class="c2">The Wyrm</div></div>
 {gap(100)}
 {narr(TEXT[0],'L0','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L0b">{img('p01','full')}</div>{gap(180)}
 {narr(TEXT[1],'L1','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L1b">{img('p02','full')}</div>{gap(180)}
 {bub(TEXT[2],'L2','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L2b" style="margin-left:210px">{img('p03','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[3],'L3','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L3b" style="margin-left:180px">{img('p04','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[4],'L4','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L4b">{img('p05','full')}</div>{gap(180)}
 {narr(TEXT[5],'L5','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L5b">{img('p06','full')}</div>{gap(180)}
 {narr(TEXT[6],'L6','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L6b" style="margin-left:180px">{img('p07','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[7],'L7','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L7b" style="margin-left:210px">{img('p08','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[8],'L8','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L8b">{img('p09','full')}</div>{gap(180)}
 {narr(TEXT[9],'L9','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L9b">{img('p10','full')}</div>{gap(180)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L10b">{img('p11','full')}</div>{gap(180)}
 {narr(TEXT[11],'L11','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L11b" style="margin-left:210px">{img('p12','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[12],'L12','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L12b" style="margin-left:210px">{img('p13','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[13],'L13','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L13b" style="margin-left:180px">{img('p14','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[14],'L14','margin:0 110px;padding:72px 100px')}{gap(45)}
 {bub(TEXT[15],'L15','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L15b">{img('p15','full')}</div>{gap(180)}
 {bub(TEXT[16],'L16','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L16b">{img('p16','full')}</div>{gap(180)}
 {bub(TEXT[17],'L17','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[18],'L18','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L18b" style="margin-left:180px">{img('p17','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[19],'L19','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {narr(TEXT[20],'L20','margin:0 110px;padding:72px 100px')}{gap(45)}
 {narr(TEXT[21],'L21','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L21b" style="margin-left:210px">{img('p18','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[22],'L22','margin:0 110px;padding:72px 100px')}{gap(45)}
 {gap(120,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L23" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 38 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
