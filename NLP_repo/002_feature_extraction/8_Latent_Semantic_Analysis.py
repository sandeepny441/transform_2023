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


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Sample data
documents = ["The car is driven on the road",
             "The dog is running in the park",
             "The car is parked in the park",
             "A dog is in the car"]

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Fit and transform the documents
X = vectorizer.fit_transform(documents)

# Create a TruncatedSVD object
lsa = TruncatedSVD(n_components=2)

# Fit and transform the tf-idf matrix
lsa.fit_transform(X)

# Print the topics
terms = vectorizer.get_feature_names_out()
for i, comp in enumerate(lsa.components_):
    termsInComp = zip(terms, comp)
    sortedTerms = sorted(termsInComp, key=lambda x: x[1], reverse=True) [:10]
    print("Topic %d:" % i)
    for term in sortedTerms:
        print(term[0])
    print(" ")







