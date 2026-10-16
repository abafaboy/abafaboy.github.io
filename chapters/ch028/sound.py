"""Chapter 28 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("realm", 0, T0(4), fade_in=0.8)
S("candle_fire", 0, 0.1, length=T0(10), fade_in=1.0, fade_out=1.5)
M("labour", T0(4), T0(7), fade_in=0.6)
M("mystery", T0(7), T0(10), fade_in=0.6)
M("dread", T0(10), T0(13), fade_in=0.6, nothing_at=at(11) - T0(10) + 0.2)
S("candle_fire", T0(10), 0.1, length=T0(13) - T0(10), fade_in=0.8, fade_out=0.8)
M("mockery", T0(13), T0(15), gain=0.85, fade_in=0.4)
S("coins", at(13, 0.4), 0.3)
S("paper_rustle_1", at(13, 0.1), 0.25)
M("tender", T0(15), T0(16), fade_in=0.6)
M("outro", T0(16), END, fade_in=0.8, fade_out=2.0)
