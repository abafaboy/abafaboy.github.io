"""Chapter 18 layout."""
FACES = {
    "t01": [(320, 75, 520, 290), (690, 285, 890, 500), (1036, 57, 1236, 290)],
    "t02": [(280, 40, 800, 640)],
    "t03": [(300, 160, 500, 400), (970, 145, 1180, 415)],
    "t04": [(425, 75, 640, 310)],
    "t05": [(232, 110, 415, 290), (897, 110, 1061, 290)],
    "t06": [(460, 390, 710, 640)],
    "t07": [(617, 180, 835, 415), (810, 127, 1010, 380)],
    "t08": [(300, 150, 630, 570)],
    "t09": [(0, 120, 1536, 420)],
    "t10": [(250, 75, 520, 360)],
    "t11": [(300, 150, 560, 520), (650, 40, 910, 360)],
    "t12": [(650, 90, 780, 220)],
    "t13": [(190, 40, 830, 830)],
    "t14": [(160, 40, 720, 640)],
    "t15": [(250, 75, 485, 310), (680, 430, 1536, 720)],
    "t16": [(150, 100, 1100, 720)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 18</div><div class="c2">The Fourth Article</div></div>
  {gap(160, 'linear-gradient(#fff,#1a1416)')}
</div>
<div class="sec night" style="background:#1a1416">
  {narr('The writ covered every soul in Greyhollow. Including mine. Including the one lord in Aldmere who had promised never to touch a Measuring Stone again.','L0', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('t01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('t02','', 'width:660px;height:660px')}
    {bub("If he puts a lens on you properly, in daylight, without smoke, it's over.",'L1', 'up','position:absolute;left:-270px;bottom:-200px;width:420px')}
  </div>
  {gap(300)}
  <div class="rel">{img('t03','full')}
    {bub("Then we don't let him.",'L2', 'up','position:absolute;right:40px;bottom:-140px;width:320px')}
    {bub("We can't stop him. Unless the law does.",'L3', 'up','position:absolute;left:40px;bottom:-250px;width:380px')}
  </div>
  {gap(360)}
  <div class="rel" data-a="L4" style="margin-left:330px">{img('t04','', 'width:720px;height:1080px')}
    {narr('The Charter of Aldric. Every noble child in the kingdom has to learn the first page by heart. Nobody ever reads the rest. I had read it twice.','', 'position:absolute;left:-300px;top:420px;width:420px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L5">{img('t05','full')}
    {narr('So I read it a third time. All night.','', 'position:absolute;left:330px;width:420px;bottom:-110px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:0">{img('t06','', 'width:720px;height:1080px')}
    {bub("Here. The Fourth Article. No lord of the realm shall be measured, held, or questioned in his person, save by the King's own warrant, under the King's own seal.",'L6', 'left','position:absolute;right:-350px;top:40px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel">{img('t07','full')}
    {bub("The King's seal. Not the Grand Measurer's.",'L7', 'up','position:absolute;right:30px;bottom:-170px;width:380px')}
    {bub("His writ covers my people. It doesn't cover me.",'L8', 'up','position:absolute;left:30px;bottom:-290px;width:400px')}
  </div>
  {gap(520)}
  <div class="rel" data-a="L9" style="margin-left:300px">{img('t08','', 'width:660px;height:660px')}
    {narr('And two pages later, I found something else. Something strange.','', 'position:absolute;left:-270px;width:380px;top:-100px')}
  </div>
  {gap(40)}
  {bub('Any lord may raise to knighthood any commoner who holds a bridge for the realm.','L10', 'up','position:relative;margin-left:80px;width:520px')}
  {gap(20)}
  {bub('What does that mean?','L11', 'up','position:relative;margin-left:560px;width:300px')}
  {gap(20)}
  {bub('I have no idea. Yet.','L12', 'up','position:relative;margin-left:160px;width:280px')}
  {gap(160, 'linear-gradient(#1a1416,#fff)')}
</div>
<div class="sec white">
  <div class="rel">{img('t09','full')}
    {bub('Magister. With respect, you may not measure me. Not without a royal warrant.','L13', 'up','position:absolute;left:180px;bottom:-200px;width:500px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('t10','', 'width:720px;height:1080px')}
    {bub("The Fourth Article! Oh, that's wonderful. I haven't heard anyone cite the Fourth Article in thirty years.",'L14', 'right','position:absolute;left:-300px;top:420px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('t11','', 'width:660px;height:660px')}
    {bub("You're quite right, of course. My writ covers your people. Not you.",'L15', 'up','position:absolute;left:40px;bottom:-200px;width:440px')}
  </div>
  {gap(300)}
  <div class="rel">{img('t12','full')}
    {bub('Brother Aldo. Ride south today. Ask His Majesty for a warrant, under his own seal.','L16', 'up','position:absolute;left:40px;bottom:-200px;width:480px')}
    {sfx('KLOP KLOP','right:60px;top:520px;transform:rotate(-6deg);font-size:58px', 'quiet')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('t13','', 'width:720px;height:1080px')}
    {bub('Six weeks to the capital and back, I should think. And then, well. Royal warrants do tend to travel with soldiers.','L17', 'right','position:absolute;left:-300px;top:600px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L18" style="margin-left:0">{img('t14','', 'width:660px;height:660px')}
    {narr('I had bought six weeks. For myself.','', 'position:absolute;right:-360px;width:340px;top:260px')}
  </div>
  {gap(160)}
  <div class="rel">{img('t15','full')}
    {bub("In the meantime, I'm sure your people won't mind being measured. Shall we begin tomorrow? Everyone. Starting with the children.",'L19', 'up','position:absolute;left:30px;bottom:-280px;width:560px')}
  </div>
  {gap(380)}
  <div class="rel" data-a="L20">{img('t16','full')}
    {narr('Not for them.','', 'position:absolute;left:390px;width:300px;bottom:-110px')}
  </div>
  {gap(300, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L21" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 19 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
