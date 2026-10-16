"""Chapter 6 layout."""
FACES = {
    "h02": [(250, 200, 450, 430)],
    "h04": [(520, 300, 740, 540)],
    "h05": [(300, 80, 470, 280), (990, 50, 1150, 240), (0, 350, 120, 500)],
    "h07": [(200, 250, 400, 460)],
    "h08": [(210, 120, 390, 310)],
    "h09": [(100, 30, 430, 410)],
    "h10": [(360, 0, 820, 500)],
    "h12": [(1040, 540, 1200, 720)],
    "h13": [(420, 60, 600, 260), (220, 480, 380, 640)],
    "h14": [(520, 90, 680, 270)],
    "h15": [(150, 120, 1400, 420)],
    "h17": [(180, 0, 640, 560)],
    "h18": [(500, 330, 780, 620)],
    "h19": [(520, 80, 680, 270), (1130, 300, 1290, 460)],
    "h20": [(260, 170, 450, 400), (700, 640, 920, 860)],
    "h21": [(180, 100, 730, 740)],
    "h22": [(0, 0, 1024, 1024)],
}

def build():
    return f"""
<div class="sec night">
  <div class="chap" style="color:#e8e2d0"><div class="c0" style="color:#e8e2d0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 6</div><div class="c2">The Longest Night</div></div>
  {gap(100)}
  {narr('Midwinter came. The sun barely rose. And on the longest night of the year, the wolves came out of the Pale.','L0', 'margin:0 130px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('h01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:330px">{img('h02','', 'width:720px;height:1080px')}
    {bub('Lord Lucan! Wolves on the ridge! Not one or two. A pack. Twenty, maybe more!','L1', 'right','position:absolute;left:-300px;top:520px;width:440px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L2">{img('h03','full')}
    {narr("Frost-wolves only hunt in packs when they're starving. Something in the Pale had driven them south. Toward us.",'', 'position:absolute;left:30px;width:540px;bottom:-180px')}
    {sfx('AWOOOO...','left:640px;top:520px;transform:rotate(-6deg);font-size:70px', 'quiet')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:0">{img('h04','', 'width:720px;height:1080px')}
    {bub('Everyone who can hold a spear, to the palisade! Everyone else, into the keep!','L3', 'left','position:absolute;right:-330px;top:120px;width:420px')}
  </div>
  {gap(180)}
  {narr("I couldn't fight. So I did the only useful thing I could. I counted, and I gave orders.",'L4', 'margin:0 150px')}
  {gap(40)}
  <div class="rel">{img('h05','full')}
    {bub("Tobin, the lamps! Hang them on the wall, frost-wolves hate the light. Wren, archers on the gatehouse. Bram, the barn. They'll go for the goats first.",'L5', 'up','position:absolute;left:150px;bottom:-280px;width:560px')}
  </div>
  {gap(450)}
  <div class="rel" data-a="L6">{img('h06','full')}
    {narr('They hit the palisade like a white wave.','', 'position:absolute;left:30px;top:-70px;width:440px')}
    {sfx('CRASH!!','left:520px;top:540px;transform:rotate(-8deg);font-size:100px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L7" style="margin-left:330px">{img('h07','', 'width:720px;height:1080px')}
    {narr("Wren's first arrow killed the lead wolf at a hundred paces. Her second went through two.",'', 'position:absolute;left:-300px;top:620px;width:440px')}
    {sfx('SHHK!','left:420px;top:60px;transform:rotate(-10deg);font-size:70px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L8">{img('h08','full')}
    {narr('Tobin swung his hammer, and a wolf the size of a pony flew backwards over the wall.','', 'position:absolute;right:30px;width:500px;bottom:-160px')}
    {sfx('BWAMM!','left:460px;top:30px;transform:rotate(-8deg);font-size:90px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:300px">{img('h09','', 'width:660px;height:660px')}
    {bub('Hold the line! Hold it! By the gods. Where did you people learn to fight like knights?','L9', 'up','position:absolute;left:-270px;bottom:-220px;width:470px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:210px">{img('h10','', 'width:660px;height:660px')}
    {bub('Morale!','L10', 'right','position:absolute;left:-190px;top:360px;width:240px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L11">{img('h11','full')}
    {narr('Ash took the biggest of them alone, at the gate. It was over in seconds.','', 'position:absolute;left:30px;width:480px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L12">{img('h12','full')}
    {narr('And then one got past the wall. It went for the youngest of the goatherds, a boy of nine.','', 'position:absolute;left:30px;width:500px;bottom:-160px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L13" style="margin-left:330px">{img('h13','', 'width:720px;height:1080px')}
    {narr('Bram got there first. One arm, one old sword, and fifty years of soldiering.','', 'position:absolute;left:-300px;top:620px;width:440px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L14">{img('h14','full')}
    {sfx('SHINGG!','left:520px;top:560px;transform:rotate(-8deg);font-size:90px')}
  </div>
  {gap(40)}
  {narr('He cut it down with a single stroke.','L14b', 'margin:0 280px')}
  {gap(280, 'linear-gradient(#0b0d16,#c9cfdc)')}
</div>
<div class="sec white" style="background:#c9cfdc">
  <div class="rel" data-a="L15">{img('h15','full')}
    {narr('By dawn, the wolves were gone. Nineteen dead in the snow. Not one of ours.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(230)}
  <div class="rel" data-a="L16" style="margin-left:210px">{img('h16','', 'width:660px;height:660px')}
    {narr('Nineteen frost-wolf hearts. Nineteen pieces of rimeglass. Seven hundred and sixty crowns, lying in the snow.','', 'position:absolute;left:-170px;width:500px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L17" style="margin-left:300px">{img('h17','', 'width:660px;height:660px')}
    {narr('I tried to laugh. Instead, I fell over.','', 'position:absolute;left:-270px;bottom:-110px;width:400px')}
  </div>
  {gap(260, 'linear-gradient(#c9cfdc,#1a1410)')}
</div>
<div class="sec night" style="background:#1a1410">
  <div class="rel" data-a="L18" style="margin-left:0">{img('h18','', 'width:720px;height:1080px')}
    {narr('I woke three days later, burning with fever, my fingertips white with frostbite, though I had never left the keep.','', 'position:absolute;right:-330px;width:440px;top:120px')}
  </div>
  {gap(180)}
  <div class="rel">{img('h19','full')}
    {bub('You collapsed on the wall, my lord. The healer says it was the cold.','L19', 'up','position:absolute;left:30px;bottom:-200px;width:440px')}
    {bub('Strange. I was wearing two cloaks.','L20', 'up','position:absolute;right:30px;bottom:-330px;width:380px')}
  </div>
  {gap(400)}
  <div class="rel" data-a="L21" style="margin-left:330px">{img('h20','', 'width:720px;height:1080px')}
    {narr("Beside my bed sat the scholar. She wasn't writing anything down this time. She was just looking at me.",'', 'position:absolute;left:-300px;top:40px;width:440px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('h21','', 'width:660px;height:660px')}
    {bub('Rest, my lord. You did a great deal of work that night.','L22', 'up','position:absolute;left:-270px;bottom:-200px;width:430px')}
  </div>
  {gap(240)}
  {bub('I only gave orders.','L23', 'up','position:relative;margin-left:600px;width:320px')}
  {gap(80)}
  <div class="rel" style="margin-left:210px">{img('h22','', 'width:660px;height:660px')}
    {bub("Yes. I suppose that's one word for it.",'L24', 'up','position:absolute;left:-180px;bottom:-250px;width:420px')}
  </div>
  {gap(320, 'linear-gradient(#1a1410,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L25" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 7 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
