"""Chapter 77 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("realm", 0, T0(2), fade_in=0.8)
S("crowd_murmur_2", 0, 0.1, length=T0(5), fade_in=1.0, fade_out=1.5)
M("wry", T0(2), T0(5), fade_in=0.3)
S("woman_laugh_1", at(3, 0.95), 0.2)
M("mystery", T0(5), T0(10), fade_in=0.5)
M("cold", T0(10), T0(12), fade_in=0.5)
M("dread", T0(12), T0(18), fade_in=0.5, nothing_at=at(17) - T0(12))
S("coins", at(15, 0.3), 0.3)
M("mystery", T0(18), T0(22), fade_in=0.5)
S("man_chuckle", at(19, 0.1), 0.2)
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
