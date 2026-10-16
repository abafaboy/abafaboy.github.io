"""Chapter 33 layout.
FACES uses original panel PNG coordinates. Conservative head/crowd regions and
one spider protection box are retained along with human and wolf faces.
"""
FACES = {'p01': [(100, 145, 250, 310),
         (210, 280, 320, 410),
         (310, 340, 395, 455),
         (375, 380, 465, 485),
         (420, 425, 505, 525),
         (470, 430, 550, 525),
         (520, 420, 602, 525),
         (570, 410, 660, 530),
         (685, 195, 825, 355),
         (885, 490, 945, 585),
         (920, 455, 1010, 570),
         (998, 420, 1090, 520),
         (1060, 365, 1150, 465),
         (1085, 395, 1190, 505),
         (1185, 380, 1270, 475),
         (1220, 345, 1315, 460),
         (1320, 270, 1445, 400),
         (1478, 200, 1536, 335)],
 'p02': [(155, 145, 345, 385), (500, 125, 795, 425), (1070, 195, 1275, 440)],
 'p03': [(360, 55, 700, 410), (700, 805, 795, 875)],
 'p04': [(130, 410, 415, 665), (695, 420, 1010, 725)],
 'p05': [(190, 115, 320, 235),
         (40, 330, 180, 495),
         (160, 520, 320, 670),
         (885, 165, 1050, 350),
         (1110, 280, 1265, 480),
         (1325, 160, 1536, 465),
         (1235, 390, 1370, 550),
         (1195, 515, 1415, 740),
         (1335, 620, 1536, 815)],
 'p06': [(150, 60, 590, 455), (825, 750, 1024, 955)],
 'p07': [(75, 135, 550, 655)],
 'p08': [(190, 540, 445, 800), (605, 395, 885, 690)],
 'p09': [(520, 50, 745, 300), (90, 165, 215, 300), (265, 135, 370, 250), (860, 290, 950, 380), (975, 235, 1090, 345)],
 'p10': [(245, 150, 460, 405), (680, 180, 995, 465)],
 'p11': [(165, 145, 375, 360),
         (550, 195, 740, 430),
         (355, 375, 520, 545),
         (45, 415, 245, 600),
         (845, 380, 1000, 555),
         (1085, 275, 1245, 480),
         (1305, 165, 1525, 430),
         (1220, 445, 1350, 615),
         (1015, 540, 1225, 735),
         (1280, 585, 1440, 720)],
 'p12': [(170, 670, 430, 880)],
 'p13': [(425, 250, 645, 490), (165, 15, 540, 400)],
 'p14': [(410, 25, 790, 430), (1120, 180, 1260, 365)],
 'p15': [(165, 65, 400, 275), (780, 170, 985, 355)],
 'p16': [(415, 140, 705, 455)],
 'p17': [(1030, 35, 1150, 180),
         (385, 425, 530, 595),
         (150, 455, 300, 630),
         (0, 465, 135, 630),
         (630, 555, 775, 705),
         (820, 530, 985, 705),
         (1320, 345, 1536, 520)],
 'p18': [(60, 110, 430, 530), (680, 435, 905, 695)]}


def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 33</div><div class="c2">The Night Test</div></div>
  {gap(160, 'linear-gradient(#fff,#e6edf4)')}
</div>
<div class="sec white" style="background:#e6edf4">
  {narr('At dawn, the whole camp came out to watch the Warm One hunt.','L0', 'margin:0 150px')}
  {gap(40)}
  <div class="rel">{img('p01','full')}</div>
  {gap(330)}
  <div class="rel">{img('p02','full')}
    {bub("I'll do it, my lord! My arm's nearly healed!",'L1', 'left','position:absolute;left:60px;top:-300px;width:420px')}
    {bub('The guest hunts. Not his men. Not his dog.','L2', 'right','position:absolute;right:40px;top:-220px;width:420px')}
  </div>
  {gap(200, 'linear-gradient(#e6edf4,#f1e6d4)')}
</div>
<div class="sec white" style="background:#f1e6d4">
  <div class="rel" data-a="L3" style="margin-left:300px">{img('p03','', 'width:660px;height:660px')}
    {narr('I had never killed anything bigger than a spider. And I had apologised to the spider.','', 'position:absolute;left:-290px;top:140px;width:430px')}
  </div>
  {gap(200, 'linear-gradient(#f1e6d4,#e6edf4)')}
