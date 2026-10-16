"""Chapter 21 layout."""
FACES = {
    "w01": [(455, 65, 590, 220)],
    "w02": [(305, 145, 775, 580)],
    "w03": [(480, 0, 690, 290)],
    "w05": [(95, 125, 545, 615)],
    "w06": [(280, 0, 600, 380)],
    "w07": [(20, 0, 600, 650)],
    "w08": [(275, 195, 450, 425)],
    "w09": [(540, 155, 785, 445)],
    "w10": [(20, 0, 615, 575)],
    "w11": [(215, 230, 495, 570)],
    "w12": [(200, 50, 485, 390), (1120, 35, 1290, 245)],
    "w13": [(155, 10, 570, 525)],
    "w14": [(320, 280, 720, 740)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 21</div><div class="c2">What the Lens Saw</div></div>
  {gap(160, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(40)}
  {narr('Past midnight, when the whole camp was asleep, Hask walked out alone into my fields.','L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('w01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1" style="margin-left:300px">{img('w02','', 'width:660px;height:660px')}
    {narr("He didn't know that someone was still awake to see him.",'', 'position:absolute;left:-270px;top:330px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L2">{img('w03','full')}
    {narr('He knelt in the barley. He took off his glove. And he laid his bare hand flat on the earth.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(300)}
  {narr('Tamsin told me later what she saw that night. The ground lit up under his hand. Faint and pale, like frost. Except it was warm.','L3', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L3b">{img('w04','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:0">{img('w05','', 'width:720px;height:1080px')}
    {bub('Warm. The whole field is warm. Gods above. The whole valley.','L4', 'left','position:absolute;right:-330px;top:160px;width:400px')}
  </div>
  {gap(160)}
  {narr('He went back to his tent and wrote a letter. Just one word, Tamsin said. She saw it over his shoulder before he sealed it.','L5', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L5b" style="margin-left:210px">{img('w06','', 'width:660px;height:660px')}</div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('w07','', 'width:660px;height:660px')}
    {bub('Confirmed.','L6', 'left','position:absolute;right:-320px;top:250px;width:290px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L7">{img('w08','full')}
    {narr('Then he tied it to a white bird, and let it go. South. Toward the capital.','', 'position:absolute;left:220px;width:640px;bottom:-170px')}
    {sfx('FLAP FLAP','left:700px;top:250px;transform:rotate(-8deg);font-size:50px', 'quiet')}
  </div>
  {gap(300, 'linear-gradient(#0b0d16,#0c1322)')}
</div>
<div class="sec night" style="background:#0c1322">
  <div class="rel" data-a="L8">{img('w09','full')}
    {narr("At that same moment, in the keep, I woke up so cold I couldn't breathe.",'', 'position:absolute;left:220px;width:640px;bottom:-170px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:300px">{img('w10','', 'width:660px;height:660px')}
    {bub('Wren.','L9', 'right','position:absolute;left:-260px;top:110px;width:230px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L10" style="margin-left:0">{img('w11','', 'width:720px;height:1080px')}
    {narr("One of the threads was pulling north. Far north, into the Pale. And it hurt. Someone in Wren's party was bleeding.",'', 'position:absolute;right:-330px;top:540px;width:420px')}
  </div>
  {gap(180)}
  <div class="rel">{img('w12','full')}
    {bub('My lord? I heard you shout.','L11', 'up','position:absolute;right:40px;bottom:-150px;width:360px')}
    {bub("Someone's hurt. In the Pale. I can feel it.",'L12', 'up','position:absolute;left:50px;bottom:-330px;width:420px')}
  </div>
  {gap(420)}
  <div class="rel" style="margin-left:0">{img('w13','', 'width:660px;height:660px')}
    {bub("Then there's nothing to do tonight but trust her.",'L13', 'left','position:absolute;right:-340px;top:130px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L14" style="margin-left:330px">{img('w14','', 'width:720px;height:1080px')}
    {narr("Bram was right. That was the worst part. Being a lord who can feel his people bleeding, and can't do a single thing about it.",'', 'position:absolute;left:-310px;top:400px;width:400px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L15">{img('w15','full')}
    {narr('And far above us, a white bird flew south, carrying one word that would change everything.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(320, 'linear-gradient(#0c1322,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L16" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 22 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
