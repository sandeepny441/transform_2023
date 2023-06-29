import numpy as np

# Sample text data
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# Create a TfidfVectorizer object
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the text data
vectorizer.fit(corpus)

# Transform the text data into a TF-IDF matrix
tfidf_matrix = vectorizer.transform(corpus)

# Convert the TF-IDF matrix to a numpy array
tfidf_array = tfidf_matrix.toarray()

# Print the TF-IDF matrix
print(tfidf_array)
