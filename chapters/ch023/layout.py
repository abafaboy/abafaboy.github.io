"""Chapter 23 layout."""
FACES = {
    "y01": [(60, 480, 850, 670), (880, 320, 1040, 500), (1060, 455, 1240, 615), (1290, 375, 1455, 555)],
    "y02": [(60, 690, 430, 1040), (480, 270, 850, 670)],
    "y03": [(528, 175, 690, 335), (0, 440, 845, 675), (920, 378, 1100, 565), (1215, 290, 1410, 495)],
    "y04": [(35, 415, 885, 655), (995, 310, 1180, 515)],
    "y05": [(445, 385, 625, 565), (5, 745, 395, 930), (620, 745, 1000, 930)],
    "y06": [(220, 95, 600, 430), (345, 465, 610, 730)],
    "y07": [(378, 110, 565, 290), (1050, 25, 1257, 243), (0, 360, 300, 670), (535, 390, 1100, 640)],
    "y08": [(40, 0, 645, 700)],
    "y09": [(355, 180, 600, 435)],
    "y10": [(495, 115, 655, 305), (915, 130, 1090, 320), (0, 395, 420, 770), (1270, 285, 1536, 800)],
    "y11": [(130, 300, 320, 520), (550, 250, 820, 555), (330, 735, 500, 945), (880, 650, 1024, 875)],
    "y12": [(175, 35, 595, 520)],
    "y13": [(330, 110, 625, 480)],
    "y14": [(170, 370, 1130, 780), (1095, 430, 1536, 820)],
    "y15": [(110, 0, 790, 620)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 23</div><div class="c2">An Honour</div></div>
  {gap(100)}
  {narr("On the second day of the measuring, the wind changed. It blew Tobin's smoke straight out of the square. And it was the children's turn.",'L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('y01','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:330px">{img('y02','', 'width:720px;height:1080px')}
    {bub('Three rings. And this one. Three. Again.','L1', 'right','position:absolute;left:-300px;top:80px;width:380px')}
    {sfx('SHIIING','left:330px;top:640px;transform:rotate(-6deg);font-size:52px', 'quiet')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L2">{img('y03','full')}
    {narr('Oswin had taught the grown-ups to groan. Nobody can teach a seven-year-old to be weak. They just bounced up to the table, grinning, and glowed.','', 'position:absolute;left:200px;width:680px;bottom:-230px')}
  </div>
  {gap(330)}
  <div class="rel">{img('y04','full')}
    {bub('Six gifted children, in one little northern village. How remarkable.','L3', 'up','position:absolute;right:30px;bottom:-200px;width:540px')}
  </div>
  {gap(380)}
  <div class="rel" style="margin-left:0">{img('y05','', 'width:720px;height:1080px')}
    {bub('The Order honours gifted commoners. These six will come with us to the Academy in Aldcrown. They will be fed, clothed and educated. We leave in three days.','L4', 'left','position:absolute;right:-350px;top:-60px;width:620px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('y06','', 'width:660px;height:660px')}
    {bub("No. Please. She's only seven.",'L5', 'right','position:absolute;left:-280px;top:150px;width:320px')}
  </div>
  {gap(160)}
  <div class="rel">{img('y07','full')}
    {bub("Magister, they're children. They belong with their families.",'L6', 'up','position:absolute;left:60px;bottom:-200px;width:460px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:0">{img('y08','', 'width:660px;height:660px')}
    {bub('And the law says gifted commoners belong to the realm, my lord. You know the Charter better than I do. Show me where it says otherwise.','L7', 'left','position:absolute;right:-400px;top:40px;width:520px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L8" style="margin-left:330px">{img('y09','', 'width:720px;height:1080px')}
    {narr('I knew the Charter better than he did. That was the problem. He was right.','', 'position:absolute;left:-300px;top:520px;width:400px')}
  </div>
  {gap(300, 'linear-gradient(#fff,#0b0d16)')}
</div>
<div class="sec night">
  {gap(40)}
  {narr('That night, half the village crowded into the hall.','L9', 'margin:0 160px')}
  {gap(40)}
  <div class="rel">{img('y10','full')}</div>
  {gap(150)}
  <div class="rel" style="margin-left:0">{img('y11','', 'width:660px;height:660px')}
    {bub("We could fight them. Twelve Measurers. We'd be done before supper.",'L10', 'left','position:absolute;right:-380px;top:60px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('y12','', 'width:660px;height:660px')}
    {bub('And then the king sends a thousand. And then ten thousand.','L11', 'up','position:absolute;left:-270px;bottom:-200px;width:480px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:0">{img('y13','', 'width:720px;height:1080px')}
    {bub('Laws are written by men who never had to keep them.','L12', 'left','position:absolute;right:-340px;top:60px;width:380px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L13">{img('y14','full')}
    {narr("The six children were asleep in the corner. Their parents wouldn't let them out of sight. Ash had curled himself around all six of them, like a wall.",'', 'position:absolute;left:200px;width:680px;bottom:-240px')}
  </div>
  {gap(340)}
  <div class="rel" data-a="L14" style="margin-left:210px">{img('y15','', 'width:660px;height:660px')}
    {narr('Three days. Again.','', 'position:absolute;left:150px;width:360px;bottom:-140px')}
  </div>
  {gap(320, 'linear-gradient(#0b0d16,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L15" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 24 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
