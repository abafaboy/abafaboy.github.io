"""Chapter 24 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("tender", 0, T0(8), fade_in=0.8)
S("candle_fire", 0, 0.1, length=T0(19), fade_in=1.0, fade_out=1.5)
S("magic_shimmer", at(5, 0.3), 0.25)
M("cold", T0(8), T0(12), fade_in=0.6)
M("mystery", T0(12), T0(14), fade_in=0.6)
S("paper_rustle_1", at(12, 0.2), 0.3)
M("reveal", T0(14), T0(17), fade_in=0.4, hit_at=at(14) - T0(14) + 0.3)
M("tender", T0(17), T0(19), fade_in=0.6)
S("magic_shimmer", at(17, 0.5), 0.35)
M("outro", T0(19), END, fade_in=0.8, fade_out=2.0)
