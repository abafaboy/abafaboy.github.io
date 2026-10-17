"""Chapter36: The Carving. Face boxes freshly measured on production-size PNGs.
All text matches the unchanged source script. Raw/candidate and visual evidence: qa/art_review.json.
"""
FACES = {'p01': [(95, 165, 650, 775), (670, 610, 840, 820), (475, 755, 635, 915), (635, 820, 865, 1035)], 'p02': [(10, 675, 620, 970), (1370, 150, 1440, 250), (1130, 360, 1370, 565)], 'p03': [(815, 120, 990, 310), (10, 370, 810, 735)], 'p04': [(180, 130, 520, 450), (650, 510, 940, 775)], 'p05': [(40, 330, 285, 580), (340, 460, 535, 695), (950, 35, 1095, 210), (735, 350, 940, 620), (1215, 240, 1450, 560)], 'p06': [(680, 50, 845, 245), (160, 380, 370, 585), (330, 540, 500, 730), (1175, 400, 1355, 600), (1035, 545, 1210, 750)], 'p07': [(420, 320, 640, 585), (70, 280, 350, 570), (735, 300, 1015, 570)], 'p08': [(45, 450, 445, 845), (515, 730, 830, 1065), (795, 115, 1024, 440)], 'p09': [(295, 300, 485, 490), (535, 375, 705, 545), (810, 50, 1030, 320)], 'p10': [(100, 175, 1480, 400), (310, 420, 500, 590)], 'p11': [(140, 190, 590, 730), (800, 430, 970, 590)], 'p12': [(210, 470, 500, 800), (730, 75, 960, 375)], 'p13': [(200, 200, 530, 495), (635, 430, 915, 765)], 'p14': [(130, 225, 575, 795)], 'p15': [(1195, 0, 1410, 185), (1000, 170, 1536, 520)], 'p16': [], 'p17': [(600, 220, 915, 570)], 'p18': [(10, 675, 620, 970), (695, 185, 820, 330), (780, 350, 875, 455), (1370, 150, 1440, 250), (1130, 360, 1370, 565)], 'end': []}
TEXT = ['Below the wall of people, a stair had been cut into the ice. Old steps, worn smooth by feet.', 'At the bottom was a hall. Stone pillars half swallowed by ice. Long tables. A broken throne. Somebody had lived down here once. A great many somebodies.', 'The children had gone very quiet. All eleven of them were holding onto my cloak. I had become a mother duck.', 'Is this where the Queen sleeps?', 'This is where she lived, little one.', 'Along the far wall ran a carving, as long as the hall itself. Ilse held up her lamp.', 'It began with a woman in a crown. People knelt around her, and the land at her feet was full of flowers.', 'Every other figure on that wall had rings carved behind its head. Knights with three. Lords with five. The queen had none.', "No rings. She's a zero.", 'Or she was like you.', 'I had heard of her before. From Hask, at the edge of my barley. A woman in the north, three hundred years ago. Hollow-born, like me. Everything she touched grew.', 'The carving went on. The queen lay on a bier, with hooded figures standing around her. Their faces had been chipped away.', 'And from her body, carved lines spread out across the stone. Frost. Over the flowers. Over the people. Over everything.', 'The Winter Queen. Your kind, Warm One.', 'Is she your mother?', 'No. My mother died the day I was born.', "Yrsa tilted her head, as if she'd heard a wrong note in a song. But she didn't say anything.", 'Then the floor moved.', 'Not a tremor. A slow, enormous shifting. Like something very large, turning over in its sleep.', 'Everyone. Back to the stair. Now.', 'Behind the ice of the far wall, something slid past. Pale. Scaled. Longer than the hall.', 'And it stopped, right behind the queen. As if it had smelled something warm.', 'The Lord Who Measured Zero. Chapter thirty-seven, coming soon.']

def build():
 return f"""
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 36</div><div class="c2">The Carving</div></div>
 {gap(100)}{narr(TEXT[0],'L0','margin:0 120px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L0b" style="margin-left:180px">{img('p01','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[1],'L1','margin:0 110px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L1b">{img('p02','full')}</div>{gap(180)}
 {narr(TEXT[2],'L2','margin:0 150px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L2b" style="margin-left:210px">{img('p03','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[3],'L3','right','position:relative;margin-left:350px;width:680px')}{gap(65)}
 <div class="rel" data-a="L3b" style="margin-left:210px">{img('p04','','width:660px;height:660px')}</div>{gap(65)}
 {bub(TEXT[4],'L4','up','position:relative;margin-left:45px;width:700px')}{gap(180)}
 {narr(TEXT[5],'L5','margin:0 130px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L5b">{img('p05','full')}</div>{gap(160)}
 {narr(TEXT[6],'L6','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L6b">{img('p06','full')}</div>{gap(160)}
 {narr(TEXT[7],'L7','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L7b" style="margin-left:120px">{img('p07','','width:840px;height:840px')}</div>{gap(180)}
 <div class="rel">{img('p08','','width:720px;height:1080px')}
  {bub(TEXT[8],'L8','left','left:740px;top:120px;width:310px')}
  {bub(TEXT[9],'L9','left','left:740px;top:600px;width:310px')}
 </div>{gap(180)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L10b">{img('p09','full')}</div>{gap(180)}
 {narr(TEXT[11],'L11','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L11b">{img('p10','full')}</div>{gap(160)}
 {narr(TEXT[12],'L12','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L12b">{img('p11','full')}</div>{gap(180)}
 <div class="rel" style="margin-left:330px">{img('p12','','width:720px;height:1080px')}
  {bub(TEXT[13],'L13','right','left:-300px;top:80px;width:420px')}
 </div>{gap(180)}
 {bub(TEXT[14],'L14','right','position:relative;margin-left:420px;width:610px')}{gap(65)}
 <div class="rel" data-a="L14b" style="margin-left:210px">{img('p13','','width:660px;height:660px')}</div>{gap(65)}
 {bub(TEXT[15],'L15','up','position:relative;margin-left:45px;width:700px')}{gap(180)}
 {narr(TEXT[16],'L16','margin:0 140px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L16b" style="margin-left:210px">{img('p14','','width:660px;height:660px')}</div>{gap(200)}
 {narr(TEXT[17],'L17','margin:0 210px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L17b">{img('p15','full')}</div>{gap(180)}
 {narr(TEXT[18],'L18','margin:0 130px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L18b" style="margin-left:150px">{img('p16','','width:780px;height:780px')}</div>{gap(180)}
 {bub(TEXT[19],'L19','right','position:relative;margin-left:120px;width:840px')}{gap(65)}
 <div class="rel" data-a="L19b" style="margin-left:180px">{img('p17','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[20],'L20','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L20b">{img('p18','full')}</div>{gap(55)}
 {narr(TEXT[21],'L21','margin:0 140px;padding:72px 100px')}{gap(300,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L22" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 37 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
