"""Chapter 50 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(6), fade_in=0.6)
S("man_chuckle", at(2, 0.6), 0.25)
M("mystery", T0(6), T0(11), fade_in=0.6)
S("magic_shimmer", at(8, 0.4), 0.3)
M("reveal", T0(11), T0(13), fade_in=0.4, hit_at=at(12) - T0(11) + 0.2)
M("cold", T0(13), T0(16), fade_in=0.5)
S("candle_fire", T0(13), 0.1, length=T0(21) - T0(13), fade_in=1.0, fade_out=1.0)
M("wry", T0(16), T0(19), fade_in=0.4)
M("dread", T0(19), T0(21), fade_in=0.6, nothing_at=at(20) - T0(19) + 0.1)
M("outro", T0(21), END, fade_in=0.8, fade_out=2.0)
