"""Fresh final-PNG face protection; unchanged script text, with retained raw and visual QA."""
FACES = {'p01': [[0, 250, 1536, 580]], 'p02': [[160, 120, 525, 440]], 'p03': [[280, 610, 735, 1085]], 'p04': [[195, 70, 350, 245], [285, 390, 470, 610], [785, 440, 945, 655]], 'p05': [[0, 175, 1536, 900]], 'p06': [[390, 180, 610, 410], [700, 800, 1024, 1040]], 'p07': [[110, 250, 465, 665], [670, 440, 955, 770]], 'p08': [[245, 85, 370, 235], [525, 385, 865, 685], [520, 655, 790, 825]], 'p09': [[295, 365, 460, 540], [1135, 100, 1215, 180]], 'p10': [[430, 110, 845, 575]], 'p11': [[245, 315, 405, 455], [490, 320, 665, 500]], 'p12': [[270, 585, 650, 1010]], 'p13': [[430, 180, 1024, 610]], 'p14': [[0, 140, 1536, 750]], 'p15': [[0, 570, 1536, 1024]], 'p16': [[0, 185, 285, 500], [310, 335, 665, 650]], 'end': []}
TEXT = ['Saltmouth had forty-one people, nine boats that still floated, and one opinion of lords.', 'Another lord. The last one came to count our boats. Then he taxed the ones that sank.', 'Her name was Agna. She was the oldest woman in Saltmouth, and in charge of it, because nobody had ever dared to argue with her.', "I haven't come to count your boats. I've come to dig out your harbour.", "The sea took thirty years to fill it, boy. And you'll empty it in what? A summer?", 'A fortnight.', 'I had read a book about harbours. Of course I had. At low tide, the sandbar sat right out of the water, like a sleeping whale. All we had to do was cut it in half.', 'Sixty farmers dug at every low tide, by day and by lantern. Most of them were threes by now. A dozen were fours.', 'When the tide came in, they built the breakwater instead. One boulder at a time. Sometimes two.', "Close your mouth, Harl. You'll catch a gull.", "Ash had stayed at home. For the first time since I named him, he wouldn't leave someone's side, and it wasn't mine.", 'Tobin! Can you make a light that a ship can see through fog, twenty miles out to sea?', 'Impossible, my lord!', 'Give me a week.', 'See those rocks? The Teeth. There was a light on that tower once. When the harbour silted up, the lords stopped paying for oil, and the light went out.', 'That winter, my man and both my boys were coming home in the fog. The Teeth took them a hundred yards from their own door.', "This light won't need oil.", 'On the twelfth day, the tide came in through our channel instead of over the sandbar. Harl cried. He said it was the wind.', 'On the fourteenth night, the tower stood finished, with a heart of Deep rimeglass the size of a barrel. Every soul in Saltmouth came out to see it.', 'Well, boy? Light it.', 'The Lord Who Measured Zero. Chapter forty-five, coming soon.']

def build():
 return f"""
<style>
.bub[data-a="L3"]:after{{right:auto;left:calc(30% - 16px);transform:rotate(14deg)}}
.bub[data-a="L3"]:before{{right:auto;left:calc(30% - 12px);transform:rotate(14deg)}}
.bub[data-a="L4"]:after,.bub[data-a="L14"]:after{{right:auto;left:calc(50% - 16px)}}
.bub[data-a="L4"]:before,.bub[data-a="L14"]:before{{right:auto;left:calc(50% - 12px)}}
</style>
<div class="sec night">
 <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8d4a0">THE LORD WHO MEASURED ZERO</div><div class="c1" style="color:#b8c8e3">CHAPTER 44</div><div class="c2">Saltmouth</div></div>
 {gap(100)}
 {narr(TEXT[0],'L0','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L0b">{img('p01','full')}</div>{gap(180)}
 {bub(TEXT[1],'L1','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {narr(TEXT[2],'L2','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L2b" style="margin-left:210px">{img('p02','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[3],'L3','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[4],'L4','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L4b" style="margin-left:180px">{img('p03','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[5],'L5','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {narr(TEXT[6],'L6','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L6b">{img('p04','full')}</div>{gap(180)}
 {narr(TEXT[7],'L7','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L7b">{img('p05','full')}</div>{gap(180)}
 {narr(TEXT[8],'L8','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L8b" style="margin-left:180px">{img('p06','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[9],'L9','right','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L9b" style="margin-left:210px">{img('p07','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[10],'L10','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L10b">{img('p08','full')}</div>{gap(180)}
 {bub(TEXT[11],'L11','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L11b">{img('p09','full')}</div>{gap(180)}
 {bub(TEXT[12],'L12','up','position:relative;margin-left:145px;width:790px')}{gap(65)}
 {bub(TEXT[13],'L13','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L13b" style="margin-left:210px">{img('p10','','width:660px;height:660px')}</div>{gap(180)}
 {bub(TEXT[14],'L14','right','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L14b">{img('p11','full')}</div>{gap(180)}
 {bub(TEXT[15],'L15','left','position:relative;margin-left:90px;width:900px')}{gap(65)}
 <div class="rel" data-a="L15b" style="margin-left:180px">{img('p12','','width:720px;height:1080px')}</div>{gap(180)}
 {bub(TEXT[16],'L16','left','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L16b" style="margin-left:210px">{img('p13','','width:660px;height:660px')}</div>{gap(180)}
 {narr(TEXT[17],'L17','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L17b">{img('p14','full')}</div>{gap(180)}
 {narr(TEXT[18],'L18','margin:0 110px;padding:72px 100px')}{gap(45)}
 <div class="rel" data-a="L18b">{img('p15','full')}</div>{gap(180)}
 {bub(TEXT[19],'L19','right','position:relative;margin-left:145px;width:790px')}{gap(65)}
 <div class="rel" data-a="L19b" style="margin-left:210px">{img('p16','','width:660px;height:660px')}</div>{gap(180)}
 {gap(120,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black"><div class="rel" data-a="L20" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
 <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 45 &middot; COMING SOON</div></div>
</div>{gap(360)}</div>
"""
