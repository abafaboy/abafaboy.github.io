"""Chapter 34: One Eye. Face coordinates refer to the original panel PNGs.

All 19 source panels were inspected. p15 protects two rear heads as well as
visible faces elsewhere; animal faces are included. p01 uses the accepted corrected expedition roster.
"""
FACES = {
    "p01": [
        (32, 179, 159, 302),  # Lucan
        (165, 219, 271, 348),  # anonymous1
        (256, 269, 353, 392),  # anonymous2
        (329, 281, 436, 405),  # anonymous3
        (407, 245, 492, 357),  # anonymous4
        (330, 364, 424, 487),  # anonymous5
        (457, 244, 591, 381),  # Wren
        (591, 280, 690, 398),  # Oswin
        (669, 336, 780, 460),  # Ilse
        (767, 344, 867, 459),  # Dunn
        (845, 365, 962, 489),  # Kell
        (1121, 192, 1277, 354),  # Garrow
        (1343, 324, 1427, 448),  # host1
        (1399, 305, 1488, 437),  # host2
        (1474, 302, 1536, 426),  # host3
        (113, 271, 323, 463),  # Ash
    ],
    "p02": [(225, 450, 760, 1020)],
    "p03": [(135, 245, 350, 470), (1145, 55, 1410, 310)],
    "p04": [(130, 75, 655, 610)],
    "p05": [(110, 145, 575, 610)],
    "p06": [(425, 350, 725, 640), (0, 625, 175, 890), (840, 315, 1024, 680)],
    "p07": [(195, 120, 335, 255), (550, 125, 640, 230),
            (400, 285, 565, 455), (1305, 270, 1536, 505)],
    "p08": [(90, 105, 575, 590)],
    "p09": [(520, 50, 710, 235), (590, 555, 735, 690)],
    "p10": [(350, 280, 800, 690)],
    "p11": [(205, 65, 570, 370)],
    "p12": [(325, 320, 605, 605), (495, 540, 720, 720)],
    "p13": [(285, 150, 505, 340), (1150, 260, 1305, 385)],
    "p14": [(370, 595, 445, 665)],  # tiny right-facing profile
    "p15": [(380, 275, 580, 450), (925, 250, 1120, 435)],  # rear heads
    "p16": [(205, 530, 645, 960)],
    "p17": [(335, 290, 475, 420), (740, 95, 1015, 295),
            (1325, 295, 1410, 380)],  # Dunn, Ash, white she-wolf
    "p18": [(225, 185, 475, 445), (685, 335, 870, 525)],
    "p19": [(345, 565, 745, 965)],
    "end": [],  # the established obelisk end card contains no faces
}


