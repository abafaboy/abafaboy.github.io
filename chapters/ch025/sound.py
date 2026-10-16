"""Chapter 25 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("cold", 0, T0(4), fade_in=0.6)
S("crowd_murmur_1", 0, 0.1, length=T0(4), fade_in=1.0, fade_out=1.0)
M("triumph", T0(4), T0(6), fade_in=0.2)
S("crowd_cheer_1", at(5) - 0.2, 0.35, length=4, fade_out=1.5)
M("mystery", T0(6), T0(8), fade_in=0.6)
M("dread", T0(8), T0(11), fade_in=0.6, nothing_at=at(10) - T0(8) - 0.2)
M("tender", T0(11), T0(13), fade_in=0.6)
M("frost", T0(13), T0(15), fade_in=0.4)
M("sorrow", T0(15), T0(16), fade_in=0.6)
S("wind_winter", T0(15), 0.12, length=T0(16) - T0(15) + 1, fade_in=1.0, fade_out=1.0)
M("outro", T0(16), END, fade_in=0.8, fade_out=2.0)
