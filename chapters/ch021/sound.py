"""Chapter 21 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("mystery", 0, T0(4), fade_in=0.8)
S("wind_winter", 0, 0.1, length=T0(9), fade_in=1.5, fade_out=1.5)
M("reveal", T0(4), T0(6), fade_in=0.6, hit_at=at(4) - T0(4) + 1.0)
S("magic_shimmer", at(4, 0.2), 0.35)
M("cold", T0(6), T0(9), fade_in=0.6)
S("paper_rustle_1", at(6, 0.5), 0.3)
M("frost", T0(9), T0(12), fade_in=0.3)
S("heartbeat", at(9), 0.35, length=6, fade_out=2)
M("sorrow", T0(12), T0(15), fade_in=0.8)
M("dread", T0(15), T0(16), fade_in=0.6, nothing_at=at(15) - T0(15) + 3)
M("outro", T0(16), END, fade_in=0.8, fade_out=2.0)
