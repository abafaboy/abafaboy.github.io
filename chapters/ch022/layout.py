"""Chapter 22 layout."""
FACES = {
    "x01": [(555, 595, 1035, 725)],
    "x02": [(335, 270, 565, 570), (780, 0, 1080, 315)],
    "x03": [(125, 75, 890, 360)],
    "x04": [(15, 255, 405, 660), (540, 85, 955, 560)],
    "x05": [(830, 140, 1290, 545)],
    "x06": [(505, 180, 835, 590), (710, 750, 970, 970)],
    "x07": [(130, 140, 620, 600)],
    "x08": [(75, 260, 165, 350), (1160, 485, 1495, 860)],
    "x09": [(515, 340, 750, 605), (860, 135, 1135, 425)],
    "x10": [(420, 10, 620, 230)],
    "x11": [(90, 40, 650, 660)],
    "x12": [(105, 160, 375, 395), (1125, 115, 1320, 340)],
    "x13": [(160, 440, 540, 790)],
    "x14": [(110, 80, 720, 730)],
    "x15": [(225, 50, 445, 315)],
    "x16": [(60, 300, 215, 470), (325, 300, 470, 470), (835, 435, 980, 590), (1000, 310, 1135, 470), (1230, 250, 1375, 420)],
}

def build():
    return f"""
<div class="sec white" style="background:#eef4fa">
  <div class="chap"><div class="c0">THE LORD WHO MEASURED ZERO</div><div class="c1">CHAPTER 22</div><div class="c2">The Pale Moves</div></div>
  {gap(100)}
  {narr('Wren told me the story afterwards, the way she tells everything. Short, and with far too much about arrows.','L0', 'margin:0 120px')}
  {gap(40)}
  <div class="rel" data-a="L0b">{img('x01','full')}</div>
  {gap(440)}
  <div class="rel">{img('x02','full')}
    {bub("This stone marked the edge of the Pale when my father hunted here. It's a mile inside the ice now.",'L1', 'left','position:absolute;left:120px;top:-380px;width:620px')}
    {bub('So the Pale moved?','L2', 'left','position:absolute;right:30px;top:-230px;width:290px')}
    {bub('The Pale moved.','L3', 'up','position:absolute;left:200px;bottom:-150px;width:300px')}
  </div>
  {gap(250)}
  {narr("And everything that lived in it was running. Elk, foxes, frost-wolves. All running south, straight past the hunters, as if they weren't even there.",'L4', 'margin:0 100px')}
  {gap(40)}
  <div class="rel" data-a="L4b">{img('x03','full')}</div>
  {gap(400)}
  <div class="rel" style="margin-left:300px">{img('x04','', 'width:660px;height:660px')}
    {bub("That's not normal, is it.",'L5', 'left','position:absolute;right:-90px;top:-220px;width:360px')}
    {bub('Nothing that runs from wolves runs with wolves, Dunn.','L6', 'up','position:absolute;left:-280px;top:440px;width:440px')}
  </div>
  {gap(240)}
  <div class="rel" data-a="L7">{img('x05','full')}
    {sfx('KRRAASH!','left:30px;top:470px;transform:rotate(-8deg);font-size:100px')}
    {narr('Then the trees broke apart.','', 'position:absolute;left:420px;width:520px;bottom:-120px')}
  </div>
  {gap(240)}
  <div class="rel" style="margin-left:0">{img('x06','', 'width:720px;height:1080px')}
    {bub('Argh!','L8', 'left','position:absolute;right:-310px;top:430px;width:320px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L9" style="margin-left:330px">{img('x07','', 'width:720px;height:1080px')}
    {narr("Wren said she didn't think. She just shot.",'', 'position:absolute;left:-300px;top:560px;width:400px')}
  </div>
  {gap(160)}
  <div class="rel" data-a="L10">{img('x08','full')}
    {sfx('THOOM!','left:50px;top:450px;transform:rotate(-6deg);font-size:100px')}
    {narr('One arrow. Through the eye.','', 'position:absolute;left:480px;width:520px;bottom:-120px')}
  </div>
  {gap(240)}
  <div class="rel">{img('x09','full')}
    {bub('Ow. Ow! Did you see that? I think it liked me.','L11', 'up','position:absolute;left:40px;bottom:-200px;width:440px')}
    {bub('Shut up and hold still.','L12', 'up','position:absolute;right:200px;bottom:-330px;width:340px')}
  </div>
  {gap(430)}
  <div class="rel" data-a="L13">{img('x10','full')}
    {narr('That was when they saw him. A man painted white, standing between the frozen trees, with a spear in his hand.','', 'position:absolute;left:220px;width:640px;bottom:-280px')}
  </div>
  {gap(380)}
  <div class="rel" style="margin-left:0">{img('x11','', 'width:660px;height:660px')}
    {bub('You killed the white bear. Good. It would have followed you home.','L14', 'left','position:absolute;right:-340px;top:100px;width:420px')}
  </div>
  {gap(160)}
  <div class="rel">{img('x12','full')}
    {bub('Who are you?','L15', 'up','position:absolute;left:60px;bottom:-150px;width:300px')}
    {bub('Kell. Of the Skeld. The people of the White.','L16', 'up','position:absolute;right:40px;bottom:-310px;width:420px')}
  </div>
  {gap(400)}
  <div class="rel" style="margin-left:330px">{img('x13','', 'width:720px;height:1080px')}
    {bub('You are hunters from the warm valley. The one where the snow is melting.','L17', 'right','position:absolute;left:-300px;top:-40px;width:500px')}
    {bub('How do you know about that?','L18', 'left','position:absolute;left:-310px;top:350px;width:330px')}
    {bub('Everyone in the White knows. The animals know. That is why they are running toward it.','L19', 'up','position:absolute;left:-300px;top:680px;width:480px')}
  </div>
  {gap(160)}
  <div class="rel" style="margin-left:0">{img('x14','', 'width:660px;height:660px')}
    {bub('Go home, hunter. Tell your warm lord this.','L20', 'left','position:absolute;right:-340px;top:60px;width:400px')}
    {bub('The White is waking.','L21', 'left','position:absolute;right:-320px;top:420px;width:340px')}
  </div>
  {gap(300, 'linear-gradient(#eef4fa,#1b2236)')}
</div>
<div class="sec night" style="background:#1b2236">
  <div class="rel">{img('x15','full')}
    {bub("You're coming with us. You can tell him yourself.",'L22', 'up','position:absolute;left:20px;bottom:-230px;width:460px')}
  </div>
  {gap(330)}
  <div class="rel" data-a="L23">{img('x16','full')}
    {narr("They turned for home that same night, with a stranger, a dead bear's claw, and Dunn complaining the whole way.",'', 'position:absolute;left:200px;width:680px;bottom:-220px')}
  </div>
  {gap(320, 'linear-gradient(#1b2236,#05060a)')}
</div>
<div class="sec black">
  <div class="rel" data-a="L24" style="margin-left:120px">{img('end','', 'width:840px;height:1260px')}
    <div class="title"><div class="t1">THE LORD<br>WHO MEASURED</div><div class="t2">ZERO</div><div class="t3">CHAPTER 23 · COMING SOON</div></div>
  </div>
  {gap(360)}
</div>
"""
