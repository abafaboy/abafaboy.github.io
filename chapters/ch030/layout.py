"""Chapter 30 layout."""
FACES = {
    "p01": [(1330, 230, 1490, 395), (1175, 280, 1320, 450), (430, 260, 570, 405), (285, 310, 405, 435), (565, 370, 655, 475), (690, 375, 775, 485), (785, 380, 880, 490), (0, 360, 260, 520)],
    "p02": [(170, 60, 600, 500), (950, 150, 1170, 520)],
    "p03": [(60, 20, 720, 680)],
    "p06": [(170, 60, 340, 225), (415, 170, 560, 325), (615, 235, 750, 385), (755, 285, 855, 415), (885, 240, 1015, 395), (1040, 345, 1135, 455), (1145, 355, 1430, 495), (1335, 110, 1536, 300)],
    "p08": [(110, 420, 340, 625), (290, 250, 520, 450), (0, 370, 110, 480), (845, 430, 965, 530), (1095, 420, 1240, 540), (1085, 590, 1230, 715), (1380, 520, 1500, 690)],
    "p09": [(130, 230, 600, 860)],
    "p18": [(870, 120, 1080, 340), (245, 320, 420, 510)],
}

def build():
    return f"""
<div class="sec white" style="background:#eef4fa">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 30</div><div class="c2">Into the White</div></div>
  {gap(100)}
  {narr("The Skeld don't call it the Pale. They call it the White. On the first morning, I understood why.",'L0', 'margin:0 130px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('p01','full')}</div>
  {gap(160)}
  <div class="rel" data-a="L1">{img('p02','full')}
    {narr('The trees were made of ice. Not covered in it. Made of it. You could see green leaves inside them, frozen in the middle of some summer nobody remembered.','', 'position:absolute;left:160px;width:760px;bottom:-200px')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:0">{img('p03','', 'width:660px;height:660px')}
    {bub('Fascinating. Truly fascinating.','L2', 'left','position:absolute;left:400px;top:30px;width:400px')}
    {narr('Ilse said fascinating eleven times that morning. By noon, her spectacles had frozen to her nose.','L3', 'position:absolute;left:390px;top:330px;width:670px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:330px">{img('p04','', 'width:720px;height:1080px')}
    {bub('My lord. Look at your feet.','L4', 'right','position:absolute;left:-300px;top:100px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L5">{img('p05','full')}
    {narr('Wherever I stepped, the snow melted. A path of wet black earth followed me through the white, steaming a little, like bread fresh from the oven.','', 'position:absolute;left:160px;width:760px;bottom:-220px')}
  </div>
  {gap(340)}
  <div class="rel" data-a="L6">{img('p06','full')}
    {narr('By afternoon, all eleven of us were walking in single file, exactly in my footprints. Even the dog.','', 'position:absolute;left:200px;width:680px;bottom:-170px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:300px">{img('p07','', 'width:660px;height:660px')}
    {bub("Best I've felt in a week. Can we keep him, Wren?",'L7', 'right','position:absolute;left:-290px;top:20px;width:380px')}
    {bub("He's the lord, Dunn.",'L8', 'right','position:absolute;left:-290px;top:330px;width:320px')}
    {bub('Can we keep him anyway?','L9', 'up','position:absolute;right:20px;bottom:-200px;width:360px')}
  </div>
  {gap(300, 'linear-gradient(#eef4fa,#121827)')}
</div>
<div class="sec night" style="background:#121827">
  <div class="rel" data-a="L10">{img('p08','full')}
    {narr('At night I lay awake and felt the threads. A hundred and twelve of them, running south. Every mile north, they stretched a little thinner.','', 'position:absolute;left:160px;width:760px;bottom:-220px')}
  </div>
  {gap(340)}
  <div class="rel" data-a="L11" style="margin-left:330px">{img('p09','', 'width:720px;height:1080px')}
    {narr('Not weaker. Just further away. Like voices from another room.','', 'position:absolute;left:-300px;top:660px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p10','', 'width:660px;height:660px')}
    {bub('You are listening to your people. Skeld mothers make that face when their children are out on the ice.','L12', 'left','position:absolute;right:-400px;top:60px;width:460px')}
  </div>
  {gap(300, 'linear-gradient(#121827,#e9f0f6)')}
</div>
<div class="sec white" style="background:#e9f0f6">
  {narr("On the third day, Ilse took Dunn's stitches out. Underneath, the wound had closed into a thin pink line. Ilse said it should have taken a month.",'L13', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" style="margin-left:300px">{img('p11','', 'width:660px;height:660px')}
    {bub('Look at that! Good as new. Almost. Mostly. Ow.','L14', 'right','position:absolute;left:-290px;top:120px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L15">{img('p12','full')}
    {narr('That afternoon we crossed a frozen lake. Halfway over, Kell stopped dead.','', 'position:absolute;left:220px;width:640px;bottom:-170px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:0">{img('p13','', 'width:660px;height:660px')}
    {bub("Down. Everyone, down. Don't move. Don't breathe.",'L16', 'left','position:absolute;right:-400px;top:80px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L17">{img('p14','full')}
    {narr('Under the ice, something was moving. A shadow. Long, and pale, and slow.','', 'position:absolute;left:220px;width:640px;bottom:-170px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L18" style="margin-left:330px">{img('p15','', 'width:720px;height:1080px')}
    {narr("It passed beneath us for a very long time. The ice was melting under my hands, and I prayed that whatever it was couldn't feel warm.",'', 'position:absolute;left:-300px;top:500px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L19" style="margin-left:0">{img('p16','', 'width:660px;height:660px')}
    {narr('When it was gone, nobody spoke for an hour.','', 'position:absolute;right:-400px;top:40px;width:440px')}
    {bub('...Can we go home now?','L20', 'left','position:absolute;right:-380px;top:360px;width:340px')}
  </div>
  {gap(320, 'linear-gradient(#e9f0f6,#262b40)')}
</div>
<div class="sec night" style="background:#262b40">
  <div class="rel" style="margin-left:330px">{img('p17','', 'width:720px;height:1080px')}
    {bub('The oldest thing in the White. We do not say its name.','L21', 'right','position:absolute;left:-300px;top:100px;width:420px')}
  </div>
  {gap(320)}
  <div class="rel">{img('p18','full')}
    {bub("Tomorrow we reach a hunter's camp. A southerner's. He went into the White five winters ago, and never came back for it.",'L22', 'right','position:absolute;left:150px;top:-390px;width:620px')}
    {bub('...Whose camp?','L23', 'up','position:absolute;left:20px;bottom:-170px;width:300px')}
  </div>
  {gap(320, 'linear-gradient(#262b40,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L24" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 31 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
