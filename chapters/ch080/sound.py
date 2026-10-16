"""Chapter 80 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(3), fade_in=0.8)
S("crowd_murmur_1", T0(1), 0.1, length=T0(11) - T0(1), fade_in=1.0, fade_out=1.5)
M("sorrow", T0(3), T0(11), fade_in=0.6)
M("labour", T0(11), T0(16), fade_in=0.5)
M("dawn", T0(16), T0(21), fade_in=0.5)
S("woman_laugh_1", at(20) + 0.1, 0.2)
M("mystery", T0(21), T0(23), fade_in=0.5)
M("outro", T0(23), END, fade_in=0.8, fade_out=2.0)
