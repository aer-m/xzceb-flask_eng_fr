import unittest
from translator import translater_english_to_french, translater_french_to_english

class TestTranslator(unittest.TestCase):
        def test_english_to_french_null(self):
                actual=translater_english_to_french(None)
                expected=""
                self.assertEqual(actual,expected)

        def test_french_to_english_null(self):
                actual=translater_french_to_english(None)
                expected=""
                self.assertEqual(actual,expected)

        def test_french_to_english(self):
                actual=translater_french_to_english("Bonjour")
                expected="Hello"
                self.assertEqual(actual,expected)

        def test_english_to_french(self):
                actual=translater_english_to_french("Hello")
                expected="Bonjour"
                self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
