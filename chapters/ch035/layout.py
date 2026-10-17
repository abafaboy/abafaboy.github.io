"""Chapter35: The Glass Deep. Fresh production-size face regions, including frozen crowds.
All text matches unchanged script. Full pre-redraw baseline is preserved separately.
"""
FACES = {'p01': [(300, 730, 1500, 1024)], 'p02': [(180, 425, 1480, 790), (530, 145, 750, 350), (100, 195, 290, 415), (1190, 100, 1390, 340)], 'p03': [(115, 155, 355, 435), (600, 270, 870, 565)], 'p04': [(85, 230, 200, 350), (340, 145, 485, 305), (260, 470, 405, 600), (570, 325, 695, 435), (1050, 160, 1220, 315), (1360, 310, 1490, 435), (1080, 460, 1235, 590)], 'p05': [(305, 675, 615, 1025), (615, 475, 850, 755), (775, 325, 995, 600), (525, 265, 730, 480), (715, 105, 905, 335)], 'p06': [(200, 65, 850, 710)], 'p07': [(350, 660, 1160, 1024), (0, 0, 650, 620), (1100, 190, 1536, 650)], 'p08': [(365, 490, 925, 930)], 'p09': [(0, 10, 1536, 860)], 'p10': [(255, 155, 635, 545), (595, 175, 880, 455)], 'p11': [], 'p12': [(410, 130, 930, 805)], 'p13': [(375, 475, 730, 885), (760, 330, 1024, 675), (115, 180, 325, 420), (240, 400, 425, 580)], 'p14': [(0, 425, 1536, 1000), (450, 0, 1536, 500)], 'p15': [(0, 0, 1536, 915)], 'p16': [(0, 0, 1024, 1310), (285, 435, 520, 675), (650, 490, 825, 705)], 'p17': [(275, 275, 675, 665), (50, 10, 245, 190), (65, 270, 250, 450), (40, 475, 210, 675), (795, 25, 1015, 210), (795, 300, 1015, 495), (870, 590, 1024, 785)], 'p18': [(0, 0, 1330, 980)], 'end': []}
TEXT = ["The Glass Deep lay a day's walk north, under a mountain the Skeld would not name.", 'Yrsa came with us, and eleven Skeld children, Rune among them. Every Skeld child must see the Queen once, Yrsa said. And near me, they were warm.', 'This is a terrible idea.', 'Yes. Come along.', "We left Dunn and the hunters at the entrance with Tobin's harpoon sledge. Dunn had started calling it Tobin's Mistake. They had hauled it for nine days, and they hated it.", "Something in there took Garrow's eye. If it comes out, I want that Mistake loaded.", 'Then Garrow led us down.', 'The tunnel opened, and I forgot how to breathe.', 'Rimeglass. Not slivers, not shards. Whole walls of it, glowing blue, taller than the Cathedral of the Seven.', 'And inside the glass, there were animals.', 'Elk with antlers like trees. Bears the size of houses. A pack of wolves, frozen mid-stride. Thousands of them.', 'The old beasts. From before the White.', 'Ilse pulled off her glove, and laid her bare hand on the wall.', 'Oh. Oh, no.', "Rimeglass doesn't grow in a beast's heart, Lucan. It is the heart. It's what a Vessel becomes when it freezes. Every lamp we ever sold was a life.", 'Garrow led us deeper. The beasts got older, and stranger. And at the very bottom, they stopped being beasts.', 'People. A whole wall of them. Men, women, children, standing in the glass as if they had simply stopped.', 'Skeld law. What has a human shape is never cut. Not for warmth. Not for anything.', 'If a beast can become rimeglass, Lucan... then so can a person.', 'Then I saw something worse.', 'Every face in that wall was turned the same way. Down. Toward something further in.', 'The Lord Who Measured Zero. Chapter thirty-six, coming soon.']

def build():
 return f"""
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 35</div><div class="c2">The Glass Deep</div></div>
 {gap(100)}{narr(TEXT[0],'L0','margin:0 130px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L0b">{img('p01','full')}</div>{gap(180)}
 {narr(TEXT[1],'L1','margin:0 110px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L1b">{img('p02','full')}</div>{gap(180)}
 {bub(TEXT[2],'L2','left','position:relative;margin-left:45px;width:650px')}{gap(65)}
 <div class="rel" data-a="L2b" style="margin-left:210px">{img('p03','','width:660px;height:660px')}</div>{gap(65)}
 {bub(TEXT[3],'L3','up','position:relative;margin-left:530px;width:500px')}{gap(180)}
 {narr(TEXT[4],'L4','margin:0 110px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L4b">{img('p04','full')}</div>{gap(65)}
 {bub(TEXT[5],'L5','up','position:relative;margin-left:45px;width:850px')}{gap(180)}
 {narr(TEXT[6],'L6','margin:0 210px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L6b" style="margin-left:180px">{img('p05','','width:720px;height:1080px')}</div>{gap(160)}
 {narr(TEXT[7],'L7','margin:0 170px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L7b" style="margin-left:210px">{img('p06','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[8],'L8','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L8b">{img('p07','full')}</div>{gap(180)}
 {narr(TEXT[9],'L9','margin:0 180px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L9b" style="margin-left:180px">{img('p08','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L10b">{img('p09','full')}</div>{gap(180)}
 {bub(TEXT[11],'L11','left','position:relative;margin-left:130px;width:820px')}{gap(65)}
 <div class="rel" data-a="L11b" style="margin-left:210px">{img('p10','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[12],'L12','margin:0 150px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L12b" style="margin-left:210px">{img('p11','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[13],'L13','left','position:relative;margin-left:210px;width:660px')}{gap(65)}
 <div class="rel" data-a="L13b" style="margin-left:210px">{img('p12','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[14],'L14','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L14b" style="margin-left:180px">{img('p13','','width:720px;height:1080px')}</div>{gap(180)}
 {narr(TEXT[15],'L15','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L15b">{img('p14','full')}</div>{gap(180)}
 {narr(TEXT[16],'L16','margin:0 120px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L16b">{img('p15','full')}</div>{gap(180)}
 {bub(TEXT[17],'L17','left','position:relative;margin-left:45px;width:840px')}{gap(65)}
 <div class="rel" data-a="L17b" style="margin-left:180px">{img('p16','','width:720px;height:1080px')}</div>{gap(65)}
 {bub(TEXT[18],'L18','up','position:relative;margin-left:280px;width:750px')}{gap(180)}
 {narr(TEXT[19],'L19','margin:0 210px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L19b" style="margin-left:210px">{img('p17','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[20],'L20','margin:0 140px;padding:72px 100px')}{gap(45)}<div class="rel" data-a="L20b">{img('p18','full')}</div>{gap(300,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L21" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 36 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
