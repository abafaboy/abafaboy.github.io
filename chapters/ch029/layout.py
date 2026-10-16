"""Chapter 29 layout."""
FACES = {
    "p01": [(280, 120, 480, 320), (690, 180, 850, 400), (1030, 220, 1200, 410)],
    "p02": [(220, 40, 440, 330), (640, 370, 870, 640)],
    "p03": [(395, 525, 580, 720)],
    "p04": [(120, 150, 340, 400), (500, 0, 690, 200), (610, 220, 830, 530)],
    "p05": [(260, 40, 510, 300), (735, 235, 905, 445), (1100, 200, 1290, 425)],
    "p06": [(140, 460, 450, 740)],
    "p07": [(205, 40, 375, 235), (760, 110, 1070, 460)],
    "p08": [(150, 20, 450, 335), (560, 330, 940, 640)],
    "p09": [(520, 150, 690, 340), (790, 100, 950, 290), (50, 330, 245, 500), (1095, 370, 1200, 470), (1340, 380, 1480, 520)],
    "p10": [(240, 100, 520, 430)],
    "p11": [(255, 120, 420, 320)],
    "p12": [(70, 280, 245, 455), (375, 270, 535, 445)],
    "p13": [(300, 30, 560, 340)],
    "p14": [(0, 320, 1120, 700), (1260, 260, 1536, 570)],
    "p15": [(260, 35, 590, 430)],
    "p16": [(65, 590, 325, 850), (535, 490, 850, 820)],
    "p17": [(120, 620, 1340, 825)],
    "p18": [(280, 400, 675, 810)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 29</div><div class="c2">The Invitation</div></div>
  {gap(100)}
  {narr("Bram spent the whole next morning trying to talk me out of it. He tried four different ways. He's very thorough.",'L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('p01','full')}</div>
  {gap(460)}
  <div class="rel" style="margin-left:0">{img('p02','', 'width:660px;height:660px')}
    {bub('Then send me instead, my lord. Or Wren. Or Oswin. Anyone who can swing a sword.','L1', 'left','position:absolute;left:20px;top:-420px;width:440px')}
    {bub("They didn't invite a sword, Bram.",'L2', 'left','position:absolute;right:-400px;top:240px;width:380px')}
  </div>
  {gap(240, 'linear-gradient(#fff,#e9eef4)')}
</div>
<div class="sec white" style="background:#e9eef4">
  <div class="rel" style="margin-left:330px">{img('p03','', 'width:720px;height:1080px')}
    {bub("And he has to go himself. A claim needs the claimer. You can't bond a people by letter.",'L3', 'right','position:absolute;left:-310px;top:80px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p04','sepia', 'width:660px;height:660px')}
    {bub("But there's a price. Wren's hunters were gone two weeks. When they came back, I measured them. Not one had grown. Not one had slipped.",'L4', 'left','position:absolute;right:-400px;top:60px;width:520px')}
  </div>
  {gap(500)}
  <div class="rel">{img('p05','full')}
    {bub("If I'm right, the moment you leave, it's the same for everyone here. Like dough in a cold kitchen. It doesn't fall. It just stops rising.",'L5', 'right','position:absolute;left:300px;top:-450px;width:640px')}
    {bub('With soldiers coming.','L6', 'up','position:absolute;left:320px;bottom:-130px;width:400px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L7" style="margin-left:0">{img('p06','', 'width:720px;height:1080px')}
    {narr('A hundred and twelve people. Three weeks of growing, thrown away. Or a whole people in the north who might stand with us when the soldiers came.','', 'position:absolute;left:330px;top:30px;width:620px')}
    {bub("I'm going.",'L8', 'left','position:absolute;left:340px;top:520px;width:360px')}
  </div>
  {gap(480, 'linear-gradient(#e9eef4,#fff)')}
</div>
<div class="sec white">
  <div class="rel">{img('p07','full')}
    {bub("Then I'll write to the Order while you're gone. Their hand, their codes. The village is quiet, and Lord Lucan is in bed with a cold.",'L9', 'right','position:absolute;left:300px;top:-440px;width:620px')}
    {bub("It won't stop the warrant. Nothing will. But they won't know where you are, or what you're doing.",'L10', 'up','position:absolute;left:420px;bottom:-330px;width:560px')}
  </div>
  {gap(400)}
  <div class="rel" style="margin-left:300px">{img('p08','', 'width:660px;height:660px')}
    {bub('A cold. Very believable.','L11', 'right','position:absolute;left:-290px;top:40px;width:380px')}
    {bub("My lord, you're always cold. It's the most believable thing about you.",'L12', 'up','position:absolute;right:20px;bottom:-280px;width:480px')}
  </div>
  {gap(360)}
  <div class="rel" data-a="L13">{img('p09','full')}
    {narr('Then I went to the forge and asked Tobin for two things. Sledges, for the snow. And stoves, for the Skeld.','', 'position:absolute;left:200px;width:680px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:0">{img('p10','', 'width:660px;height:660px')}
    {bub("Stoves? My lord, they live in the Pale. There's no wood up there. The trees are made of ice.",'L14', 'left','position:absolute;right:-400px;top:40px;width:480px')}
    {bub("That's why I want rimeglass stoves. No wood. No smoke. Just warm.",'L15', 'right','position:absolute;right:-400px;top:470px;width:440px')}
  </div>
  {gap(260)}
  {narr("We still had a barn full of rimeglass from the White Night. Tobin said a dozen stoves in two days was impossible. Then he built them anyway, plus one thing I hadn't asked for.",'L16', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L16b">{img('p11','full')}</div>
  {gap(300)}
  <div class="rel">{img('p12','full')}
    {bub('Tobin. What is that?','L17', 'left','position:absolute;left:40px;top:-170px;width:360px')}
    {bub('Harpoon launcher, my lord. Just in case.','L18', 'left','position:absolute;left:440px;top:-70px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('p13','', 'width:660px;height:660px')}
    {bub('In case of what?','L19', 'left','position:absolute;left:-290px;top:20px;width:300px')}
    {bub("Something big. It's the Pale.",'L20', 'left','position:absolute;left:390px;top:150px;width:380px')}
  </div>
  {gap(300, 'linear-gradient(#fff,#f4e6da)')}
</div>
<div class="sec white" style="background:#f4e6da">
  {narr('We left on the third morning. Wren, Oswin, Ilse, Kell, five hunters, my dog, and Dunn, who had forty stitches in his shoulder and refused to stay behind.','L21', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L21b">{img('p14','full')}</div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p15','', 'width:660px;height:660px')}
    {bub("I can't hold a spear yet, my lord. But I can hold a conversation.",'L22', 'left','position:absolute;right:-400px;top:60px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('p16','', 'width:720px;height:1080px')}
    {bub("Come back, my lord. I'll keep everything exactly where you left it.",'L23', 'right','position:absolute;left:-300px;top:-110px;width:420px')}
  </div>
  {gap(320, 'linear-gradient(#f4e6da,#e4ecf5)')}
</div>
<div class="sec white" style="background:#e4ecf5">
  <div class="rel" data-a="L24">{img('p17','full')}
    {narr('An hour past the north field, the green ended like a line drawn with a knife. Beyond it, there was only white.','', 'position:absolute;left:200px;width:680px;bottom:-200px')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:0">{img('p18','', 'width:720px;height:1080px')}
    {bub('From here, Warm One, nothing is warm but you. And the White does not like warm things.','L25', 'left','position:absolute;right:-340px;top:60px;width:440px')}
  </div>
  {gap(320, 'linear-gradient(#e4ecf5,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L26" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 30 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
