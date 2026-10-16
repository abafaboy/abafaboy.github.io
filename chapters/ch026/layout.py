"""Chapter 26 layout."""
FACES = {
    "bb01": [(370, 480, 470, 600), (180, 600, 280, 710), (0, 180, 1536, 280)],
    "bb02": [(230, 110, 540, 460)],
    "bb03": [(200, 220, 350, 370), (440, 280, 575, 390), (320, 450, 490, 630), (705, 430, 830, 580), (775, 650, 920, 790), (1150, 645, 1275, 750), (1350, 650, 1470, 750), (565, 790, 750, 930), (1160, 510, 1520, 640)],
    "bb04": [(90, 180, 520, 560), (880, 520, 1024, 700), (630, 180, 790, 350)],
    "bb05": [(490, 370, 730, 640), (0, 0, 270, 390)],
    "bb06": [(0, 0, 660, 590)],
    "bb07": [(550, 90, 800, 370), (995, 55, 1265, 350)],
    "bb08": [(490, 40, 620, 160), (920, 70, 1020, 180), (1165, 235, 1280, 340), (430, 340, 590, 510), (60, 450, 200, 610), (765, 495, 900, 645), (990, 565, 1110, 705), (1190, 585, 1315, 725), (180, 470, 1320, 820)],
    "bb09": [(310, 60, 490, 280), (675, 220, 820, 400), (885, 470, 1035, 620), (990, 380, 1125, 530), (1340, 390, 1490, 550), (290, 580, 520, 830), (1290, 850, 1536, 1024)],
    "bb10": [(590, 100, 815, 330), (40, 680, 390, 980)],
    "bb11": [(430, 430, 620, 610), (895, 280, 1024, 520)],
    "bb12": [(230, 0, 440, 250), (500, 350, 700, 580)],
    "bb13": [(290, 60, 510, 300), (785, 185, 965, 400), (1100, 570, 1430, 690)],
    "bb14": [(200, 175, 365, 350), (620, 125, 815, 340), (855, 0, 1024, 200)],
    "bb15": [(0, 260, 300, 530), (370, 420, 650, 690), (1250, 520, 1536, 830), (615, 100, 750, 245), (835, 100, 985, 245), (995, 150, 1536, 510)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 26</div><div class="c2">White Night</div></div>
  {gap(160, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(40)}
  {narr('Two nights later, the animals came.','L0', 'margin:0 210px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('bb01','full')}</div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('bb02','', 'width:720px;height:1080px')}
    {bub('Bram. Ring the bell.','L1', 'left','position:absolute;right:-330px;top:120px;width:310px')}
  </div>
  {gap(160)}
  {narr("They came out of the north like a white flood. Wolves, elk, frost-bears. Not hunting. Fleeing. And the Measurers' camp was right in their path.",'L2', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L2b">{img('bb03','full')}
    {sfx('RUMBLE!','left:560px;top:595px;transform:rotate(-5deg);font-size:90px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('bb04','', 'width:660px;height:660px')}
    {bub('Help! Somebody help us!','L3', 'right','position:absolute;left:-280px;top:80px;width:320px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('bb05','', 'width:720px;height:1080px')}
    {bub("They're outside the wall, my lord! If we open that gate, they'll see everything. Every ring we've hidden.",'L4', 'left','position:absolute;right:-340px;top:20px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('bb06','', 'width:660px;height:660px')}
    {bub('Open the gate.','L5', 'right','position:absolute;left:-285px;top:200px;width:265px')}
  </div>
  {gap(160)}
  <div class="rel">{img('bb07','full')}
    {bub('My lord...','L6', 'up','position:absolute;left:250px;bottom:-150px;width:260px')}
    {bub("They're people, Bram. Open it.",'L7', 'up','position:absolute;right:120px;bottom:-290px;width:380px')}
  </div>
  {gap(370)}
  {narr('And Greyhollow stopped pretending.','L8', 'margin:0 220px')}
  {gap(40)}
  <div class="rel">{img('bb08','full')}
    {sfx('RAAAAH!','left:40px;top:598px;transform:rotate(-3deg);font-size:88px')}
  </div>
  {gap(180)}
  {narr('Tobin swung his hammer. Granny swung her axe. And two little girls carried a grown Measurer to safety between them, like a sack of turnips.','L9', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L9b">{img('bb09','full')}</div>
  {gap(160)}
  <div class="rel" data-a="L10" style="margin-left:330px">{img('bb10','', 'width:720px;height:1080px')}
    {narr('Then I saw Hask. Down in the snow, his lens cracked, and a frost-bear rising over him.','', 'position:absolute;left:-300px;top:60px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L11" style="margin-left:0">{img('bb11','', 'width:720px;height:1080px')}
    {narr("I can't fight. I've never been able to fight. I ran at it anyway.",'', 'position:absolute;right:-330px;top:560px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L12">{img('bb12','full')}
    {sfx('WHAAM!','left:520px;top:440px;transform:rotate(-6deg);font-size:110px')}
    {narr('Ash got there first.','', 'position:absolute;left:330px;width:420px;bottom:-110px')}
  </div>
  {gap(440)}
  <div class="rel">{img('bb13','full')}
    {bub('We leave for two weeks, and you start a war?','L13', 'left','position:absolute;left:120px;top:-280px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('bb14','', 'width:660px;height:660px')}
    {bub("Hello! I'm injured!",'L14', 'right','position:absolute;left:-280px;top:40px;width:300px')}
  </div>
  {gap(360, 'linear-gradient(#0b0d16,#3b3550 55%,#e6d4c5)')}
</div>
<div class="sec white" style="background:#e6d4c5">
  <div class="rel" data-a="L15">{img('bb15','full')}
    {narr('By dawn it was over. And eleven Measurers had seen exactly what the people of Greyhollow were.','', 'position:absolute;left:200px;width:680px;bottom:-200px')}
  </div>
  {gap(280)}
  {gap(320, 'linear-gradient(#e6d4c5,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L16" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 27 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
