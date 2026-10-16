"""Chapter 67 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("battle", 0, T0(3), fade_in=0.4)
S("candle_fire", 0, 0.2, length=T0(6), fade_in=0.5, fade_out=0.5)
S("crowd_gasp", at(1, 0.6), 0.2)
M("dread", T0(3), T0(7), fade_in=0.4, nothing_at=at(6, 0.4) - T0(3))
M("sorrow", T0(7), T0(9), fade_in=0.5)
M("tender", T0(9), T0(12), fade_in=0.6)
M("cold", T0(12), T0(15), fade_in=0.5)
M("sorrow", T0(15), T0(19), fade_in=0.6)
M("wry", T0(19), T0(20), fade_in=0.3)
M("dread", T0(20), T0(22), fade_in=0.6, nothing_at=at(21, 0.7) - T0(20))
S("wind_winter", T0(20), 0.08, length=T0(22) - T0(20) + 1.0, fade_in=1.0, fade_out=1.5)
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
