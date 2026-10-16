"""Chapter 7 layout."""
FACES = {
    "i01": [(1180, 0, 1380, 180)],
    "i05": [(700, 520, 790, 610)],
    "i06": [(520, 100, 690, 300), (840, 180, 960, 320)],
    "i07": [(290, 50, 450, 230), (1050, 30, 1220, 230), (0, 120, 110, 260), (1350, 160, 1536, 330)],
    "i09": [(160, 0, 760, 760)],
    "i10": [(340, 50, 540, 270), (60, 230, 220, 370), (760, 280, 920, 420)],
    "i12": [(120, 0, 920, 760)],
    "i13": [(170, 120, 380, 330), (560, 80, 760, 300)],
    "i14": [(200, 0, 780, 640)],
    "i15": [(320, 150, 1500, 400)],
    "i16": [(170, 120, 460, 420), (440, 30, 760, 420)],
    "i17": [(1100, 380, 1250, 560)],
    "i18": [(0, 0, 1536, 520)],
    "i19": [(330, 130, 500, 320)],
    "i20": [(240, 0, 860, 640)],
    "i21": [(0, 120, 920, 860)],
    "i22": [(80, 30, 250, 220), (440, 160, 960, 360)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 7</div><div class="c2">First Thaw</div></div>
  {gap(100)}
  {narr('The lamps were finished in the last week of winter. Twenty-one, in fact. Tobin made an extra one, for luck.','L0', 'margin:0 140px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('i01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1" style="margin-left:210px">{img('i02','', 'width:660px;height:660px')}
    {narr("Pell's sleigh came and went. Four thousand two hundred crowns, in gold and Vaskan notes, locked in a chest in my bedroom. Ash slept on top of it.",'', 'position:absolute;left:-170px;width:500px;bottom:-220px')}
    {sfx('zzz...','left:470px;top:80px;transform:rotate(-8deg);font-size:60px', 'quiet')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L2">{img('i03','full')}
    {narr('The snow began to soften. Then the river ice cracked. First thaw.','', 'position:absolute;left:30px;width:480px;bottom:-140px')}
    {sfx('KRRRK','left:700px;top:520px;transform:rotate(-6deg);font-size:76px')}
  </div>
  {gap(220)}
  <div class="rel" data-a="L3" style="margin-left:300px">{img('i04','', 'width:660px;height:660px')}
    {narr('And with it, House Corrow.','', 'position:absolute;left:-270px;top:260px;width:360px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L4">{img('i05','full')}
    {narr('Thirty riders came up the north road, with crows on their banners. And at their head, a thin man with a thin smile.','', 'position:absolute;left:250px;width:580px;bottom:-170px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:0">{img('i06','', 'width:720px;height:1080px')}
    {bub("Lord Lucan Varr? I am Steward Corvin, of House Corrow. I'm here to collect a debt. Or, failing that, to collect Greyhollow.",'L5', 'left','position:absolute;right:-340px;top:260px;width:480px')}
  </div>
  {gap(200)}
  <div class="rel">{img('i07','full')}
    {bub("Four thousand crowns, due at first thaw. It's all here. Count it.",'L6', 'up','position:absolute;left:150px;bottom:-200px;width:440px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L7" style="margin-left:210px">{img('i08','', 'width:660px;height:660px')}
    {narr('He counted it. Slowly. Every coin. Then his smile grew wider.','', 'position:absolute;left:-170px;width:440px;bottom:-130px')}
    {sfx('clink... clink...','left:300px;top:30px;transform:rotate(-6deg);font-size:50px', 'quiet')}
  </div>
  {gap(230)}
  <div class="rel" style="margin-left:300px">{img('i09','', 'width:660px;height:660px')}
    {bub('Four thousand crowns. Excellent. And the interest?','L8', 'right','position:absolute;left:-285px;bottom:60px;width:350px')}
  </div>
  {gap(40)}
  {bub('What interest?','L9', 'up','position:relative;margin-left:80px;width:300px')}
  {gap(100)}
  <div class="rel" style="margin-left:330px">{img('i10','', 'width:720px;height:1080px')}
    {bub('Clause nine. Interest at twenty parts in a hundred, added every season. You owe eight thousand, my lord.','L10', 'right','position:absolute;left:-310px;top:460px;width:460px')}
  </div>
  {gap(200)}
  <div class="rel" data-a="L11" style="margin-left:210px">{img('i11','', 'width:660px;height:660px')}
    {narr('He held up the contract. The ink of clause nine was a little darker than the rest.','', 'position:absolute;left:-170px;width:460px;bottom:-140px')}
  </div>
  {gap(230)}
  <div class="rel" data-a="L12" style="margin-left:300px">{img('i12','', 'width:660px;height:660px')}
    {narr('I had read that contract a hundred times on the road north. There was no clause nine.','', 'position:absolute;left:-270px;width:440px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('i13','', 'width:720px;height:1080px')}
    {bub("That clause is a forgery. The ink is fresh. Your scribe didn't even match the hand.",'L13', 'right','position:absolute;left:-310px;top:420px;width:440px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('i14','', 'width:660px;height:660px')}
    {bub('A serious accusation, from a boy with no rings. Who will the court believe? House Corrow, or the zero of House Varr?','L14', 'up','position:absolute;left:-270px;bottom:-250px;width:480px')}
  </div>
  {gap(320)}
  <div class="rel" data-a="L15">{img('i15','full')}
    {narr("Behind him, thirty riders put their hands on their swords. Not Corrow men. Sellswords, paid to do what a lord's own men can't be seen doing.",'', 'position:absolute;left:250px;width:580px;bottom:-200px')}
    {sfx('shk','left:20px;top:20px;transform:rotate(-6deg);font-size:60px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:210px">{img('i16','', 'width:660px;height:660px')}
    {bub('My lord. Thirty sellswords. Professionals. We have thirty-seven farmers.','L16', 'up','position:absolute;left:-170px;bottom:-200px;width:430px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L17">{img('i17','full')}
    {narr('I looked at my farmers. Tobin, with his hammer. Wren, with her bow. Bram, with his one arm and his old sword. And Ash, the size of a horse, showing his teeth.','', 'position:absolute;left:250px;width:580px;bottom:-210px')}
  </div>
  {gap(290)}
  <div class="rel" data-a="L18">{img('i18','full')}
    {narr("I didn't know then what I know now. But I remember thinking, very clearly: they don't look like farmers anymore.",'', 'position:absolute;left:250px;width:580px;bottom:-180px')}
  </div>
  {gap(260)}
  <div class="rel" style="margin-left:0">{img('i19','', 'width:720px;height:1080px')}
    {bub("Steward Corvin. You have your four thousand crowns. Take them, and leave my land.",'L19', 'left','position:absolute;right:-330px;top:120px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('i20','', 'width:660px;height:660px')}
    {bub('Or what?','L20', 'right','position:absolute;left:-230px;bottom:120px;width:240px')}
  </div>
  {gap(170)}
  <div class="rel" style="margin-left:210px">{img('i21','', 'width:660px;height:660px')}
    {bub('Or I find out what thirty-seven farmers can do.','L21', 'up','position:absolute;left:-170px;bottom:-200px;width:420px')}
  </div>
  {gap(280)}
  <div class="rel">{img('i22','full')}
    {bub('Kill the dog first.','L22', 'up','position:absolute;left:40px;bottom:-140px;width:340px')}
    {sfx('SHING!','left:560px;top:590px;transform:rotate(-8deg);font-size:80px')}
  </div>
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L23" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 8 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
