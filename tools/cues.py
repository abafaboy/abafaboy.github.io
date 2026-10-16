"""Original cues for The Lord Who Measured Zero. Each returns a stereo array."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from music import Track, reverb, save, SR

def realm(L=34):
    """Processional, D Dorian, 72 bpm: harp arpeggios, strings, recorder tune, choir later."""
    b = 60 / 72; bar = 4 * b
    T = Track(L)
    prog = [("D3", ["D3", "A3", "F4"]), ("C3", ["C3", "G3", "E4"]), ("D3", ["D3", "A3", "F4"]), ("A2", ["A2", "E3", "C4"]),
            ("F2", ["F2", "C3", "A3"]), ("G2", ["G2", "D3", "B3"]), ("D3", ["D3", "A3", "F4"]), ("D3", ["D3", "A3", "D4"]),
            ("Bb2", ["Bb2", "F3", "D4"]), ("C3", ["C3", "G3", "E4"])]
    for k, (bass, ch) in enumerate(prog):
        t = k * bar
        if t > L: break
        T.chord("string_ensemble_1", ch, t, bar, vel=0.22)
        T.note("contrabass", bass[:-1] + str(int(bass[-1]) - 1), t, bar, 0.25)
        arp = [ch[0], ch[1], ch[2], ch[1][:-1] + str(int(ch[1][-1]) + 1), ch[2], ch[1], ch[2], ch[1][:-1] + str(int(ch[1][-1]) + 1)]
        for j, nn in enumerate(arp):
            T.note("orchestral_harp", nn, t + j * b / 2, b / 2, 0.32, pan=0.3)
    tune = [("D5", 1), ("E5", 1), ("F5", 1), ("A5", 1), ("G5", 1.5), ("F5", .5), ("E5", 1), ("C5", 1),
            ("D5", 1), ("F5", 1), ("E5", 1), ("D5", 1), ("A4", 4)]
    t = 0
    for nn, d in tune:
        T.note("recorder", nn, t, d * b * 0.95, 0.30, pan=-0.2); t += d * b
    choir = ["A4", "G4", "A4", "E4", "F4", "G4"]
    for k, nn in enumerate(choir):
        T.note("choir_aahs", nn, (4 + k) * bar, bar, 0.28)
        T.note("choir_aahs", {"A4": "D4", "G4": "B3", "E4": "C4", "F4": "A3"}[nn], (4 + k) * bar, bar, 0.2)
    for k in (6, 7, 8, 9):
        T.note("timpani", "D2", k * bar, 1.5, 0.35)
    return reverb(T.buf[:int(L * SR)], 0.35)

def triumph(L=8):
    """Fanfare in D major for Maric's five rings."""
    b = 60 / 100
    T = Track(L)
    fan = [("D4", .5), ("D4", .5), ("A4", 1), ("D5", .75), ("C#5", .25), ("D5", .5), ("A4", .5), ("F#4", .5), ("A4", .5), ("D5", 3)]
    t = 0.0
    for nn, d in fan:
        T.note("trumpet", nn, t, d * b * 0.9, 0.5); T.note("french_horn", nn[:-1] + str(int(nn[-1]) - 1), t, d * b * 0.9, 0.3)
        t += d * b
    for k in range(12):
        T.note("timpani", "A2" if k % 2 else "D2", k * b / 2, b / 2, 0.25 + 0.03 * k)
    T.chord("string_ensemble_1", ["D3", "F#3", "A3", "D4", "F#4"], 3 * b, 6 * b, 0.25)
    T.chord("church_organ", ["D3", "A3", "D4", "F#4"], 3 * b, 6 * b, 0.18)
    return reverb(T.buf[:int(L * SR)], 0.4)

def dread(L=12, nothing_at=3.7):
    """Low drone, a single bell on 'Nothing.', dissonant cluster after."""
    T = Track(L)
    T.note("cello", "D2", 0, nothing_at, 0.35)
    T.note("contrabass", "D1", 0, nothing_at, 0.3)
    T.note("tubular_bells", "D4", nothing_at, 3, 0.5)
    T.note("tubular_bells", "D3", nothing_at + 0.02, 3, 0.3)
    T.chord("string_ensemble_1", ["D3", "Eb3", "A3"], nothing_at + 1.6, L - nothing_at - 1.6, 0.2)
    T.note("cello", "D2", nothing_at + 1.6, L - nothing_at - 1.6, 0.3)
    for k in range(4):
        T.note("orchestral_harp", ["Eb4", "D4", "A3", "Eb3"][k], nothing_at + 2.4 + k * 1.1, 1.0, 0.18)
    return reverb(T.buf[:int(L * SR)], 0.5)

