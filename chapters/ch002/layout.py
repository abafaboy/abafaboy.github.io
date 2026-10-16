"""Chapter 2 layout. Uses helpers img, narr, bub, sfx, gap provided by strip.py."""
FACES = {
    "d01": [(60, 40, 240, 230)],
    "d03": [(440, 50, 610, 240), (740, 30, 920, 220), (0, 170, 130, 320), (1400, 200, 1536, 350)],
    "d05": [(380, 60, 580, 280)],
    "d06": [(300, 200, 470, 390)],
    "d07": [(330, 60, 560, 320)],
    "d08": [(240, 60, 430, 300)],
    "d09": [(30, 0, 200, 190), (680, 230, 840, 400)],
    "d10": [(380, 40, 620, 300)],
    "d11": [(180, 20, 800, 620)],
    "d12": [(480, 180, 720, 440)],
    "d14": [(480, 200, 690, 420), (20, 280, 180, 430), (200, 350, 360, 500), (800, 400, 960, 540), (920, 460, 1060, 590)],
    "d15": [(200, 0, 720, 620)],
    "d17": [(160, 320, 380, 560)],
    "d24": [(380, 170, 540, 340)],
    "d19": [(180, 0, 650, 480)],
    "d21": [(230, 40, 420, 260)],
    "d22": [(200, 0, 680, 520)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 2</div><div class="c2">The Mill That Wouldn\'t Turn</div></div>
  {gap(120)}
  <div class="rel" data-a="L0">{img('d01','full')}
    {narr('Greyhollow, day one. Assets: one keep, half a roof, thirty-seven people, six goats, and a dog who now eats more than all of them combined.','', 'position:absolute;left:330px;width:560px;bottom:-190px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L1" style="margin-left:210px">{img('d02','', 'width:660px;height:660px')}
    {narr('Liabilities: four thousand crowns, owed to House Corrow, due at first thaw. Roughly ninety days.','', 'position:absolute;left:-180px;width:470px;bottom:-150px')}
  </div>
  {gap(240)}
  {narr('I spent the morning walking the village with Bram. Nobody waved.','L2', 'margin:0 200px')}
  {gap(40)}
  <div class="rel">{img('d03','full')}
    {bub("They've had four lords in ten years, my lord. They stopped learning the names.",'L3', 'up','position:absolute;right:40px;bottom:-230px;width:480px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L4">{img('d04','full')}
    {narr('The mill was the worst of it. A good stream, a good wheel, and both frozen solid.','', 'position:absolute;left:40px;top:40px;width:500px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:240px">{img('d05','', 'width:840px;height:1260px')}
    {bub("Wheel's been dead three winters, my lord. Ice gets in the gears. We grind by hand now.",'L5', 'right','position:absolute;left:-220px;top:300px;width:440px')}
    {bub('And you are?','L6', 'up','position:absolute;left:-210px;top:720px;width:340px')}
    {bub('Tobin. Blacksmith. Also miller, carpenter, and the man who fixes whatever the last lord broke.','L7', 'right','position:absolute;left:-220px;top:930px;width:460px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L8">{img('d06','full')}
    {narr('I looked at the stream. Then at the hill above it. Then at the ditch someone had dug, badly, a long time ago.','', 'position:absolute;right:30px;width:520px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:300px">{img('d07','', 'width:660px;height:660px')}
    {bub("The ice isn't the problem. Your water comes in too slowly. It pools behind the wheel and freezes before it can move.",'L9', 'right','position:absolute;left:-280px;top:-60px;width:470px')}
  </div>
  <div style="position:relative;height:420px">
    {bub('And you know that how?','L10', 'up','position:absolute;right:60px;top:30px;width:340px')}
    {bub('Chapter nine of On the Management of Northern Estates. Very dry. Excellent diagrams.','L11', 'up','position:absolute;left:40px;top:150px;width:480px')}
  </div>
  {gap(80)}
  <div class="rel" style="margin-left:60px">{img('d08','', 'width:840px;height:1260px')}
    {bub("A book. He's going to fix the wheel with a book.",'L12', 'left','position:absolute;right:-165px;top:330px;width:380px')}
    {narr('That was Wren. Village huntress, seventeen, and by the look of her, already certain I would fail.','L13', 'position:absolute;right:-165px;bottom:120px;width:430px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L14">{img('d09','full')}
    {narr('We dug for four days. We re-cut the old channel, steeper and narrower, lined with stone, so the water would come in fast enough to stay alive.','', 'position:absolute;left:250px;width:600px;bottom:-200px')}
  </div>
  {gap(260)}
  {narr('Strange thing. Nobody got tired. Old men who had coughed all winter were swinging picks at dawn.','L15', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L15b" style="margin-left:210px">{img('d10','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr('Good food and a clear goal. Morale is an underrated resource.','L16', 'margin:0 170px')}
  {gap(90)}
  <div class="rel" style="margin-left:420px">{img('d11','', 'width:480px;height:480px')}
    {bub('Morale. Right.','L17', 'right','position:absolute;left:-330px;top:280px;width:300px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L18" style="margin-left:120px">{img('d12','', 'width:840px;height:1260px')}
    {narr('On the fifth morning, Tobin pulled the last stone out of the channel.','', 'position:absolute;left:-90px;width:430px;top:40px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L19">{img('d13','full')}
    {narr('The water hit the wheel. The wheel groaned. And then it turned.','', 'position:absolute;left:40px;top:30px;width:480px')}
    {sfx('KRRK... WHOOSH','left:360px;top:560px;transform:rotate(-6deg);font-size:64px')}
  </div>
  {gap(150)}
  <div class="rel">{img('d14','full')}
    {bub("Ha! Three winters! Three winters, and it's turning!",'L20', 'left','position:absolute;right:20px;top:-130px;width:430px')}
    {narr('The whole village was cheering. Even the goats looked impressed.','L21', 'position:absolute;left:30px;bottom:-130px;width:500px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('d15','', 'width:660px;height:660px')}
    {bub("Fine. You're not useless. Yet.",'L22', 'right','position:absolute;left:-270px;bottom:60px;width:330px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L23" style="margin-left:210px">{img('d16','', 'width:660px;height:660px')}
    {narr('Nobody noticed the frost on the mill roof melting. Not even me.','', 'position:absolute;left:-170px;width:450px;bottom:-120px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L24" style="margin-left:0">{img('d17','', 'width:840px;height:1260px')}
    {narr('That afternoon, Wren went hunting. She told me later she drew her bow the same way she had a thousand times before.','', 'position:absolute;right:-200px;width:440px;top:700px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L25">{img('d18','full')}
    {narr('The arrow flew two hundred paces. Then it went straight through a tree.','', 'position:absolute;left:40px;top:30px;width:480px')}
    {sfx('THWACK!!','left:420px;top:520px;transform:rotate(-10deg);font-size:96px')}
  </div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('d19','', 'width:660px;height:660px')}
    {bub('What.','L26', 'right','position:absolute;left:-230px;top:300px;width:250px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L27">{img('d20','full')}
    {narr('That evening, Ash came home from the Pale with something in his mouth.','', 'position:absolute;left:40px;top:-60px;width:480px')}
  </div>
  {gap(160)}
  {narr('He dropped it at my feet. A blue crystal, glowing faintly, cold as winter.','L28', 'margin:0 160px')}
  {gap(40)}
  <div class="rel" style="margin-left:120px">{img('d21','', 'width:840px;height:1260px')}
    {bub('Good boy. You brought me a rock.','L29', 'up','position:absolute;right:-60px;bottom:-150px;width:380px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:210px">{img('d22','', 'width:660px;height:660px')}
    {bub("My lord, that's not a rock. That's rimeglass. From a frost-wolf's heart.",'L30', 'up','position:absolute;left:-190px;bottom:-250px;width:470px')}
    {bub('One like that sells for forty crowns. Maybe fifty.','L31', 'up','position:absolute;right:-180px;bottom:-400px;width:400px')}
  </div>
  {gap(520)}
  {narr('Forty crowns. I did the maths. Four thousand crowns is a hundred frost-wolves.','L32', 'margin:0 150px')}
  {gap(60)}
  <div class="rel" data-a="L32b" style="margin-left:300px">{img('d23','', 'width:660px;height:660px')}</div>
  {gap(200)}
  <div class="rel" data-a="L33">{img('d24','full')}
    {narr('I looked at Ash. Ash looked at me. His tail thumped once.','', 'position:absolute;right:30px;top:-70px;width:460px')}
    {sfx('thump','left:900px;top:600px;transform:rotate(-8deg);font-size:56px', 'quiet')}
  </div>
  {gap(60)}
  {narr('We were going to need a bigger plan.','L34', 'margin:0 250px')}
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L35" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 3 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
