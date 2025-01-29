import unittest
from src.summarizer.extractive import ExtractiveSummarizer
from src.summarizer.abstractive import AbstractiveSummarizer

class TestSummarizer(unittest.TestCase):

    def setUp(self):
        self.extractive_summarizer = ExtractiveSummarizer()
        self.abstractive_summarizer = AbstractiveSummarizer()
        self.sample_text = (
            "Natural language processing (NLP) is a field of artificial intelligence "
            "that focuses on the interaction between computers and humans through natural language."
        )

    def test_extractive_summary(self):
        summary = self.extractive_summarizer.summarize(self.sample_text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

    def test_abstractive_summary(self):
        summary = self.abstractive_summarizer.summarize(self.sample_text)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(summary), 0)

if __name__ == '__main__':
    unittest.main()