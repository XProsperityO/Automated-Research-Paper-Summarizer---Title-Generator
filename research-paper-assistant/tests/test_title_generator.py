import unittest
from src.title_generator.gpt2_model import TitleGenerator

class TestTitleGenerator(unittest.TestCase):

    def setUp(self):
        self.title_generator = TitleGenerator()

    def test_generate_title(self):
        input_text = "This is a sample research paper about machine learning."
        generated_title = self.title_generator.generate_title(input_text)
        self.assertIsInstance(generated_title, str)
        self.assertGreater(len(generated_title), 0)

    def test_generate_title_with_empty_input(self):
        input_text = ""
        generated_title = self.title_generator.generate_title(input_text)
        self.assertEqual(generated_title, "Untitled")

if __name__ == '__main__':
    unittest.main()