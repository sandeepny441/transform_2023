from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

# Sample data
documents = ["The car is driven on the road",
             "The dog is running in the park",
             "The car is parked in the park",
             "A dog is in the car"]

# Preprocess the data
documents = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(documents)]

# Create a Doc2Vec model
model = Doc2Vec(vector_size=20, min_count=1, epochs=10)

# Build the vocabulary
model.build_vocab(documents)

# Train the model
model.train(documents, total_examples=model.corpus_count, epochs=model.epochs)

# Get the vector for a document
vector = model.infer_vector(word_tokenize("The car is parked in the park".lower()))

print(vector)
