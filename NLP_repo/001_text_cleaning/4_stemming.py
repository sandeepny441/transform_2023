import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Sample text data
text = "I am learning natural language processing and its various techniques like tokenization, stemming, and lemmatization."

# Tokenize the text
tokens = word_tokenize(text)

# Create a stemmer object
stemmer = PorterStemmer()

# Perform stemming on the tokens
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Re-join the stemmed tokens into a string
stemmed_text = ' '.join(stemmed_tokens)

# Print the stemmed text
print(stemmed_text)
