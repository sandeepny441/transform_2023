import torch
import torch.nn as nn
import pandas as pd

# Load the dataset 
df = pd.read_csv("udemy_dataset.csv")

print(df.head())
df.drop(columns = "courseid", axis = 1, inplace = True)

df.columns = ["Text", "Label"]



# Convert text to integers using sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Text']) 

# Convert labels to integers
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
y = le.fit_transform(df['Label'])

# Split data into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# Convert sparse matrix to dense tensor
X_train = X_train.toarray()
X_test = X_test.toarray() 

X_train = torch.from_numpy(X_train).float()
X_test = torch.from_numpy(X_test).float()

y_train = torch.from_numpy(y_train).long()
y_test = torch.from_numpy(y_test).long()


# MLP model 
class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) 
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

input_size = X_train.shape[1] 
hidden_size = 128
output_size = 2 

model = MLP(input_size, hidden_size, output_size)

# Train the model
import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

model.train()
for epoch in range(100):
  optimizer.zero_grad()
  
  # Forward pass
  y_pred = model(X_train)
  
  # Compute loss
  loss = criterion(y_pred, y_train)
  
  # Backward pass
  loss.backward()
  
  optimizer.step()

# Evaluate on test data  
model.eval() 
y_pred = model(X_test)
y_pred = torch.argmax(y_pred,dim=1)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))