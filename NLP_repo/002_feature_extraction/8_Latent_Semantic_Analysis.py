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

# Create an LSA model
from sklearn.decomposition import TruncatedSVD
lsa_model = TruncatedSVD(n_components=2)

# Fit the LSA model to the count matrix
lsa_model.fit(count_matrix)

# Transform the count matrix into an LSA matrix
lsa_matrix = lsa_model.transform(count_matrix)

# Print the LSA matrix
print(lsa_matrix)
