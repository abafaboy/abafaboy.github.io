"""Chapter 46 layout."""
FACES = {
    "p01": [(167, 325, 493, 667), (812, 121, 1119, 401)],
    "p02": [(290, 282, 486, 509), (612, 235, 831, 470), (40, 455, 175, 600), (880, 645, 940, 715)],
    "p03": [(235, 585, 485, 805)],
    "p04": [(165, 190, 745, 730), (330, 700, 580, 930)],
    "p05": [(895, 55, 1085, 270), (30, 10, 420, 270), (250, 120, 540, 390), (555, 290, 745, 430)],
    "p06": [(95, 255, 390, 575), (595, 125, 860, 415), (510, 525, 835, 860)],
    "p07": [(900, 165, 1112, 412), (600, 265, 775, 465), (0, 230, 500, 625), (90, 245, 690, 440)],
    "p08": [(115, 25, 330, 245), (470, 40, 736, 306), (1230, 195, 1497, 467)],
    "p09": [(285, 15, 625, 375), (690, 360, 815, 570)],
    "p10": [(455, 0, 885, 475)],
    "p11": [(185, 330, 400, 520), (600, 195, 860, 430)],
    "p12": [(255, 285, 645, 665)],
    "p13": [(40, 515, 1536, 795)],
    "p14": [(360, 15, 680, 405)],
    "p15": [(425, 100, 635, 305), (970, 440, 1180, 625), (690, 675, 770, 770), (1280, 650, 1355, 725)],
}

# Bram's one-line letter: a parchment note, not a speech bubble (the boy holding it is not the speaker).
LETTER = 'position:absolute;left:470px;top:40px;width:360px;border-radius:8px;background:#f3e6c6;color:#3a2410;border:2px solid #7a5a30;padding:26px 34px;transform:rotate(-3deg);font-size:38px;box-shadow:0 6px 0 #3a241033'

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 46</div><div class="c2">Paper and Glass</div></div>
  {gap(160, 'linear-gradient(#fff,#dde4ea)')}
</div>
<div class="sec white" style="background:#dde4ea">
  {narr('I had read two books about ships. Neither of them mentioned that the sea goes up and down. For four days.','L0', 'margin:0 120px')}
  {gap(330)}
  <div class="rel">{img('p01','full')}
    {bub("Cheer up, my lord. You've gone a lovely shade of green. Very fashionable in Vask.",'L1', 'right','position:absolute;left:210px;top:-290px;width:560px')}
  </div>
  {gap(200, 'linear-gradient(#dde4ea,#f6efe1)')}
