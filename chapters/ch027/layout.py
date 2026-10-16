"""Chapter 27 layout."""
FACES = {
    "cc01": [(90, 290, 270, 475), (350, 220, 505, 380), (640, 405, 785, 545), (1060, 355, 1190, 505), (1250, 390, 1400, 540), (240, 320, 1250, 455)],
    "cc02": [(360, 10, 610, 330), (930, 50, 1180, 380)],
    "cc04": [(330, 100, 720, 540)],
    "cc05": [(150, 30, 545, 440)],
    "cc06": [(300, 50, 690, 500), (0, 40, 240, 620)],
    "cc07": [(250, 0, 590, 400)],
    "cc08": [(255, 0, 590, 345)],
    "cc09": [(235, 20, 410, 210), (480, 150, 1220, 490), (1215, 300, 1370, 475)],
    "cc10": [(290, 360, 510, 600), (875, 0, 1115, 225)],
    "cc11": [(160, 100, 780, 700)],
    "cc12": [(20, 320, 290, 560), (580, 25, 820, 275)],
    "cc13": [(380, 210, 1240, 720)],
    "cc14": [(175, 80, 445, 410), (425, 290, 680, 575), (610, 0, 1000, 420)],
    "cc15": [(130, 0, 480, 440)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 27</div><div class="c2">Debts</div></div>
  {gap(100)}
  {narr('Eleven of the twelve lived. The twelfth had been trampled before the gate ever opened. We buried him in our cemetery, under a Greyhollow stone.','L0', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('cc01','full')}</div>
  {gap(150)}
  <div class="rel">{img('cc02','full')}
    {bub('You carried me. I felt it. Your hands were freezing.','L1', 'up','position:absolute;left:40px;bottom:-230px;width:460px')}
    {bub("I'm always cold.",'L2', 'up','position:absolute;right:120px;bottom:-270px;width:300px')}
  </div>
  {gap(380)}
  <div class="rel" style="margin-left:300px">{img('cc03','', 'width:660px;height:660px')}
    {bub('My lens shattered when you touched me. Thirty years, and it never once so much as scratched.','L3', 'right','position:absolute;left:-270px;top:40px;width:460px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('cc04','', 'width:720px;height:1080px')}
    {bub('I owe you my life, Lord Lucan. That is an inconvenient thing for a Measurer to owe.','L4', 'left','position:absolute;right:-340px;top:60px;width:470px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('cc05','', 'width:660px;height:660px')}
    {bub("Then don't report me.",'L5', 'right','position:absolute;left:-270px;top:60px;width:320px')}
    {bub("I can't. Word has already gone south. And I serve the Order. What I owe the Order is the truth.",'L6', 'up','position:absolute;right:20px;bottom:-280px;width:540px')}
  </div>
  {gap(380)}
  <div class="rel" style="margin-left:0">{img('cc06','', 'width:720px;height:1080px')}
    {bub("But what I owe you, I will pay. I won't name Magister Thorne. As far as my report is concerned, she found nothing, because a junior would find nothing.",'L7', 'left','position:absolute;right:-350px;top:60px;width:560px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L8" style="margin-left:300px">{img('cc07','', 'width:660px;height:660px')}
    {narr('In the doorway, Ilse stood very still.','', 'position:absolute;left:-270px;width:400px;top:380px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('cc08','', 'width:660px;height:660px')}
    {bub('And I will ride south slowly. Very slowly. My arm, you understand.','L9', 'left','position:absolute;right:-380px;top:100px;width:420px')}
  </div>
  {gap(260, 'linear-gradient(#fff,#eef2f4)')}
</div>
<div class="sec white" style="background:#eef2f4">
  {narr('The next morning, the Measurers saddled their horses. All except one.','L10', 'margin:0 140px')}
  {gap(40)}
  <div class="rel" data-a="L10b">{img('cc09','full')}</div>
  {gap(260)}
  <div class="rel">{img('cc10','full')}
    {bub('Reed. Your horse.','L11', 'left','position:absolute;right:110px;top:-250px;width:380px')}
    {bub("I'm staying, Magister.",'L12', 'up','position:absolute;left:60px;bottom:-190px;width:340px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('cc11','', 'width:720px;height:1080px')}
    {bub("I asked eleven times to see my sister. Last night, a farmer carried me out of a stampede on his back. He had three rings. I'm staying.",'L13', 'up','position:absolute;left:-300px;top:540px;width:560px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('cc12','', 'width:660px;height:660px')}
    {bub('Take care of her, my lord.','L14', 'left','position:absolute;right:-360px;top:20px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L15">{img('cc13','full')}
    {narr('Ten blue robes rode out of the south gate. The smoke festival was over.','', 'position:absolute;left:220px;width:640px;bottom:-170px')}
    {sfx('KLOP KLOP','left:40px;top:560px;transform:rotate(-6deg);font-size:54px', 'quiet')}
  </div>
  {gap(300)}
  <div class="rel">{img('cc14','full')}
    {bub("I can write the Order's reports, my lord. In the Order's hand, with the Order's codes. Whatever you need them to believe.",'L16', 'up','position:absolute;left:40px;bottom:-300px;width:600px')}
    {sfx('SLURRP','left:730px;top:320px;transform:rotate(-8deg);font-size:54px', 'quiet')}
  </div>
  {gap(420)}
  <div class="rel" style="margin-left:300px">{img('cc15','', 'width:660px;height:660px')}
    {bub("Right now, I need them to believe we're harmless.",'L17', 'left','position:absolute;left:-270px;top:-40px;width:350px')}
    {bub('I think that ship has sailed.','L18', 'right','position:absolute;left:-270px;top:330px;width:340px')}
  </div>
  {gap(320, 'linear-gradient(#eef2f4,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L19" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 28 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
