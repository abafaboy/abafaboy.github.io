"""Chapter 92 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("sorrow", 0, T0(3), fade_in=0.8)
S("candle_fire", 0, 0.1, length=T0(15), fade_in=1.0, fade_out=1.0)
M("cold", T0(3), T0(8), fade_in=0.5)
M("tender", T0(8), T0(12), fade_in=0.6)
M("sorrow", T0(12), T0(15), fade_in=0.6)
M("mystery", T0(15), T0(19), fade_in=0.5)
M("wry", T0(19), T0(21), fade_in=0.4)
S("man_chuckle", at(20, 0.9), 0.2)
M("labour", T0(21), T0(23), fade_in=0.5)
S("candle_fire", T0(21), 0.12, length=T0(23) - T0(21), fade_in=0.8, fade_out=1.0)
S("crowd_murmur_1", at(22, 0.1), 0.1, length=T0(23) - at(22, 0.1), fade_in=0.8, fade_out=1.0)
M("outro", T0(23), END, fade_in=0.8, fade_out=2.0)
