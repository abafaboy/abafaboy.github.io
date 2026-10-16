"""Chapter 9 layout."""
FACES = {
    "k02": [(290, 50, 470, 260), (1000, 250, 1180, 400)],
    "k04": [(470, 140, 650, 330)],
    "k05": [(190, 140, 380, 360), (860, 50, 1050, 260)],
    "k06": [(220, 30, 820, 640)],
    "k07": [(230, 70, 420, 300)],
    "k09": [(40, 120, 1150, 560)],
    "k10": [(200, 0, 720, 560)],
    "k11": [(260, 160, 600, 360), (700, 20, 900, 260)],
    "k12": [(330, 30, 520, 240), (930, 20, 1120, 230)],
    "k13": [(170, 10, 640, 520)],
    "k14": [(250, 200, 1300, 480)],
    "k15": [(50, 160, 1450, 520)],
    "k16": [(800, 60, 980, 250), (1080, 140, 1250, 330)],
    "k17": [(220, 50, 640, 560)],
    "k18": [(220, 0, 900, 700)],
    "k19": [(500, 60, 640, 200)],
    "k20": [(320, 340, 520, 560), (680, 40, 860, 240)],
    "k22": [(270, 60, 600, 440)],
    "k23": [(160, 20, 820, 720)],
    "k24": [(0, 30, 1536, 560)],
    "k26": [(200, 0, 820, 700)],
    "k27": [(300, 60, 760, 560)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 9</div><div class="c2">Strays</div></div>
  {gap(100)}
  {narr('Spring came to Greyhollow three weeks early. Nobody in the village could remember that happening before.','L0', 'margin:0 140px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('k01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1">{img('k02','full')}
    {narr("The debt was paid. The glasshouses were full. Tobin's lamps were selling in three cities. For the first time in its history, Greyhollow had money.",'', 'position:absolute;left:250px;width:580px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L2" style="margin-left:210px">{img('k03','', 'width:660px;height:660px')}
    {narr('So, naturally, everyone wanted some.','', 'position:absolute;left:-170px;top:-80px;width:400px')}
  </div>
  {gap(170)}
  <div class="rel" style="margin-left:0">{img('k04','', 'width:720px;height:1080px')}
    {bub("My lord! Vaskan merchants want rimeglass. Southern lords want rimeglass. A bishop has written asking for rimeglass candles. I don't know what that means, but he's offering a fortune.",'L3', 'left','position:absolute;right:-340px;top:400px;width:590px')}
  </div>
  {gap(200)}
  <div class="rel">{img('k05','full')}
    {bub("Tobin can make two lamps a week. That's the limit.",'L4', 'up','position:absolute;left:40px;bottom:-170px;width:400px')}
    {bub('Then hire more blacksmiths!','L5', 'up','position:absolute;right:40px;bottom:-280px;width:340px')}
  </div>
  {gap(350)}
  <div class="rel" style="margin-left:300px">{img('k06','', 'width:660px;height:660px')}
    {bub('There are no more blacksmiths. There are thirty-seven people, and one of them is nine.','L6', 'up','position:absolute;left:-270px;bottom:-230px;width:470px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L7">{img('k07','full')}
    {narr('That was the real problem. Greyhollow was too small. We needed people.','', 'position:absolute;right:30px;width:480px;bottom:-140px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L8">{img('k08','full')}
    {narr('As it turned out, people needed us too.','', 'position:absolute;left:30px;top:-60px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L9">{img('k09','full')}
    {narr('They started arriving in the second week of spring. Families from burned villages in the east. Runaway serfs. A miller whose lord had taken his mill. All of them had heard the same rumour.','', 'position:absolute;left:220px;width:640px;bottom:-230px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:300px">{img('k10','', 'width:660px;height:660px')}
    {bub('They say the lord of Greyhollow feeds everyone. They say nobody here goes cold.','L10', 'right','position:absolute;left:-290px;bottom:40px;width:380px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:330px">{img('k11','', 'width:720px;height:1080px')}
    {bub('My lord, there are forty more at the gate. Do we turn them away?','L11', 'right','position:absolute;left:-310px;top:520px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel">{img('k12','full')}
    {bub('Do we have food?','L12', 'up','position:absolute;left:40px;bottom:-140px;width:300px')}
    {bub('With the glasshouses? For a hundred more, easily.','L13', 'up','position:absolute;right:40px;bottom:-260px;width:400px')}
  </div>
  {gap(330)}
  <div class="rel" style="margin-left:300px">{img('k13','', 'width:660px;height:660px')}
    {bub('Then open the gate.','L14', 'right','position:absolute;left:-270px;top:-60px;width:320px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L15">{img('k14','full')}
    {narr('By midspring, Greyhollow had a hundred and twelve people. We built twenty new houses. Tobin took four apprentices. Wren taught archery to anyone who would hold a bow.','', 'position:absolute;left:220px;width:640px;bottom:-220px')}
  </div>
  {gap(290)}
  <div class="rel" data-a="L16">{img('k15','full')}
    {narr("And every one of them, within a month, was healthier than they'd ever been in their lives. Good food, I thought. Fresh air. Honest work.",'', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel">{img('k16','full')}
    {bub('Your lord collects people the way a fire collects moths, Steward.','L17', 'up','position:absolute;right:30px;bottom:-200px;width:420px')}
    {bub('He collects strays. Always has. Look at me.','L18', 'up','position:absolute;left:40px;bottom:-330px;width:380px')}
  </div>
  {gap(400)}
  <div class="rel" style="margin-left:0">{img('k17','', 'width:660px;height:660px')}
    {bub("I'm meant to send my report to the capital by the end of spring.",'L19', 'left','position:absolute;right:-380px;top:60px;width:420px')}
    {bub('And will you?','L20', 'left','position:absolute;right:-330px;top:440px;width:300px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('k18','', 'width:660px;height:660px')}
    {bub("I haven't decided.",'L21', 'up','position:absolute;left:-270px;bottom:-140px;width:320px')}
  </div>
  {gap(250)}
  <div class="rel" data-a="L22">{img('k19','full')}
    {narr("And then, one morning, a rider came from the south, wearing my father's colours.",'', 'position:absolute;left:30px;width:480px;bottom:-140px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:330px">{img('k20','', 'width:720px;height:1080px')}
    {bub('A letter for Lord Lucan, from Lord Varr.','L23', 'right','position:absolute;left:-310px;top:620px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L24" style="margin-left:210px">{img('k21','', 'width:660px;height:660px')}
    {narr("I knew my father's handwriting. Short. Cold. Exactly four lines.",'', 'position:absolute;left:-170px;width:420px;bottom:-120px')}
  </div>
  {gap(220, 'linear-gradient(#fff,#1a1210)')}
</div>
<div class="sec night" style="background:#1a1210">
  <div class="rel" style="margin-left:330px">{img('k22','', 'width:720px;height:1080px')}
    {narr('House Corrow has crossed the River Senn with two thousand men. Maric marches to meet them. Every vassal of House Varr is summoned. Bring your levy.','L25', 'position:absolute;left:-310px;top:560px;width:470px')}
  </div>
  {gap(220, 'linear-gradient(#1a1210,#fff)')}
</div>
<div class="sec white">
  <div class="rel" style="margin-left:300px">{img('k23','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr("My levy. My father was calling up Greyhollow's soldiers. A hundred and twelve farmers, a third of them children.",'L26', 'margin:0 140px')}
  {gap(130)}
  <div class="rel" data-a="L27">{img('k24','full', 'filter:sepia(.4) saturate(.7)')}
    {narr('He meant it as a formality. A joke, probably. Nobody expected the zero to bring anyone at all.','', 'position:absolute;left:250px;width:580px;bottom:-160px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L28">{img('k25','full')}
    {narr("I looked out of the window. At Wren, drilling thirty archers in the yard. At Tobin's forge, glowing blue. At Oswin, teaching sword drills to men who had been serfs a month ago.",'', 'position:absolute;left:220px;width:640px;bottom:-220px')}
  </div>
  {gap(290)}
  <div class="rel" style="margin-left:300px">{img('k26','', 'width:660px;height:660px')}
    {bub('Bram. How many of ours can fight?','L29', 'up','position:absolute;left:-270px;bottom:-160px;width:380px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:0">{img('k27','', 'width:720px;height:1080px')}
    {bub('All of them, my lord. All of them.','L30', 'left','position:absolute;right:-320px;top:620px;width:380px')}
  </div>
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L31" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 10 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
