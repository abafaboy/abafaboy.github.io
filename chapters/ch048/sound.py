"""Chapter 48 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("wry", 0, T0(3), fade_in=0.6)
S("crowd_murmur_1", 0, 0.1, length=T0(2), fade_in=1.0, fade_out=1.0)
M("realm", T0(3), T0(8), fade_in=0.5)
S("crowd_murmur_2", T0(3), 0.12, length=T0(5) - T0(3), fade_in=0.8, fade_out=1.0)
S("man_chuckle", at(6, 0.85), 0.25)
M("wry", T0(8), T0(12), fade_in=0.4)
M("mystery", T0(12), T0(18), fade_in=0.6)
S("magic_shimmer", at(16) - 0.2, 0.25)
S("dog_growl", at(17) - 0.3, 0.4, length=2.5)
M("wry", T0(18), T0(21), fade_in=0.4)
M("dread", T0(21), T0(22), fade_in=0.6, nothing_at=at(21, 0.92) - T0(21))
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
