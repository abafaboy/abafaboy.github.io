"""Production name pronunciations; displayed dialogue is never rewritten."""
import re

NAME_PHONEMES = {'Taeo': 'tˈeɪoʊ', 'Nib': 'nɪb', 'Chae': 'tʃɛ'}
NAMES = re.compile(r'\b(Taeo|Nib|Chae)\b')


def phonemize_dialogue(tokenizer, text, language):
    return ' '.join(NAME_PHONEMES[part] if part in NAME_PHONEMES else tokenizer.phonemize(part, language)
                    for part in NAMES.split(text) if part)