def mockery(L=12):
    """A sly harpsichord minuet in D minor with pizzicato bass, 3/4 at 120 bpm."""
    b = 0.5
    T = Track(L)
    mel = ["A4", "D5", "E5", "F5", "E5", "D5", "C#5", "A4", "Bb4", "A4", None, None,
           "D5", "F5", "A5", "G5", "F5", "E5", "F5", "D5", "C#5", "D5", None, None]
    bass = ["D3", "A2", "G2", "A2", "D3", "Bb2", "A2", "D3"]
    chords = [["F3", "A3"], ["E3", "A3"], ["G3", "Bb3"], ["E3", "G3"], ["F3", "A3"], ["G3", "Bb3"], ["E3", "G3"], ["F3", "A3"]]
    for k, nn in enumerate(mel):
        if nn and k * b < L: T.note("harpsichord", nn, k * b, b, 0.42, pan=0.2)
    for k, (bs, ch) in enumerate(zip(bass, chords)):
        t = k * 3 * b
        if t > L: break
        T.note("pizzicato_strings", bs, t, b, 0.45, pan=-0.3)
        T.chord("harpsichord", ch, t + b, b * 0.8, 0.22)
        T.chord("harpsichord", ch, t + 2 * b, b * 0.8, 0.2)
    return reverb(T.buf[:int(L * SR)], 0.25)

def cold(L=7):
    """Low strings and a horn: the father's verdict."""
    T = Track(L)
    T.chord("string_ensemble_1", ["D2", "A2", "F3"], 0, L - 1, 0.25)
    T.note("contrabass", "D1", 0, L - 1, 0.3)
    T.note("french_horn", "A2", 0.6, 3.0, 0.3)
    T.note("french_horn", "F2", 3.6, 2.4, 0.28)
    return reverb(T.buf[:int(L * SR)], 0.45)

def frost(L=30):
    """Arrival in Greyhollow: A aeolian, lonely flute over sparse harp, 64 bpm."""
    b = 60 / 64; bar = 4 * b
    T = Track(L)
    prog = [["A2", "E3", "C4"], ["F2", "C3", "A3"], ["G2", "D3", "B3"], ["E2", "B2", "G3"]]
    for k in range(int(L / bar) + 1):
        ch = prog[k % 4]; t = k * bar
        T.chord("string_ensemble_1", ch, t, bar, 0.16)
        for j, nn in enumerate([ch[0], ch[2], ch[1], ch[2]]):
            T.note("orchestral_harp", nn, t + j * b, b, 0.24, pan=0.25)
    tune = [("E5", 2), ("D5", 1), ("C5", 1), ("B4", 3), (None, 1), ("C5", 2), ("D5", 1), ("E5", 1), ("A4", 4),
            ("E5", 2), ("G5", 1), ("F5", 1), ("E5", 3), (None, 1), ("D5", 1.5), ("C5", .5), ("B4", 2), ("A4", 4)]
    t = bar
    for nn, d in tune:
        if nn and t < L: T.note("flute", nn, t, d * b * 0.95, 0.26, pan=-0.2)
        t += d * b
    return reverb(T.buf[:int(L * SR)], 0.45)

