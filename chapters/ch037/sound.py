"""Chapter 37 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("battle", 0, T0(9), fade_in=0.1)
S("stone_crack", 0.1, 0.45)
S("dog_growl", at(5, 0.6), 0.35, length=2)
S("dog_whimper", at(5, 0.95), 0.25)
S("stone_crack", at(8, 0.7), 0.45)
M("dread", T0(9), T0(13), fade_in=0.2, nothing_at=at(9) - T0(9) + 0.3)
S("wind_winter", at(10), 0.1, length=T0(15) - at(10), fade_in=1.5, fade_out=1.5)
M("tender", T0(13), T0(15), fade_in=0.6)
M("mystery", T0(15), T0(20), fade_in=0.6)
M("frost", T0(20), T0(23), fade_in=0.6)
S("heartbeat", at(21), 0.3, length=T0(23) - at(21) + 1, fade_out=1.5)
M("outro", T0(23), END, fade_in=0.8, fade_out=2.0)
