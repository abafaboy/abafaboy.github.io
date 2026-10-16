"""Chapter 32 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("cold", 0, T0(4), fade_in=0.8)
S("wind_winter", 0, 0.12, length=T0(4), fade_in=1.0, fade_out=1.0)
M("reveal", T0(4), T0(6), fade_in=0.4, hit_at=at(5) - T0(4) + 0.3)
S("crowd_murmur_1", at(5), 0.12, length=4, fade_in=0.5, fade_out=1.5)
M("wry", T0(6), T0(9), fade_in=0.3)
M("tender", T0(9), T0(13), fade_in=0.6)
S("magic_shimmer", at(12, 0.6), 0.3)
M("mystery", T0(13), T0(16), fade_in=0.6)
M("cold", T0(16), T0(19), fade_in=0.4)
S("crowd_murmur_2", T0(16), 0.1, length=T0(19) - T0(16), fade_in=1.0, fade_out=1.0)
M("wry", T0(19), T0(21), fade_in=0.3)
M("outro", T0(21), END, fade_in=0.8, fade_out=2.0)
