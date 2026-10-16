"""Chapter 97 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("mystery", 0, T0(3), fade_in=0.8)
S("wood_creak", at(2, 0.3), 0.25)
M("tender", T0(3), T0(7), fade_in=0.6)
M("wry", T0(7), T0(9), fade_in=0.3)
S("woman_laugh_1", at(8, 0.9), 0.15)
M("sorrow", T0(9), T0(12), fade_in=0.6)
M("cold", T0(12), T0(15), fade_in=0.5)
M("wry", T0(15), T0(17), fade_in=0.3)
M("mystery", T0(17), T0(20), fade_in=0.5)
S("footsteps_stone", at(17, 0.1), 0.2, length=4, fade_out=1.0)
S("magic_shimmer", at(18, 0.5), 0.15)
M("outro", T0(20), END, fade_in=0.8, fade_out=2.0)
