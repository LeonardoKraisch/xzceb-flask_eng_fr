import unittest
from translator import english_to_french, french_to_english


class TestTranslatorE2F(unittest.TestCase):

    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Ola')


class TestTranslatorF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Ola')

if __name__ == '__main__':
    unittest.main()
