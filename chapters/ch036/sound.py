"""Chapter 36 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("mystery", 0, T0(2), fade_in=0.8)
S("footsteps_stone", 0.3, 0.25, length=4, fade_out=1.0)
M("wry", T0(2), T0(5), fade_in=0.4)
M("mystery", T0(5), T0(7), fade_in=0.6)
M("reveal", T0(7), T0(10), fade_in=0.4, hit_at=at(8) - T0(7) + 0.3)
M("frost", T0(10), T0(14), fade_in=0.6)
M("tender", T0(14), T0(17), fade_in=0.6)
M("dread", T0(17), T0(22), fade_in=0.3, nothing_at=at(17) - T0(17) + 0.5)
S("stone_crack", at(17, 0.4), 0.4)
S("heartbeat", at(20), 0.3, length=T0(22) - at(20) + 1, fade_out=1.5)
M("outro", T0(22), END, fade_in=0.8, fade_out=2.0)
