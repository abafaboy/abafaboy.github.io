"""Chapter 16 layout."""
FACES = {
    "r01": [(310, 60, 510, 290), (850, 180, 1040, 400), (1250, 220, 1430, 430)],
    "r02": [(530, 280, 780, 630)],
    "r03": [(200, 150, 690, 720)],
    "r04": [(340, 70, 550, 330), (990, 160, 1160, 400)],
    "r05": [(90, 60, 470, 520), (500, 40, 800, 430)],
    "r06": [(900, 30, 1040, 200), (0, 330, 1536, 1024)],
    "r07": [(300, 520, 480, 730), (570, 420, 740, 610), (0, 500, 240, 700)],
    "r08": [(250, 20, 800, 560)],
    "r09": [(290, 40, 620, 380), (760, 20, 1060, 360)],
    "r10": [(320, 30, 480, 200)],
    "r11": [(300, 110, 480, 300), (580, 180, 1536, 500)],
    "r12": [(620, 390, 810, 610), (0, 650, 560, 870)],
    "r13": [(160, 220, 350, 430), (630, 130, 890, 430)],
    "r14": [(430, 270, 640, 500), (850, 20, 1080, 280)],
    "r15": [(0, 60, 1000, 420), (1210, 10, 1370, 190)],
    "r16": [(300, 320, 500, 540), (620, 320, 810, 540)],
    "r17": [(280, 60, 720, 590)],
    "r18": [(80, 110, 830, 730)],
    "r20": [(450, 20, 740, 180)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 16</div><div class="c2">Fog</div></div>
  {gap(100)}
  {narr("Ilse said Measurers' lenses fog up whenever they come near me. Nobody knows why. So Tobin had an idea.",'L0', 'margin:0 140px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('r01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:330px">{img('r02','', 'width:720px;height:1080px')}
    {bub("Steam lanterns, my lord! The rimeglass heats the water, the water makes fog. Put one in every doorway, and their fancy lenses will be as blind as a fish in milk.",'L1', 'right','position:absolute;left:-310px;top:40px;width:460px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('r03','', 'width:660px;height:660px')}
    {bub('...It works.','L2', 'left','position:absolute;right:-280px;top:300px;width:240px')}
    {sfx('FSSSH','left:40px;top:500px;transform:rotate(-8deg);font-size:64px', 'quiet')}
  </div>
  {gap(160)}
  <div class="rel">{img('r04','full')}
    {bub('And when they ask why the whole village is full of smoke?','L3', 'up','position:absolute;left:40px;bottom:-200px;width:420px')}
    {bub("You tell them it's tradition.",'L4', 'up','position:absolute;right:40px;bottom:-330px;width:340px')}
  </div>
  {gap(420)}
  <div class="rel" style="margin-left:210px">{img('r05','', 'width:660px;height:660px')}
    {bub('What tradition?','L5', 'up','position:absolute;left:-170px;bottom:-130px;width:280px')}
    {bub("You'll think of one.",'L6', 'up','position:absolute;right:-150px;bottom:-250px;width:300px')}
  </div>
  {gap(640)}
  <div class="rel">{img('r06','full')}
    {bub('As you all know, every midsummer, Greyhollow celebrates the ancient and sacred festival of smoke.','L7', 'right','position:absolute;left:30px;top:-300px;width:520px')}
    {bub('Since when?','L8', 'up','position:absolute;left:60px;bottom:-200px;width:240px')}
    {bub('Since this morning.','L9', 'up','position:absolute;right:60px;bottom:-320px;width:300px')}
  </div>
  {gap(420)}
  <div class="rel" style="margin-left:330px">{img('r07','', 'width:720px;height:1080px')}
    {bub('And us?','L10', 'right','position:absolute;left:-250px;top:60px;width:200px')}
    {bub("You and your hunters read like knights. You're going hunting in the Pale. For two weeks.",'L11', 'right','position:absolute;left:-300px;top:780px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('r08','', 'width:660px;height:660px')}
    {bub('Two weeks in the Pale? Finally, some peace and quiet. No offence, my lord.','L12', 'left','position:absolute;right:-360px;top:180px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel">{img('r09','full')}
    {bub("You're sending away your best fighters, right when the Order shows up.",'L13', 'up','position:absolute;left:40px;bottom:-200px;width:440px')}
    {bub("I'm sending away my best evidence.",'L14', 'up','position:absolute;right:40px;bottom:-300px;width:360px')}
  </div>
  {gap(400)}
  <div class="rel" data-a="L15">{img('r10','full')}
    {narr('They left before dawn. Wren looked back once. I pretended not to see.','', 'position:absolute;left:250px;width:580px;bottom:-140px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L16">{img('r11','full')}
    {narr('That left the hardest part. Teaching a hundred and twelve people how to be weak.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:330px">{img('r12','', 'width:720px;height:1080px')}
    {bub('Right. A Measurer is watching you. You lift a sack of grain. Go.','L17', 'right','position:absolute;left:-300px;top:860px;width:380px')}
    {sfx('HUP!','left:420px;top:40px;transform:rotate(8deg);font-size:72px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('r13','', 'width:660px;height:660px')}
    {bub("No. No! You're a one-ring farmer. That sack is heavy. Drop it. Slower. Now groan.",'L18', 'left','position:absolute;right:-380px;top:-40px;width:420px')}
    {bub('Ugh?','L19', 'left','position:absolute;right:-240px;top:380px;width:180px')}
    {bub('Like you mean it.','L20', 'left','position:absolute;right:-300px;top:540px;width:280px')}
  </div>
  {gap(200)}
  <div class="rel">{img('r14','full')}
    {bub('Granny. Please. Miss the log. At least once.','L21', 'up','position:absolute;right:30px;bottom:-200px;width:400px')}
    {bub("I'm eighty-one, Sir Oswin. I don't miss.",'L22', 'up','position:absolute;left:30px;bottom:-310px;width:380px')}
    {sfx('THWACK!','left:40px;top:40px;transform:rotate(-8deg);font-size:76px')}
  </div>
  {gap(400)}
  <div class="rel" data-a="L23">{img('r15','full')}
    {narr("The children were the worst. Children can't pretend to be anything. They just run, very fast, and laugh.",'', 'position:absolute;left:220px;width:640px;bottom:-180px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:330px">{img('r16','', 'width:720px;height:1080px')}
    {bub('You realise this is the most ridiculous thing I have ever seen.','L24', 'right','position:absolute;left:-300px;top:40px;width:400px')}
    {bub('Yes. Is it working?','L25', 'right','position:absolute;left:-280px;top:620px;width:300px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('r17','', 'width:660px;height:660px')}
    {bub('On a lens? Perhaps. On Hask?','L26', 'left','position:absolute;right:-320px;top:120px;width:320px')}
    {bub("Who's Hask?",'L27', 'left','position:absolute;right:-260px;top:440px;width:220px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('r18','', 'width:720px;height:1080px')}
    {bub('My teacher. The finest Measurer in Aldmere. If he is one of those twelve, my lord, no amount of smoke will save us.','L28', 'right','position:absolute;left:-300px;top:760px;width:440px')}
  </div>
  {gap(260, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  <div class="rel" data-a="L29">{img('r19','full')}
    {narr("That night, every doorway in Greyhollow glowed with one of Tobin's lanterns, and the whole village sat inside its own small cloud.",'', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L30">{img('r20','full')}
    {narr('And on the south road, twelve lights of a different kind came over the hill.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L31" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 17 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
