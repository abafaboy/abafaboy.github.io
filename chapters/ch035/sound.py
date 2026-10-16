"""Chapter 35 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("frost", 0, T0(2), fade_in=0.8)
S("wind_winter", 0, 0.12, length=T0(2) + 1, fade_in=1.0, fade_out=1.0)
M("wry", T0(2), T0(6), fade_in=0.4)
M("mystery", T0(6), T0(12), fade_in=0.6)
S("footsteps_stone", at(6, 0.2), 0.25, length=4, fade_out=1.0)
S("magic_shimmer", at(7, 0.3), 0.3)
M("dread", T0(12), T0(15), fade_in=0.4, nothing_at=at(13) - T0(12))
S("heartbeat", at(13), 0.3, length=6, fade_out=1.5)
M("cold", T0(15), T0(19), fade_in=0.6)
M("dread", T0(19), T0(21), fade_in=0.4, nothing_at=at(20) - T0(19))
M("outro", T0(21), END, fade_in=0.8, fade_out=2.0)
