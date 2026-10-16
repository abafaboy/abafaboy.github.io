"""Chapter 31 layout."""
FACES = {
    "p01": [(120, 250, 300, 430), (360, 360, 495, 520), (520, 400, 630, 545), (665, 425, 785, 570), (795, 460, 910, 595), (895, 455, 1005, 595), (1000, 300, 1200, 520)],
    "p02": [(200, 200, 540, 620)],
    "p03": [(530, 170, 670, 340)],
    "p04": [(40, 190, 560, 680)],
    "p06": [(140, 340, 420, 690), (360, 630, 600, 840)],
    "p07": [(495, 200, 715, 510), (695, 130, 905, 360), (840, 25, 980, 215), (1015, 75, 1175, 265), (1195, 0, 1370, 180)],
    "p08": [(240, 260, 600, 760)],
    "p09": [(410, 70, 640, 350), (650, 220, 890, 540), (1030, 30, 1280, 310)],
    "p11": [(240, 280, 700, 830)],
    "p12": [(310, 80, 540, 340), (800, 180, 930, 320), (920, 230, 1050, 360), (1040, 150, 1180, 300), (1250, 140, 1370, 270), (1350, 90, 1480, 240)],
    "p13": [(240, 130, 590, 490)],
    "p14": [(110, 210, 300, 410), (410, 210, 610, 420), (280, 390, 520, 620), (740, 120, 1040, 400), (1060, 440, 1300, 680), (1320, 170, 1520, 390)],
    "p15": [(170, 380, 360, 520), (930, 250, 1110, 420)],
    "p16": [(220, 400, 540, 700)],
    "p17": [(270, 150, 520, 420), (700, 260, 920, 500)],
    "p18": [(990, 30, 1300, 340), (110, 350, 320, 520)],
}

def build():
    return f"""
<div class="sec white" style="background:#eef4fa">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 31</div><div class="c2">Garrow's Camp</div></div>
  {gap(100)}
  {narr("The camp was a stone hut, half swallowed by the ice. Its door hadn't been opened in years.",'L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('p01','full')}</div>
  {gap(260, 'linear-gradient(#eef4fa,#1b2236)')}
</div>
<div class="sec night" style="background:#1b2236">
  <div class="rel" data-a="L1" style="margin-left:330px">{img('p02','', 'width:720px;height:1080px')}
    {narr("Wren went in first. She didn't wait for anyone.",'', 'position:absolute;left:-300px;top:600px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L2">{img('p03','full')}
    {narr('Inside, everything was where its owner had left it. A cold fire pit. A cooking pot. A bow on the wall, and a quiver of arrows.','', 'position:absolute;left:150px;width:780px;bottom:-260px')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:0">{img('p04','', 'width:660px;height:660px')}
    {bub("That's my father's bow.",'L3', 'left','position:absolute;right:-370px;top:110px;width:340px')}
  </div>
  {gap(160)}
  {narr('The arrows were fletched with grey goose feathers, bound with red thread. Wren fletched hers exactly the same way. He had taught her.','L4', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L4b" style="margin-left:210px">{img('p05','', 'width:660px;height:660px')}</div>
  {gap(260, 'linear-gradient(#1b2236,#f3e6cf)')}
</div>
<div class="sec white" style="background:#f3e6cf">
  <div class="rel" style="margin-left:0">{img('p06','sepia', 'width:720px;height:1080px')}
    {bub("He went hunting five winters ago. He said he'd be back in ten days. I was twelve.",'L5', 'left','position:absolute;right:-330px;top:40px;width:440px')}
  </div>
  {gap(260, 'linear-gradient(#f3e6cf,#1b2236)')}
</div>
<div class="sec night" style="background:#1b2236">
  <div class="rel" data-a="L6">{img('p07','full')}
    {narr('Under the bunk, wrapped in oilskin, Ilse found a journal.','', 'position:absolute;left:200px;width:680px;bottom:-200px')}
  </div>
  {gap(470)}
  <div class="rel" style="margin-left:330px">{img('p08','', 'width:720px;height:1080px')}
    {bub('Every winter, he set a stone at the edge of the White, and paced how far it had moved since the last one.','L7', 'right','position:absolute;left:-310px;top:-230px;width:600px')}
    {bub('Three hundred paces south. Then six hundred. Then a thousand. The White moves south every winter. And faster every year.','L8', 'right','position:absolute;left:-320px;top:560px;width:540px')}
  </div>
  {gap(420)}
  <div class="rel">{img('p09','full')}
    {bub('A hunter keeping records like a scholar.','L9', 'left','position:absolute;left:240px;top:-270px;width:400px')}
    {bub('He wanted to know why the game was leaving. He always wanted to know why.','L10', 'up','position:absolute;right:80px;bottom:-340px;width:460px')}
  </div>
  {gap(440)}
  <div class="rel" style="margin-left:300px">{img('p10','', 'width:660px;height:660px')}
    {narr('The last page was different. The writing shook, and a dark stain had soaked into one corner.','L11', 'position:absolute;left:-290px;top:140px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p11','', 'width:720px;height:1080px')}
    {bub("Something in the deep ice. Can't see from the left eye. If anyone finds this, tell Wren...",'L12', 'left','position:absolute;right:-340px;top:60px;width:420px')}
    {narr('That was all. The rest of the page was empty.','L13', 'position:absolute;right:-340px;top:520px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L14">{img('p12','full')}
    {narr("Wren didn't cry. She didn't say anything at all. She just sat on her father's bunk and held his bow.",'', 'position:absolute;left:180px;width:720px;bottom:-240px')}
  </div>
  {gap(300, 'linear-gradient(#1b2236,#231c1d)')}
</div>
<div class="sec night" style="background:#231c1d">
  {narr('Nobody knew what to say. So Dunn did what Dunn always does.','L15', 'margin:0 150px')}
  {gap(40)}
  <div class="rel" style="margin-left:0">{img('p13','', 'width:660px;height:660px')}
    {bub("I'll make soup. Everybody likes soup. Even sad people. Especially sad people.",'L16', 'left','position:absolute;right:-370px;top:20px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L17">{img('p14','full')}
    {narr('It was terrible soup. Wren ate two bowls.','', 'position:absolute;left:250px;width:580px;bottom:-160px')}
  </div>
  {gap(280, 'linear-gradient(#231c1d,#0b0d16)')}
</div>
<div class="sec night">
  <div class="rel" data-a="L18">{img('p15','full')}
    {narr("That night she slept with the bow beside her. I didn't sleep much at all.",'', 'position:absolute;left:200px;width:680px;bottom:-200px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L19" style="margin-left:330px">{img('p16','', 'width:720px;height:1080px')}
    {narr('By the door, Kell sat turning one of the red-thread arrows in his fingers. Over and over.','', 'position:absolute;left:-300px;top:500px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('p17','', 'width:660px;height:660px')}
    {bub('Kell? Is something wrong?','L20', 'right','position:absolute;left:-280px;top:50px;width:330px')}
    {bub('No, Warm One. Sleep.','L21', 'up','position:absolute;right:30px;bottom:-200px;width:320px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L22">{img('p18','full')}
    {narr("He set the arrow down very carefully, as if it belonged to someone. Then he looked across the fire at Wren, the way you look at someone you're about to give very good news. Or very bad.",'', 'position:absolute;left:110px;width:860px;bottom:-330px')}
  </div>
  {gap(380)}
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L23" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 32 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
