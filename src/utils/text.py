import re
from collections import Counter
from typing import List, Tuple, Dict
import nltk
from nltk.corpus import stopwords
import string

# Garantir que as stopwords sejam obtidas pela biblioteca NLTK

try:
    nltk.data.find('corpora/stopwords')

except LookupError:
    nltk.download('stopwords', quiet=True)

PORTUGUESE_STOPWORDS = set(stopwords.words('portuguese'))

# Função para limpar o texto e conseguir as palavras

def clean_text(text: str) -> List[str]:

    text = text.lower()
    # Remover grande parte da pontuação
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    return words

def filter_stopwords(words: List[str]) -> List[str]:
    # Limpar texto de stopwords utilizando NLTK
    no_stopwords_text = [word for word in words if word not in PORTUGUESE_STOPWORDS]
    no_stopwords_text = [word for word in no_stopwords_text if word]

    return no_stopwords_text

def get_num_words(words: List[str]):
    totalWords = len(words)

    return totalWords

def get_vocabulary_stats(words: List[str], no_stopwords_text: List[str]) -> Dict:

    # Tamanho do vocabulário, utilizando set para tirar repetições
    vocabularySize = len(set(words))

    # Contagem de elementos e ver os 10 que mais se repetem
    word_counts = Counter(no_stopwords_text)
    top_10_words = word_counts.most_common(10)

    return vocabularySize, top_10_words
