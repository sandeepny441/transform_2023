import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
import torch

# Sample dataframe
# df = pd.DataFrame({
#    'Text': ['Sample text 1', 'Sample text 2', ...],
#    'Label': ['Category1', 'Category2', ...]
# })

# Load the dataset 
df = pd.read_csv("udemy_dataset.csv")

print(df.head())
df.drop(columns = "courseid", axis = 1, inplace = True)

df.columns = ["Text", "Label"]

# Convert textual labels to integers
le = LabelEncoder()
df['encoded_labels'] = le.fit_transform(df['Label'])

texts = df['Text'].tolist()
labels = df['encoded_labels'].tolist()

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
encodings = tokenizer(texts, truncation=True, padding=True, return_tensors='pt')
dataset = torch.utils.data.TensorDataset(encodings['input_ids'], encodings['attention_mask'], torch.tensor(labels))

train_size = 0.8
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [int(train_size * len(dataset)), len(dataset) - int(train_size * len(dataset))])

num_labels = len(df['Label'].unique())
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=num_labels)


training_args = TrainingArguments(
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_dir='./logs',
    logging_steps=10,
    do_train=True,
    do_eval=True,
    evaluation_strategy="steps",
    save_strategy="steps",
    save_steps=500,
    num_train_epochs=3,
    output_dir='./results'
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

trainer.train()

results = trainer.evaluate()
print(results)

from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate a dataset with non-linear decision boundary
X, y = make_moons(noise=0.3, random_state=0)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use PolynomialFeatures to transform the dataset
polynomial_features = PolynomialFeatures(degree=3, include_bias=False)

# Create a logistic regression model
logreg = LogisticRegression(solver='lbfgs')

# Create a pipeline that first applies polynomial feature transformation, then logistic regression
pipeline = make_pipeline(polynomial_features, logreg)

# Fit the model
pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred = pipeline.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

