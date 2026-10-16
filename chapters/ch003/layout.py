"""Chapter 3 layout."""
FACES = {
    "e01": [(350, 40, 530, 250), (940, 120, 1090, 300)],
    "e02": [(300, 100, 520, 360)],
    "e03": [(330, 270, 560, 520)],
    "e04": [(830, 110, 1000, 300)],
    "e05": [(270, 90, 500, 380)],
    "e06": [(680, 190, 830, 360), (40, 380, 180, 530), (220, 420, 350, 560), (80, 670, 210, 800), (1090, 350, 1230, 500), (1190, 520, 1330, 670), (1350, 630, 1490, 770)],
    "e07": [(100, 40, 720, 640)],
    "e08": [(340, 120, 540, 360)],
    "e09": [(500, 380, 620, 520), (40, 250, 170, 380), (110, 430, 230, 560)],
    "e10": [(350, 170, 530, 360)],
    "e12": [(200, 0, 800, 640)],
    "e13": [(420, 40, 700, 360)],
    "e14": [(200, 110, 370, 320), (1060, 80, 1240, 300)],
    "e15": [(260, 0, 780, 640)],
    "e16": [(530, 200, 740, 440)],
    "e17": [(260, 30, 760, 560)],
    "e18": [(290, 100, 450, 290), (1030, 60, 1210, 260)],
    "e19": [(370, 110, 540, 310), (1240, 390, 1390, 560), (700, 280, 1100, 520)],
    "e20": [(340, 60, 500, 230), (1080, 50, 1240, 230)],
    "e21": [(500, 0, 900, 500)],
    "e23": [(390, 90, 600, 360)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 3</div><div class="c2">The Merchant from Vask</div></div>
  {gap(100)}
  {narr('A hundred frost-wolves. Ash could not hunt a hundred frost-wolves before first thaw. So I did what any reasonable lord would do. I asked the blacksmith.','L0', 'margin:0 90px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('e01','full')}</div>
  {gap(180)}
  <div class="rel" style="margin-left:300px">{img('e02','', 'width:720px;height:1080px')}
    {bub("Raw rimeglass is worth forty crowns, my lord. Worked, it's worth five times that. Lamps, forge-hearts, wards. Southern lords pay anything to stay warm.",'L1', 'right','position:absolute;left:-290px;top:420px;width:500px')}
    {bub('Can you work it?','L2', 'up','position:absolute;left:-250px;bottom:-120px;width:320px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('e03','', 'width:660px;height:660px')}
    {bub("My grandfather could. I've got his notes. Somewhere. Under the goats.",'L3', 'up','position:absolute;right:-170px;bottom:-200px;width:440px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L4">{img('e04','full')}
    {narr("The notes were under the goats. Tobin spent three days and nights at the forge. Nobody told him to sleep. He didn't seem to need it.",'', 'position:absolute;left:30px;width:560px;bottom:-190px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:330px">{img('e05','', 'width:720px;height:1080px')}
    {narr('On the fourth morning he brought me a lamp. A small iron cage with a sliver of rimeglass inside, glowing a steady, gentle blue.','L5', 'position:absolute;left:-310px;top:420px;width:470px')}
    {bub("It'll burn for a year. No oil. No smoke.",'L6', 'up','position:absolute;left:-280px;bottom:-130px;width:420px')}
  </div>
  {gap(220)}
  {narr('I held it up, and the whole hall filled with soft light. Thirty-seven people, crowded inside, went quiet.','L7', 'margin:0 140px')}
  {gap(40)}
  <div class="rel" data-a="L7b">{img('e06','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('e07','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {narr("That's when I understood. We didn't need a hundred wolves. We needed a buyer.",'L8', 'margin:0 170px')}
  {gap(120)}
  <div class="rel" style="margin-left:330px">{img('e08','', 'width:720px;height:1080px')}
    {bub("There's a trader who comes north each winter, my lord. From Vask, across the eastern sea. Sharp as a knife, and twice as honest. Which isn't saying much.",'L9', 'right','position:absolute;left:-300px;top:460px;width:500px')}
  </div>
  {gap(200)}
  {narr('He arrived a week later, in a sleigh painted teal and gold.','L10', 'margin:0 200px')}
  {gap(40)}
  <div class="rel" data-a="L10b">{img('e09','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:0">{img('e10','', 'width:720px;height:1080px')}
    {bub('Pell Marrow, of the Free City of Vask. Buyer of furs, seller of everything else. And you must be the lord who measured zero.','L11', 'left','position:absolute;right:-340px;top:60px;width:500px')}
    {bub('News travels.','L12', 'left','position:absolute;right:-300px;top:540px;width:300px')}
    {bub('News is my second-best product. So. What have you got for me?','L13', 'left','position:absolute;right:-340px;top:760px;width:430px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L14" style="margin-left:210px">{img('e11','', 'width:660px;height:660px')}
    {narr('I put the lamp on the table.','', 'position:absolute;left:-170px;top:-80px;width:400px')}
  </div>
  {gap(180)}
  {narr('For a long moment, Pell Marrow said nothing at all.','L15', 'margin:0 200px')}
  {gap(40)}
  <div class="rel" data-a="L15b" style="margin-left:300px">{img('e12','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {bub('Worked rimeglass. In Greyhollow. Who made this?','L16', 'up','position:relative;margin-left:520px;width:440px')}
  {gap(60)}
  <div class="rel" style="margin-left:300px">{img('e13','', 'width:660px;height:660px')}
    {bub('Me.','L17', 'right','position:absolute;left:-230px;top:330px;width:210px')}
  </div>
  {gap(200)}
  <div class="rel">{img('e14','full')}
    {bub("I'll give you sixty crowns for it.",'L18', 'up','position:absolute;right:40px;bottom:-170px;width:400px')}
    {bub('Corrow merchants in the capital sell these for three hundred.','L19', 'up','position:absolute;left:30px;bottom:-330px;width:440px')}
  </div>
  {gap(400)}
  <div class="rel" style="margin-left:300px">{img('e15','', 'width:660px;height:660px')}
    {bub("You've done your reading.",'L20', 'right','position:absolute;left:-270px;top:40px;width:330px')}
  </div>
  {gap(40)}
  {bub("Chapter four of A Merchant's Guide to Southern Markets. Very dry. Excellent price tables.",'L21', 'up','position:relative;margin-left:60px;width:520px')}
  {gap(120)}
  <div class="rel" style="margin-left:60px">{img('e16','', 'width:720px;height:1080px')}
    {bub('Two hundred. And I take every lamp you can make before the spring ships sail.','L22', 'left','position:absolute;right:-290px;top:60px;width:460px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('e17','', 'width:660px;height:660px')}
    {narr('Two hundred crowns a lamp. Twenty lamps, and the debt was paid.','L23', 'position:absolute;left:-280px;top:-130px;width:410px')}
    {bub('Deal.','L24', 'up','position:absolute;left:-230px;bottom:-60px;width:220px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L25">{img('e18','full')}
    {narr("We shook hands. His grip was warm. Warmer than it should have been, he said later, for a man who'd spent six days in a sleigh.",'', 'position:absolute;left:250px;width:580px;bottom:-200px')}
  </div>
  {gap(260)}
  {narr('That night, the village celebrated. Bram even smiled, though he would deny it.','L26', 'margin:0 160px')}
  {gap(40)}
  <div class="rel" data-a="L26b">{img('e19','full')}</div>
  {gap(150)}
  {narr("I didn't notice Pell watching the villagers. Watching Wren split a log with one swing. Watching an old woman carry two full water barrels as if they were empty.",'L27', 'margin:0 90px')}
  {gap(40)}
  <div class="rel" data-a="L27b">{img('e20','full')}
    {sfx('CRACK!','left:420px;top:560px;transform:rotate(-8deg);font-size:80px')}
  </div>
  {gap(150)}
  <div class="rel" style="margin-left:300px">{img('e21','', 'width:660px;height:660px')}
    {bub('Interesting place, Greyhollow.','L28', 'right','position:absolute;left:-270px;bottom:120px;width:350px')}
  </div>
  {gap(300, 'linear-gradient(#fff,#2a1d1a)')}
</div>
<div class="sec night" style="background:#2a1d1a">
  {narr('And far to the south, in a house that wanted our river, a letter arrived.','L29', 'margin:0 160px')}
  {gap(40)}
  <div class="rel" data-a="L29b">{img('e22','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:330px">{img('e23','', 'width:720px;height:1080px')}
    {bub('Greyhollow is selling rimeglass? Then the boy might actually pay us.','L30', 'right','position:absolute;left:-310px;top:460px;width:440px')}
    {bub("We can't have that.",'L31', 'right','position:absolute;left:-290px;top:800px;width:330px')}
  </div>
  {gap(320, 'linear-gradient(#2a1d1a,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L32" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 4 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
