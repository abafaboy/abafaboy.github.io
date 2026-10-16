"""Chapter 4 layout."""
FACES = {
    "f01": [(340, 60, 500, 250), (960, 10, 1140, 220)],
    "f02": [(270, 250, 440, 420)],
    "f03": [(200, 0, 560, 420)],
    "f04": [(520, 20, 670, 200), (1040, 460, 1200, 620)],
    "f05": [(340, 100, 560, 360)],
    "f06": [(380, 40, 640, 330), (600, 250, 800, 480)],
    "f07": [(410, 150, 640, 420)],
    "f08": [(90, 240, 230, 390), (450, 90, 600, 260), (870, 120, 1020, 300), (1220, 160, 1370, 330)],
    "f09": [(220, 0, 430, 220)],
    "f10": [(360, 0, 880, 580)],
    "f11": [(270, 180, 430, 340), (870, 70, 1030, 250)],
    "f12": [(90, 330, 270, 520), (470, 220, 650, 420)],
    "f13": [(360, 20, 730, 520)],
    "f14": [(440, 140, 610, 320), (760, 140, 920, 320)],
    "f17": [(340, 190, 580, 450)],
    "f20": [(450, 50, 740, 430)],
    "f22": [(290, 190, 450, 370)],
    "f23": [(330, 400, 600, 660)],
    "f24": [(120, 60, 780, 760)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 4</div><div class="c2">The Knight in the Snowdrift</div></div>
  {gap(100)}
  {narr('Twenty lamps. Tobin could make one every two days, if Ash kept bringing rimeglass. Forty days. We had sixty. For the first time since the Measuring, the numbers were on my side.','L0', 'margin:0 80px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('f01','full')}</div>
  {gap(150)}
  {narr('Naturally, that was when a knight fell off his horse at our gate.','L1', 'margin:0 190px')}
  {gap(40)}
  <div class="rel" data-a="L1b">{img('f02','full')}
    {sfx('THUD!','left:620px;top:520px;transform:rotate(-8deg);font-size:90px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:300px">{img('f03','', 'width:660px;height:660px')}
    {bub("My lord! There's a man in the snowdrift. He's either dead, or very drunk.",'L2', 'right','position:absolute;left:-280px;bottom:-80px;width:440px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L3">{img('f04','full')}
    {narr('Very drunk, as it turned out. A steel breastplate, a good sword, and a smell that made the goats leave.','', 'position:absolute;left:30px;width:520px;bottom:-170px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:330px">{img('f05','', 'width:720px;height:1080px')}
    {bub("Sir Oswin Hale. Formerly of the King's Third Company. Formerly of a lot of things. Is this the edge of the world?",'L4', 'right','position:absolute;left:-300px;top:260px;width:500px')}
    {bub("Close. It's Greyhollow.",'L5', 'up','position:absolute;left:-290px;top:820px;width:330px')}
    {bub('Same thing.','L6', 'right','position:absolute;left:-250px;top:1040px;width:280px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('f06','', 'width:660px;height:660px')}
    {bub('I know that name, my lord. Hale was stripped of his spurs last year. They say he refused an order.','L7', 'up','position:absolute;left:-180px;bottom:-250px;width:480px')}
  </div>
  {gap(300)}
  {bub('What order?','L8', 'up','position:relative;margin-left:600px;width:280px')}
  {gap(60)}
  <div class="rel" style="margin-left:0">{img('f07','', 'width:720px;height:1080px')}
    {bub("To burn a village that couldn't pay its taxes. With the villagers still inside.",'L9', 'left','position:absolute;right:-330px;top:520px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L10">{img('f08','full')}
    {narr('Nobody said anything for a while.','', 'position:absolute;left:340px;right:340px;bottom:-110px')}
  </div>
  {gap(250)}
  <div class="rel" style="margin-left:300px">{img('f09','', 'width:660px;height:660px')}
    {bub('We could use a man who knows how to fight. The pay is terrible. The roof is half finished. Breakfast is mostly goat.','L11', 'right','position:absolute;left:-280px;top:280px;width:460px')}
  </div>
  {gap(170)}
  <div class="rel" style="margin-left:210px">{img('f10','', 'width:660px;height:660px')}
    {bub("You're offering me a post? I'm a disgrace.",'L12', 'up','position:absolute;left:-180px;bottom:-200px;width:380px')}
    {bub("I'm a zero. We'll get along fine.",'L13', 'up','position:absolute;right:-180px;bottom:-340px;width:360px')}
  </div>
  {gap(440)}
  <div class="rel" data-a="L14">{img('f11','full')}
    {narr('He stayed. On the first day, he slept. On the second, he trained Wren. On the third, he trained everyone.','', 'position:absolute;right:30px;width:520px;bottom:-170px')}
  </div>
  {gap(250)}
  <div class="rel" style="margin-left:330px">{img('f12','', 'width:720px;height:1080px')}
    {bub('Again! Shield up, Tobin! You hit like a man apologising!','L15', 'right','position:absolute;left:-310px;top:-90px;width:420px')}
    {sfx('CLONK!','left:-260px;top:620px;transform:rotate(-8deg);font-size:80px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('f13','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr('By the end of the week, Oswin had stopped drinking. He said the cold air cleared his head.','L16', 'margin:0 150px')}
  {gap(160)}
  <div class="rel" data-a="L17">{img('f14','full')}
    {narr("I found out much later that he'd told Bram his sword arm felt ten years younger. And that Bram had told him to keep it to himself.",'', 'position:absolute;left:30px;width:560px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L18" style="margin-left:210px">{img('f15','', 'width:660px;height:660px')}
    {narr("Meanwhile, the lamps piled up. Seven. Eight. Nine. Pell's sleigh would be back within the month.",'', 'position:absolute;left:-170px;width:470px;bottom:-140px')}
  </div>
  {gap(250, 'linear-gradient(#fff,#120c0a)')}
</div>
<div class="sec night" style="background:#120c0a">
  {narr('On the night of the ninth lamp, the grain store caught fire.','L19', 'margin:0 190px')}
  {gap(40)}
  <div class="rel" data-a="L19b">{img('f16','full')}
    {sfx('FWOOSH','left:520px;top:40px;transform:rotate(-6deg);font-size:96px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('f17','', 'width:720px;height:1080px')}
    {bub("Fire! The grain store's on fire!",'L20', 'right','position:absolute;left:-300px;top:500px;width:380px')}
  </div>
  {gap(160)}
  {narr('We formed a line from the stream. Buckets, pots, anything that held water. Ash dragged sacks out of the flames with his teeth.','L21', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L21b">{img('f18','full')}</div>
  {gap(260, 'linear-gradient(#120c0a,#d9dde6)')}
</div>
<div class="sec white" style="background:#d9dde6">
  <div class="rel" data-a="L22">{img('f19','full')}
    {narr('We saved the building. We lost half the grain. Half of everything we had to eat until spring.','', 'position:absolute;left:220px;right:220px;bottom:-150px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:300px">{img('f20','', 'width:660px;height:660px')}
    {bub('This was no accident, my lord. Someone poured lamp oil along the back wall. I can still smell it.','L23', 'right','position:absolute;left:-280px;top:360px;width:460px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L24" style="margin-left:210px">{img('f21','', 'width:660px;height:660px')}
    {narr('In the snow behind the store, Wren found boot prints. Southern boots, heading for the road.','', 'position:absolute;left:-170px;width:470px;bottom:-140px')}
  </div>
  {gap(260, 'linear-gradient(#d9dde6,#0b0d16)')}
</div>
<div class="sec night">
  {narr('That night I sat alone with the ledger. Half the grain. Thirty-seven mouths. Ninety days of winter.','L25', 'margin:0 140px')}
  {gap(40)}
  <div class="rel" data-a="L25b">{img('f22','full')}</div>
  {gap(160)}
  <div class="rel" data-a="L26" style="margin-left:0">{img('f23','', 'width:720px;height:1080px')}
    {narr("And for the first time since I arrived, I felt the cold. Truly felt it. Deep in my bones, as if something I couldn't see had been hurt.",'', 'position:absolute;right:-330px;width:440px;top:620px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('f24','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr('Somewhere to the south, someone was smiling. I intended to ruin their day.','L27', 'margin:0 170px')}
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L28" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 5 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
