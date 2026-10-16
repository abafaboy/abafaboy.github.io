"""Chapter 75 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("mystery", 0, T0(1), fade_in=0.8)
S("candle_fire", 0, 0.1, length=T0(8), fade_in=1.0, fade_out=1.0)
M("wry", T0(1), T0(8), fade_in=0.3)
M("mystery", T0(8), T0(12), fade_in=0.5)
M("cold", T0(12), T0(14), fade_in=0.4)
M("reveal", T0(14), T0(16), fade_in=0.4, hit_at=at(15, 0.15) - T0(14))
M("wry", T0(16), T0(20), fade_in=0.3)
S("paper_rustle_1", at(17, 0.6), 0.2)
M("triumph", T0(20), T0(21), fade_in=0.3)
M("wry", T0(21), T0(22), fade_in=0.3)
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