def build():
    return f"""
<div class="sec white" style="background:#eef4fa">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 34</div><div class="c2">One Eye</div></div>
  {gap(100)}
  {narr('Nobody moved. Not the Skeld. Not the hunters. Not even the wind.', 'L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('p01', 'full')}</div>
  {gap(180)}
  <div class="rel" style="margin-left:330px">{img('p02', '', 'width:720px;height:1080px')}
    {bub("Wren. You've grown.", 'L1', 'right', 'left:-300px;top:70px;width:400px')}
  </div>
  {gap(160)}
  {narr('Wren had an arrow on the string before I saw her move. Aimed at his heart.', 'L2', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L2b">{img('p03', 'full')}
    {bub('Five years. You were alive for five years.', 'L3', 'up', 'left:40px;top:740px;width:660px')}
  </div>
  {gap(370)}
  <div class="rel" style="margin-left:300px">{img('p04', '', 'width:660px;height:660px')}
    {bub('Yes.', 'L4', 'right', 'left:-270px;top:250px;width:210px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('p05', '', 'width:660px;height:660px')}
    {bub('Mother kept your bowl on the table. Every night. For two years.', 'L5', 'left', 'right:-390px;top:100px;width:390px')}
  </div>
  {gap(160)}
  {bub('He came to us half dead, five winters ago. We called him One-Eye. We never asked his southern name. That is not our way.', 'L6', 'left', 'position:relative;margin:0 110px;width:860px')}
  {gap(55)}
  <div class="rel" data-a="L6b" style="margin-left:180px">{img('p06', '', 'width:720px;height:1080px')}</div>
  {gap(160)}
  <div class="rel" data-a="L7">{img('p07', 'full')}
    {bub("Something in the deep ice took my eye. The Skeld carried me out. By their law, a life saved is owed a year. When my year was done, the White had moved behind me.", 'L7b', 'up', 'left:60px;width:960px;bottom:-330px')}
  </div>
  {gap(430)}
  <div class="rel" style="margin-left:300px">{img('p08', '', 'width:660px;height:660px')}
    {bub("That's one year. What about the other four?", 'L8', 'up', 'left:-270px;width:480px;bottom:-180px')}
  </div>
  {gap(280)}
  {narr("He didn't answer. A small boy had come running out of the tents, and wrapped himself around Garrow's leg.", 'L9', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L9b">{img('p09', 'full')}</div>
  {gap(160)}
  <div class="rel" style="margin-left:300px">{img('p10', '', 'width:660px;height:660px')}
    {bub("Papa! Papa, you're back!", 'L10', 'up', 'left:-270px;width:340px;bottom:-120px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L11" style="margin-left:0">{img('p11', '', 'width:660px;height:660px')}
    {narr("The boy had red-brown hair. Like Garrow's. Like Wren's.", '', 'position:absolute;right:-390px;top:360px;width:390px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:330px">{img('p12', '', 'width:720px;height:1080px')}
    {bub("This is Rune. His mother was Freydis's daughter. The cold took her last winter.", 'L12', 'right', 'left:-300px;top:640px;width:470px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L13">{img('p13', 'full')}
    {narr("Wren lowered the bow. I think it would have been easier for her if he'd been a monster.", '', 'position:absolute;left:140px;width:800px;bottom:-210px')}
  </div>
  {gap(310)}
  {narr('She walked out onto the ice, a long way, and sat down in the snow.', 'L14', 'margin:0 150px')}
  {gap(40)}
  <div class="rel" data-a="L14b">{img('p14', 'full')}</div>
  {gap(180)}
  <div class="rel" data-a="L15">{img('p15', 'full')}
    {narr("I followed, sat beside her, and said nothing. Bram taught me that. Sometimes a lord's whole job is to sit nearby and be warm.", '', 'position:absolute;left:110px;width:860px;bottom:-260px')}
  </div>
  {gap(360)}
  <div class="rel" style="margin-left:0">{img('p16', '', 'width:720px;height:1080px')}
    {bub("I used to dream he'd come home. Now he's here, and I don't know what I want.", 'L16', 'left', 'right:-340px;top:60px;width:430px')}
  </div>
  {gap(180)}
  {narr('When we came back, Ash was waiting for us. He looked extremely pleased with himself. And a white wolf watched from the trees.', 'L17', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L17b">{img('p17', 'full')}
    {bub('Where have you been all night? ...Oh. Oh, I see.', 'L18', 'up', 'left:30px;width:500px;bottom:-220px')}
  </div>
  {gap(340)}
  <div class="rel" data-a="L19" style="margin-left:210px">{img('p18', '', 'width:660px;height:660px')}
    {bub("My lord. You came for allies, and the Skeld need warmth. I know where there's more rimeglass than your smith could work in a hundred years.", 'L19b', 'up', 'left:-100px;top:680px;width:860px')}
  </div>
  {gap(440)}
  <div class="rel" style="margin-left:330px">{img('p19', '', 'width:720px;height:1080px')}
    {bub("The Glass Deep, under the mountain. I've been inside it once.", 'L20', 'right', 'left:-300px;top:60px;width:540px')}
    {bub("That's where I lost this.", 'L21', 'right', 'left:-300px;top:750px;width:380px')}
  </div>
  {gap(300, 'linear-gradient(#eef4fa,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L22" style="margin-left:120px">{img('end', '', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 35 &middot; COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
