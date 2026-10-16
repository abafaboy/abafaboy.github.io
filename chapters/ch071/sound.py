"""Chapter 71 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(1), fade_in=0.6)
M("realm", T0(1), T0(3), fade_in=0.5)
S("crowd_murmur_2", T0(1), 0.12, length=T0(13) - T0(1), fade_in=1.0, fade_out=1.5)
S("woman_laugh_2", at(1, 0.9), 0.2)
M("cold", T0(3), T0(6), fade_in=0.5)
M("wry", T0(6), T0(13), fade_in=0.3)
M("mystery", T0(13), T0(19), fade_in=0.5)
S("man_chuckle", at(18, 0.6), 0.25)
M("cold", T0(19), T0(20), fade_in=0.4)
M("dread", T0(20), T0(22), fade_in=0.5, nothing_at=at(21) - T0(20))
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
