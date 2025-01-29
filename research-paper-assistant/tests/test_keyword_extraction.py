import unittest
from src.keyword_extraction.tfidf import KeywordExtractor

class TestKeywordExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = KeywordExtractor()

    def test_extract_keywords(self):
        text = "Natural Language Processing is a field of artificial intelligence."
        expected_keywords = ["Natural Language Processing", "artificial intelligence"]
        extracted_keywords = self.extractor.extract_keywords(text)
        self.assertEqual(set(expected_keywords), set(extracted_keywords))

    def test_empty_text(self):
        text = ""
        expected_keywords = []
        extracted_keywords = self.extractor.extract_keywords(text)
        self.assertEqual(set(expected_keywords), set(extracted_keywords))

    def test_non_english_text(self):
        text = "El procesamiento del lenguaje natural es un campo de la inteligencia artificial."
        expected_keywords = ["procesamiento", "lenguaje", "natural", "inteligencia", "artificial"]
        extracted_keywords = self.extractor.extract_keywords(text)
        self.assertEqual(set(expected_keywords), set(extracted_keywords))

if __name__ == '__main__':
    unittest.main()