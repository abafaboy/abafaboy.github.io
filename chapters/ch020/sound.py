"""Chapter 20 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(6), fade_in=0.6)
S("woman_laugh_2", at(0, 0.5), 0.2)
S("woman_laugh_1", at(1, 0.4), 0.25)
M("tender", T0(6), T0(8), fade_in=0.6)
M("sorrow", T0(8), T0(14), fade_in=0.8)
M("tender", T0(14), T0(15), fade_in=0.6)
S("dog_whimper", at(14, 0.2), 0.2)
M("mystery", T0(15), T0(17), fade_in=0.6)
S("candle_fire", T0(16), 0.12, length=T0(17) - T0(16) + 0.5, fade_in=0.5, fade_out=0.8)
M("outro", T0(17), END, fade_in=0.8, fade_out=2.0)
