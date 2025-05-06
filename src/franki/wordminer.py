import spacy
from pathlib import Path
from collections import deque

_nlp = spacy.load("fr_core_news_sm")

# Global queue for subtitles
subtitle_queue = deque()


def load_b1_wordlist(max_common=5000):
    path = Path("src/franki/resources/b1_words.txt")
    if not path.exists():
        raise FileNotFoundError("B1 word list not found. Please download it manually and place it at src/franki/resources/b1_words.txt")

    frequent_words = set()
    for i, line in enumerate(path.read_text().splitlines()):
        if i >= max_common:
            break
        word = line.strip().split()[0].lower()
        frequent_words.add(word)
    return frequent_words

def get_hard_words(sentence, b1_words):
    doc = _nlp(sentence)
    return [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop and not token.ent_type_ and token.lemma_.lower() not in b1_words
    ]
