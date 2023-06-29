from sklearn.feature_extraction.text import CountVectorizer

# Sample text data
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Fit the vectorizer to the text data
vectorizer.fit(corpus)

# Print the vocabulary of the vectorizer
print(vectorizer.vocabulary_)

# Transform the text data into a BoW matrix
bow_matrix = vectorizer.transform(corpus)

# Print the BoW matrix
print(bow_matrix.toarray())
