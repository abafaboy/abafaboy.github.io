"""Chapter 1 sound: music cues and sound effects, keyed to line indices."""
t_tri, t_dread, t_mock, t_cold = at(4) - 0.3, at(5) - 0.2, at(8) - 0.2, at(10) - 0.25
M("realm", 0, t_tri, fade_in=0.8, fade_out=1.5)
M("triumph", t_tri, t_dread, fade_in=0.05)
M("dread", t_dread, t_mock, gain=1.1, fade_in=0.6, nothing_at=at(6) - t_dread)
M("mockery", t_mock, t_cold, gain=0.9, fade_in=0.3)
S("crowd_murmur", at(1), 0.10, length=at(4) - at(1), fade_in=1.5, fade_out=1.5)
S("magic_shimmer", at(2, 0.05), 0.25)
S("crowd_cheer_2", at(4, frac_after(4, "lit five.")), 0.5, length=3.5, fade_out=1.5)
S("footsteps_stone", at(5) - 0.1, 0.35, length=3.2)
S("heartbeat", at(5, 0.6), 0.55, length=at(7, 1.0) - at(5, 0.6), fade_out=1.5)
S("woman_laugh_2", at(8, frac_after(8, "someone laughed.")) - 0.1, 0.55, length=3.0, fade_out=0.8)

# ---- rest of chapter 1 (lines 10-30) ----
def T0(i, pad=0.3): return at(i) - pad
if LAST >= 30:
    M("cold", t_cold, T0(11), fade_in=0.6)
    M("frost", T0(11), T0(14), fade_in=1.0, fade_out=1.2)
    S("wind_winter", T0(11), 0.22, length=T0(14) - T0(11) + 1, fade_in=1.5, fade_out=1.5)
    S("coins", at(12, frac_after(12, "four thousand crowns")), 0.3)
    S("paper_rustle_1", at(13) - 0.2, 0.4)
    M("wry", T0(14), T0(17), gain=0.9, fade_in=0.3)
    S("wood_creak", at(14) - 0.3, 0.4)
    M("tender", T0(17), T0(20), fade_in=1.0, fade_out=1.5)
    S("dog_whimper", at(17, frac_after(17, "I found a wolfhound.")), 0.45)
    S("magic_shimmer", at(19, frac_after(19, "thumped its tail once.")), 0.3)
    M("mystery", T0(20), T0(24), fade_in=1.2)
    S("candle_fire", T0(20), 0.12, length=T0(24) - T0(20), fade_in=1.5, fade_out=1.5)
    S("stone_crack", at(21) - 0.4, 0.55)
    M("dawn", T0(24), T0(28), gain=0.95, fade_in=0.05)
    S("dog_growl", at(24, 0.7), 0.25, length=2.5, fade_out=1.0)
    M("reveal", T0(28), T0(30), fade_in=1.0, hit_at=at(29) - T0(28))
    S("magic_shimmer", at(29) - 0.1, 0.4)
    M("outro", T0(30), END, fade_in=0.8, fade_out=2.0)
else:
    M("cold", t_cold, END, fade_in=0.6, fade_out=2.0)
