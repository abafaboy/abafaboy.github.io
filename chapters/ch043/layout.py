"""Fresh final-PNG face protection; unchanged script text, with retained raw and visual QA."""
FACES = {'p01': [], 'p02': [[105, 275, 440, 600]], 'p03': [[300, 425, 575, 670]], 'p04': [[155, 195, 335, 390], [535, 180, 690, 370], [905, 230, 1045, 430], [1235, 225, 1390, 440]], 'p05': [[450, 105, 755, 425]], 'p06': [[65, 175, 1536, 610]], 'p07': [[205, 395, 500, 665], [480, 730, 960, 1190]], 'p08': [], 'p09': [[290, 145, 525, 365], [865, 180, 1065, 420], [1255, 40, 1455, 250]], 'p10': [], 'p11': [[150, 105, 575, 505]], 'p12': [[410, 560, 765, 925]], 'p13': [[120, 180, 615, 655]], 'p14': [[190, 305, 460, 630], [955, 265, 1175, 595]], 'p15': [[0, 420, 1536, 820]], 'p16': [[675, 370, 1536, 715]], 'end': []}
TEXT = ['The morning after I promised a Moot, Bram sent riders to every lord in the north. That same week, House Corrow closed the river.', 'Not with soldiers. Lady Sabine was far too clever for soldiers.', 'The treaty gave Lord Varr his river. Not the mouth of it. From today, anything that comes down from the north pays a toll. Nine crowns in every ten. Perfectly legal.', 'I checked. It was.', "So the first sled from the Glass Deep sat in Tobin's barn. Forty thousand crowns of rimeglass, and nowhere in Aldmere to sell it.", "A fortune you can't sell, my lord, is a very pretty pile of rocks.", 'Pell had come north with one coat, one ledger, and a debt to Lady Sabine bigger than Greyhollow.', "I've been ruined before, you understand. Usually by women. Never this efficiently.", 'Overland, then. Through the midlands, the way the furs used to go.', 'Her ban covers every midland market. Not one merchant south of the Senn will touch our glass.', 'That night I read the Greyhollow deed again. The one my brother signed over to me. Everyone else had stopped at the first line. I had read all four pages. Twice.', 'Greyhollow, and all lands north to the salt water, together with the harbour of Saltmouth.', "Saltmouth? That's a dead town, my lord. The harbour filled with sand thirty years ago. Nobody goes there now but fishermen and ghosts.", 'So my brother had given me a harbour. He just never read far enough to notice.', "A harbour on the north coast. Vask is four days' sail from there. No river. No toll. No Lady Sabine.", "My lord. I think I'm in love.", "No ship has docked at Saltmouth in thirty years. The channel's choked with sand, and the whole coast is fog and rocks.", 'Then we dig out the sand. And we light the fog.', 'My lord, every time you smile like that, I end up building something impossible.', "Two days later, sixty of Greyhollow's strongest walked out to the coast, with picks, shovels, and every cart Tobin owned.", 'Saltmouth was waiting for us. Twelve families on a grey shore, a broken tower, and a harbour full of sand. Nobody waved.', 'The Lord Who Measured Zero. Chapter forty-four, coming soon.']

def build():
 return f"""
<style>
.bub[data-a="L2"]:after,.bub[data-a="L7"]:after{{right:auto;left:calc(30% - 16px);transform:rotate(14deg)}}
.bub[data-a="L2"]:before,.bub[data-a="L7"]:before{{right:auto;left:calc(30% - 12px);transform:rotate(14deg)}}
.bub[data-a="L9"]:after{{right:auto;left:calc(53% - 16px)}}
.bub[data-a="L9"]:before{{right:auto;left:calc(53% - 12px)}}
</style>
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 43</div><div class="c2">Blockade</div></div>
 {gap(100)}
 {narr(TEXT[0],'L0','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L0b">{img('p01','full')}</div>{gap(180)}
 {narr(TEXT[1],'L1','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L1b" style="margin-left:180px">{img('p02','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[2],'L2','up','position:relative;margin-left:90px;width:900px')}{gap(65)}
 {narr(TEXT[3],'L3','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L3b" style="margin-left:210px">{img('p03','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[4],'L4','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L4b">{img('p04','full')}</div>{gap(180)}
 {bub(TEXT[5],'L5','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L5b" style="margin-left:210px">{img('p05','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[6],'L6','margin:0 110px;padding:72px 100px')}{gap(45)}
 {bub(TEXT[7],'L7','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[8],'L8','right','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L8b">{img('p06','full')}</div>{gap(180)}
 {bub(TEXT[9],'L9','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L10b" style="margin-left:180px">{img('p07','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[11],'L11','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L11b" style="margin-left:210px">{img('p08','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[12],'L12','right','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L12b">{img('p09','full')}</div>{gap(180)}
 {narr(TEXT[13],'L13','margin:0 110px;padding:72px 100px')}{gap(45)}
 {bub(TEXT[14],'L14','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L14b">{img('p10','full')}</div>{gap(180)}
 {bub(TEXT[15],'L15','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L15b" style="margin-left:210px">{img('p11','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[16],'L16','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L16b" style="margin-left:180px">{img('p12','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[17],'L17','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L17b" style="margin-left:210px">{img('p13','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[18],'L18','right','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L18b">{img('p14','full')}</div>{gap(180)}
 {narr(TEXT[19],'L19','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L19b">{img('p15','full')}</div>{gap(180)}
 {narr(TEXT[20],'L20','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L20b">{img('p16','full')}</div>{gap(180)}
 {gap(120,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L21" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 44 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
