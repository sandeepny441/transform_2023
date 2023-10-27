import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class FastText(nn.Module):
    def __init__(self, vocab_size, embed_dim, word_ngrams=2):
        super(FastText, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embed_dim)
        self.word_ngrams = word_ngrams

    def forward(self, input):
        embeds = self.embeddings(input)
        out = F.avg_pool2d(embeds, (embeds.shape[1], 1)).squeeze(1) 
        return out

corpus = [["king"], ["queen"], ["man"], ["woman"], ["palace"], ["home"]]
vocab = {"king": 0, "queen": 1, "man": 2, "woman": 3, "palace": 4, "home": 5}
inv_vocab = {v: k for k, v in vocab.items()}

# Hyperparameters
embedding_dim = 10
learning_rate = 0.01
epochs = 1000

model = FastText(len(vocab), embedding_dim)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(epochs):
    total_loss = 0
    for context, target in corpus:  # Here you need to prepare your data in (context, target) pairs
        context_idxs = torch.tensor([vocab[w] for w in context], dtype=torch.long)
        optimizer.zero_grad()
        embeds = model(context_idxs)
        loss = criterion(embeds, torch.tensor([vocab[target[0]]], dtype=torch.long))
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

# To get the vector of a word
word_idx = vocab['king']
word_embedding = model.embeddings(torch.tensor(word_idx))
print(word_embedding)
