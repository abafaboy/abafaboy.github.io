"""Chapter 22 sound."""
def T0(i, pad=0.3): return at(i) - pad
M("frost", 0, T0(5), fade_in=0.8)
S("wind_winter", 0, 0.15, length=T0(16), fade_in=1.5, fade_out=1.5)
S("wolf_howl_1", at(3, 0.5), 0.25)
M("battle", T0(5), T0(9), fade_in=0.1)
S("wood_creak", at(5) - 0.3, 0.4)
S("dog_growl", at(5, 0.2), 0.4, length=2)
S("sword_draw", at(7, 0.7), 0.3)
M("wry", T0(9), T0(10), fade_in=0.3)
M("mystery", T0(10), T0(15), fade_in=0.6)
M("tender", T0(15), T0(17), fade_in=0.6)
M("outro", T0(17), END, fade_in=0.8, fade_out=2.0)
