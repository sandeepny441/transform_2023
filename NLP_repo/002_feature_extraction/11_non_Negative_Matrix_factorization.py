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

# Create an NMF model
from sklearn.decomposition import NMF
nmf_model = NMF(n_components=2)

# Fit the NMF model to the count matrix
nmf_model.fit(count_matrix)

# Print the top words for each topic
feature_names = vectorizer.get_feature_names()
for topic_idx, topic in enumerate(nmf_model.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-5 - 1:-1]]))
    print()

# Transform the count matrix into an NMF matrix
nmf_matrix = nmf_model.transform(count_matrix)

# Print the NMF matrix
print(nmf_matrix)
