"""Chapter 14 layout."""
FACES = {
    "p01": [(0, 260, 1536, 560)],
    "p02": [(270, 0, 460, 220)],
    "p03": [(380, 70, 600, 330)],
    "p04": [(220, 0, 780, 560)],
    "p06": [(130, 30, 330, 250), (580, 130, 760, 330), (1170, 120, 1360, 330)],
    "p07": [(30, 30, 380, 420), (500, 70, 860, 470)],
    "p09": [(240, 0, 520, 300)],
    "p10": [(220, 0, 820, 560)],
    "p12": [(160, 0, 780, 600), (780, 270, 1024, 500)],
    "p13": [(500, 380, 640, 520), (180, 530, 340, 700), (260, 300, 400, 440), (960, 330, 1100, 470)],
    "p14": [(0, 100, 1536, 520)],
    "p15": [(150, 520, 460, 860), (680, 140, 920, 400)],
    "p16": [(200, 80, 900, 840)],
    "p17": [(390, 280, 560, 460), (1030, 270, 1200, 460)],
    "p18": [(300, 50, 560, 360)],
    "p19": [(500, 40, 800, 380), (880, 200, 1024, 420)],
    "p20": [(310, 160, 560, 440), (680, 120, 900, 370)],
    "p21": [(0, 0, 1024, 1024)],
    "p22": [(150, 420, 1100, 760)],
    "p23": [(270, 100, 500, 400), (750, 120, 960, 380)],
    "p24": [(330, 80, 580, 360)],
}

