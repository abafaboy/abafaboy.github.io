"""Chapter 34 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("cold", 0, T0(2), fade_in=0.6)
S("wind_winter", 0, 0.1, length=T0(2) + 1, fade_in=0.5, fade_out=1.0)
M("frost", T0(2), T0(9), fade_in=0.4)
S("heartbeat", at(2), 0.3, length=5, fade_out=1.5)
M("sorrow", T0(9), T0(14), fade_in=0.6)
M("tender", T0(14), T0(17), fade_in=0.6)
M("wry", T0(17), T0(19), fade_in=0.3)
S("wolf_howl_1", at(17, 0.8), 0.2)
M("mystery", T0(19), T0(22), fade_in=0.6)
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
