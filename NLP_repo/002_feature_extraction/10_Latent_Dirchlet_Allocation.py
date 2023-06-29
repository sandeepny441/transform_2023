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

# Create an LDA model
from sklearn.decomposition import LatentDirichletAllocation
lda_model = LatentDirichletAllocation(n_components=2)

# Fit the LDA model to the count matrix
lda_model.fit(count_matrix)

# Print the top words for each topic
feature_names = vectorizer.get_feature_names()
for topic_idx, topic in enumerate(lda_model.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-5 - 1:-1]]))
    print()

# Transform the count matrix into an LDA matrix
lda_matrix = lda_model.transform(count_matrix)

# Print the LDA matrix
print(lda_matrix)
