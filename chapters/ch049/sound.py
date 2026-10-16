"""Chapter 49 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("realm", 0, T0(1), fade_in=0.8)
S("crowd_murmur_2", 0, 0.12, length=T0(8), fade_in=1.0, fade_out=1.0)
S("candle_fire", 0, 0.08, length=T0(20), fade_in=1.0, fade_out=1.5)
M("wry", T0(1), T0(8), fade_in=0.4)
S("crowd_gasp", at(1, 0.65), 0.25)
S("woman_laugh_1", at(7, 0.5), 0.22)
M("realm", T0(8), T0(13), fade_in=0.6)
M("mockery", T0(13), T0(17), fade_in=0.3)
S("man_chuckle", at(13, 0.3), 0.35)
M("cold", T0(17), T0(18), fade_in=0.4)
M("wry", T0(18), T0(20), fade_in=0.4)
M("outro", T0(20), END, fade_in=0.8, fade_out=2.0)
