"""Chapter 19 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(7), fade_in=0.6)
S("crowd_murmur_1", 0, 0.1, length=T0(7), fade_in=1.0, fade_out=1.0)
S("man_chuckle", at(4, 0.5), 0.3)
M("cold", T0(7), T0(11), fade_in=0.6)
M("dread", T0(11), T0(14), fade_in=0.4, nothing_at=at(14) - T0(11) - 0.4)
S("heartbeat", at(11), 0.3, length=at(14) - at(11), fade_out=1.0)
M("tender", T0(14), T0(16), fade_in=0.6)
M("wry", T0(16), T0(18), fade_in=0.3)
S("man_chuckle", at(17, 0.5), 0.3)
M("mystery", T0(18), T0(20), fade_in=0.6)
M("outro", T0(20), END, fade_in=0.8, fade_out=2.0)
