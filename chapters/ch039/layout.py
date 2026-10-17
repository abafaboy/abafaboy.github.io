"""Chapter39: Breath of the Skeld. Fresh final-PNG face regions, corrected p13.
All text is taken verbatim from the unchanged source script; raw and visual checks in qa.
"""
FACES = {'p01': [[175, 335, 365, 520], [800, 220, 1060, 465]], 'p02': [[45, 325, 1345, 730], [1025, 105, 1155, 235], [1110, 170, 1230, 280], [1260, 95, 1410, 245]], 'p03': [[140, 470, 505, 835]], 'p04': [[0, 440, 275, 710], [500, 230, 840, 555]], 'p05': [[185, 365, 505, 690]], 'p06': [[165, 225, 510, 540]], 'p07': [[295, 115, 540, 405], [845, 320, 1140, 590]], 'p08': [[365, 215, 665, 465]], 'p09': [[570, 75, 855, 365], [0, 340, 175, 555]], 'p10': [[280, 185, 520, 420]], 'p11': [], 'p12': [[180, 465, 705, 975]], 'p13': [[0, 45, 1536, 675]], 'p14': [[990, 90, 1415, 435], [730, 775, 875, 925], [945, 700, 1080, 820]], 'p15': [[620, 115, 1024, 455]], 'p16': [[0, 295, 1536, 825]], 'p17': [[490, 220, 735, 455], [405, 95, 765, 280]], 'p18': [[530, 175, 975, 625], [365, 0, 1024, 335]], 'end': []}
TEXT = ["They dug all night. Kell told me Garrow dug until his hands bled, and that Wren dug beside him. They didn't say a word to each other. They didn't need to.", 'When they pulled us out at dawn, eleven children walked out on their own feet, pink-cheeked and arguing. I had to be carried.', "I woke in Yrsa's tent, burning and freezing at the same time. My fingertips were black to the first knuckle.", 'Overdraw. Like the night of the wolves, only worse. Every bit of cold you pulled out of them went somewhere, Lucan. Into you.', 'Because he holds it like a fist. Southern boy, you breathe like a man carrying a stone up a hill.', 'Then how should I breathe?', "Like the Skeld. We have lived in the cold for three hundred years. We don't fight it. We let it through.", "Breathe in, and let the cold come with it. Don't hold it. Let it go out again, the way it came. Like wind through a house with two doors.", "It took me all day. Breathe in the cold. Let it pass. Don't grip it.", 'Dunn tried it with me, to keep me company. He fell asleep on the third breath.', 'By evening, something had changed. The cold was still there. Twelve threads, still pulling. But now it moved through me, instead of settling in my hands.', 'The black in my fingers stopped spreading.', "Good. It won't take the cost away, Warm One. It lets you carry it. There is a difference.", 'That night the children came to visit. All eleven of them, with presents.', 'A bone bead. A frozen fish. A very small snowman. Rune gave me his only mitten.', 'For your hands. So they get warm too.', 'Outside, I could hear the camp. Two hundred voices, all saying the same thing, louder and louder.', "Then the tent flap opened, and Freydis came in, with snow in her bear's fur.", 'My people saw what you did for the children, Warm One. Now every one of them wants the same. Two hundred Skeld. Will you claim them all?', 'The Lord Who Measured Zero. Chapter forty, coming soon.']

def build():
 return f"""
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 39</div><div class="c2">Breath of the Skeld</div></div>
 {gap(100)}
 {narr(TEXT[0],'L0','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L0b">{img('p01','full')}</div>{gap(180)}
 {narr(TEXT[1],'L1','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L1b">{img('p02','full')}</div>{gap(180)}
 {narr(TEXT[2],'L2','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L2b" style="margin-left:180px">{img('p03','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[3],'L3','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L3b" style="margin-left:210px">{img('p04','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[4],'L4','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L4b" style="margin-left:180px">{img('p05','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[5],'L5','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L5b" style="margin-left:210px">{img('p06','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[6],'L6','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 {bub(TEXT[7],'L7','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L7b">{img('p07','full')}</div>{gap(180)}
 {narr(TEXT[8],'L8','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L8b" style="margin-left:210px">{img('p08','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[9],'L9','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L9b" style="margin-left:210px">{img('p09','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L10b">{img('p10','full')}</div>{gap(180)}
 {narr(TEXT[11],'L11','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L11b" style="margin-left:210px">{img('p11','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[12],'L12','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L12b" style="margin-left:180px">{img('p12','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[13],'L13','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L13b">{img('p13','full')}</div>{gap(180)}
 {narr(TEXT[14],'L14','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L14b">{img('p14','full')}</div>{gap(180)}
 {bub(TEXT[15],'L15','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L15b" style="margin-left:210px">{img('p15','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[16],'L16','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L16b">{img('p16','full')}</div>{gap(180)}
 {narr(TEXT[17],'L17','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L17b" style="margin-left:180px">{img('p17','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[18],'L18','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L18b" style="margin-left:210px">{img('p18','','width:660px;height:660px')}</div>{gap(180)}
 {gap(120,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L19" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 40 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
