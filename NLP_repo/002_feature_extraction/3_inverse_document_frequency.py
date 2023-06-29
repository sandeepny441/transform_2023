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

# Calculate the inverse document frequency of each term
idf = np.log(len(corpus) / (1 + np.sum(vectorizer.transform(corpus) > 0, axis=0)))

# Print the IDF values
print(idf)
