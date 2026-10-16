"""Chapter 12 layout."""
FACES = {
    "n02": [(0, 100, 140, 260), (320, 110, 520, 330), (840, 110, 1000, 290), (1000, 130, 1200, 330), (1180, 80, 1380, 290)],
    "n03": [(390, 90, 600, 330), (1100, 90, 1290, 310)],
    "n04": [(300, 80, 720, 560)],
    "n06": [(380, 280, 620, 560)],
    "n07": [(120, 60, 840, 840)],
    "n08": [(350, 40, 600, 330)],
    "n10": [(380, 90, 580, 310), (0, 330, 120, 480)],
    "n11": [(220, 80, 450, 340)],
    "n12": [(500, 110, 620, 250), (920, 160, 1060, 300)],
    "n13": [(250, 40, 560, 400)],
    "n14": [(320, 0, 820, 620)],
    "n15": [(210, 140, 410, 360), (440, 120, 680, 380)],
    "n16": [(260, 60, 860, 760)],
    "n17": [(380, 120, 560, 300), (1040, 100, 1240, 320)],
    "n18": [(300, 100, 520, 330), (680, 200, 880, 420)],
    "n19": [(80, 0, 400, 320), (1050, 100, 1300, 400)],
    "n20": [(250, 0, 920, 700)],
    "n21": [(130, 500, 330, 700), (780, 0, 960, 200)],
    "n22": [(160, 150, 520, 520), (500, 30, 860, 460)],
    "n23": [(300, 280, 560, 560)],
    "n24": [(400, 340, 620, 580)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 12</div><div class="c2">The Price of Peace</div></div>
  {gap(100)}
  {narr('The peace talks were held in a white tent on a sandbar in the middle of the river. Neutral ground, they called it. It was mostly mud.','L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('n01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1">{img('n02','full')}
    {narr('My father sat on one side. Lady Sabine Corrow sat on the other. And I sat in the corner, where my father had told me to sit, and say nothing.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel">{img('n03','full')}
    {bub('House Corrow withdraws its claim to the River Senn. For one generation.','L2', 'up','position:absolute;right:30px;bottom:-200px;width:420px')}
    {bub('Forever. And reparations, for the villages you burned on our side of the river.','L3', 'up','position:absolute;left:30px;bottom:-350px;width:440px')}
  </div>
  {gap(450)}
  <div class="rel" style="margin-left:300px">{img('n04','', 'width:660px;height:660px')}
    {bub('Forever is a very long time, Lord Varr.','L4', 'right','position:absolute;left:-270px;top:-60px;width:340px')}
  </div>
  {gap(40)}
  {bub('So is starving. Your army has eaten its horses.','L5', 'up','position:relative;margin-left:60px;width:420px')}
  {gap(140)}
  <div class="rel" data-a="L6" style="margin-left:210px">{img('n05','', 'width:660px;height:660px')}
    {narr('She signed. Her hand did not shake once. Then she looked past my father, straight at me.','', 'position:absolute;left:-170px;width:450px;bottom:-140px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:330px">{img('n06','', 'width:720px;height:1080px')}
    {bub("The second son. The zero. I laughed at you once, in your father's hall. Do you remember?",'L7', 'right','position:absolute;left:-300px;top:80px;width:430px')}
    {bub('I remember.','L8', 'up','position:absolute;left:-270px;top:500px;width:280px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('n07','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {bub("I won't make that mistake twice.",'L9', 'up','position:relative;margin-left:420px;width:360px')}
  {gap(120)}
  <div class="rel" data-a="L10" style="margin-left:0">{img('n08','', 'width:660px;height:660px')}
    {narr('She smiled as she said it. It was the most frightening thing I saw in the whole war.','', 'position:absolute;right:-380px;width:400px;top:200px')}
  </div>
  {gap(240, 'linear-gradient(#fff,#1a1210)')}
</div>
<div class="sec night" style="background:#1a1210">
  <div class="rel" data-a="L11">{img('n09','full')}
    {narr('That evening, the camp celebrated. Every soldier, every knight, every lord. Except one.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:330px">{img('n10','', 'width:720px;height:1080px')}
    {bub('You! Little brother! You made a fool of me in front of the whole army!','L12', 'right','position:absolute;left:-300px;top:380px;width:400px')}
    {bub("I won your war, Maric. You're welcome.",'L13', 'up','position:absolute;left:-300px;top:820px;width:380px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:0">{img('n11','', 'width:720px;height:1080px')}
    {bub('You won nothing. You hid behind farmers and a ditch. A Varr settles honour with steel. I challenge you. Here. Now.','L14', 'left','position:absolute;right:-340px;top:420px;width:460px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L15">{img('n12','full')}
    {narr('The whole camp went quiet. A five-ring lord, challenging a zero to a duel. Everyone knew how that ended.','', 'position:absolute;left:250px;width:580px;bottom:-160px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('n13','', 'width:660px;height:660px')}
    {bub('The law allows a lord to name a champion. I name Sir Oswin Hale.','L16', 'right','position:absolute;left:-270px;top:-60px;width:400px')}
  </div>
  {gap(150)}
  <div class="rel" style="margin-left:0">{img('n14','', 'width:660px;height:660px')}
    {bub("A drunk? A disgraced drunk? Fine. I'll beat him first, and then you.",'L17', 'left','position:absolute;right:-380px;top:240px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('n15','', 'width:720px;height:1080px')}
    {bub('My lord. He has five rings. I have three. Or I had three, last time anyone checked.','L18', 'right','position:absolute;left:-300px;top:420px;width:420px')}
    {bub('When did anyone last check?','L19', 'up','position:absolute;left:-290px;top:800px;width:340px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('n16','', 'width:660px;height:660px')}
    {bub('...Before Greyhollow.','L20', 'up','position:absolute;left:-180px;bottom:-140px;width:320px')}
  </div>
  {gap(260)}
  <div class="rel" data-a="L21">{img('n17','full')}
    {narr('Maric attacked like a storm. Fire burst along his blade. Ember aether, the pride of House Varr. The first blow knocked Oswin back three paces.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
    {sfx('FWOOM!','left:20px;top:400px;transform:rotate(-6deg);font-size:80px')}
  </div>
  {gap(270)}
  <div class="rel" data-a="L22" style="margin-left:300px">{img('n18','', 'width:720px;height:720px')}
    {narr("The second blow didn't.",'', 'position:absolute;left:-270px;top:300px;width:340px')}
    {sfx('KLANG!','left:380px;top:620px;transform:rotate(-8deg);font-size:72px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L23">{img('n19','full')}
    {narr("Frost spread along Oswin's sword. Thick, white, and cold enough to hiss against my brother's fire.",'', 'position:absolute;left:250px;width:580px;bottom:-150px')}
    {sfx('HSSSS','left:30px;top:420px;transform:rotate(-6deg);font-size:64px', 'quiet')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('n20','', 'width:660px;height:660px')}
    {bub("Rime aether? At that strength? You're a three-ring nobody!",'L24', 'up','position:absolute;left:-270px;bottom:-200px;width:400px')}
  </div>
  {gap(260)}
  {bub('I was.','L25', 'up','position:relative;margin-left:620px;width:220px')}
  {gap(100)}
  <div class="rel" data-a="L26">{img('n21','full')}
    {narr('Three strokes later, my brother was flat on his back in the mud, with a frozen blade at his throat.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:210px">{img('n22','', 'width:660px;height:660px')}
    {bub('Now can I shoot him?','L27', 'up','position:absolute;left:-180px;bottom:-140px;width:320px')}
    {bub('Still no.','L28', 'up','position:absolute;right:-150px;bottom:-240px;width:240px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L29" style="margin-left:0">{img('n23','', 'width:720px;height:1080px')}
    {narr("Maric got up without a word. He didn't look at Oswin. He looked at me. And for the first time in my life, my brother looked afraid.",'', 'position:absolute;right:-330px;width:420px;top:420px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L30" style="margin-left:330px">{img('n24','', 'width:720px;height:1080px')}
    {narr("Behind the crowd, unnoticed, my father watched. He wasn't smiling. He looked like a man watching a storm come in from the sea.",'', 'position:absolute;left:-300px;top:620px;width:440px')}
  </div>
  {gap(320, 'linear-gradient(#1a1210,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L31" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 13 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