</div>
<div class="sec white" style="background:#e6edf4">
  {gap(140)}
  <div class="rel" style="margin-left:0">{img('p04','', 'width:720px;height:1080px')}
    {bub("Elder Freydis, I can't hunt. But I didn't come with empty hands.",'L4', 'left','position:absolute;left:20px;top:-140px;width:470px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L5">{img('p05','full')}
    {narr("Tobin's stoves. Iron boxes with a heart of rimeglass, warm for a month without a single stick of wood.",'', 'position:absolute;left:250px;width:580px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:300px">{img('p06','', 'width:660px;height:660px')}
    {bub('Skeld do not trade. Skeld hunt. That is the law.','L6', 'right','position:absolute;left:-280px;top:40px;width:370px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p07','', 'width:660px;height:660px')}
    {bub('Then may I hear the law? The exact words?','L7', 'left','position:absolute;right:-390px;top:30px;width:370px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('p08','', 'width:720px;height:1080px')}
    {bub('A guest who would sit at our fire must first feed it.','L8', 'right','position:absolute;left:-200px;top:-60px;width:440px')}
    {bub("Feed it. It doesn't say kill anything.",'L9', 'left','position:absolute;right:20px;top:-40px;width:400px')}
  </div>
  {gap(200, 'linear-gradient(#e6edf4,#f6e8d6)')}
</div>
<div class="sec white" style="background:#f6e8d6">
  {narr('So I set a stove beside their fire, and lit its heart. Warmth rolled out over the camp like a summer morning.','L10', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L10b">{img('p09','full')}
    {sfx('FWOOMPH!','left:560px;top:20px;transform:rotate(-6deg);font-size:64px')}
  </div>
  {gap(520)}
  <div class="rel">{img('p10','full')}
    {bub('That is not a hunt!','L11', 'left','position:absolute;right:120px;top:-430px;width:360px')}
    {bub('No. But it fed the fire.','L12', 'right','position:absolute;left:40px;top:-170px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L13">{img('p11','full')}
    {sfx('HA HA HA!','left:530px;top:14px;transform:rotate(-5deg);font-size:54px')}
    {narr('And the Skeld laughed. Kell said nobody in that camp had laughed in a year.','', 'position:absolute;left:180px;width:720px;bottom:-170px')}
  </div>
  {gap(260, 'linear-gradient(#f6e8d6,#e6edf4)')}
</div>
<div class="sec white" style="background:#e6edf4">
  <div class="rel" style="margin-left:330px">{img('p12','', 'width:720px;height:1080px')}
    {bub('The law is satisfied. I am not. Spend one night in the ice cave, Warm One, without fire. No one ever has, and lived.','L14', 'right','position:absolute;left:-300px;top:0px;width:560px')}
  </div>
  {gap(300, 'linear-gradient(#e6edf4,#0b1424)')}
</div>
<div class="sec night" style="background:#0b1424">
  {gap(40)}
  {narr('So I spent the night in a cave of solid ice, with only my dog for company. For an hour, it was almost cosy.','L15', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L15b">{img('p13','full')}</div>
  {gap(160)}
  <div class="rel" data-a="L16">{img('p14','full')}
    {sfx('awooo...','left:560px;top:60px;transform:rotate(-6deg);font-size:50px', 'quiet')}
    {narr('Then a white wolf appeared at the mouth of the cave. Ash looked at her. He looked at me. He looked at her again.','', 'position:absolute;left:80px;width:720px;bottom:-190px')}
  </div>
  {gap(290)}
  <div class="rel" style="margin-left:300px">{img('p15','', 'width:660px;height:660px')}
    {bub("Ash. Don't you dare.",'L17', 'right','position:absolute;left:-280px;top:-40px;width:340px')}
    {narr('He dared.','L18', 'position:absolute;right:-30px;bottom:-100px;width:300px')}
  </div>
  {gap(300, 'linear-gradient(#0b1424,#e3ecf4)')}
</div>
<div class="sec white" style="background:#e3ecf4">
  <div class="rel" data-a="L19">{img('p16','full')}
    {narr('By morning, the ice cave was a pond, and I was sitting in the middle of it. Wet, alone, and perfectly warm.','', 'position:absolute;left:180px;width:720px;bottom:-190px')}
  </div>
  {gap(310)}
  {narr('The Skeld were waiting outside. So was a hunting party, just back from the north. Their leader had one eye, and red-brown hair going grey.','L20', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L20b">{img('p17','full')}</div>
  {gap(160)}
  {narr("He wasn't looking at me. He was looking past me. At Wren.",'L21', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" style="margin-left:0">{img('p18','', 'width:720px;height:1080px')}
    {bub('...Father?','L22', 'left','position:absolute;left:340px;top:10px;width:300px')}
  </div>
  {gap(320, 'linear-gradient(#e3ecf4,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L23" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 34 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
