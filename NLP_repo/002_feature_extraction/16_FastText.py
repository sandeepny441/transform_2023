from gensim.models.fasttext import FastText
from gensim.test.utils import common_texts

# Train a FastText model on a toy dataset
model = FastText(size=100, window=5, min_count=1, sentences=common_texts, iter=10)

# Get the word vector for a specific word
vector = model.wv['computer']

# Find the most similar words to a given word
similar_words = model.wv.most_similar('computer')
print(similar_words)
