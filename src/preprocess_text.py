import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords", quiet=True)
_stop = set(stopwords.words("english"))
_stem = PorterStemmer()

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " urltoken ", text)
    text = re.sub(r"\d+", " numtoken ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = [_stem.stem(w) for w in text.split() if w not in _stop]
    return " ".join(tokens)