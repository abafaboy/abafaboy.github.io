"""Chapter 39 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("tender", 0, T0(2), fade_in=0.8)
S("footsteps_stone", 0.4, 0.2, length=4, fade_out=1.0)
M("sorrow", T0(2), T0(4), fade_in=0.6)
S("candle_fire", T0(2), 0.09, length=T0(16) - T0(2), fade_in=1.0, fade_out=1.0)
M("mystery", T0(4), T0(8), fade_in=0.6)
M("wry", T0(8), T0(10), fade_in=0.3)
M("dawn", T0(10), T0(13), fade_in=0.6)
S("magic_shimmer", at(11, 0.3), 0.25)
M("tender", T0(13), T0(16), fade_in=0.6)
M("cold", T0(16), T0(19), fade_in=0.4)
S("crowd_murmur_2", T0(16), 0.14, length=at(19) - T0(16), fade_in=1.0, fade_out=1.0)
M("outro", T0(19), END, fade_in=0.8, fade_out=2.0)
