"""Chapter 28 layout."""
FACES = {
    "dd01": [(35, 370, 215, 560), (170, 225, 320, 405), (370, 140, 515, 320), (610, 350, 765, 530), (800, 185, 940, 350), (995, 255, 1130, 420), (1110, 350, 1245, 515), (1280, 150, 1420, 340), (1320, 415, 1465, 600)],
    "dd02": [(355, 30, 665, 360)],
    "dd03": [(420, 70, 680, 400), (930, 10, 1175, 290)],
    "dd04": [(200, 195, 475, 490)],
    "dd05": [(110, 160, 420, 480), (680, 190, 960, 480)],
    "dd06": [(285, 60, 580, 440)],
    "dd07": [(210, 140, 490, 440), (1025, 95, 1290, 405)],
    "dd08": [(680, 200, 780, 300)],
    "dd09": [(220, 270, 510, 640), (560, 650, 720, 790), (830, 720, 1024, 1010)],
    "dd10": [(390, 15, 600, 260)],
    "dd11": [(480, 60, 700, 400)],
    "dd12": [(330, 0, 720, 470)],
    "dd13": [(1060, 240, 1170, 370)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 28</div><div class="c2">The Clock</div></div>
  {gap(160, 'linear-gradient(#fff,#f3e8d2)')}
</div>
<div class="sec white" style="background:#f3e8d2">
  {narr('So the war council grew. Now it had a runaway Measurer, a man from the White, and a hunter with forty stitches in his shoulder.','L0', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('dd01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('dd02','', 'width:660px;height:660px')}
    {bub("Six weeks for Hask's warrant. Then soldiers. Two hundred, maybe more.",'L1', 'right','position:absolute;left:-270px;top:60px;width:440px')}
  </div>
  {gap(330)}
  <div class="rel">{img('dd03','full')}
    {bub('We beat thirty sellswords. We can beat two hundred.','L2', 'left','position:absolute;left:200px;top:-280px;width:520px')}
    {bub('Two hundred is how it starts. The crown has ten thousand.','L3', 'up','position:absolute;right:180px;bottom:-220px;width:520px')}
    {sfx('THUD!','left:590px;top:470px;transform:rotate(-8deg);font-size:64px')}
  </div>
  {gap(330)}
  <div class="rel" style="margin-left:0">{img('dd04','', 'width:720px;height:1080px')}
    {bub("Then we can't be a village anymore. A village gets burned. We have to become something the king can't afford to touch.",'L4', 'left','position:absolute;right:-350px;top:400px;width:560px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:300px">{img('dd05','', 'width:660px;height:660px')}
    {bub('Rich?','L5', 'left','position:absolute;right:30px;top:-190px;width:220px')}
    {bub('Rich. And not alone.','L6', 'right','position:absolute;left:-270px;top:180px;width:320px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('dd06','', 'width:720px;height:1080px')}
    {bub('Then come to the Skeld. My elders want to meet you. The Warm One, they call you. They are freezing, lord. They will listen to anyone who is warm.','L7', 'left','position:absolute;right:-350px;top:40px;width:560px')}
  </div>
  {gap(160)}
  <div class="rel">{img('dd07','full')}
    {bub('Into the Pale. You.','L8', 'up','position:absolute;right:100px;bottom:-170px;width:340px')}
    {bub('Me.','L9', 'up','position:absolute;left:150px;bottom:-300px;width:200px')}
  </div>
  {gap(420, 'linear-gradient(#f3e8d2,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L10">{img('dd08','full')}
    {narr('Far to the south, nine days later, a white bird landed beneath the Cathedral of the Seven.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
    {sfx('FLAP FLAP','left:560px;top:110px;transform:rotate(-8deg);font-size:50px', 'quiet')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:330px">{img('dd09','', 'width:720px;height:1080px')}
    {bub('Confirmed.','L11', 'right','position:absolute;left:-290px;top:330px;width:300px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:0">{img('dd10','', 'width:660px;height:660px')}
    {bub('Then we stop asking. Prepare a petition for His Majesty. A royal warrant, and a column of soldiers to carry it north.','L12', 'left','position:absolute;right:-400px;top:-20px;width:560px')}
  </div>
  {gap(300, 'linear-gradient(#05060a,#1d1527)')}
</div>
<div class="sec night" style="background:#1d1527">
  <div class="rel" data-a="L13">{img('dd11','full')}
    {narr('And in House Corrow, Lady Sabine bought every debt Pell Marrow owed, for twice what they were worth.','', 'position:absolute;left:220px;width:640px;bottom:-210px')}
    {sfx('clink... clink...','left:660px;top:440px;transform:rotate(-6deg);font-size:44px', 'quiet')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:300px">{img('dd12','', 'width:660px;height:660px')}
    {bub("Let's see how the zero trades without a merchant.",'L14', 'right','position:absolute;left:-270px;top:120px;width:400px')}
  </div>
  {gap(260, 'linear-gradient(#1d1527,#0b0d16)')}
</div>
<div class="sec night">
  <div class="rel" data-a="L15">{img('dd13','full')}
    {narr("In Greyhollow, the lamp in the hall burned a little brighter than the night before. It didn't know about any of it.",'', 'position:absolute;left:200px;width:680px;bottom:-230px')}
  </div>
  {gap(340, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L16" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 29 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
