"""Chapter 8 layout."""
FACES = {
    "j01": [(0, 0, 160, 120), (130, 40, 260, 170), (360, 230, 560, 400), (880, 160, 1030, 300), (1000, 200, 1140, 340), (1200, 210, 1340, 350)],
    "j03": [(300, 0, 760, 500)],
    "j04": [(470, 280, 650, 480), (20, 720, 140, 850), (870, 700, 1000, 830)],
    "j05": [(150, 120, 320, 300), (520, 100, 700, 300), (1050, 190, 1210, 360)],
    "j06": [(560, 0, 760, 230), (680, 150, 880, 360), (780, 300, 940, 470)],
    "j07": [(570, 220, 760, 430)],
    "j08": [(230, 140, 400, 330), (1290, 160, 1480, 330)],
    "j09": [(200, 0, 400, 200)],
    "j11": [(240, 0, 560, 400)],
    "j12": [(380, 60, 560, 260)],
    "j13": [(0, 180, 1536, 420)],
    "j14": [(380, 0, 720, 460)],
    "j15": [(300, 200, 470, 380)],
    "j16": [(280, 180, 460, 380), (1050, 20, 1260, 260)],
    "j18": [(370, 70, 660, 380)],
    "j19": [(0, 50, 1536, 700)],
    "j20": [(140, 330, 280, 470), (480, 50, 800, 420)],
    "j21": [(110, 110, 260, 290), (920, 40, 1110, 230)],
    "j22": [(380, 280, 740, 760)],
    "j23": [(150, 50, 820, 760)],
    "j24": [(0, 0, 1024, 1024)],
    "j25": [(30, 0, 760, 860)],
    "j26": [(360, 120, 560, 330), (880, 50, 1080, 260)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 8</div><div class="c2">Thirty-Seven Farmers</div></div>
  {gap(100)}
  {narr('The first crossbow bolt flew at Ash. It never reached him.','L0', 'margin:0 200px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('j01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1" style="margin-left:210px">{img('j02','', 'width:660px;height:660px')}
    {narr("Wren's arrow hit it in mid-air, and split it in two.",'', 'position:absolute;left:-170px;width:420px;bottom:-110px')}
    {sfx('KRAK!','left:420px;top:60px;transform:rotate(10deg);font-size:96px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('j03','', 'width:660px;height:660px')}
    {bub('What in the...','L2', 'right','position:absolute;left:-250px;top:300px;width:300px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('j04','', 'width:720px;height:1080px')}
    {bub('Shields! Now!','L3', 'right','position:absolute;left:-280px;top:200px;width:300px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L4">{img('j05','full')}
    {narr('Thirty sellswords charged into the yard. Professionals. Men who had fought in three wars.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L5" style="margin-left:300px">{img('j06','', 'width:720px;height:1080px')}
    {narr('They had never fought Greyhollow.','', 'position:absolute;left:-270px;top:650px;width:380px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L6" style="margin-left:0">{img('j07','', 'width:720px;height:1080px')}
    {narr('Tobin caught a sword on the handle of his hammer, and the sword broke.','', 'position:absolute;right:-330px;width:420px;top:620px')}
    {sfx('CLANG!','left:40px;top:860px;transform:rotate(-8deg);font-size:84px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L7">{img('j08','full')}
    {narr('Old Hanne, who carried the water, swung a full bucket. A man in chainmail flew across the yard.','', 'position:absolute;left:250px;width:580px;bottom:-160px')}
    {sfx('SPLOOSH!','left:360px;top:30px;transform:rotate(-6deg);font-size:72px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L8">{img('j09','full')}
    {narr('Wren fired from the roof of the mill. Three arrows, three sellswords down, and none of them dead. She aimed for the legs.','', 'position:absolute;right:30px;width:520px;bottom:-190px')}
  </div>
  {gap(270)}
  <div class="rel" data-a="L9">{img('j10','full')}
    {narr("Ash didn't bite anyone. He didn't need to. He stood in front of the gate and roared, and the horses bolted with their riders still on them.",'', 'position:absolute;left:250px;width:580px;bottom:-200px')}
    {sfx('ROOOAR!!','left:470px;top:30px;transform:rotate(-6deg);font-size:96px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:300px">{img('j11','', 'width:660px;height:660px')}
    {bub("These aren't farmers! Nobody said they had knights!",'L10', 'right','position:absolute;left:-270px;top:360px;width:380px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L11" style="margin-left:330px">{img('j12','', 'width:720px;height:1080px')}
    {narr('And Bram. Bram walked through the middle of it all with his one arm and his old sword, and every man who stood in front of him ended up in the mud.','', 'position:absolute;left:-310px;top:340px;width:460px')}
  </div>
  {gap(170)}
  <div class="rel" data-a="L12">{img('j13','full')}
    {narr('It was over before the sun had moved. Not one of ours had fallen.','', 'position:absolute;left:250px;width:580px;bottom:-140px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L13" style="margin-left:300px">{img('j14','', 'width:660px;height:660px')}
    {narr('Steward Corvin was still sitting on his horse, pale as milk.','', 'position:absolute;left:-270px;width:420px;bottom:-120px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:330px">{img('j15','', 'width:720px;height:1080px')}
    {bub("Steward. You'll take your four thousand crowns, and your wounded, and you'll go home.",'L14', 'right','position:absolute;left:-310px;top:40px;width:450px')}
    {bub("And you'll tell Lady Sabine the debt is paid. In full.",'L15', 'right','position:absolute;left:-300px;top:420px;width:420px')}
  </div>
  {gap(200)}
  <div class="rel">{img('j16','full')}
    {bub("This isn't over, Varr.",'L16', 'up','position:absolute;right:40px;bottom:-150px;width:340px')}
    {bub('It is for today.','L17', 'up','position:absolute;left:60px;bottom:-280px;width:300px')}
  </div>
  {gap(370)}
  <div class="rel" data-a="L18">{img('j17','full')}
    {narr('They limped south down the muddy road. The villagers cheered until their voices gave out.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L19" style="margin-left:0">{img('j18','', 'width:720px;height:1080px')}
    {narr('And I sat down very suddenly on the keep steps, because my legs had stopped working, and my hands were as cold as ice.','', 'position:absolute;right:-330px;width:430px;top:520px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L20">{img('j19','full')}
    {narr('Nobody noticed. They were too busy celebrating.','', 'position:absolute;left:250px;width:580px;bottom:-120px')}
  </div>
  {gap(210)}
  <div class="rel" data-a="L21" style="margin-left:120px">{img('j20','', 'width:840px;height:840px')}
    {narr('Almost nobody.','', 'position:absolute;left:-90px;bottom:-110px;width:320px')}
  </div>
  {gap(260, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  <div class="rel">{img('j21','full')}
    {bub('Steward Bram. A word.','L22', 'up','position:absolute;left:40px;bottom:-140px;width:340px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:330px">{img('j22','', 'width:720px;height:1080px')}
    {bub('I have measured every person in this village. Thirty-seven commoners. Not one of them is below two rings. Three of them are at four.','L23', 'right','position:absolute;left:-310px;top:120px;width:470px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('j23','', 'width:660px;height:660px')}
    {bub("That doesn't happen. Not in a lifetime. Not in a hundred lifetimes.",'L24', 'up','position:absolute;left:-270px;bottom:-200px;width:430px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:210px">{img('j24','', 'width:660px;height:660px')}</div>
  {gap(30)}
  {bub('Do you know what he is?','L25', 'up','position:relative;margin-left:420px;width:340px')}
  {gap(90)}
  <div class="rel" style="margin-left:0">{img('j25','', 'width:660px;height:660px')}
    {bub('Yes.','L26', 'left','position:absolute;right:-260px;top:260px;width:220px')}
  </div>
  {gap(180)}
  <div class="rel">{img('j26','full')}
    {bub("And he's not to know.",'L27', 'up','position:absolute;right:40px;bottom:-140px;width:340px')}
  </div>
  {gap(330, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L28" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 9 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
