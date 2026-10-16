"""Chapter 32 layout."""
FACES = {
    "p01": [(0, 250, 330, 420), (150, 370, 290, 500), (450, 360, 580, 470), (620, 460, 740, 560), (800, 540, 910, 640), (1030, 560, 1140, 660)],
    "p02": [(0, 0, 270, 340), (270, 40, 490, 350), (520, 300, 1536, 740)],
    "p03": [(470, 200, 950, 680), (90, 450, 320, 670), (250, 520, 480, 740), (70, 660, 300, 880)],
    "p04": [(40, 70, 420, 460), (330, 110, 690, 520), (690, 560, 1024, 800)],
    "p06": [(465, 30, 620, 215), (250, 215, 390, 380), (615, 195, 740, 355), (750, 230, 880, 390), (905, 300, 1030, 440), (1235, 250, 1395, 425), (990, 30, 1270, 290)],
    "p07": [(320, 190, 590, 440)],
    "p08": [(380, 300, 560, 520), (0, 780, 280, 1010), (740, 860, 1024, 1060)],
    "p09": [(60, 0, 620, 700)],
    "p10": [(690, 320, 920, 580), (880, 350, 1110, 580), (1080, 240, 1310, 480), (1230, 320, 1460, 580)],
    "p11": [(0, 0, 290, 350), (470, 110, 760, 440)],
    "p12": [(0, 0, 540, 640), (540, 30, 830, 470)],
    "p13": [(160, 210, 480, 590), (540, 590, 920, 930)],
    "p14": [(220, 90, 560, 460)],
    "p15": [(330, 140, 720, 500), (990, 600, 1240, 780), (1010, 200, 1130, 330)],
    "p16": [(380, 170, 620, 440), (0, 800, 220, 960), (150, 1000, 400, 1180), (840, 860, 1024, 1040), (790, 1080, 1000, 1240)],
    "p17": [(250, 40, 570, 400), (700, 470, 940, 710)],
    "p18": [(30, 310, 200, 520), (190, 250, 350, 430), (330, 240, 500, 410), (1040, 90, 1300, 330), (500, 680, 780, 830), (900, 760, 1010, 870)],
}

def build():
    return f"""
<div class="sec white" style="background:#eef4fa">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 32</div><div class="c2">The Skeld</div></div>
  {gap(100)}
  <div class="rel" data-a="L0">{img('p01','full')}
    {narr('Two days later, Kell brought us to his people.','', 'position:absolute;left:300px;top:16px;width:640px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L1">{img('p02','full')}
    {narr('The Skeld camp sat beneath a frozen cliff. Forty tents of white hide, around one small fire. Two hundred people. All of them cold.','', 'position:absolute;left:150px;width:780px;bottom:-260px')}
  </div>
  {gap(400)}
  <div class="rel" data-a="L2" style="margin-left:330px">{img('p03','', 'width:720px;height:1080px')}
    {narr('An old man was feeding the fire with bones. In the White, even the wood is ice.','', 'position:absolute;left:-300px;top:-80px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p04','', 'width:660px;height:660px')}
    {bub('Seven died last moon. Four of them were children.','L3', 'left','position:absolute;right:-380px;top:60px;width:360px')}
  </div>
  {gap(160)}
  {narr('Then they saw the snow around my boots. Melting. Steaming. Running in little streams toward their fire.','L4', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L4b" style="margin-left:210px">{img('p05','', 'width:660px;height:660px')}
    {sfx('HSSSS...','left:330px;top:560px;transform:rotate(-4deg);font-size:46px', 'quiet')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L5">{img('p06','full')}
    {narr('And one by one, the Skeld went down on their knees.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('p07','', 'width:720px;height:1080px')}
    {bub("No. Please, get up. I'm not anybody. I'm a zero.",'L6', 'right','position:absolute;left:-300px;top:60px;width:400px')}
    {narr("Nobody got up. I don't think I have ever hated anything so much.",'L7', 'position:absolute;left:-300px;top:520px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p08','', 'width:720px;height:1080px')}
    {bub("They don't kneel to you, boy. They kneel to the warmth. You just happen to be standing in it.",'L8', 'left','position:absolute;right:-340px;top:60px;width:440px')}
  </div>
  {gap(160)}
  {narr('She was small and very old, and her eyes were as white as the snow. Kell said Yrsa had been blind since birth, and saw more than anyone in the White.','L9', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L9b" style="margin-left:210px">{img('p09','', 'width:660px;height:660px')}</div>
  {gap(160)}
  <div class="rel" data-a="L10">{img('p10','full')}
    {narr('Behind me, the children crept up and held their hands over my footprints, as if they were a hearth.','', 'position:absolute;left:180px;width:720px;bottom:-240px')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:0">{img('p11','', 'width:660px;height:660px')}
    {bub('Come here, Warm One. Let me look at you.','L11', 'left','position:absolute;right:-370px;top:40px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L12" style="margin-left:210px">{img('p12','', 'width:660px;height:660px')}
    {narr("She put her hands on my face. They were like ice. And then they weren't.",'', 'position:absolute;left:-60px;width:780px;bottom:-200px')}
  </div>
  {gap(330)}
  <div class="rel" style="margin-left:0">{img('p13','', 'width:720px;height:1080px')}
    {bub('Hm. Everyone has a cup inside them, big or small. You have no cup at all. Only the water, pouring out.','L13', 'left','position:absolute;right:-340px;top:-40px;width:460px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('p14','', 'width:660px;height:660px')}
    {bub('The Sleeping Queen poured like that, once. Before she slept.','L14', 'right','position:absolute;left:-290px;top:170px;width:390px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L15">{img('p15','full')}
    {narr('Kell had told us about her on the road. The Skeld believed a queen slept beneath the White, and the cold was her dreaming.','', 'position:absolute;left:150px;width:780px;bottom:-260px')}
  </div>
  {gap(320)}
  {narr("Behind Yrsa, one Skeld had not knelt. A big woman in a bear's skin, with the bear's head for a hood.",'L16', 'margin:0 90px')}
  {gap(40)}
  <div class="rel" style="margin-left:330px">{img('p16','', 'width:720px;height:1080px')}
    {bub('I am Freydis, first of the elders. Kneeling is for the desperate, southerner. The White does not run on miracles. It runs on law.','L17', 'right','position:absolute;left:-310px;top:40px;width:470px')}
  </div>
  {gap(160)}
  {narr("In the crowd, a small boy with red-brown hair was staring at Wren. Wren was staring back. I didn't think anything of it. Not then.",'L18', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L18b" style="margin-left:210px">{img('p17','', 'width:660px;height:660px')}</div>
  {gap(420)}
  <div class="rel">{img('p18','full')}
    {bub('Skeld law. A guest who would sit at our fire must first feed it. Tomorrow, Warm One, you hunt.','L19', 'right','position:absolute;right:60px;top:-330px;width:560px')}
    {narr('I had never hunted anything in my life. Unless you count books.','L20', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(300)}
  {gap(320, 'linear-gradient(#eef4fa,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L21" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 33 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
