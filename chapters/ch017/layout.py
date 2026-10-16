"""Chapter 17 layout."""
FACES = {
    "s01": [(0, 150, 1536, 520)],
    "s02": [(240, 80, 430, 310), (780, 420, 1180, 590)],
    "s03": [(380, 250, 600, 500)],
    "s04": [(300, 20, 520, 260), (850, 90, 1060, 330)],
    "s05": [(170, 110, 400, 360), (740, 180, 910, 380)],
    "s06": [(360, 230, 620, 500)],
    "s07": [(50, 0, 640, 640)],
    "s08": [(130, 10, 360, 240), (710, 110, 900, 340), (1060, 130, 1250, 360), (1360, 180, 1536, 410)],
    "s09": [(400, 20, 820, 560)],
    "s10": [(260, 40, 720, 520)],
    "s11": [(170, 30, 340, 220), (600, 180, 1536, 720)],
    "s12": [(330, 150, 580, 430)],
    "s13": [(150, 40, 290, 200), (360, 160, 520, 340)],
    "s14": [(400, 60, 580, 270), (730, 10, 910, 220)],
    "s15": [(200, 0, 520, 350)],
    "s16": [(190, 110, 370, 340), (680, 110, 860, 340)],
    "s17": [(260, 110, 580, 450)],
    "s18": [(120, 110, 300, 320), (380, 110, 560, 320)],
    "s19": [(160, 20, 630, 560)],
    "s20": [(260, 80, 550, 410)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 17</div><div class="c2">The Measurers</div></div>
  {gap(100)}
  {narr('They came in the morning, through the smoke. Twelve riders in blue, with silver lenses at their throats.','L0', 'margin:0 150px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('s01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1">{img('s02','full')}
    {narr('The village did its best. Our blacksmith coughed. Our farmers limped. One of the goats, for reasons nobody could ever explain, also limped.','', 'position:absolute;left:220px;width:640px;bottom:-210px')}
    {sfx('COUGH COUGH','left:470px;top:30px;transform:rotate(-6deg);font-size:56px', 'quiet')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('s03','', 'width:720px;height:1080px')}
    {bub("What a charming festival. I don't believe I've ever seen one quite like it.",'L2', 'right','position:absolute;left:-300px;top:60px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel">{img('s04','full')}
    {bub('Ancient tradition, Magister. Very old. Very sacred.','L3', 'up','position:absolute;right:30px;bottom:-190px;width:400px')}
    {bub('How old?','L4', 'up','position:absolute;left:60px;bottom:-150px;width:220px')}
    {bub('Older than me.','L5', 'up','position:absolute;right:120px;bottom:-400px;width:280px')}
  </div>
  {gap(480)}
  <div class="rel" style="margin-left:300px">{img('s05','', 'width:660px;height:660px')}
    {bub("Ilse! My best student. You've been gone so long, the College thought the wolves had eaten you.",'L6', 'up','position:absolute;left:-270px;bottom:-250px;width:460px')}
  </div>
  {gap(330)}
  <div class="rel" style="margin-left:0">{img('s06','', 'width:720px;height:1080px')}
    {bub('Magister Hask. I found nothing here. A cold village, and a boy who reads too many books.','L7', 'left','position:absolute;right:-340px;top:520px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('s07','', 'width:660px;height:660px')}
    {bub("Then you won't mind if I look.",'L8', 'up','position:absolute;left:-270px;bottom:-130px;width:340px')}
  </div>
  {gap(260)}
  <div class="rel">{img('s08','full')}
    {bub("Welcome to Greyhollow, Magister. I'm Lucan Varr.",'L9', 'up','position:absolute;left:300px;bottom:-170px;width:420px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L10" style="margin-left:0">{img('s09','', 'width:660px;height:660px')}
    {narr('He raised his lens to look at me. It fogged over at once. He wiped it on his sleeve, and looked again. It fogged again.','', 'position:absolute;right:-380px;width:400px;top:120px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('s10','', 'width:720px;height:1080px')}
    {bub('This damp northern air. It gets into everything.','L11', 'right','position:absolute;left:-290px;top:600px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel">{img('s11','full')}
    {bub('By writ of the Grand Measurer, the Order will measure every soul in Greyhollow. Every man, every woman, every child.','L12', 'up','position:absolute;left:30px;bottom:-330px;width:560px')}
    {sfx('KRRSH','left:200px;top:560px;transform:rotate(-6deg);font-size:56px', 'quiet')}
  </div>
  {gap(420)}
  <div class="rel" data-a="L13" style="margin-left:330px">{img('s12','', 'width:720px;height:1080px')}
    {narr('Behind him, the youngest of the twelve, a girl not much older than me, was staring at Ash with her mouth open.','', 'position:absolute;left:-300px;top:500px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel">{img('s13','full')}
    {bub('Is he going to eat me?','L14', 'up','position:absolute;left:30px;bottom:-150px;width:320px')}
    {bub("No. He likes you. That's worse. Now he'll follow you everywhere.",'L15', 'up','position:absolute;right:30px;bottom:-280px;width:440px')}
  </div>
  {gap(380)}
  <div class="rel" data-a="L16">{img('s14','full')}
    {narr("Hask asked to see the village. I couldn't refuse. So I walked him through it myself, and prayed.",'', 'position:absolute;left:250px;width:580px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:300px">{img('s15','', 'width:660px;height:660px')}
    {bub('Glasshouses. In the north. How clever.','L17', 'up','position:absolute;left:-270px;bottom:-130px;width:360px')}
  </div>
  {gap(240)}
  <div class="rel">{img('s16','full')}
    {bub("And the mill turns. I was told the mill here hadn't turned in ten years.",'L18', 'up','position:absolute;right:30px;bottom:-200px;width:440px')}
    {bub('I read a book about it.','L19', 'up','position:absolute;left:40px;bottom:-280px;width:320px')}
  </div>
  {gap(380)}
  <div class="rel" style="margin-left:0">{img('s17','', 'width:720px;height:1080px')}
    {bub('You read a great many books, Lord Lucan.','L20', 'left','position:absolute;right:-330px;top:80px;width:340px')}
    {bub("There wasn't much else to do. I'm a zero.",'L21', 'left','position:absolute;right:-330px;top:560px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L22">{img('s18','full')}
    {narr('Then we reached the south field, and he stopped walking.','', 'position:absolute;left:250px;width:580px;bottom:-130px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('s19','', 'width:660px;height:660px')}
    {bub('Barley.','L23', 'right','position:absolute;left:-230px;top:420px;width:200px')}
    {bub('This far north.','L24', 'up','position:absolute;left:-150px;bottom:-140px;width:280px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L25" style="margin-left:0">{img('s20','', 'width:720px;height:1080px')}
    {narr("He didn't say anything else. He didn't have to.",'', 'position:absolute;right:-330px;width:400px;top:600px')}
  </div>
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L26" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 18 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
