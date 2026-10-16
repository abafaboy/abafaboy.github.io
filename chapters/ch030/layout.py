"""Chapter 30 layout."""
FACES = {'p01': [(1305, 225, 1495, 405),
         (1120, 285, 1325, 465),
         (425, 260, 570, 405),
         (280, 305, 405, 435),
         (560, 365, 665, 485),
         (675, 365, 775, 485),
         (780, 370, 885, 495),
         (5, 375, 65, 465),
         (45, 370, 115, 470),
         (90, 390, 150, 480),
         (120, 395, 185, 495),
         (185, 405, 255, 495)],
 'p02': [(140, 55, 640, 545), (950, 150, 1200, 530)],
 'p03': [(115, 115, 575, 590)],
 'p04': [(270, 440, 490, 625), (755, 330, 875, 440)],
 'p05': [],
 'p06': [(170, 60, 345, 235),
         (410, 170, 565, 335),
         (610, 230, 755, 390),
         (755, 280, 860, 425),
         (885, 240, 1020, 405),
         (1040, 340, 1140, 465),
         (1155, 365, 1250, 475),
         (1220, 345, 1320, 445),
         (1270, 340, 1365, 430),
         (1305, 300, 1390, 395),
         (1370, 320, 1465, 405),
         (1320, 105, 1536, 365)],
 'p07': [(0, 290, 190, 510), (270, 205, 435, 415), (650, 270, 755, 365), (760, 195, 885, 340)],
 'p08': [(100, 415, 345, 650),
         (285, 245, 580, 480),
         (0, 355, 180, 510),
         (825, 415, 965, 550),
         (1090, 410, 1240, 565),
         (1080, 580, 1245, 745),
         (1360, 510, 1510, 710)],
 'p09': [(80, 415, 565, 900)],
 'p10': [(575, 150, 850, 435), (165, 340, 305, 475)],
 'p11': [(320, 110, 580, 365), (620, 330, 865, 570)],
 'p12': [(1130, 95, 1290, 245),
         (860, 245, 1005, 390),
         (635, 250, 745, 375),
         (465, 320, 570, 445),
         (355, 315, 455, 425),
         (245, 345, 335, 445),
         (185, 350, 280, 445),
         (135, 335, 215, 425),
         (120, 390, 195, 485),
         (60, 400, 135, 480),
         (30, 420, 100, 495),
         (0, 405, 60, 480)],
 'p13': [(245, 90, 500, 355)],
 'p14': [(35, 100, 155, 210),
         (205, 80, 315, 205),
         (300, 10, 405, 115),
         (395, 70, 515, 200),
         (600, 135, 730, 255),
         (835, 130, 1010, 290),
         (980, 30, 1105, 150),
         (1065, 125, 1190, 235),
         (1125, 35, 1245, 165),
         (1255, 0, 1360, 100),
         (1280, 85, 1405, 210),
         (1390, 95, 1515, 210)],
 'p15': [(410, 555, 790, 875), (395, 855, 770, 1080)],
 'p16': [(35, 285, 205, 450),
         (205, 265, 355, 400),
         (460, 280, 595, 415),
         (700, 225, 835, 355),
         (870, 165, 1005, 305),
         (210, 435, 445, 740),
         (755, 465, 1005, 715),
         (0, 210, 70, 290),
         (85, 205, 190, 300),
         (400, 215, 500, 310),
         (550, 210, 645, 290),
         (625, 190, 705, 265)],
 'p17': [(255, 370, 430, 565)],
 'p18': [(870, 120, 1090, 355), (250, 330, 445, 520)],
 'end': []}

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
  {gap(550)}
  <div class="rel" style="margin-left:300px">{img('p07','', 'width:660px;height:660px')}
    {bub("Best I've felt in a week. Can we keep him, Wren?",'L7', 'right','position:absolute;left:-270px;top:-300px;width:550px')}
    {bub("He's the lord, Dunn.",'L8', 'right','position:absolute;left:-290px;top:330px;width:320px')}
    {bub('Can we keep him anyway?','L9', 'up','position:absolute;left:-30px;bottom:-250px;width:400px')}
  </div>
  {gap(350, 'linear-gradient(#eef4fa,#121827)')}
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
    {narr('When it was gone, nobody spoke for an hour.','', 'position:absolute;left:680px;top:-100px;width:380px')}
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
