"""Chapter 66 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("mystery", 0, T0(1), fade_in=0.8)
S("candle_fire", 0, 0.1, length=T0(24), fade_in=1.0, fade_out=2.0)
M("dread", T0(1), T0(3), fade_in=0.3, nothing_at=at(1) - T0(1) + 0.2)
M("cold", T0(3), T0(6), fade_in=0.5)
M("sorrow", T0(6), T0(11), fade_in=0.6)
M("mystery", T0(11), T0(15), fade_in=0.5)
S("heartbeat", at(12), 0.2, length=5, fade_in=0.3, fade_out=1.5)
M("tender", T0(15), T0(24), fade_in=0.6)
M("reveal", T0(24), T0(26), fade_in=0.4, hit_at=at(25) - T0(24) + 0.1)
M("outro", T0(26), END, fade_in=0.8, fade_out=2.0)
