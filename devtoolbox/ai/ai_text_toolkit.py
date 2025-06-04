import re
import string
import nltk
from langdetect import detect
from textblob import TextBlob
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from collections import defaultdict

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")


def get_wordnet_pos(treebank_tag):
    """Map POS tag to first character lemmatize() accepts"""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # fallback


class AITextToolkit:
    def __init__(self, language="english"):
        self.language = language
        self.stop_words = set(stopwords.words(language))
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self, text):
        """Split text into tokens (words)"""
        return nltk.word_tokenize(text)

    def basic_tokenizer(self, text):
        """Splits text into lowercase tokens using regex"""
        return re.findall(r'\b\w+\b', text.lower())

    def remove_stopwords(self, tokens):
        """Remove common stopwords"""
        return [word for word in tokens if word.lower() not in self.stop_words]

    def lemmatize(self, tokens):
        """Reduce words to base form with POS support"""
        tagged = pos_tag(tokens)
        return [self.lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in tagged]

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
