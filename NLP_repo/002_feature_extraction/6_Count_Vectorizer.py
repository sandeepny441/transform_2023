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

# Transform the text data into a count matrix
count_matrix = vectorizer.transform(corpus)

# Convert the count matrix to a numpy array
count_array = count_matrix.toarray()

# Print the count matrix
print(count_array)