</div>
<div class="sec white" style="background:#f6efe1">
  {narr('Vask was the first city I had ever seen where nobody asked how many rings I had. They only asked what I had to sell.','L2', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L2b">{img('p02','full')}</div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('p03','', 'width:720px;height:1080px')}
    {bub('My counting house. My warehouses. My two ships. At the next quarter-day, Lady Sabine takes all of them. I owe eleven thousand crowns. She paid twenty-two thousand for the pleasure of collecting it.','L3', 'right','position:absolute;left:-310px;top:-210px;width:640px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p04','', 'width:660px;height:660px')}
    {bub("We don't have eleven thousand crowns.",'L4', 'left','position:absolute;right:-400px;top:-40px;width:380px')}
    {bub('We have something better.','L5', 'left','position:absolute;right:-370px;top:330px;width:330px')}
  </div>
  {gap(240, 'linear-gradient(#f6efe1,#0f1828)')}
</div>
<div class="sec night" style="background:#0f1828">
  {gap(40)}
  {narr('We rented a vault on the Exchange canal and filled it with Deep rimeglass. Then Pell invited every merchant in Vask to come and look.','L6', 'margin:0 110px')}
  {gap(530)}
  <div class="rel">{img('p05','full')}
    {bub("Every note we print says Greyhollow will pay the bearer in rimeglass. And there's the rimeglass. Bring a lamp if you don't believe me. You won't need it.",'L7', 'left','position:absolute;left:500px;top:-500px;width:560px')}
    {sfx('OOOH!','left:60px;top:560px;transform:rotate(-6deg);font-size:84px')}
  </div>
  {gap(260, 'linear-gradient(#0f1828,#f6efe1)')}
</div>
<div class="sec white" style="background:#f6efe1">
  {gap(60)}
  <div class="rel" style="margin-left:0">{img('p06','', 'width:720px;height:1080px')}
    {bub('In Vask, anyone may open a counting house. Even a lord with no rings. We only ask one thing. Is the glass real?','L8', 'left','position:absolute;right:-350px;top:300px;width:440px')}
    {narr('It was real. And none of it had a shape inside. That was Skeld law now, and mine.','L9', 'position:absolute;left:380px;width:640px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L10">{img('p07','full')}
    {narr('By the end of the week, merchants were buying Greyhollow notes faster than the printer could dry them.','', 'position:absolute;left:160px;width:760px;bottom:-190px')}
  </div>
  {gap(560)}
  <div class="rel">{img('p08','full')}
    {bub("Pell Marrow's debts. Eleven thousand crowns. Paid in full.",'L11', 'right','position:absolute;left:100px;top:-330px;width:440px')}
    {bub('Lady Sabine wants the ships, my lord, not your paper. I refuse your payment.','L12', 'right','position:absolute;right:20px;top:-260px;width:460px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('p09','', 'width:660px;height:660px')}
    {bub('In Vask, sir, a debt offered in full is a debt paid. Refuse it, and you have simply given it away.','L13', 'right','position:absolute;left:-280px;top:70px;width:430px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L14" style="margin-left:210px">{img('p10','', 'width:660px;height:660px')}
    {sfx('scritch... scritch...','left:-180px;top:190px;transform:rotate(-8deg);font-size:44px', 'quiet')}
    {narr("He signed. Lady Sabine had paid twice what Pell's debts were worth. We had paid exactly what they were worth. By law, she had to take it.",'', 'position:absolute;left:-110px;width:880px;bottom:-250px')}
  </div>
  {gap(300, 'linear-gradient(#f6efe1,#f3d9bd)')}
</div>
<div class="sec white" style="background:#f3d9bd">
  {gap(460)}
  <div class="rel">{img('p11','full')}
    {bub('My ships. My house. My good name, such as it was. And now I owe all of it to you, my lord.','L15', 'left','position:absolute;right:100px;top:-450px;width:520px')}
    {bub('So why should I trust a merchant who owes me eleven thousand crowns?','L16', 'left','position:absolute;left:30px;top:-250px;width:410px')}
    {sfx('RRRIP!','right:40px;top:500px;transform:rotate(-8deg);font-size:90px')}
  </div>
  {gap(220)}
  <div class="rel" style="margin-left:330px">{img('p12','', 'width:720px;height:1080px')}
    {bub("Loyal to profit, my lord. And you're very profitable.",'L17', 'right','position:absolute;left:-300px;top:180px;width:440px')}
  </div>
  {gap(240, 'linear-gradient(#f3d9bd,#f6efe1)')}
</div>
<div class="sec white" style="background:#f6efe1">
  {narr("So the Greyhollow counting house opened its doors in Vask, under Pell's old roof. Pell said it was the first bank in the world built on glass. For once, I didn't check.",'L18', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L18b">{img('p13','full')}</div>
  {gap(280, 'linear-gradient(#f6efe1,#1d1527)')}
</div>
<div class="sec night" style="background:#1d1527">
  {gap(40)}
  {narr("In Corrow, Lady Sabine read her factor's letter twice. Then she closed her fan.",'L19', 'margin:0 150px')}
  {gap(60)}
  <div class="rel" style="margin-left:300px">{img('p14','', 'width:660px;height:660px')}
    {bub('Clever boy.','L20', 'right','position:absolute;left:-210px;top:160px;width:300px')}
  </div>
  {gap(260, 'linear-gradient(#1d1527,#d9dde2)')}
</div>
<div class="sec white" style="background:#d9dde2">
  {narr('When we sailed back into Saltmouth, another letter from Bram was waiting on the dock. Also one line.','L21', 'margin:0 120px')}
  {gap(60)}
  <div class="rel">{img('p15','full')}
    {narr('Come home. Tobin has built something.','L22', LETTER)}
  </div>
  {gap(320, 'linear-gradient(#d9dde2,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L23" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 47 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
