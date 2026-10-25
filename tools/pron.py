"""pron: respell Korean names for the Kokoro narrator so it says them close to NAME_SHEET.md's guide.

Checked against the narrator's own phonemizer on 25 October 2026 (en-us): left as written, "Jaeha" came out as
"YEE-huh", "Seoa" as "SEE-uh", "Hwang" as "H-wang" and "tteokbokki" as "tee-dee-AHK-bah-kee". Only the voice sees the
respelling; the recap files keep the real spellings.
"""
import re

RESPELL = {
    "Jaeha": "Jay-ha", "Seoa": "Suh-ah", "Ahin": "Ah-heen", "Kanghan": "Kahng-hahn", "Pyo": "Peeyo",
    "Minseok": "Minsuk", "Baek": "Beck", "Taegun": "Teh-goon", "Hangyu": "Hahng-yoo", "Mangwon": "Mahng-won",
    "Saebyeok": "Seb-yuk", "Geum": "Gum", "Busan": "Boo-sahn", "Ryu": "Rue", "Hwang": "Whang", "Dami": "Dahmi",
    "Jang": "Jahng", "Hapjeong": "Hahp-jung", "Dongsik": "Dong-sheek", "Han": "Hahn", "Sora": "Soh-rah",
    "hyung": "hyeong", "Hyung": "Hyeong", "tteokbokki": "tuck-bo-kee", "Tteokbokki": "Tuck-bo-kee",
}
_RX = re.compile(r"\b(" + "|".join(sorted(map(re.escape, RESPELL), key=len, reverse=True)) + r")\b")


def respell(text):
    return _RX.sub(lambda m: RESPELL[m.group(1)], text)


if __name__ == "__main__":
    print(respell("Jaeha's sister Seoa, Moon Ahin, Director Baek Taegun, Uncle Pyo, the Han River, hyung, tteokbokki in Busan."))
