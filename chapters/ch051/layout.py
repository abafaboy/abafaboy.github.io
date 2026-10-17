"""Chapter 51: The Column. Fresh face boxes measured on final production PNGs.
Dialogue/narration exactly match source script; upstream art provenance limits are in qa/art_review.json.
"""
FACES = {'p01': [(120, 65, 345, 305), (375, 195, 555, 375), (565, 205, 740, 390), (825, 210, 1020, 420), (1100, 185, 1280, 390), (1320, 145, 1515, 365)], 'p02': [(265, 240, 720, 675), (770, 825, 915, 970)], 'p03': [(0, 475, 1536, 645)], 'p04': [(400, 75, 755, 415), (770, 510, 1024, 755)], 'p05': [(455, 135, 815, 450)], 'p06': [(315, 110, 815, 615)], 'p07': [], 'p08': [(435, 55, 720, 355), (45, 400, 265, 650)], 'p09': [(300, 150, 530, 375), (900, 185, 1075, 340), (1135, 235, 1260, 365), (1320, 215, 1445, 350)], 'p10': [(295, 345, 590, 630), (900, 115, 1160, 405)], 'p11': [(140, 300, 450, 600), (525, 120, 835, 455)], 'p12': [(445, 155, 785, 515)], 'p13': [(935, 10, 1210, 285)], 'p14': [(210, 455, 415, 645)], 'end': []}

TEXT = ['By the third morning, I thought we had them. Ysolde had been promised her bathhouse. Halvard had stopped calling me boy. Twice.', 'Then a bird came for Lady Marrick, from her steward on the north road.', "Two hundred soldiers under the King's banner, and six blue robes. They crossed the Senn four days ago. They carry a royal warrant, under the King's own seal.", "Hask's warrant had come at last. Weeks late, as if someone in the south had argued about it. But with soldiers, exactly as he'd promised.", "I've no love for the Order, boy. But I won't stand between the King and his own seal. That's not a Compact. That's a rebellion.", "My people need a partner, Lord Lucan. Not a martyr. I can't sign with a man who'll be in chains by the new moon.", 'How very unfortunate. For everyone.', "His ring flickered again, just for a moment. He didn't notice. I did.", 'Saltmouth shares, my lords! Half price! Today only, owing to a small chance of arrest.', 'Nobody laughed this time. One by one, they went back to their rooms. The Compact lay on the table with four empty places, and not one drop of wax.', 'What will you do when they come, my lord?', 'Read them the Fourth Article?', "They'll have the King's own seal. The Fourth Article is satisfied.", "I know. I'm the one who told Hask how to get it.", "Then we'll think of something else. We always do.", 'A little after midnight, Kell came running into the hall. I had never seen a Skeld run indoors.', 'Lord. The White is moving. All of it. Yrsa woke screaming. It is coming south, toward the pass.', 'The pass? Kesting Pass?', "Far off in the north-west, a light flared on a mountain. Kesting's beacon. And somewhere beneath it, two hundred of the King's soldiers had just made camp.", 'The Lord Who Measured Zero. Chapter fifty-two, coming soon.']

def build():
    return f"""
<div class="sec white" style="background:#f6f1e7">
 <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 51</div><div class="c2">The Column</div></div>
 {gap(100)}{narr(TEXT[0], 'L0', 'margin:0 110px')}{gap(45)}
 <div class="rel" data-a="L0b">{img('p01','full')}</div>{gap(170)}
 {narr(TEXT[1], 'L1', 'margin:0 130px')}{gap(70)}
 <div class="rel" style="margin-left:330px">{img('p02','','width:720px;height:1080px')}
  {bub(TEXT[2], 'L2', 'right', 'left:-300px;top:15px;width:440px')}
 </div>{gap(180)}
 {narr(TEXT[3], 'L3', 'margin:0 110px')}{gap(45)}
 <div class="rel" data-a="L3b">{img('p03','full')}</div>{gap(200)}
 <div class="rel">{img('p04','','width:660px;height:660px')}
  {bub(TEXT[4], 'L4', 'left', 'left:675px;top:15px;width:375px')}
 </div>{gap(180)}
 <div class="rel" style="margin-left:330px">{img('p05','','width:660px;height:660px')}
  {bub(TEXT[5], 'L5', 'right', 'left:-300px;top:160px;width:400px')}
 </div>{gap(200)}
 <div class="rel" style="margin-left:330px">{img('p06','','width:720px;height:1080px')}
  {bub(TEXT[6], 'L6', 'right', 'left:-300px;top:55px;width:410px')}
 </div>{gap(140)}
 {narr(TEXT[7], 'L7', 'margin:0 190px')}{gap(45)}
 <div class="rel" data-a="L7b" style="margin-left:210px">{img('p07','','width:660px;height:660px')}</div>{gap(200)}
 <div class="rel">{img('p08','','width:660px;height:660px')}
  {bub(TEXT[8], 'L8', 'left', 'left:675px;top:105px;width:375px')}
 </div>{gap(190)}
 {narr(TEXT[9], 'L9', 'margin:0 110px')}{gap(45)}
 <div class="rel" data-a="L9b">{img('p09','full')}</div>
 {gap(260,'linear-gradient(#f6f1e7,#0b0d16)')}
</div>
<div class="sec night">
 {gap(80)}
 {bub(TEXT[10], 'L10', 'right', 'position:relative;margin:0 50px 0 370px;width:660px')}{gap(65)}
 <div class="rel" data-a="L10b">{img('p10','full')}</div>{gap(60)}
 {bub(TEXT[11], 'L11', 'up', 'position:relative;margin-left:45px;width:620px')}{gap(95)}
 {bub(TEXT[12], 'L12', 'up', 'position:relative;margin-left:330px;width:700px')}{gap(95)}
 {bub(TEXT[13], 'L13', 'up', 'position:relative;margin-left:45px;width:680px')}{gap(190)}
 <div class="rel" style="margin-left:330px">{img('p11','','width:660px;height:660px')}
  {bub(TEXT[14], 'L14', 'right', 'left:-300px;top:90px;width:370px')}
 </div>{gap(220)}
 {narr(TEXT[15], 'L15', 'margin:0 140px')}{gap(70)}
 <div class="rel">{img('p12','','width:660px;height:990px')}
  {bub(TEXT[16], 'L16', 'left', 'left:690px;top:50px;width:360px')}
 </div>{gap(180)}
 <div class="rel">{img('p13','full')}
  {bub(TEXT[17], 'L17', 'right', 'left:50px;top:90px;width:540px')}
 </div>{gap(180)}
 <div class="rel" data-a="L18">{img('p14','full')}</div>{gap(45)}
 {narr(TEXT[18], 'L18b', 'margin:0 110px')}{gap(300,'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
 <div class="rel" data-a="L19" style="margin-left:120px">{img('end','','width:840px;height:1260px')}
  <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 52 &middot; COMING SOON</div></div>
 </div>{gap(360)}
</div>
"""
