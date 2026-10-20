import unittest

from pronunciation import NAME_PHONEMES, phonemize_dialogue


class Tokenizer:
    def phonemize(self, text, language):
        return '[' + text + ']'


class PronunciationTests(unittest.TestCase):
    def test_one_syllable_chae_and_display_text_preserved(self):
        text = "I'm Chae. I'll be doing your assessment."
        self.assertEqual(phonemize_dialogue(Tokenizer(), text, 'en-gb'),
                         "[I'm ] tʃɛ [. I'll be doing your assessment.]")
        self.assertEqual(text, "I'm Chae. I'll be doing your assessment.")

    def test_established_names_unchanged(self):
        self.assertEqual(NAME_PHONEMES['Taeo'], 'tˈeɪoʊ')
        self.assertEqual(NAME_PHONEMES['Nib'], 'nɪb')
        self.assertEqual(phonemize_dialogue(Tokenizer(), 'Taeo, that mark. Nib, over here.', 'en-gb'),
                         'tˈeɪoʊ [, that mark. ] nɪb [, over here.]')

    def test_complete_names_only(self):
        self.assertEqual(phonemize_dialogue(Tokenizer(), 'Chae?', 'en-gb'), 'tʃɛ [?]')
        self.assertEqual(phonemize_dialogue(Tokenizer(), 'Chaeology', 'en-gb'), '[Chaeology]')


if __name__ == '__main__':
    unittest.main()
