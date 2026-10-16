"""Chapter 11 layout."""
FACES = {
    "m01": [(300, 30, 500, 230), (920, 30, 1110, 240)],
    "m03": [(320, 0, 860, 640)],
    "m04": [(250, 40, 760, 600)],
    "m05": [(280, 140, 420, 290), (1120, 120, 1260, 280)],
    "m06": [(400, 50, 640, 320)],
    "m07": [(0, 0, 1024, 1024)],
    "m08": [(250, 260, 1350, 600)],
    "m10": [(300, 100, 720, 520)],
    "m11": [(360, 290, 520, 440), (1060, 300, 1200, 440)],
    "m12": [(140, 80, 340, 290)],
    "m13": [(80, 30, 360, 330), (500, 120, 700, 330)],
    "m14": [(0, 140, 1000, 560)],
    "m17": [(240, 210, 560, 520)],
    "m19": [(260, 70, 480, 300)],
    "m20": [(260, 20, 760, 560)],
    "m21": [(150, 30, 920, 860)],
    "m22": [(260, 20, 640, 400)],
    "m24": [(300, 60, 530, 300)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 11</div><div class="c2">Turnips and Bridges</div></div>
  {gap(100)}
  {narr('I told my father everything. The grain. The supply road. And the river.','L0', 'margin:0 180px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('m01','full')}</div>
  {gap(150)}
  <div class="rel">{img('m02','full')}
    {bub("Corrow's army is camped on the low meadow, on the far bank. Their supply road runs along the river, below the old Senn weir. If the weir were opened at night, the meadow would flood to the knee. The road would be mud for a week.",'L1', 'up','position:absolute;left:100px;bottom:-330px;width:660px')}
  </div>
  {gap(440)}
  <div class="rel" style="margin-left:300px">{img('m03','', 'width:660px;height:660px')}
    {bub('And how would you open a stone weir, under the eyes of two thousand men?','L2', 'right','position:absolute;left:-280px;top:-90px;width:420px')}
  </div>
  {gap(40)}
  {bub('Quietly. With a blacksmith who knows how sluice gates work.','L3', 'up','position:relative;margin-left:60px;width:440px')}
  {gap(140)}
  <div class="rel" style="margin-left:300px">{img('m04','', 'width:660px;height:660px')}
    {bub('You read that in a book, I suppose.','L4', 'right','position:absolute;left:-270px;top:-80px;width:340px')}
    {bub('Chapter fourteen. Drainage of Lowland Fields. Very dry. Excellent diagrams.','L5', 'up','position:absolute;left:-270px;bottom:-210px;width:430px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L6">{img('m05','full')}
    {narr('My father was quiet for a long time.','', 'position:absolute;left:340px;right:340px;bottom:-110px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:330px">{img('m06','', 'width:720px;height:1080px')}
    {bub('Your brother plans to charge the ford at dawn, the day after tomorrow.','L7', 'right','position:absolute;left:-300px;top:380px;width:420px')}
    {bub("Into two thousand men on solid ground? He'll lose half his knights.",'L8', 'up','position:absolute;left:-300px;top:800px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('m07','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {bub('Then you have one night.','L9', 'up','position:relative;margin-left:420px;width:340px')}
  {gap(130, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {narr('We went the next night. Tobin, Wren, Oswin, twelve of ours, and Ash. No torches. No armour. Just rope, crowbars, and the dark.','L10', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L10b">{img('m08','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L11">{img('m09','full')}
    {narr('The weir was guarded by four Corrow sentries, half asleep around a fire.','', 'position:absolute;left:250px;width:580px;bottom:-140px')}
  </div>
  {gap(230)}
  <div class="rel" style="margin-left:300px">{img('m10','', 'width:660px;height:660px')}
    {bub('Four. I can drop them before they shout.','L12', 'right','position:absolute;left:-270px;top:-60px;width:350px')}
    {bub('No killing, Wren. Not if we can help it.','L13', 'up','position:absolute;left:-270px;bottom:-150px;width:380px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L14">{img('m11','full')}
    {narr('So Ash walked out of the dark and sat down beside their fire.','', 'position:absolute;left:250px;width:580px;bottom:-130px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L15">{img('m12','full')}
    {narr("All four sentries ran. I don't think they stopped until morning.",'', 'position:absolute;right:30px;width:480px;bottom:-130px')}
    {sfx('AAAAH!!','left:560px;top:30px;transform:rotate(-6deg);font-size:84px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:330px">{img('m13','', 'width:720px;height:1080px')}
    {bub("These gates haven't moved in twenty years, my lord. Rusted solid.",'L16', 'right','position:absolute;left:-300px;top:400px;width:400px')}
    {bub('Then we unrust them. Together. Heave!','L17', 'right','position:absolute;left:-290px;top:760px;width:360px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L18">{img('m14','full')}
    {narr('Twelve farmers, a knight and a blacksmith pulled on those ropes. Iron screamed. Stone cracked. And the old Senn weir opened for the first time in twenty years.','', 'position:absolute;left:220px;width:640px;bottom:-210px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L19">{img('m15','full')}
    {narr('The river roared through like a living thing.','', 'position:absolute;left:30px;top:-60px;width:440px')}
    {sfx('ROOOAAR','left:520px;top:580px;transform:rotate(-6deg);font-size:90px')}
  </div>
  {gap(260, 'linear-gradient(#0b0d16,#c9cfdc)')}
</div>
<div class="sec white" style="background:#c9cfdc">
  <div class="rel" data-a="L20">{img('m16','full')}
    {narr('By dawn, the Corrow camp was standing in water to the knee. Tents collapsed. Wagons sank. Their supply road had vanished under a brown lake.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(270)}
  <div class="rel" style="margin-left:330px">{img('m17','', 'width:720px;height:1080px')}
    {bub("The meadow's flooding! Move the wagons! Move them!",'L21', 'right','position:absolute;left:-300px;top:120px;width:380px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L22">{img('m18','full')}
    {narr('And on our side of the river, the ford was narrower, shallower, and easy to hold.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:0">{img('m19','', 'width:720px;height:1080px')}
    {bub('What is this? Who did this? I was going to charge at dawn!','L23', 'left','position:absolute;right:-330px;top:80px;width:400px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:300px">{img('m20','', 'width:660px;height:660px')}
    {bub('Your brother did it. With a book.','L24', 'right','position:absolute;left:-270px;bottom:80px;width:340px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L25" style="margin-left:0">{img('m21','', 'width:660px;height:660px')}
    {narr("I'll never forget Maric's face. Not angry. Just confused, as if the world had stopped making sense.",'', 'position:absolute;right:-380px;width:400px;top:180px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L26" style="margin-left:300px">{img('m22','', 'width:660px;height:660px')}
    {narr("I knew the feeling. I'd been having it all winter.",'', 'position:absolute;left:-270px;width:400px;bottom:-110px')}
  </div>
  {gap(230)}
  <div class="rel" data-a="L27">{img('m23','full')}
    {narr('Corrow held out for six days, with no road and no food. On the seventh, they sent a rider with a white flag.','', 'position:absolute;left:250px;width:580px;bottom:-160px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L28" style="margin-left:0">{img('m24','', 'width:720px;height:1080px')}
    {narr('But across the river, behind the white flag, one figure stood apart. A woman in violet, watching our camp. Watching me.','', 'position:absolute;right:-330px;width:420px;top:520px')}
  </div>
  {gap(320, 'linear-gradient(#c9cfdc,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L29" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 12 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
