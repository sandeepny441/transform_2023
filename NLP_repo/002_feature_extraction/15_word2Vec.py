# Import the necessary libraries
from gensim.models import Word2Vec
import nltk

corpus = nltk.corpus.brown.sents()
# Load the Brown corpus from NLTK
# corpus = brown.sents()

# Train the Word2Vec model on the corpus
model = Word2Vec(corpus, vector_size=100, window=5, min_count=1, workers=4)

# Get the embedding vector for a word
embedding = model.wv['dog']

# Find the most similar words to a given word
similar_words = model.wv.most_similar('dog')

# Print the embedding vector and similar words
print('Embedding vector for "dog":', embedding)
print('Most similar words to "dog":', similar_words)
