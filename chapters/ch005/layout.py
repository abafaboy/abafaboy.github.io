"""Chapter 5 layout."""
FACES = {
    "g01": [(480, 100, 640, 290)],
    "g03": [(360, 40, 560, 260)],
    "g04": [(400, 40, 580, 260), (1000, 60, 1170, 280)],
    "g05": [(340, 80, 500, 270), (620, 220, 740, 330), (860, 230, 990, 350), (1230, 180, 1360, 310)],
    "g06": [(640, 220, 830, 420), (1000, 330, 1536, 700)],
    "g08": [(180, 140, 390, 370), (600, 70, 800, 300)],
    "g10": [(100, 40, 500, 320)],
    "g12": [(320, 50, 490, 250)],
    "g13": [(130, 0, 760, 640)],
    "g14": [(330, 30, 780, 600)],
    "g15": [(320, 50, 490, 240), (700, 70, 880, 290)],
    "g16": [(40, 180, 840, 500), (930, 110, 1100, 310)],
    "g17": [(200, 30, 690, 600)],
    "g19": [(550, 40, 720, 260)],
    "g20": [(260, 0, 720, 560)],
    "g22": [(360, 80, 520, 270)],
    "g23": [(180, 0, 800, 680)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 5</div><div class="c2">The Glass Gardens</div></div>
  {gap(100)}
  {narr('Half the grain was gone. Thirty-seven people would be hungry by midwinter. So I went back to my books.','L0', 'margin:0 130px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('g01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1" style="margin-left:300px">{img('g02','', 'width:660px;height:660px')}
    {narr('Chapter eleven of On the Management of Northern Estates. Glasshouses, and the forcing of vegetables in cold climates. The author had never seen rimeglass. I had a forge full of it.','', 'position:absolute;left:-270px;width:500px;bottom:-230px')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:330px">{img('g03','', 'width:720px;height:1080px')}
    {bub("You want me to bury rimeglass in the dirt? My lord, that's two hundred crowns a lamp!",'L2', 'right','position:absolute;left:-300px;top:260px;width:440px')}
    {bub("Not lamps. Slivers. The shavings you sweep off the floor. Buried under a glass roof, they'll keep the soil warm all winter.",'L3', 'up','position:absolute;left:-300px;top:640px;width:480px')}
  </div>
  {gap(220)}
  <div class="rel">{img('g04','full')}
    {bub("That's either genius, or madness.",'L4', 'up','position:absolute;left:40px;bottom:-170px;width:380px')}
    {bub("With him, it's usually both.",'L5', 'up','position:absolute;right:40px;bottom:-300px;width:360px')}
  </div>
  {gap(380)}
  <div class="rel" data-a="L6">{img('g05','full')}
    {narr('We built the first glasshouse against the south wall of the keep. Old windows from the ruined half of the castle, and rimeglass shavings in the soil beneath.','', 'position:absolute;right:30px;width:560px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L7">{img('g06','full')}
    {narr("Wren's mother planted turnips. Everyone laughed. Turnips, in the dead of winter.",'', 'position:absolute;left:30px;top:-80px;width:480px')}
    {sfx('ha ha ha','left:760px;top:640px;transform:rotate(-6deg);font-size:54px', 'quiet')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L8" style="margin-left:210px">{img('g07','', 'width:660px;height:660px')}
    {narr('Nine days later, the turnips came up.','', 'position:absolute;left:-170px;top:-90px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:330px">{img('g08','', 'width:720px;height:1080px')}
    {bub("That's not possible. Turnips take two months. Even in summer.",'L9', 'right','position:absolute;left:-300px;top:180px;width:420px')}
    {bub('Good soil.','L10', 'up','position:absolute;left:-260px;top:580px;width:260px')}
    {bub('Stop saying that.','L11', 'right','position:absolute;left:-290px;top:840px;width:320px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L12">{img('g09','full')}
    {narr('By the end of the month we had four glasshouses. Turnips, cabbages, beans. Nobody would starve this winter.','', 'position:absolute;left:250px;width:580px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L13" style="margin-left:300px">{img('g10','', 'width:660px;height:660px')}
    {narr('And the strange cold in my bones, the one that began the night of the fire, faded. I slept well for the first time in weeks.','', 'position:absolute;left:-270px;width:470px;bottom:-200px')}
  </div>
  {gap(320)}
  <div class="rel" data-a="L14">{img('g11','full')}
    {narr('That was the week the scholar arrived.','', 'position:absolute;right:40px;top:-60px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('g12','', 'width:720px;height:1080px')}
    {bub("Good afternoon. My name is Ilse, a travelling scholar from the Royal Academy. I'm writing a survey of northern farming. Might I stay a few days?",'L15', 'right','position:absolute;left:-300px;top:260px;width:480px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('g13','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr('She had kind eyes behind round spectacles, a satchel full of notebooks, and very cold hands.','L16', 'margin:0 150px')}
  {gap(120)}
  <div class="rel" style="margin-left:300px">{img('g14','', 'width:660px;height:660px')}
    {bub('Of course. We have turnips.','L17', 'up','position:absolute;left:-270px;bottom:-140px;width:360px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L18">{img('g15','full')}
    {narr('She asked a great many questions. About the soil. About the mill. About the villagers.','', 'position:absolute;right:30px;width:500px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L19">{img('g16','full')}
    {narr('She asked to shake hands with everyone. Thirty-seven people. Every single one.','', 'position:absolute;left:30px;width:500px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L20" style="margin-left:300px">{img('g17','', 'width:660px;height:660px')}
    {narr('I thought it was a southern custom.','', 'position:absolute;left:-270px;bottom:-110px;width:400px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L21" style="margin-left:210px">{img('g18','', 'width:660px;height:660px')}
    {sfx('shine...','left:470px;top:440px;transform:rotate(-8deg);font-size:50px', 'quiet')}
  </div>
  {gap(40)}
  <div class="big" style="font-size:110px;color:#2a1d10;text-shadow:none">It wasn't.</div>
  {gap(260, 'linear-gradient(#fff,#1a1410)')}
</div>
<div class="sec night" style="background:#1a1410">
  <div class="rel">{img('g19','full')}
    {bub('Wren, the huntress. Three rings. Tobin, the blacksmith. Three rings. The old woman who carries the water. Two.','L22', 'up','position:absolute;left:40px;bottom:-250px;width:500px')}
  </div>
  {gap(330)}
  <div class="rel" style="margin-left:300px">{img('g20','', 'width:660px;height:660px')}
    {bub("A village of commoners, where the commoners don't stay common.",'L23', 'up','position:absolute;left:-270px;bottom:-200px;width:440px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:210px">{img('g21','', 'width:660px;height:660px')}
    {bub("And the lord himself. Nothing. The lens doesn't even flicker.",'L24', 'up','position:absolute;right:-170px;bottom:-200px;width:430px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L25">{img('g22','full')}
    {narr('Outside her window, Bram stood in the snow, watching her candle burn late into the night.','', 'position:absolute;right:30px;width:500px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('g23','', 'width:660px;height:660px')}
    {bub('Scholar. My one remaining arm.','L26', 'up','position:absolute;left:-270px;bottom:-130px;width:380px')}
  </div>
  {gap(330, 'linear-gradient(#1a1410,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L27" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 6 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
