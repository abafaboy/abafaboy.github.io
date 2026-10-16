"""Chapter 68 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("realm", 0, T0(2), fade_in=0.8)
M("wry", T0(2), T0(5), fade_in=0.3)
S("woman_laugh_1", at(4) - 0.4, 0.2)
M("wry", T0(5), T0(11), fade_in=0.4)
M("tender", T0(11), T0(12), fade_in=0.5)
M("cold", T0(12), T0(18), fade_in=0.5)
M("wry", T0(18), T0(20), fade_in=0.3)
M("dread", T0(20), T0(22), fade_in=0.4, nothing_at=at(20, 0.9) - T0(20))
M("mystery", T0(22), T0(23), fade_in=0.5)
S("wind_winter", T0(22), 0.08, length=T0(23) - T0(22) + 1.0, fade_in=1.0, fade_out=1.5)
M("outro", T0(23), END, fade_in=0.8, fade_out=2.0)
