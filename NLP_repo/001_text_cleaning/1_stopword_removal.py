import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text data
text = "This is an example of text processing. It involves several steps such as normalization, tokenization, stopword removal, stemming, and lemmatization."

# Tokenize the text
tokens = word_tokenize(text)

# Get the list of English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words from the tokenized text
filtered_tokens = [word for word in tokens if word.casefold() not in stop_words]

# Re-join the filtered tokens into a string
filtered_text = ' '.join(filtered_tokens)

# Print the filtered text
print(filtered_text)
