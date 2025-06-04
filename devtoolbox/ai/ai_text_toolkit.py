# devtoolbox/ai/ai_text_toolkit.py

import re
import string
import nltk
from langdetect import detect
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

class AITextToolkit:
    def __init__(self, language="english"):
        self.language = language
        self.stop_words = set(stopwords.words(language))
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self, text):
        """Split text into tokens (words)"""
        return nltk.word_tokenize(text)

    def remove_stopwords(self, tokens):
        """Remove common stopwords"""
        return [word for word in tokens if word.lower() not in self.stop_words]

    def lemmatize(self, tokens):
        """Reduce words to base form"""
        return [self.lemmatizer.lemmatize(word) for word in tokens]

    def detect_language(self, text):
        """Detect the language of the input text"""
        return detect(text)

    def analyze_sentiment(self, text):
        """Return sentiment polarity and subjectivity"""
        blob = TextBlob(text)
        return {"polarity": blob.sentiment.polarity, "subjectivity": blob.sentiment.subjectivity}

    def summarize_entities(self, text):
        """Placeholder for future NER implementation"""
        return {"Note": "NER coming soon – will use spaCy or similar lib"}

def basic_tokenizer(self, text):
    """Splits text into lowercase tokens using regex"""
    return re.findall(r'\b\w+\b', text.lower())
