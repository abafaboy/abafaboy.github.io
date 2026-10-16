"""Chapter 73 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(2), fade_in=0.6)
M("battle", T0(2), T0(10), fade_in=0.3)
S("sword_draw", at(3, 0.8), 0.3)
S("crowd_gasp", at(6, 0.5), 0.2)
M("triumph", T0(10), T0(12), fade_in=0.3)
M("tender", T0(12), T0(17), fade_in=0.6)
M("wry", T0(17), T0(19), fade_in=0.3)
S("wood_creak", at(18, 0.4), 0.25)
M("tender", T0(19), T0(22), fade_in=0.5)
M("wry", T0(22), T0(24), fade_in=0.3)
M("dread", T0(24), T0(26), fade_in=0.5, nothing_at=at(25, 0.3) - T0(24))
M("outro", T0(26), END, fade_in=0.8, fade_out=2.0)
