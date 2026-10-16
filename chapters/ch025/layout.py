"""Chapter 25 layout."""
FACES = {
    "aa01": [(820, 220, 990, 400), (320, 350, 460, 500), (495, 450, 595, 550), (655, 395, 765, 505), (1160, 455, 1255, 550), (0, 370, 270, 600), (1300, 180, 1536, 720)],
    "aa02": [(360, 270, 720, 690), (10, 430, 250, 700), (870, 590, 1024, 800)],
    "aa03": [(265, 50, 665, 500)],
    "aa04": [(205, 0, 500, 335), (830, 0, 1024, 380)],
    "aa05": [(0, 330, 400, 670), (420, 285, 640, 520), (670, 330, 865, 520), (985, 370, 1170, 560), (1170, 360, 1536, 860), (880, 480, 1010, 620)],
    "aa06": [(255, 60, 450, 280), (615, 145, 825, 350), (0, 500, 240, 690), (880, 520, 1180, 620)],
    "aa07": [(40, 50, 370, 340), (510, 55, 750, 300)],
    "aa08": [(360, 20, 540, 260)],
    "aa09": [(0, 0, 620, 760)],
    "aa10": [(370, 200, 830, 730), (0, 200, 290, 880)],
    "aa11": [(280, 0, 640, 380)],
    "aa12": [(0, 30, 400, 580), (400, 390, 610, 580), (670, 290, 805, 450), (805, 230, 1015, 430), (1165, 270, 1300, 430), (1370, 360, 1536, 620)],
    "aa13": [(0, 0, 620, 590)],
    "aa14": [(255, 220, 605, 610)],
    "aa15": [(420, 560, 540, 770), (990, 600, 1080, 720)],
}

VISION = '<div style="position:absolute;inset:0;background:#7f9cc8;mix-blend-mode:color;opacity:.45;pointer-events:none"></div>'

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 25</div><div class="c2">Wards of Greyhollow</div></div>
  {gap(100)}
  {narr('At dawn, the Measurers brought a covered cart into the square, for the children.','L0', 'margin:0 150px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('aa01','full')}
    {sfx('CREAK... CREAK...','left:600px;top:615px;transform:rotate(-5deg);font-size:44px', 'quiet')}
  </div>
  {gap(150)}
  <div class="rel" style="margin-left:330px">{img('aa02','', 'width:720px;height:1080px')}
    {bub("Magister. These six are my wards, members of my household. Under the Eleventh Article and the Fourth, you can't take them without a royal warrant.",'L1', 'right','position:absolute;left:-300px;top:500px;width:470px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('aa03','', 'width:660px;height:660px')}
    {bub('Six wards. Dated last night.','L2', 'left','position:absolute;right:-360px;top:40px;width:360px')}
    {bub("The law doesn't care when.",'L3', 'right','position:absolute;right:-380px;top:380px;width:340px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('aa04','', 'width:660px;height:660px')}
    {bub("No. It doesn't. Unload the cart.",'L4', 'right','position:absolute;left:-270px;top:60px;width:330px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L5">{img('aa05','full')}
    {sfx('HURRAH!','left:220px;top:30px;transform:rotate(-6deg);font-size:80px')}
    {narr("I don't think Greyhollow had ever made that much noise.",'', 'position:absolute;left:220px;width:640px;bottom:-170px')}
  </div>
  {gap(280)}
  <div class="rel">{img('aa06','full')}
    {bub('Walk with me, Lord Lucan.','L6', 'up','position:absolute;left:60px;bottom:-170px;width:330px')}
  </div>
  {gap(260)}
  <div class="rel">{img('aa07','full')}
    {bub("Do you know why the Order exists? Three hundred years ago, there was a woman in the north. Hollow-born, like you. Everything she touched grew. Her people loved her.",'L7', 'up','position:absolute;left:20px;bottom:-330px;width:620px')}
  </div>
  {gap(400)}
  {gap(160, 'linear-gradient(#fff,#d2deec)')}
</div>
<div class="sec white" style="background:#d2deec">
  {gap(60)}
  <div class="rel">{img('aa08','full', 'filter:saturate(.8) brightness(1.04)')}{VISION}
    {bub("And when she died, the whole North froze. The Pale is her grave, my lord. That is what your kind leaves behind.",'L8', 'up','position:absolute;left:420px;bottom:-290px;width:600px')}
  </div>
  {gap(360)}
  {gap(160, 'linear-gradient(#d2deec,#fff)')}
</div>
<div class="sec white">
  <div class="rel" style="margin-left:300px">{img('aa09','', 'width:660px;height:660px')}
    {bub("You don't know that I'm...",'L9', 'right','position:absolute;left:-290px;top:70px;width:285px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('aa10','', 'width:720px;height:1080px')}
    {bub('I knelt in your barley last night. The soil is warm a foot deep. I know exactly what you are.','L10', 'left','position:absolute;right:-340px;top:80px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:210px">{img('aa11','', 'width:660px;height:660px')}
    {bub('So here is my offer. Come south with me, quietly. The Order will take care of you. And Greyhollow will be left in peace. Your people keep their barley. Their children. Everything.','L11', 'up','position:absolute;left:-170px;bottom:-360px;width:640px')}
  </div>
  {gap(440)}
  <div class="rel" data-a="L12">{img('aa12','full')}
    {narr('I looked back at the village. At Bram by the gate. At six children being squeezed half to death by their mothers.','', 'position:absolute;left:200px;width:680px;bottom:-230px')}
  </div>
  {gap(320)}
  <div class="rel" style="margin-left:300px">{img('aa13','', 'width:660px;height:660px')}
    {bub('No.','L13', 'right','position:absolute;left:-240px;top:230px;width:200px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('aa14','', 'width:720px;height:1080px')}
    {bub('I thought you would say that. Then the warrant will come, my lord. And it will come with soldiers.','L14', 'right','position:absolute;left:-300px;top:120px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L15">{img('aa15','full')}
    {narr('He walked back into the mist. I stood in the warm barley for a long time. For the first time in my life, I wished I really was nothing at all.','', 'position:absolute;left:180px;width:720px;bottom:-260px')}
  </div>
  {gap(300)}
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L16" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 26 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
