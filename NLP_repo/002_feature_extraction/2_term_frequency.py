import numpy as np

# Sample text data
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# Create a CountVectorizer object
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer to the text data
vectorizer.fit(corpus)

# Transform the text data into a term frequency matrix
tf_matrix = vectorizer.transform(corpus)

# Convert the term frequency matrix to a numpy array
tf_array = tf_matrix.toarray()

# Calculate the term frequency of each term in each document
tf = np.zeros_like(tf_array, dtype=np.float64)
for i, row in enumerate(tf_array):
    tf[i] = row / np.sum(row)

# Print the term frequency matrix
print(tf)
