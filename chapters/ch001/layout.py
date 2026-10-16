"""Chapter 1 layout. Uses helpers img, narr, bub, sfx, gap provided by strip.py."""
# Face boxes in SOURCE pixels (x0, y0, x1, y1), annotated by eye from grid overlays.
FACES = {
    "t04": [(440, 130, 620, 330)],                      # the king
    "t05": [(230, 120, 470, 360), (270, 920, 330, 990), (920, 880, 1020, 960)],  # Maric + two crowd faces
    "t06": [(140, 40, 720, 720)],                       # Lord Varr, tearful
    "t09": [(0, 0, 1536, 1024)],                        # whole panel is Lucan's eyes
    "t10": [(390, 0, 710, 340)],                        # Lady Sabine
    "t11": [(380, 0, 800, 420)],                        # Lord Varr, low angle (redo)
    "c14b": [(830, 120, 980, 300), (430, 300, 560, 440), (60, 330, 160, 450)],
    "c16": [(240, 90, 480, 370)],
    "c17": [(330, 240, 480, 400)],
    "c18": [(100, 0, 900, 800)],
    "c19": [(560, 40, 800, 280)],
    "c21": [(290, 180, 520, 440), (500, 820, 830, 1000)],
    "c24": [(640, 360, 820, 560)],
    "c25": [(250, 60, 820, 760)],
    "c27": [(280, 100, 720, 500)],
    "c28": [(400, 0, 600, 230)],
    "c29": [(230, 0, 680, 580)],
    "c30": [(630, 60, 830, 260), (160, 400, 260, 520)],
    "c31": [(500, 90, 660, 280)],
    "c32": [(820, 90, 1100, 420)],
}