def build():
    return f"""
<div class="sec white">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 14</div><div class="c2">The Soil Was Fine</div></div>
  {gap(100)}
  {narr('Summer came to Greyhollow. It had never really come before. The old women said the north had always had two seasons. Winter, and almost winter.','L0', 'margin:0 110px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('p01','full')}</div>
  {gap(150)}
  <div class="rel" data-a="L1">{img('p02','full')}
    {narr('Now the fields were gold with barley. The glasshouses stood open to the sun. And for three peaceful weeks, I forgot what my father had said.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L2" style="margin-left:330px">{img('p03','', 'width:720px;height:1080px')}
    {narr('Then Wren came back from a hunt, pale and out of breath.','', 'position:absolute;left:-300px;top:620px;width:400px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:300px">{img('p04','', 'width:660px;height:660px')}
    {bub('Riders on the south road. Twelve of them, in blue robes, with silver lenses round their necks. Two days away. Maybe less.','L3', 'up','position:absolute;left:-280px;bottom:-280px;width:500px')}
  </div>
  {gap(360)}
  <div class="rel" data-a="L4">{img('p05','full')}
    {narr('Blue robes. Silver lenses. Measurers. The Royal Order of the Measure.','', 'position:absolute;left:250px;width:580px;bottom:-140px')}
  </div>
  {gap(230)}
  <div class="rel" data-a="L5">{img('p06','full')}
    {narr('And for some reason, when Wren said it, both Bram and our scholar went completely still.','', 'position:absolute;left:250px;width:580px;bottom:-150px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:0">{img('p07','', 'width:660px;height:660px')}
    {bub('Lord Lucan. We need to talk. Now. Privately.','L6', 'left','position:absolute;right:-380px;top:240px;width:400px')}
  </div>
  {gap(180)}
  <div class="rel" data-a="L7" style="margin-left:210px">{img('p08','', 'width:660px;height:660px')}
    {narr('She took off her spectacles and put them on the table. Then she took something from her satchel. A silver lens, exactly like the ones Wren had described.','', 'position:absolute;left:-170px;width:500px;bottom:-200px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('p09','', 'width:720px;height:1080px')}
    {bub('My name is Ilse Thorne. I am not a scholar. I am a Royal Measurer. The Order sent me here to find you.','L8', 'right','position:absolute;left:-300px;top:420px;width:440px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('p10','', 'width:660px;height:660px')}
    {bub("Find me? Why? I'm a zero. Everyone knows that.",'L9', 'up','position:absolute;left:-270px;bottom:-170px;width:380px')}
  </div>
  {gap(230, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel">{img('p11','full', 'filter:saturate(.6)')}
    {bub('The night after your Measuring, the Stone in the capital cracked. Straight through its heart.','L10', 'up','position:absolute;left:40px;bottom:-200px;width:440px')}
    {bub("A stone doesn't crack because it finds nothing, my lord. It cracks because it can't hold what it finds.",'L11', 'up','position:absolute;right:30px;bottom:-400px;width:480px')}
  </div>
  {gap(480, 'linear-gradient(#05060a,#fff)')}
</div>
<div class="sec white">
  <div class="rel" data-a="L12" style="margin-left:300px">{img('p12','', 'width:660px;height:660px')}
    {narr("I didn't understand. I said so.",'', 'position:absolute;left:-270px;width:380px;bottom:-100px')}
  </div>
  {gap(200)}
  <div class="rel">{img('p13','full')}
    {bub("You don't have a Vessel. You have something else. Something that pours. Everything you take responsibility for, grows. Your land. Your animals. Your people.",'L13', 'up','position:absolute;left:120px;bottom:-300px;width:600px')}
  </div>
  {gap(400)}
  <div class="rel">{img('p14','full')}
    {bub('When you arrived, every person in this village measured one ring. Now not one of them is below two. Wren is at four. Tobin is at four. Bram is at five.','L14', 'up','position:absolute;left:120px;bottom:-300px;width:600px')}
  </div>
  {gap(400)}
  <div class="rel" style="margin-left:0">{img('p15','', 'width:720px;height:1080px')}
    {bub('Bram is at five?','L15', 'left','position:absolute;right:-300px;top:460px;width:300px')}
    {bub('Since midwinter, my lord.','L16', 'left','position:absolute;right:-320px;top:720px;width:320px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:300px">{img('p16','', 'width:660px;height:660px')}
    {bub('You knew?','L17', 'right','position:absolute;left:-250px;top:-60px;width:240px')}
    {bub('Since the morning the dog came home bigger than a horse.','L18', 'up','position:absolute;left:-270px;bottom:-260px;width:420px')}
  </div>
  {gap(300)}
  <div class="rel" data-a="L19">{img('p17','full', 'filter:saturate(.8)')}
    {narr("I sat down. The mill. The glasshouses. The wolves. Wren's arrow through the tree. Bram, one-armed, cutting down a frost-wolf in one stroke. Oswin's frost, against my brother's fire.",'', 'position:absolute;left:220px;width:640px;bottom:-230px')}
  </div>
  {gap(300)}
  <div class="rel" style="margin-left:330px">{img('p18','', 'width:720px;height:720px')}
    {bub('So the soil was fine.','L20', 'right','position:absolute;left:-280px;top:280px;width:320px')}
  </div>
  {gap(170)}
  <div class="rel" style="margin-left:0">{img('p19','', 'width:720px;height:720px')}
    {bub('The soil was fine, my lord.','L21', 'left','position:absolute;right:-320px;top:300px;width:330px')}
  </div>
  {gap(170)}
  <div class="rel" style="margin-left:330px">{img('p20','', 'width:720px;height:1080px')}
    {bub('The Order has a name for what you are. Hollow-born. They have hunted your kind for three hundred years. Those twelve riders are not coming to measure you, Lucan.','L22', 'right','position:absolute;left:-310px;top:480px;width:470px')}
  </div>
  {gap(200)}
  <div class="rel" style="margin-left:210px">{img('p21','', 'width:660px;height:660px')}</div>
  {gap(40)}
  {bub('They are coming to take you.','L23', 'up','position:relative;margin-left:420px;width:360px')}
  {gap(130)}
  <div class="rel" data-a="L24">{img('p22','full')}
    {narr('Outside the window, the barley moved in the wind. A hundred and twelve people were bringing in the harvest. Every one of them mine.','', 'position:absolute;left:220px;width:640px;bottom:-200px')}
  </div>
  {gap(280)}
  <div class="rel" data-a="L25" style="margin-left:0">{img('p23','', 'width:720px;height:1080px')}
    {narr('And every one of them, I realised, was now in danger. Because of me.','', 'position:absolute;right:-330px;width:400px;top:520px')}
  </div>
  {gap(180)}
  <div class="rel" style="margin-left:330px">{img('p24','', 'width:720px;height:1080px')}
    {bub("Then they'll have to get past Greyhollow first.",'L26', 'right','position:absolute;left:-290px;top:500px;width:360px')}
  </div>
  {gap(320, 'linear-gradient(#fff,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L27" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 15 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
