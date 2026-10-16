"""Chapter 13 layout."""
FACES = {
    "o02": [(0, 0, 1536, 520)],
    "o03": [(60, 180, 280, 420), (300, 120, 520, 380), (640, 330, 900, 620)],
    "o04": [(200, 100, 380, 300), (1050, 50, 1220, 230)],
    "o05": [(120, 40, 800, 760)],
    "o06": [(300, 180, 640, 580)],
    "o07": [(0, 0, 1024, 1024)],
    "o08": [(250, 40, 840, 720)],
    "o09": [(370, 80, 600, 330)],
    "o10": [(150, 60, 380, 300), (1100, 140, 1300, 360)],
    "o11": [(1100, 240, 1240, 380)],
    "o12": [(420, 90, 680, 360)],
    "o13": [(160, 40, 560, 520)],
    "o14": [(500, 30, 900, 520)],
    "o16": [(300, 150, 560, 460)],
    "o17": [(280, 100, 420, 240)],
    "o18": [(200, 0, 900, 700)],
    "o19": [(200, 30, 440, 300)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 13</div><div class="c2">Go Home</div></div>
  {gap(100)}
  {narr('The army broke camp three days after the duel. The war was won, the river was ours, and every lord in House Varr wanted to shake my hand.','L0', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('o01','full')}</div>
  {gap(150)}
  {narr('The same lords who had laughed at my farmers. Now they wanted to buy my turnips, borrow my blacksmith, and marry their daughters to the zero.','L1', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L1b">{img('o02','full')}</div>
  {gap(150)}
  {bub('That one keeps staring at you. The lord with the moustache.','L2', 'up','position:relative;margin-left:40px;width:400px;z-index:6')}
  {gap(30)}
  <div class="rel" style="margin-left:330px">{img('o03','', 'width:720px;height:1080px')}
    {bub('He wants to sell me his daughter.','L3', 'up','position:absolute;left:-290px;top:380px;width:360px')}
    {bub('Should I shoot him?','L4', 'right','position:absolute;left:-270px;top:640px;width:320px')}
    {bub('You have a problem, Wren.','L5', 'up','position:absolute;left:-290px;top:880px;width:340px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L6">{img('o04','full')}
    {narr('On the last night, my father sent for me again. This time there was no map on the table. Just two cups of wine.','', 'position:absolute;left:250px;width:580px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:300px">{img('o05','', 'width:660px;height:660px')}
    {bub('You did well.','L7', 'right','position:absolute;left:-260px;top:-60px;width:280px')}
  </div>
  {gap(40)}
  {narr("Three words. I had waited sixteen years for them. I didn't know what to do with my hands.",'L8', 'margin:0 160px')}
  {gap(130)}
  <div class="rel" style="margin-left:330px">{img('o06','', 'width:720px;height:1080px')}
    {bub('Now listen to me carefully. Go home. Tomorrow, at first light. Take your people and go back to Greyhollow, and stay there.','L9', 'right','position:absolute;left:-300px;top:40px;width:460px')}
    {bub('Father, the lords want trade agreements. If I stay, I could...','L10', 'up','position:absolute;left:-290px;top:700px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('o07','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {bub('Go home, Lucan.','L11', 'up','position:relative;margin-left:420px;width:300px')}
  {gap(100)}
  <div class="rel" data-a="L12" style="margin-left:0">{img('o08','', 'width:660px;height:660px')}
    {narr('He had never said my name like that before. Not like an order. Like a man who was afraid.','', 'position:absolute;right:-380px;width:400px;top:200px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:330px">{img('o09','', 'width:720px;height:1080px')}
    {bub('And if anyone, anyone, asks you to touch a Measuring Stone again, you refuse. Do you understand me?','L13', 'right','position:absolute;left:-300px;top:380px;width:440px')}
    {bub('Why?','L14', 'up','position:absolute;left:-250px;top:840px;width:200px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L15">{img('o10','full')}
    {narr('He looked at me for a long time. Then he drank his wine, and said nothing at all.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(260, 'linear-gradient(#fff,#f7f3e6)')}
  <div class="rel" data-a="L16">{img('o11','full')}
    {narr("We left at first light. Nine days later, Greyhollow's gate came into view. And standing in front of it, arms folded, exactly where I'd left him, was Bram.",'', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:330px">{img('o12','', 'width:720px;height:1080px')}
    {bub("You're late, my lord.",'L17', 'right','position:absolute;left:-280px;top:120px;width:300px')}
    {bub('We won a war.','L18', 'up','position:absolute;left:-270px;top:380px;width:280px')}
    {bub('Did you bring them all back?','L19', 'right','position:absolute;left:-290px;top:620px;width:340px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:0">{img('o13','', 'width:660px;height:660px')}
    {bub('Every one.','L20', 'left','position:absolute;right:-300px;top:200px;width:260px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L21" style="margin-left:300px">{img('o14','', 'width:660px;height:660px')}
    {narr("Bram nodded once. Then he turned away very quickly, and said there was something in his eye. There wasn't.",'', 'position:absolute;left:-270px;width:420px;bottom:-160px')}
  </div>
  {gap(260, 'linear-gradient(#f7f3e6,#1a1416)')}
</div>
<div class="sec night" style="background:#1a1416">
  <div class="rel" data-a="L22">{img('o15','full')}
    {narr('Far to the south, in a house that had lost its war, Lady Sabine Corrow wrote a letter. Not to her husband. Not to the king.','', 'position:absolute;left:250px;width:580px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:0">{img('o16','', 'width:720px;height:1080px')}
    {narr('To the Grand Measurer of the Order. Regarding a boy who reads as zero, in a village where nobody stays common.','L23', 'position:absolute;right:-330px;width:420px;top:560px')}
  </div>
  {gap(200, 'linear-gradient(#1a1416,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L24">{img('o17','full')}
    {narr('And in the capital, beneath the Cathedral of the Seven, a man in white robes read that letter by candlelight.','', 'position:absolute;left:250px;width:580px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:300px">{img('o18','', 'width:660px;height:660px')}
    {bub('A hollow-born. After all these years.','L25', 'up','position:absolute;left:-270px;bottom:-140px;width:360px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:330px">{img('o19','', 'width:720px;height:1080px')}
    {bub('Send the Measurers north.','L26', 'right','position:absolute;left:-290px;top:520px;width:340px')}
  </div>
  {gap(360)}
  <div class="rel" data-a="L27" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 14 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
