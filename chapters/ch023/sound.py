"""Chapter 23 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(3), fade_in=0.6)
S("crowd_murmur_1", 0, 0.1, length=T0(3), fade_in=1.0, fade_out=1.0)
S("magic_shimmer", at(1, 0.1), 0.3)
M("cold", T0(3), T0(5), fade_in=0.6)
M("sorrow", T0(5), T0(9), fade_in=0.6)
M("cold", T0(9), T0(12), fade_in=0.6)
S("crowd_murmur_2", T0(9), 0.15, length=T0(12) - T0(9), fade_in=0.8, fade_out=1.0)
S("candle_fire", T0(9), 0.1, length=T0(15) - T0(9), fade_in=1.0, fade_out=1.0)
M("tender", T0(12), T0(14), fade_in=0.6)
M("frost", T0(14), T0(15), fade_in=0.6)
M("outro", T0(15), END, fade_in=0.8, fade_out=2.0)
