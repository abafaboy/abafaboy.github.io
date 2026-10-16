"""Chapter 96 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("dread", 0, T0(3), fade_in=0.8, nothing_at=at(2) + 0.2)
S("wind_winter", 0, 0.08, length=T0(22), fade_in=1.5, fade_out=1.5)
M("cold", T0(3), T0(7), fade_in=0.5)
S("magic_shimmer", at(3, 0.3), 0.15)
M("sorrow", T0(7), T0(11), fade_in=0.6)
M("frost", T0(11), T0(15), fade_in=0.5)
S("footsteps_stone", at(11, 0.1), 0.15, length=4, fade_out=1.0)
M("sorrow", T0(15), T0(18), fade_in=0.6)
M("tender", T0(18), T0(20), fade_in=0.6)
M("mystery", T0(20), T0(22), fade_in=0.5)
S("footsteps_stone", at(20, 0.2), 0.2, length=5, fade_out=1.5)
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
