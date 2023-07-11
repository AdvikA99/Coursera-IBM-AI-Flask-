"""
English and French translator
"""

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates english text to french
    """
    french_text = MyMemoryTranslator("en-US", "fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates french text to enlish
    """
    english_text = MyMemoryTranslator("fr-FR", "en-US").translate(french_text)
    return english_text
