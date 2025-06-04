# tests/test_ai_text_toolkit.py

import unittest
from devtoolbox.ai.ai_text_toolkit import AITextToolkit

class TestAITextToolkit(unittest.TestCase):
    def setUp(self):
        self.toolkit = AITextToolkit()

    def test_tokenization(self):
        tokens = self.toolkit.tokenize("This is a test.")
        self.assertIn("test", tokens)

    def test_stopword_removal(self):
        tokens = ["this", "is", "a", "test"]
        cleaned = self.toolkit.remove_stopwords(tokens)
        self.assertNotIn("is", cleaned)

    def test_lemmatization(self):
        tokens = ["running", "baked"]
        lemmas = self.toolkit.lemmatize(tokens)
        self.assertIn("bake", lemmas)

    def test_language_detection(self):
        lang = self.toolkit.detect_language("Bonjour tout le monde")
        self.assertEqual(lang, "fr")

    def test_sentiment_analysis(self):
        sentiment = self.toolkit.analyze_sentiment("I love AI.")
        self.assertGreater(sentiment["polarity"], 0)

if __name__ == "__main__":
    unittest.main()
