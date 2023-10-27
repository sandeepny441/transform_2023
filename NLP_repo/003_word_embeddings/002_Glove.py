import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Co-occurrence matrix
# Rows and columns correspond to words in vocab in the order they appear
co_occurrence_matrix = np.array([
    [0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0]
])

vocab = ["king", "queen", "man", "woman", "palace", "home"]
vocab_size = len(vocab)

# Hyperparameters
embedding_dim = 2
learning_rate = 0.05
epochs = 1000

# Model definition
class GloVe(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(GloVe, self).__init__()
        self.W = nn.Embedding(vocab_size, embedding_dim)
        self.W_tilde = nn.Embedding(vocab_size, embedding_dim)
        self.b = nn.Embedding(vocab_size, 1)
        self.b_tilde = nn.Embedding(vocab_size, 1)
        
    def forward(self, i, j):
        w_i = self.W(i)
        w_j_tilde = self.W_tilde(j)
        b_i = self.b(i).squeeze()
        b_j_tilde = self.b_tilde(j).squeeze()
        return torch.dot(w_i, w_j_tilde) + b_i + b_j_tilde

model = GloVe(vocab_size, embedding_dim)
optimizer = optim.Adagrad(model.parameters(), lr=learning_rate)

# Training
for epoch in range(epochs):
    total_loss = 0
    for i in range(vocab_size):
        for j in range(vocab_size):
            if co_occurrence_matrix[i][j] > 0:
                weight = (co_occurrence_matrix[i][j]/100)**0.75
                optimizer.zero_grad()
                loss = weight * (model(torch.tensor(i), torch.tensor(j)) - np.log(co_occurrence_matrix[i][j]))**2
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss}")

# Extract embeddings
embeddings = model.W.weight.data.numpy()
print("\nWord Embeddings:")
for word, i in zip(vocab, range(vocab_size)):
    print(f"{word}: {embeddings[i]}")
