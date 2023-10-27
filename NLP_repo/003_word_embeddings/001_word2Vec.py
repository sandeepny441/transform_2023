import torch
import torch.nn as nn
import torch.optim as optim

# Sample corpus
corpus = ["king palace", "queen palace", "man home", "woman home"]

# Hyperparameters
embedding_dim = 2
learning_rate = 0.01
epochs = 1000

# Vocabulary and word-to-index mapping
vocab = ["king", "queen", "man", "woman", "palace", "home"]
word_to_ix = {word: i for i, word in enumerate(vocab)}

# Defining the Skip-gram model
class SkipGram(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(SkipGram, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embed_dim)

    def forward(self, target_word):
        return self.embeddings(target_word)

# Training data preparation (target, context)
pairs = []
for sentence in corpus:
    words = sentence.split()
    for i, target_word in enumerate(words):
        context = [words[j] for j in range(max(0, i-1), min(len(words), i+2)) if j != i]
        pairs.extend((word_to_ix[target_word], word_to_ix[context_word]) for context_word in context)


# Model, loss function, and optimizer initialization
model = SkipGram(len(vocab), embedding_dim)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training
for epoch in range(epochs):
    total_loss = 0
    for target, context in pairs:
        optimizer.zero_grad()
        target_var = torch.LongTensor([target])
        context_var = torch.LongTensor([context])
        embed = model(target_var)
        scores = torch.matmul(embed, model.embeddings.weight.t())  # Dot product with all embeddings
        loss = criterion(scores, context_var)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        

# Extract embeddings
embeddings = model.embeddings.weight.data.numpy()
print("Word Embeddings:")
for word, i in word_to_ix.items():
    print(f"{word}: {embeddings[i]}")

