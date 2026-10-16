"""Chapter 19 layout."""
FACES = {
    "u01": [(100, 480, 245, 635), (250, 430, 380, 585), (420, 460, 540, 600), (700, 330, 1536, 640)],
    "u02": [(110, 100, 540, 470), (660, 0, 920, 380)],
    "u03": [(110, 345, 285, 545), (470, 290, 625, 455), (320, 320, 460, 455), (860, 305, 1024, 560), (0, 330, 80, 480)],
    "u04": [(55, 210, 215, 385), (280, 270, 440, 440), (530, 230, 695, 400), (910, 60, 1080, 245), (1330, 200, 1490, 375)],
    "u05": [(215, 240, 560, 690), (660, 380, 950, 700), (540, 510, 660, 640)],
    "u06": [(205, 40, 440, 285), (680, 360, 1536, 560)],
    "u07": [(200, 150, 395, 385), (630, 40, 790, 210), (20, 420, 110, 515), (815, 465, 950, 575)],
    "u09": [(100, 240, 470, 780), (440, 290, 800, 780), (860, 540, 1024, 690)],
    "u11": [(330, 30, 680, 530)],
    "u12": [(0, 0, 800, 820)],
    "u13": [(165, 130, 440, 470), (720, 0, 1024, 400), (570, 540, 750, 660)],
    "u14": [(370, 50, 640, 380), (0, 540, 210, 700), (690, 620, 1024, 730)],
    "u15": [(500, 45, 840, 390), (995, 55, 1300, 400), (40, 320, 215, 460), (1400, 420, 1536, 520)],
    "u16": [(140, 220, 600, 700), (790, 680, 915, 810), (540, 705, 640, 785), (870, 830, 980, 900)],
    "u17": [(995, 240, 1210, 475), (230, 0, 700, 400), (1240, 400, 1536, 510), (650, 430, 840, 500), (0, 360, 50, 440)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 19</div><div class="c2">Groaning Lessons</div></div>
  {gap(100)}
  {narr("The measuring began at dawn, in the thickest smoke Tobin's lanterns could make.",'L0', 'margin:0 150px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('u01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('u02','', 'width:660px;height:660px')}
    {bub('One ring. Next.','L1', 'right','position:absolute;left:-270px;top:60px;width:320px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L2" style="margin-left:0">{img('u03','', 'width:720px;height:1080px')}
    {narr("Oswin's lessons were paying off. Mostly.",'', 'position:absolute;right:-340px;width:380px;top:580px')}
  </div>
  {gap(160)}
  <div class="rel">{img('u04','full')}
    {bub('Oof. So heavy.','L3', 'up','position:absolute;left:560px;bottom:-160px;width:320px')}
    {narr('Mostly.','L4', 'position:absolute;left:150px;bottom:-310px;width:300px')}
  </div>
  {gap(420)}
  <div class="rel" style="margin-left:0">{img('u05','', 'width:720px;height:1080px')}
    {bub('One ring. Are you ill, blacksmith?','L5', 'left','position:absolute;right:-340px;top:120px;width:380px')}
    {bub("It's the smoke, miss. Ancient tradition. Very bad for the chest.",'L6', 'up','position:absolute;left:40px;bottom:-130px;width:460px')}
  </div>
  {gap(260)}
  {narr("Hask didn't measure anyone himself. He just watched, smiling, sipping tea from a cup somebody had given him. It was much worse than if he'd shouted.",'L7', 'margin:0 140px;padding:52px 80px')}
  {gap(40)}
  <div class="rel" data-a="L7b">{img('u06','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('u07','', 'width:660px;height:660px')}
    {bub('Ah. The steward. Allow me.','L8', 'right','position:absolute;left:-270px;top:0px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L9" style="margin-left:0">{img('u08','', 'width:660px;height:660px')}
    {narr("He took off his glove. He wasn't going to use a lens at all.",'', 'position:absolute;right:-380px;width:400px;top:160px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('u09','', 'width:720px;height:1080px')}
    {bub("He reads by touch. The way I do. Smoke won't help.",'L10', 'up','position:absolute;left:300px;top:620px;width:390px')}
  </div>
  {gap(160, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(60)}
  <div class="rel" data-a="L11">{img('u10','full')}
    {narr("Hask took Bram's one hand in his.",'', 'position:absolute;left:210px;width:660px;bottom:-140px')}
  </div>
  {gap(260)}
  {narr('Since midwinter, Oswin had been teaching Bram to hold his aether in. Like holding your breath, all the way down. Bram called it nonsense. He had practised every single night anyway.','L12', 'margin:0 70px;padding:56px 100px')}
  {gap(40)}
  <div class="rel" data-a="L12b" style="margin-left:180px">{img('u11','', 'width:720px;height:1080px')}</div>
  {gap(160)}
  <div class="rel" data-a="L13" style="margin-left:0">{img('u12','', 'width:660px;height:660px')}
    {narr('Nobody in the square breathed.','', 'position:absolute;right:-380px;width:400px;top:200px')}
  </div>
  {gap(160, 'linear-gradient(#0b0d16,#fff)')}
</div>
<div class="sec white">
  {gap(40)}
  <div class="rel" style="margin-left:330px">{img('u13','', 'width:720px;height:1080px')}
    {bub('Two rings. A strong two.','L14', 'right','position:absolute;left:-300px;top:140px;width:360px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('u14','', 'width:660px;height:660px')}
    {bub("I've worked hard, Magister.",'L15', 'left','position:absolute;right:-340px;top:80px;width:360px')}
  </div>
  {gap(160)}
  <div class="rel">{img('u15','full')}
    {bub('Told you the breathing was good for you.','L16', 'up','position:absolute;left:40px;bottom:-200px;width:420px')}
    {bub('Shut up, Oswin.','L17', 'up','position:absolute;right:60px;bottom:-230px;width:320px')}
  </div>
  {gap(360)}
  <div class="rel" data-a="L18" style="margin-left:330px">{img('u16','', 'width:720px;height:1080px')}
    {narr('So rings could be hidden. Not erased. Not faked. Just held, like a breath. And if Bram could hold five rings down to two, what else could we hide?','', 'position:absolute;left:-310px;top:560px;width:500px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L19">{img('u17','full')}
    {narr('Across the square, Hask raised his teacup to me. As if we had both just played a very good move.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L20" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 20 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
