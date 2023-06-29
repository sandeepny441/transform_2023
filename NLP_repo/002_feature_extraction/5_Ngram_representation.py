# Sample text data
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# Create a CountVectorizer object with n-gram range of (1, 2)
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(ngram_range=(1, 2))

# Fit the vectorizer to the text data
vectorizer.fit(corpus)

# Transform the text data into an n-gram matrix
ngram_matrix = vectorizer.transform(corpus)

# Convert the n-gram matrix to a numpy array
ngram_array = ngram_matrix.toarray()

# Print the n-gram matrix
print(ngram_array)
