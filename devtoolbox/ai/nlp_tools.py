# devtoolbox/ai/nlp_tools.py

import re

def basic_tokenizer(text):
    """Splits text into lowercase tokens"""
    return re.findall(r'\b\w+\b', text.lower())
