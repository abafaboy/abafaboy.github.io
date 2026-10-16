"""Chapter 15 layout."""
FACES = {
    "q01": [(0, 100, 1300, 520)],
    "q02": [(330, 230, 560, 500)],
    "q03": [(240, 420, 410, 600), (550, 260, 720, 460)],
    "q04": [(360, 100, 580, 380), (950, 100, 1180, 380)],
    "q05": [(380, 300, 620, 560)],
    "q06": [(230, 0, 600, 330)],
    "q07": [(270, 250, 470, 430), (880, 110, 1080, 340)],
    "q08": [(180, 100, 520, 500)],
    "q09": [(220, 320, 590, 700), (0, 100, 1024, 420)],
    "q10": [(150, 320, 1500, 620)],
    "q12": [(220, 350, 420, 620), (720, 500, 900, 700)],
    "q13": [(260, 30, 360, 130), (1250, 250, 1450, 380)],
    "q14": [(200, 450, 410, 710), (600, 390, 780, 620)],
    "q15": [(230, 150, 540, 560)],
    "q16": [(360, 110, 620, 410), (900, 150, 1090, 410)],
    "q17": [(300, 260, 450, 420)],
    "q18": [(120, 0, 500, 380)],
    "q20": [(80, 20, 340, 240), (680, 190, 880, 410), (500, 450, 690, 620), (1180, 270, 1370, 460)],
    "q21": [(350, 60, 700, 400)],
    "q22": [(170, 110, 480, 450)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 15</div><div class="c2">Two Days</div></div>
  {gap(160, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(40)}
  {narr('That night, the great hall of Greyhollow held the strangest war council in the history of Aldmere. A one-armed steward. A hunter. A blacksmith. A knight who had been sober for almost a year. A spy. And a zero.','L0', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('q01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('q02','', 'width:660px;height:660px')}
    {bub("A Measurer's lens reads rings at a glance. Any one of those twelve can look at a farmer and see exactly what is inside him.",'L1', 'up','position:absolute;left:-270px;bottom:-250px;width:460px')}
  </div>
  {gap(330)}
  <div class="rel" style="margin-left:0">{img('q03','', 'width:720px;height:1080px')}
    {bub("So let them look. We're farmers.",'L2', 'left','position:absolute;right:-330px;top:140px;width:340px')}
    {bub('Farmers have one ring. You have four. Your blacksmith has four. In this village, a child carrying water has three.','L3', 'left','position:absolute;right:-340px;top:560px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel">{img('q04','full')}
    {bub('Is three a lot?','L4', 'up','position:absolute;left:60px;bottom:-140px;width:300px')}
    {bub('Three is a knight, lad.','L5', 'up','position:absolute;right:60px;bottom:-250px;width:320px')}
  </div>
  {gap(340)}
  <div class="rel" data-a="L6" style="margin-left:330px">{img('q05','', 'width:720px;height:1080px')}
    {narr('There were only three choices. I made myself say them out loud.','', 'position:absolute;left:-300px;top:120px;width:380px')}
    {bub('We could run.','L7', 'right','position:absolute;left:-280px;top:700px;width:260px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:300px">{img('q06','', 'width:660px;height:660px')}
    {bub('Then everything breaks, my lord. You heard her. Leave your people, and whatever you gave them fades. Leave the land, and the frost comes back.','L8', 'up','position:absolute;left:-270px;bottom:-290px;width:500px')}
  </div>
  {gap(380)}
  <div class="rel">{img('q07','full')}
    {bub('We could fight.','L9', 'up','position:absolute;left:40px;bottom:-120px;width:280px')}
    {bub("Twelve Measurers with the Grand Measurer's seal. Lay one finger on them and it's treason. And next spring, the king's whole army comes north.",'L10', 'up','position:absolute;right:30px;bottom:-330px;width:520px')}
  </div>
  {gap(420)}
  <div class="rel" style="margin-left:0">{img('q08','', 'width:660px;height:660px')}
    {bub('Then we hide.','L11', 'left','position:absolute;right:-300px;top:120px;width:260px')}
    {bub('Hide a hundred and twelve people? Where?','L12', 'left','position:absolute;right:-340px;top:400px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('q09','', 'width:720px;height:1080px')}
    {bub('Right here. In plain sight.','L13', 'right','position:absolute;left:-290px;top:820px;width:320px')}
  </div>
  {gap(200)}
  <div class="rel">{img('q10','full')}
    {bub('Before you plan anything, my lord, look at that lamp.','L14', 'up','position:absolute;left:220px;bottom:-200px;width:520px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:210px">{img('q11','', 'width:660px;height:660px')}
    {bub('Tobin made it the week you arrived. The first lamp of rimeglass in Greyhollow. It has grown brighter every single month since. No one has ever added a drop of oil.','L15', 'up','position:absolute;left:-170px;bottom:-310px;width:560px')}
  </div>
  {gap(400)}
  <div class="rel" style="margin-left:0">{img('q12','', 'width:720px;height:1080px')}
    {bub('I thought I was just very good at lamps.','L16', 'left','position:absolute;right:-330px;top:60px;width:340px')}
    {bub('That light is your Root. Your bond with this land. The deeper it goes, the stronger your people can grow. Bram is at five because your Root allows five. And not one ring higher.','L17', 'left','position:absolute;right:-350px;top:420px;width:400px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L18">{img('q13','full')}
    {narr('So that was it. Every roof I fixed. Every field I drained. Every debt I paid. It had all been going into that little lamp.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(300, 'linear-gradient(#0b0d16,#1a1416)')}
  <div class="rel" style="margin-left:330px">{img('q14','', 'width:720px;height:1080px')}
    {bub("Ilse. Can I ask you something? You came here to find me. You've known for months. Why didn't you report me?",'L19', 'right','position:absolute;left:-300px;top:60px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('q15','', 'width:660px;height:660px')}
    {bub('I was going to. I had the letter written.','L20', 'left','position:absolute;right:-330px;top:60px;width:340px')}
    {bub('Then you fixed the mill.','L21', 'left','position:absolute;right:-310px;top:420px;width:300px')}
  </div>
  {gap(160)}
  <div class="rel">{img('q16','full')}
    {bub("The mill? That's it?",'L22', 'up','position:absolute;left:40px;bottom:-130px;width:300px')}
    {bub("I have measured a thousand noble children, my lord. Not one of them ever asked what was wrong with a peasant's mill.",'L23', 'up','position:absolute;right:30px;bottom:-310px;width:500px')}
  </div>
  {gap(400, 'linear-gradient(#1a1416,#0b0d16)')}
  <div class="rel" data-a="L24" style="margin-left:330px">{img('q17','', 'width:720px;height:1080px')}
    {narr('After she left, I went up on the wall. She had said I could feel them. That the cold I had felt all winter was them.','', 'position:absolute;left:-300px;top:560px;width:420px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L25" style="margin-left:0">{img('q18','', 'width:660px;height:660px')}
    {narr('So I closed my eyes, and for the first time in my life, I tried to feel the cold on purpose.','', 'position:absolute;right:-380px;width:400px;top:180px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L26">{img('q19','full')}
    {narr('At first, nothing. Then, one by one, I felt them. Thin threads of cold, running out from me into the dark. A hundred and twelve of them.','', 'position:absolute;left:220px;width:640px;bottom:-220px')}
  </div>
  {gap(320)}
  <div class="rel" data-a="L27">{img('q20','full')}
    {narr('One was Tobin, snoring. One was a little girl with a fever. One was Bram, still awake, sitting by the gate.','', 'position:absolute;left:220px;width:640px;bottom:-180px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L28" style="margin-left:300px">{img('q21','', 'width:660px;height:660px')}
    {narr('And one, the thickest and warmest of all, was lying on my feet.','', 'position:absolute;left:-270px;width:400px;bottom:-140px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:0">{img('q22','', 'width:720px;height:1080px')}
    {bub('Two days.','L29', 'left','position:absolute;right:-260px;top:640px;width:240px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L30">{img('q23','full')}
    {narr('Two days, to make a hundred and twelve people look like nobody at all.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L31" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 16 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
