"""Fresh final-PNG face protection; unchanged script text, with retained raw and visual QA."""
FACES = {'p01': [[570, 155, 905, 435]], 'p02': [[370, 295, 605, 550], [10, 810, 245, 1040], [815, 140, 1020, 365], [790, 65, 1024, 215]], 'p03': [[195, 255, 410, 495], [590, 370, 775, 570], [1050, 85, 1290, 300], [1010, 0, 1405, 175]], 'p04': [[190, 480, 635, 915]], 'p05': [[570, 150, 925, 480]], 'p06': [], 'p07': [[1080, 95, 1305, 370], [260, 225, 385, 375], [220, 425, 790, 700]], 'p08': [[40, 350, 1536, 710]], 'p09': [[395, 0, 1024, 520]], 'p10': [[75, 100, 250, 315], [1345, 195, 1510, 415], [730, 275, 1160, 430]], 'p11': [[320, 0, 1024, 555]], 'p12': [[145, 265, 410, 600], [675, 275, 970, 650]], 'p13': [[70, 250, 365, 590], [465, 80, 765, 455], [1145, 45, 1465, 465]], 'p14': [[105, 75, 335, 325], [600, 220, 1425, 855]], 'p15': [[140, 0, 1465, 835]], 'p16': [[220, 545, 435, 765], [600, 815, 770, 1005], [800, 690, 1015, 920]], 'p17': [[100, 125, 370, 390], [505, 260, 740, 460], [1040, 620, 1235, 790], [1090, 345, 1536, 600]], 'p18': [[180, 140, 450, 430], [660, 305, 915, 580]], 'end': []}
TEXT = ['Two hundred threads. I looked down at my black fingers. Twelve had nearly killed me.', 'Twelve freezing people did this to your hands, Lucan. Two hundred would bury you.', 'No, Elder. Not like this.', 'You refuse us?', "I refuse to make it a bargain. A claim isn't a trade. It only works if it's meant, on both sides. Your people don't know me yet.", 'So let me offer you something else. Not a claim. A pact.', "Greyhollow's northern edge was empty land. Mine by law, and warm because I lived beside it. The Skeld could have it, to live on by their own law.", 'The Skeld would guide us in the Deep, because they knew it. Tobin would work the glass. A stove for every tent, and a share of every crown.', 'And if the White came south, or soldiers came north, we would stand together.', 'Skeld law says a guest must hunt before he bargains. You never hunted, Warm One.', 'That was when Oswin and Dunn dragged something into the tent. The heart of the wyrm. A block of rimeglass as big as a barrel, glowing blue.', "Your law says the heart belongs to the hunter. We hunted. And we're giving it to you.", '...Now you have hunted.', 'It was the first time I ever saw Freydis smile. It looked like it hurt.', 'The Skeld will come south. One-Eye goes ahead with you. He knows your ways and ours. He will speak for us.', 'I was going anyway, Elder. My daughter lives there.', "Wren didn't say anything. But she stood a little closer to him than before.", 'There was one more thing. Before we left the White, I went back down into the Deep.', 'Skeld and Greyhollow together, we sealed the wall of people with stones, until not one face could be seen.', "Nobody cuts this wall. Not for warmth. Not for coin. Not for anything. That's Skeld law. And it's mine.", 'On the first night of the road home, Garrow sat down beside Wren at the fire.', 'Your mother. Does she still live by the mill?', "She does. She's going to kill you.", 'I know.', 'The Lord Who Measured Zero. Chapter forty-one, coming soon.']

def build():
 return f"""
<style>
.bub[data-a="L11"]:after,.bub[data-a="L23"]:after{{right:auto;left:calc(30% - 16px);transform:rotate(14deg)}}
.bub[data-a="L11"]:before,.bub[data-a="L23"]:before{{right:auto;left:calc(30% - 12px);transform:rotate(14deg)}}
</style>
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 40</div><div class="c2">The Pact</div></div>
 {gap(100)}
 {narr(TEXT[0],'L0','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L0b" style="margin-left:210px">{img('p01','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[1],'L1','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L1b" style="margin-left:180px">{img('p02','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[2],'L2','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L2b">{img('p03','full')}</div>{gap(180)}
 {bub(TEXT[3],'L3','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[4],'L4','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L4b" style="margin-left:180px">{img('p04','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[5],'L5','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L5b" style="margin-left:210px">{img('p05','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[6],'L6','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L6b">{img('p06','full')}</div>{gap(180)}
 {narr(TEXT[7],'L7','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L7b">{img('p07','full')}</div>{gap(180)}
 {narr(TEXT[8],'L8','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L8b">{img('p08','full')}</div>{gap(180)}
 {bub(TEXT[9],'L9','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L9b" style="margin-left:210px">{img('p09','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L10b">{img('p10','full')}</div>{gap(180)}
 {bub(TEXT[11],'L11','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[12],'L12','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L12b" style="margin-left:210px">{img('p11','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[13],'L13','margin:0 110px;padding:72px 100px')}{gap(45)}
 {bub(TEXT[14],'L14','right','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L14b" style="margin-left:180px">{img('p12','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[15],'L15','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L15b">{img('p13','full')}</div>{gap(180)}
 {narr(TEXT[16],'L16','margin:0 110px;padding:72px 100px')}{gap(45)}
 {narr(TEXT[17],'L17','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L17b">{img('p14','full')}</div>{gap(180)}
 {narr(TEXT[18],'L18','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L18b">{img('p15','full')}</div>{gap(180)}
 {bub(TEXT[19],'L19','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L19b" style="margin-left:180px">{img('p16','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[20],'L20','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L20b">{img('p17','full')}</div>{gap(180)}
 {bub(TEXT[21],'L21','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L21b" style="margin-left:210px">{img('p18','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[22],'L22','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[23],'L23','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {gap(120,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L24" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 41 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
