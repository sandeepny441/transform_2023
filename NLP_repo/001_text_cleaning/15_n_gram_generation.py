import nltk
from nltk.util import ngrams

# Sample text data
text = "This is an example text for generating N-grams."

# Tokenize the text into words
tokens = nltk.word_tokenize(text)

# Generate trigrams (N=3) from the tokens
trigrams = list(ngrams(tokens, 3))

# Print the generated trigrams
for trigram in trigrams:
    print(trigram)