def build():
    return f"""
<div class="sec white">
  {gap(140)}
  <div class="rel" data-a="L0">{img('t01','full')}
    {narr('In the kingdom of Aldmere, one moment decides your whole life.','', 'position:absolute;left:150px;right:150px;bottom:-110px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L1" style="margin-left:180px">{img('t02','', 'width:840px;height:1260px')}
    {narr('At sixteen, every noble child places a palm on the Measuring Stone. And the stone shows the depth of their Vessel, the well of power inside them.','', 'position:absolute;left:-160px;width:560px;top:90px')}
  </div>
  {gap(170)}
  {narr('One ring of light is a commoner. Three rings, a knight. Five rings, a true lord.','', 'margin:0 150px')}
  {gap(50)}
  <div class="row" data-a="L2">
    {img('t03a','','width:330px;height:330px;margin-top:0')}
    {img('t03b','','width:330px;height:330px;margin-top:70px')}
    {img('t03c','','width:330px;height:330px;margin-top:140px')}
  </div>
  {gap(50)}
  {narr('Someone who can split a charging warhorse with a single stroke.','', 'margin:0 190px')}
  {gap(140)}
  {narr('The last man to light seven was King Aldric the First. They built a cathedral on the spot.','', 'margin:0 60px 0 470px;position:relative;top:40px')}
  <div class="rel" data-a="L3">{img('t04','full sepia')}</div>
  {gap(150)}
  {narr('My older brother Maric lit five. The hall roared.','', 'margin:0 520px 0 40px;position:relative;top:50px')}
  <div class="rel" data-a="L4" style="margin-left:60px">{img('t05','', 'width:900px;height:1350px')}
    {sfx('WOOOOAAH!!','left:20px;top:560px;transform:rotate(-8deg);font-size:84px')}
    <div style="position:absolute;right:-40px;bottom:-260px;width:520px" data-a="L4b">{img('t06','', 'width:520px;height:520px;border-width:8px;border-color:#fff;outline:4px solid #111')}</div>
    {narr('Father wept, which I had only ever seen him do over money.','', 'position:absolute;left:-30px;width:440px;bottom:-250px')}
  </div>
  {gap(430)}
  <div class="rel" data-a="L5" style="margin-left:120px">{img('t07','', 'width:840px;height:1260px')}
    {narr('Then it was my turn.','', 'position:absolute;right:-80px;top:70px;width:360px')}
    {sfx('tap... tap...','left:80px;top:1080px;transform:rotate(-4deg);font-size:58px', 'quiet')}
  </div>
  {gap(260, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  {narr('I put my hand on the stone.','', 'margin:0 260px;position:relative;top:40px')}
  <div class="rel" data-a="L5b">{img('t08','full')}</div>
  {gap(380)}
  <div class="big" data-a="L6">Nothing.</div>
  {gap(380)}
  <div class="rel" data-a="L7">{img('t09','full', 'height:540px')}</div>
  {gap(40)}
  {narr('Not one ring. Not a flicker. Just cold, black stone, like the bottom of a well.','', 'margin:0 130px')}
  {gap(300, 'linear-gradient(#05060a,#f6f0fa)')}
</div>
<div class="sec white">
  {narr('The silence lasted long enough to hurt. Then someone laughed.','L8', 'margin:0 170px')}
  {gap(70)}
  <div class="rel" data-a="L8b" style="margin-left:0">{img('t10','', 'width:840px;height:1260px')}
    {sfx('Ho ho ho~','left:660px;top:320px;transform:rotate(9deg);font-size:64px', 'mock')}
    {narr('Lady Sabine of House Corrow, whose family has wanted our river for three generations.','', 'position:absolute;right:-200px;width:460px;bottom:150px')}
    {bub('Oh, how wonderful. An empty Varr.','L9','left','position:absolute;right:-215px;top:60px;width:420px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L10" style="margin-left:300px">{img('t11','', 'width:660px;height:660px')}
    {bub('Well. At least the boy is honest.','', 'up','position:absolute;left:-270px;bottom:-200px;width:460px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L11">{img('c12','full')}
    {narr('Three days later, I was rewarded with Greyhollow.','', 'position:absolute;left:60px;top:50px;width:520px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L12">{img('c13','full')}
    {narr('A northern fief where the frost never fully leaves.','', 'position:absolute;left:200px;right:200px;bottom:-100px')}
  </div>
  {gap(170)}
  <div class="row" data-a="L12b">
    {img('c14a','','width:330px;height:330px;margin-top:0')}
    {img('c14b','','width:330px;height:330px;margin-top:70px')}
    {img('c14c','','width:330px;height:330px;margin-top:140px')}
  </div>
  {gap(40)}
  {narr('A keep with half a roof. Thirty-seven peasants. Six goats.','', 'margin:0 170px')}
  {gap(120)}
  <div class="rel" data-a="L12c" style="margin-left:210px">{img('c15','', 'width:660px;height:660px')}
    {narr('And a debt of four thousand crowns, owed to House Corrow, due at first thaw.','', 'position:absolute;left:-170px;width:500px;bottom:-130px')}
  </div>
  {gap(260)}
  {narr("The deed was in my brother's handwriting. At the bottom, he'd added a note.",'', 'margin:0 130px 0 130px;position:relative;top:40px')}
  <div class="rel" data-a="L13" style="margin-left:120px">{img('c16','', 'width:840px;height:1260px')}
    {sfx('Builds character, little brother.','left:150px;top:1120px;transform:rotate(-5deg);font-size:50px', 'note')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L14" style="margin-left:330px">{img('c17','', 'width:720px;height:1080px')}
    {bub('Welcome to Greyhollow, my lord. Mind the stairs. Or rather, mind where the stairs used to be.','', 'right','position:absolute;left:-310px;top:420px;width:470px')}
  </div>
  {gap(200)}
  {narr("Greyhollow earns maybe two hundred crowns a year. I did the maths. I'll be in debtors' prison by seventeen.",'L15', 'margin:0 110px')}
  {gap(60)}
  <div class="rel" data-a="L15b" style="margin-left:210px">{img('c18','', 'width:660px;height:660px')}</div>
  {gap(200)}
  <div class="rel" data-a="L16">{img('c19','full')}
    {narr("Fine. I can't fight. I can't channel. But I've read every book in my father's library. If my Vessel is empty, my head will have to do the work.",'', 'position:absolute;left:30px;width:560px;bottom:-200px')}
  </div>
  {gap(330, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {narr('In the ruined kennel, I found a wolfhound. Half starved. One ear torn. Too weak to stand. Everyone had left it to die.','', 'margin:0 120px;position:relative;top:40px')}
  <div class="rel" data-a="L17">{img('c20','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L18">{img('c21','', 'width:840px;height:1260px')}
    {bub("Two failures in one castle. Fine. You're mine now. Your name is Ash.",'', 'left','position:absolute;right:-225px;top:60px;width:440px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L19" style="margin-left:210px">{img('c22','', 'width:660px;height:660px')}
    {sfx('thump','left:420px;top:540px;transform:rotate(-8deg);font-size:64px', 'quiet')}
  </div>
  {gap(40)}
  {narr('The dog thumped its tail once. Neither of us noticed the air around us shiver.','', 'margin:0 130px')}
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  {narr('That night, far to the south, the Royal Measurer held a lantern over the Measuring Stone, and stopped breathing.','', 'margin:0 120px;position:relative;top:40px')}
  <div class="rel" data-a="L20">{img('c23','full')}</div>
  {gap(160)}
  <div class="rel" data-a="L21" style="margin-left:120px">{img('c24','', 'width:840px;height:1260px')}
    {sfx('KRRAK','left:150px;top:40px;transform:rotate(-8deg);font-size:100px')}
    {bub('A crack. Straight through its heart.','', 'right','position:absolute;left:-100px;top:700px;width:400px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L22" style="margin-left:300px">{img('c25','', 'width:660px;height:660px')}
    {bub("A stone doesn't crack because it found nothing. It cracks because it couldn't hold what it found.",'', 'up','position:absolute;left:-290px;bottom:-330px;width:520px')}
  </div>
  {gap(400)}
  {bub('The last boy who touched this. I want his name.','L23', 'up','position:relative;margin:0 0 0 520px;width:480px')}
  {gap(330, 'linear-gradient(#05060a,#fff3e6)')}
</div>
<div class="sec white">
  {narr('In the morning, Ash was waiting by the door. His coat had grown in thick and black. His ribs were gone. And at his feet lay a dead frost-wolf, twice the size of a man.','', 'margin:0 90px;position:relative;top:40px')}
  <div class="rel" data-a="L24">{img('c26','full')}</div>
  {gap(120)}
  <div class="rel" data-a="L24b" style="margin-left:210px">{img('c27','', 'width:660px;height:660px')}
    {sfx('?!','left:520px;top:40px;transform:rotate(8deg);font-size:120px')}
  </div>
  {gap(150)}
  <div class="row" style="gap:40px">
    <div class="rel" data-a="L25">{img('c28','', 'width:480px;height:480px')}</div>
    <div class="rel" data-a="L26" style="margin-top:160px">{img('c29','', 'width:480px;height:480px')}</div>
  </div>
  <div style="position:relative;height:320px">
    {bub('Huh. The soil up here must be good.','', 'up','position:absolute;left:40px;top:-60px;width:420px')}
    {bub("That's not how soil works, my lord.",'', 'up','position:absolute;right:40px;top:110px;width:420px')}
  </div>
  {gap(120)}
  <div class="rel" data-a="L27" style="margin-left:60px">{img('c30','', 'width:840px;height:1260px')}
    {bub('Right. Anyway. Who wants to help me fix a roof?','', 'left','position:absolute;right:-180px;top:330px;width:400px')}
  </div>
  {gap(260)}
  {narr("After I'd gone inside, Bram stood alone in the yard. Out of old habit, he laid his one hand on the village's chipped Measuring Stone. The stone that had shown him a single ring for fifty years.",'', 'margin:0 80px;position:relative;top:40px')}
  <div class="rel" data-a="L28" style="margin-left:120px">{img('c31','', 'width:840px;height:1260px')}</div>
  {gap(200)}
  <div class="rel" data-a="L29">{img('c32','full')}</div>
  {gap(60)}
  <div class="big gold">It lit two.</div>
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L30" style="margin-left:120px">{img('c33','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 2 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""