def wry(L=25):
    """Bram and the broken stairs: a plucky lute-and-pizzicato jig in D mixolydian, 6/8."""
    e = 0.2  # eighth note
    T = Track(L)
    bass = ["D3", "D3", "C3", "C3", "G2", "G2", "A2", "A2"]
    mel = ["A4", "D5", "E5", "F#5", "E5", "D5", "C5", "D5", "E5", "D5", "C5", "A4",
           "B4", "G4", "B4", "D5", "C5", "B4", "A4", "E5", "C#5", "D5", None, None]
    bar = 6 * e
    for k in range(int(L / bar) + 1):
        t = k * bar
        T.note("pizzicato_strings", bass[k % 8], t, e * 2, 0.4, pan=-0.3)
        T.note("pizzicato_strings", bass[k % 8][:-1] + str(int(bass[k % 8][-1]) + 1), t + 3 * e, e * 2, 0.25, pan=-0.3)
        for j in range(6):
            nn = mel[(k * 6 + j) % len(mel)]
            if nn and (k // 4) % 2 == 0 or (nn and j % 2 == 0):
                T.note("acoustic_guitar_nylon", nn, t + j * e, e * 1.6, 0.34, pan=0.25)
    return reverb(T.buf[:int(L * SR)], 0.25)

def tender(L=25):
    """The kennel: soft recorder over harp, E dorian, 60 bpm."""
    b = 1.0; bar = 4 * b
    T = Track(L)
    prog = [["E3", "B3", "G4"], ["D3", "A3", "F#4"], ["C3", "G3", "E4"], ["A2", "E3", "C#4"]]
    for k in range(int(L / bar) + 1):
        ch = prog[k % 4]; t = k * bar
        T.chord("string_ensemble_1", ch, t, bar, 0.15)
        for j, nn in enumerate([ch[0], ch[1], ch[2], ch[1], ch[2], ch[1], ch[0], ch[1]]):
            T.note("orchestral_harp", nn, t + j * b / 2, b / 2, 0.2, pan=0.3)
    tune = [("B4", 1.5), ("A4", .5), ("G4", 1), ("E4", 1), ("F#4", 2), ("A4", 2), ("G4", 1.5), ("F#4", .5), ("E4", 1), ("C#5", 1), ("B4", 4),
            ("E5", 1.5), ("D5", .5), ("B4", 2), ("A4", 1), ("F#4", 1), ("G4", 2), ("E4", 4)]
    t = bar
    for nn, d in tune:
        if t < L: T.note("recorder", nn, t, d * b * 0.95, 0.24, pan=-0.2)
        t += d * b
    return reverb(T.buf[:int(L * SR)], 0.4)

def mystery(L=25):
    """The vault: low pulsing strings, a slow bell, a low choir; D minor with a flat-second shadow."""
    T = Track(L)
    pulse = 0.75
    for k in range(int(L / pulse)):
        T.note("cello", "D2" if (k // 8) % 2 == 0 else "Eb2", k * pulse, pulse * 0.9, 0.22 + 0.04 * (k % 2 == 0))
    for k in range(int(L / 6) + 1):
        T.note("tubular_bells", ["A4", "Bb4", "A4", "F4"][k % 4], k * 6 + 1, 4, 0.22)
    T.chord("choir_aahs", ["D3", "A3"], 2, L - 3, 0.18)
    T.chord("string_ensemble_1", ["D3", "F3", "A3"], 4, L - 5, 0.13)
    return reverb(T.buf[:int(L * SR)], 0.55)

def dawn(L=22):
    """Morning surprise: bright playful G major, pizzicato, flute and harp, 108 bpm, with a sting at the start."""
    b = 60 / 108
    T = Track(L)
    T.note("timpani", "G2", 0, 1.2, 0.5); T.chord("string_ensemble_1", ["G3", "B3", "D4", "G4"], 0, 1.4, 0.3)
    T.note("tubular_bells", "G4", 0, 2, 0.3)
    bass = ["G2", "D3", "E2", "C3"]
    mel = ["D5", "B4", "G4", "B4", "C5", "A4", "F#4", "A4", "B4", "G4", "E4", "G4", "A4", "F#4", "D4", None]
    for k in range(int((L - 1.5) / b)):
        t = 1.5 + k * b
        if k % 2 == 0: T.note("pizzicato_strings", bass[(k // 4) % 4], t, b, 0.38, pan=-0.3)
        nn = mel[k % len(mel)]
        if nn: T.note("flute" if (k // 16) % 2 else "orchestral_harp", nn, t, b * 0.9, 0.26, pan=0.2)
    return reverb(T.buf[:int(L * SR)], 0.3)

def reveal(L=16, hit_at=12.0):
    """Bram alone, then a swell into 'It lit two.' and a choir-and-timpani hit."""
    T = Track(L)
    T.chord("string_ensemble_1", ["D3", "A3"], 0, hit_at, 0.14)
    for k, nn in enumerate(["D4", "E4", "F4", "G4", "A4", "Bb4", "C5"]):
        t = k * hit_at / 7
        T.note("choir_aahs", nn, t, hit_at / 7 + 0.3, 0.12 + 0.03 * k)
    for k in range(10):
        T.note("timpani", "D2", hit_at - 2 + k * 0.2, 0.2, 0.15 + 0.04 * k)
    T.chord("choir_aahs", ["D3", "A3", "D4", "F#4", "A4"], hit_at, L - hit_at, 0.4)
    T.chord("church_organ", ["D2", "A2", "D3", "F#3"], hit_at, L - hit_at, 0.25)
    T.chord("string_ensemble_1", ["D3", "F#3", "A3", "D4"], hit_at, L - hit_at, 0.3)
    T.note("timpani", "D2", hit_at, 2, 0.6); T.note("tubular_bells", "D4", hit_at, 3, 0.4)
    return reverb(T.buf[:int(L * SR)], 0.5)

def outro(L=10):
    """End card: the processional theme on harp and recorder, resolving."""
    b = 60 / 72
    T = Track(L)
    T.chord("string_ensemble_1", ["D3", "A3", "F4"], 0, 4 * b, 0.2)
    T.chord("string_ensemble_1", ["D3", "A3", "D4"], 4 * b, L - 4 * b, 0.2)
    t = 0
    for nn, d in [("D5", 1), ("E5", 1), ("F5", 1), ("A5", 1), ("G5", 1.5), ("F5", .5), ("E5", 1), ("D5", 3)]:
        T.note("recorder", nn, t, d * b * 0.95, 0.28); T.note("orchestral_harp", nn, t, d * b, 0.2); t += d * b
    return reverb(T.buf[:int(L * SR)], 0.4)

def labour(L=25):
    """Hard work montage: driving 6/8 in D dorian, pizzicato ostinato, timpani on the downbeat, rising strings."""
    e = 0.19; bar = 6 * e
    T = Track(L)
    ost = ["D3", "A3", "D4", "A3", "C4", "A3"]
    roots = ["D2", "D2", "C2", "C2", "Bb1", "Bb1", "A1", "A1"]
    chords = [["D3", "F3", "A3"], ["D3", "F3", "A3"], ["C3", "E3", "G3"], ["C3", "E3", "G3"], ["Bb2", "D3", "F3"], ["Bb2", "D3", "F3"], ["A2", "C#3", "E3"], ["A2", "C#3", "E3"]]
    for k in range(int(L / bar) + 1):
        t = k * bar; r = k % 8
        for j, nn in enumerate(ost):
            T.note("pizzicato_strings", nn, t + j * e, e * 1.5, 0.3, pan=-0.2)
        T.note("timpani", "D2" if r < 4 else "A2", t, 0.5, 0.3)
        T.note("contrabass", roots[r], t, bar, 0.3)
        if k >= 4: T.chord("string_ensemble_1", chords[r], t, bar, 0.12 + min(0.12, 0.01 * k))
        if k >= 8 and k % 2 == 0: T.note("french_horn", chords[r][2], t, bar * 2, 0.22)
    return reverb(T.buf[:int(L * SR)], 0.3)

def battle(L=30):
    """Night battle: D minor at 140 bpm, galloping low strings, timpani, horn calls, choir stabs."""
    b = 60 / 140; bar = 4 * b
    T = Track(L)
    prog = [["D2", "A2", "F3"], ["D2", "A2", "F3"], ["Bb1", "F2", "D3"], ["C2", "G2", "E3"], ["D2", "A2", "F3"], ["F2", "C3", "A3"], ["G2", "D3", "Bb3"], ["A1", "E2", "C#3"]]
    for k in range(int(L / bar) + 1):
        ch = prog[k % 8]; t = k * bar
        for j in range(8):  # gallop
            T.note("cello", ch[0][:-1] + str(int(ch[0][-1]) + 1), t + j * b / 2, b * 0.4, 0.28 if j % 2 == 0 else 0.2)
        T.note("contrabass", ch[0], t, bar, 0.32)
        T.note("timpani", "D2" if k % 2 == 0 else "A2", t, 0.4, 0.42)
        T.note("timpani", "D2", t + 2.5 * b, 0.3, 0.3)
        T.chord("string_ensemble_1", [c[:-1] + str(int(c[-1]) + 1) for c in ch], t, bar, 0.16)
        if k % 2 == 1:
            T.note("french_horn", ch[2], t, b * 1.5, 0.32); T.note("french_horn", ch[1][:-1] + str(int(ch[1][-1]) + 1), t + 1.5 * b, b * 2.3, 0.3)
        if k % 4 == 3:
            T.chord("choir_aahs", [c[:-1] + str(int(c[-1]) + 1) for c in ch], t + 2 * b, b * 2, 0.25)
            T.note("trumpet", ch[2][:-1] + str(int(ch[2][-1]) + 1), t + 2 * b, b * 2, 0.3)
    return reverb(T.buf[:int(L * SR)], 0.35)

def sorrow(L=20):
    """Quiet aftermath: slow cello melody over soft strings, D minor, 56 bpm."""
    b = 60 / 56; bar = 4 * b
    T = Track(L)
    prog = [["D3", "F3", "A3"], ["Bb2", "D3", "F3"], ["G2", "Bb2", "D3"], ["A2", "C#3", "E3"]]
    for k in range(int(L / bar) + 1):
        T.chord("string_ensemble_1", prog[k % 4], k * bar, bar, 0.14)
    t = 0.5
    for nn, d in [("A3", 2), ("F3", 1), ("E3", 1), ("D3", 3), ("C#3", 1), ("D3", 1.5), ("E3", .5), ("F3", 1), ("G3", 1), ("E3", 4), ("A3", 2), ("Bb3", 1), ("A3", 1), ("D3", 4)]:
        if t < L: T.note("cello", nn, t, d * b * 0.95, 0.3)
        t += d * b
    return reverb(T.buf[:int(L * SR)], 0.5)

if __name__ == "__main__":
    out = sys.argv[1]
    for f in (realm, triumph, dread, mockery, cold, frost, wry, tender, mystery, dawn, reveal, outro):
        save(f(), f"{out}/cue_{f.__name__}.wav"); print(f.__name__)
