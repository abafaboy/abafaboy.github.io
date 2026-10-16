"""Chapter 20 layout."""
FACES = {
    "v01": [(30, 360, 255, 560), (250, 405, 410, 560), (485, 170, 705, 385), (790, 90, 1050, 330), (1060, 420, 1240, 585), (1285, 445, 1465, 610)],
    "v02": [(100, 70, 1480, 660), (100, 510, 330, 730), (260, 230, 460, 530)],
    "v03": [(240, 40, 460, 270), (0, 345, 230, 640), (550, 640, 840, 900), (880, 730, 1024, 945), (0, 845, 210, 1085)],
    "v04": [(725, 190, 910, 395), (965, 250, 1170, 450), (365, 350, 650, 600), (60, 450, 400, 580), (1420, 410, 1536, 530)],
    "v05": [(260, 100, 860, 640)],
    "v06": [(180, 40, 640, 560)],
    "v07": [(300, 110, 780, 600)],
    "v08": [(30, 80, 360, 380), (230, 260, 550, 550), (1185, 85, 1360, 290), (1005, 145, 1185, 330), (1340, 130, 1515, 330)],
    "v09": [(250, 40, 780, 520)],
    "v10": [(100, 90, 860, 920)],
    "v12": [(130, 40, 610, 560)],
    "v13": [(365, 125, 570, 345), (340, 230, 835, 610)],
    "v14": [(800, 150, 1030, 350), (0, 440, 760, 700)],
    "v15": [(360, 300, 710, 720)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 20</div><div class="c2">Tamsin</div></div>
  {gap(100)}
  {narr("The youngest Measurer didn't measure anybody that afternoon. She played tag with the village children instead. And Ash followed her everywhere, exactly as I'd warned.",'L0', 'margin:0 70px;padding:56px 100px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('v01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1">{img('v02','full')}
    {narr('By the end of the day, she had lost every game, and fourteen children were sitting on my dog.','', 'position:absolute;left:200px;width:680px;bottom:-170px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:0">{img('v03','', 'width:720px;height:1080px')}
    {bub("You're not very good at being frightening.",'L2', 'left','position:absolute;left:400px;top:30px;width:420px')}
    {bub("I'm not very good at being a Measurer. Please don't tell Magister Hask.",'L3', 'up','position:absolute;left:300px;top:700px;width:400px')}
  </div>
  {gap(420)}
  <div class="rel">{img('v04','full')}
    {bub('Your village is strange, my lord. Everyone is so healthy. In my village, the children coughed all winter. Here they run like deer.','L4', 'right','position:absolute;left:300px;top:-330px;width:600px')}
    {bub("It's the turnips.",'L5', 'up','position:absolute;left:400px;bottom:-170px;width:320px')}
  </div>
  {gap(280)}
  <div class="rel" style="margin-left:300px">{img('v05','', 'width:660px;height:660px')}
    {bub("Nobody's turnips are that good.",'L6', 'right','position:absolute;left:-270px;top:120px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('v06','', 'width:660px;height:660px')}
    {bub('Why did you join the Order?','L7', 'left','position:absolute;right:-340px;top:120px;width:360px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('v07','', 'width:720px;height:1080px')}
    {bub('I have a little sister. Nell. She was five when the Measurers came to our village. They said she was special. Hollow-born. They said the Order would take care of her.','L8', 'right','position:absolute;left:-310px;top:40px;width:480px')}
  </div>
  {gap(160, 'linear-gradient(#fff,#efe4d0)')}
</div>
<div class="sec white" style="background:#efe4d0">
  {gap(40)}
  <div class="rel">{img('v08','full')}
    {bub('They promised I could visit her, once I earned my silver lens.','L9', 'up','position:absolute;left:60px;bottom:-190px;width:480px')}
  </div>
  {gap(220)}
  {gap(160, 'linear-gradient(#efe4d0,#fff)')}
</div>
<div class="sec white">
  <div class="rel" style="margin-left:0">{img('v09','', 'width:660px;height:660px')}
    {bub('I earned it last spring. I have asked to see her eleven times. They always say, next year.','L10', 'left','position:absolute;right:-380px;top:40px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L11" style="margin-left:330px">{img('v10','', 'width:720px;height:1080px')}
    {narr("Hollow-born. The same word Ilse had used for me. I didn't say anything. I couldn't.",'', 'position:absolute;left:-310px;width:380px;top:480px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('v11','', 'width:660px;height:660px')}
    {bub("She carved me this bird. She said it would fly to me if she ever needed help. Silly, isn't it.",'L12', 'left','position:absolute;right:-380px;top:20px;width:450px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('v12','', 'width:660px;height:660px')}
    {bub("It's not silly.",'L13', 'right','position:absolute;left:-250px;top:180px;width:280px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L14">{img('v13','full')}
    {narr('Ash put his enormous head in her lap, the way he always did when someone in the keep was sad.','', 'position:absolute;left:200px;width:680px;bottom:-170px')}
  </div>
  {gap(230)}
  {gap(220, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(60)}
  {narr("That night, I couldn't stop thinking about it. Somewhere, the Order was keeping a little girl called Nell. And if Ilse was right, it wanted to keep me too.",'L15', 'margin:0 70px;padding:56px 100px')}
  {gap(40)}
  <div class="rel" data-a="L15b">{img('v14','full')}</div>
  {gap(160)}
  <div class="rel" data-a="L16" style="margin-left:330px">{img('v15','', 'width:720px;height:1080px')}
    {narr("Out in the Measurers' camp, one lamp burned very late.",'', 'position:absolute;left:-300px;top:400px;width:420px')}
  </div>
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L17" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 21 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
