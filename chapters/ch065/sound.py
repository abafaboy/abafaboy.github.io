"""Chapter 65 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("realm", 0, T0(2), fade_in=0.8)
M("cold", T0(2), T0(8), fade_in=0.5)
S("candle_fire", T0(2), 0.1, length=T0(16) - T0(2), fade_in=1.0, fade_out=1.5)
M("wry", T0(8), T0(9), fade_in=0.3)
M("dread", T0(9), T0(16), fade_in=0.5, nothing_at=at(15) - T0(9))
M("frost", T0(16), T0(18), fade_in=0.6)
S("wind_winter", T0(16), 0.08, length=T0(22) - T0(16), fade_in=1.5, fade_out=1.5)
S("footsteps_stone", at(16, 0.6), 0.25)
M("mystery", T0(18), T0(22), fade_in=0.5)
S("wood_creak", at(21, 0.1), 0.3)
M("reveal", T0(22), T0(25), fade_in=0.4, hit_at=at(24) - T0(22) + 0.1)
M("outro", T0(25), END, fade_in=0.8, fade_out=2.0)
