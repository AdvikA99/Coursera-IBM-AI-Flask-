import unittest

try:
    from translator import english_to_french, french_to_english
except:
    import sys
    import os

    # Add the directory containing the 'machinetranslation' package to the Python path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    package_dir = os.path.join(current_dir, '..', '..')
    sys.path.append(package_dir)

    from machinetranslation.translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):

    def test_english_to_french_assert_equal(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
    def test_english_to_french_assert_not_equal(self):
        self.assertNotEqual(english_to_french("Hello"), "Hola")

    def test_french_to_english_assert_equal(self):
        self.assertEqual(french_to_english("Bonjour"), "Hi")
    
    def test_french_to_english_assert_not_equal(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Hola")

if __name__ == "__main__":
    unittest.main()
