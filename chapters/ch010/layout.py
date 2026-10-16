"""Chapter 10 layout."""
FACES = {
    "l01": [(300, 170, 420, 290), (0, 290, 120, 420), (980, 600, 1110, 730)],
    "l02": [(560, 40, 720, 210), (950, 160, 1110, 330)],
    "l04": [(700, 160, 860, 330), (1000, 230, 1160, 380), (100, 200, 1536, 400)],
    "l05": [(130, 150, 330, 360), (380, 150, 590, 380)],
    "l06": [(420, 70, 600, 280)],
    "l07": [(200, 0, 840, 700)],
    "l08": [(150, 20, 800, 680)],
    "l09": [(220, 10, 400, 200)],
    "l10": [(130, 180, 400, 480), (480, 0, 810, 400)],
    "l11": [(370, 70, 510, 230)],
    "l13": [(110, 180, 400, 520)],
    "l15": [(200, 120, 1400, 440)],
    "l16": [(450, 0, 800, 330)],
    "l18": [(200, 230, 330, 380), (500, 290, 620, 400)],
    "l19": [(500, 20, 760, 330)],
    "l20": [(200, 0, 840, 700)],
    "l21": [(130, 30, 800, 750)],
    "l22": [(280, 20, 520, 280)],
    "l23": [(0, 0, 1024, 1024)],
    "l24": [(140, 30, 400, 330), (1080, 200, 1300, 440)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 10</div><div class="c2">The Muster</div></div>
  {gap(100)}
  {narr("We left Greyhollow with sixty fighters, twelve wagons, and one very large dog. Bram stayed behind with the rest, to keep the village safe. I didn't like leaving him. He didn't like being left.",'L0', 'margin:0 90px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('l01','full')}</div>
  {gap(150)}
  <div class="rel">{img('l02','full')}
    {bub('Bring them all back, my lord. Every one.','L1', 'up','position:absolute;right:40px;bottom:-170px;width:380px')}
    {bub('I intend to.','L2', 'up','position:absolute;left:300px;bottom:-280px;width:280px')}
  </div>
  {gap(350)}
  <div class="rel" data-a="L3">{img('l03','full')}
    {narr("It took nine days to reach the muster field at Senn Ford. My father's banners covered the hillside. Three thousand men. Knights in steel, levies in leather, and lords everywhere you looked.",'', 'position:absolute;left:220px;width:640px;bottom:-230px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L4">{img('l04','full')}
    {narr('We arrived last. Everyone noticed.','', 'position:absolute;left:30px;top:-70px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel">{img('l05','full')}
    {bub('Is that the Greyhollow levy? Farmers, with a dog?','L5', 'up','position:absolute;left:30px;bottom:-190px;width:380px')}
    {bub('I hear the zero has been selling lamps to merchants. Trade. How embarrassing.','L6', 'up','position:absolute;right:30px;bottom:-330px;width:440px')}
  </div>
  {gap(400)}
  <div class="rel" data-a="L7" style="margin-left:330px">{img('l06','', 'width:720px;height:1080px')}
    {narr('And then my brother rode up on a white warhorse, in black and gold armour, looking exactly like a hero from a song.','', 'position:absolute;left:-310px;top:520px;width:450px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('l07','', 'width:660px;height:660px')}
    {bub('Little brother! You came! And you brought farmers. How sweet.','L8', 'up','position:absolute;left:-270px;bottom:-200px;width:420px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:0">{img('l08','', 'width:660px;height:660px')}
    {bub('Hello, Maric. Father summoned the levy. Here it is.','L9', 'left','position:absolute;right:-380px;top:260px;width:400px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:330px">{img('l09','', 'width:720px;height:1080px')}
    {bub('Keep them at the back, would you? Real soldiers will handle the fighting. Your people can dig latrines.','L10', 'right','position:absolute;left:-310px;top:300px;width:450px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('l10','', 'width:660px;height:660px')}
    {bub('Can I shoot him? Just a little?','L11', 'up','position:absolute;left:-170px;bottom:-170px;width:360px')}
    {bub('Not today.','L12', 'up','position:absolute;right:-150px;bottom:-270px;width:260px')}
  </div>
  {gap(330)}
  <div class="rel" data-a="L13">{img('l11','full')}
    {narr('That night I went looking for the quartermaster. I wanted to know how three thousand men were being fed.','', 'position:absolute;right:30px;width:520px;bottom:-160px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L14" style="margin-left:210px">{img('l12','', 'width:660px;height:660px')}
    {narr('The answer was: badly.','', 'position:absolute;left:-170px;top:-70px;width:340px')}
  </div>
  {gap(170)}
  <div class="rel" style="margin-left:330px">{img('l13','', 'width:720px;height:1080px')}
    {bub('Grain for twelve days, my lord. Maybe ten. The barges from the south are late, and the roads are all mud.','L15', 'right','position:absolute;left:-310px;top:420px;width:450px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L16">{img('l14','full')}
    {narr("Ten days of food. Corrow had two thousand men across the river, with supply lines running straight back to their own granaries. All they had to do was wait, and my father's army would starve.",'', 'position:absolute;left:220px;width:640px;bottom:-230px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L17">{img('l15','full')}
    {narr('Nobody else seemed to have noticed. They were too busy planning glorious charges.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('l16','', 'width:660px;height:660px')}
    {bub('Tobin. How many wagons did we bring?','L18', 'right','position:absolute;left:-270px;top:-40px;width:360px')}
    {bub('Twelve, my lord. Eight of them full of turnips.','L19', 'up','position:absolute;left:-270px;bottom:-150px;width:400px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L20">{img('l17','full')}
    {narr('Turnips. Eight wagons of glasshouse turnips. Enough to feed this army for two more weeks.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L21" style="margin-left:0">{img('l18','', 'width:720px;height:1080px')}
    {narr('I went to find my father.','', 'position:absolute;right:-300px;top:440px;width:360px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L22">{img('l19','full')}
    {narr("He was alone in his tent, studying a map. He didn't look up when I came in.",'', 'position:absolute;left:30px;width:480px;bottom:-140px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:300px">{img('l20','', 'width:660px;height:660px')}
    {bub('You came.','L23', 'right','position:absolute;left:-260px;top:-60px;width:250px')}
    {bub('You summoned me.','L24', 'up','position:absolute;left:-270px;bottom:-130px;width:320px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:0">{img('l21','', 'width:660px;height:660px')}
    {bub("I summoned a name on a list. I didn't expect you to answer.",'L25', 'left','position:absolute;right:-380px;top:240px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('l22','', 'width:720px;height:1080px')}
    {bub("Father, the army has ten days of grain. I've brought two more weeks. And I have an idea about the river.",'L26', 'right','position:absolute;left:-310px;top:360px;width:450px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L27" style="margin-left:210px">{img('l23','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr('For the first time in my life, my father looked at me as if I might be worth listening to.','L27b', 'margin:0 150px')}
  {gap(130)}
  <div class="rel">{img('l24','full')}
    {bub('Sit down.','L28', 'up','position:absolute;left:60px;bottom:-140px;width:260px')}
  </div>
  {gap(330, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L29" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 11 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
