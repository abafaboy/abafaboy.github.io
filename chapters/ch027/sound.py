"""Chapter 27 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("sorrow", 0, T0(1), fade_in=0.8)
M("tender", T0(1), T0(9), fade_in=0.6)
M("wry", T0(9), T0(10), fade_in=0.3)
S("man_chuckle", at(9, 0.8), 0.25)
M("dawn", T0(10), T0(11), fade_in=0.6)
M("cold", T0(11), T0(13), fade_in=0.4)
M("tender", T0(13), T0(15), fade_in=0.6)
M("realm", T0(15), T0(16), fade_in=0.6)
M("wry", T0(16), T0(19), fade_in=0.4)
S("dog_whimper", at(16) - 0.2, 0.2)
M("outro", T0(19), END, fade_in=0.8, fade_out=2.0)
