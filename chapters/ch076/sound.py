"""Chapter 76 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("mystery", 0, T0(2), fade_in=0.8)
M("wry", T0(2), T0(5), fade_in=0.3)
S("magic_shimmer", at(3) + 0.1, 0.25)
S("wood_creak", at(3, 0.75), 0.3)
M("wry", T0(5), T0(13), fade_in=0.4)
S("magic_shimmer", at(6) + 0.1, 0.3)
M("tender", T0(13), T0(14), fade_in=0.6)
M("reveal", T0(14), T0(18), fade_in=0.4, hit_at=at(15) - T0(14) + 0.1)
M("dread", T0(18), T0(21), fade_in=0.3, nothing_at=at(19) - T0(18))
S("stone_crack", at(18, 0.15), 0.4)
M("outro", T0(21), END, fade_in=0.8, fade_out=2.0)
