"""Chapter 24 layout."""
FACES = {
    "z01": [(418, 195, 620, 435), (995, 265, 1270, 520), (205, 465, 1330, 915)],
    "z02": [(215, 165, 660, 690), (400, 0, 920, 240)],
    "z03": [(175, 0, 615, 400), (580, 360, 990, 765)],
    "z04": [(440, 310, 795, 705)],
    "z05": [(180, 75, 310, 215), (965, 255, 1255, 520), (225, 480, 1335, 920)],
    "z06": [(425, 55, 610, 250)],
    "z07": [(795, 220, 995, 450), (1125, 225, 1350, 460)],
    "z08": [(240, 335, 885, 1105)],
    "z09": [(95, 125, 455, 490), (995, 245, 1270, 520), (490, 435, 1410, 825)],
    "z10": [(210, 65, 540, 435)],
    "z12": [(180, 220, 695, 735)],
    "z13": [(515, 15, 950, 560)],
    "z14": [(225, 255, 505, 545), (580, 380, 1010, 790), (10, 775, 1024, 1285)],
    "z15": [(240, 150, 535, 490), (1050, 240, 1315, 490), (620, 390, 1440, 730)],
    "z16": [(195, 150, 425, 420), (1020, 225, 1300, 520), (355, 435, 1470, 885)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 24</div><div class="c2">The Lullaby</div></div>
  {gap(160, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(40)}
  {narr('Later that night, one of the children woke up crying. Then another. Then all six.','L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('z01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('z02','', 'width:660px;height:660px')}
    {bub('Will the Academy be cold?','L1', 'right','position:absolute;left:-280px;top:200px;width:340px')}
    {bub("I don't know.",'L2', 'up','position:absolute;right:20px;bottom:-170px;width:300px')}
  </div>
  {gap(270)}
  <div class="rel" style="margin-left:0">{img('z03','', 'width:660px;height:660px')}
    {bub('Can you sing something? Mama always sings.','L3', 'left','position:absolute;right:-400px;top:60px;width:410px')}
    {bub("I don't really know any songs.",'L4', 'up','position:absolute;left:40px;bottom:-200px;width:380px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L5" style="margin-left:330px">{img('z04','', 'width:720px;height:1080px')}
    {narr("But I hummed anyway. A tune I didn't remember ever learning. Slow and low, like wind going round a chimney.",'', 'position:absolute;left:-310px;top:540px;width:440px')}
    {sfx('hmm... hmmm...','left:60px;top:90px;transform:rotate(-6deg);font-size:50px', 'quiet')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L6">{img('z05','full')}
    {narr('One by one, they fell asleep. And in the doorway, Bram had gone as white as snow.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:300px">{img('z06','', 'width:660px;height:660px')}
    {bub('Bram?','L7', 'left','position:absolute;left:-260px;top:120px;width:240px')}
  </div>
  {gap(160)}
  <div class="rel">{img('z07','full')}
    {bub("He looked like he'd seen a ghost.",'L8', 'up','position:absolute;left:260px;bottom:-180px;width:420px')}
    {bub("It's just a song.",'L9', 'up','position:absolute;right:40px;bottom:-180px;width:320px')}
  </div>
  {gap(500)}
  <div class="rel" style="margin-left:0">{img('z08','', 'width:720px;height:1080px')}
    {bub('Lucan. You should know what the Academy is. I trained in that building. I have never seen one commoner child come out of it. Not one. They go in, and the records end.','L10', 'left','position:absolute;right:-350px;top:-220px;width:670px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L11">{img('z09','full')}
    {narr('I looked at the six of them, asleep around my dog.','', 'position:absolute;left:240px;width:600px;bottom:-150px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L12" style="margin-left:0">{img('z10','', 'width:660px;height:660px')}
    {narr('So I opened the Charter again. I had read it three times. There had to be something.','', 'position:absolute;right:-400px;width:440px;top:120px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L13" style="margin-left:300px">{img('z11','', 'width:660px;height:660px')}
    {narr("And there was. Not in the Fourth Article. In the Eleventh. A lord's household is his own. His wife. His children. His servants. And his wards.",'', 'position:absolute;left:-200px;width:840px;bottom:-250px')}
  </div>
  {gap(350)}
  <div class="rel" style="margin-left:0">{img('z12','', 'width:720px;height:1080px')}
    {bub("Wards. If they're my wards, they're my household. And my household falls under the Fourth Article. No Measurer can take them without the King's own seal.",'L14', 'left','position:absolute;right:-350px;top:40px;width:570px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('z13','', 'width:660px;height:660px')}
    {bub('You would have to adopt them. Six peasant children. In law, you would be responsible for them. For everything, for the rest of their lives.','L15', 'right','position:absolute;left:-280px;top:40px;width:590px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('z14','', 'width:720px;height:1080px')}
    {bub("I'm already responsible for them.",'L16', 'right','position:absolute;left:-310px;top:60px;width:400px')}
  </div>
  {gap(160)}
  {narr('So I wrote six wardship papers, and signed every one. And with each name, I felt a thread of cold run out of my chest, and go deeper.','L17', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L17b">{img('z15','full')}
    {sfx('scritch... scritch...','left:40px;top:640px;transform:rotate(-4deg);font-size:44px', 'quiet')}
  </div>
  {gap(150)}
  <div class="rel" data-a="L18">{img('z16','full')}
    {narr('Not a contract. A claim.','', 'position:absolute;left:260px;width:560px;bottom:-110px')}
  </div>
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L19" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 25 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
