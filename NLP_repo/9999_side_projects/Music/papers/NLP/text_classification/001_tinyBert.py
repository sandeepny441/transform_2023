import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split

# Initialize tokenizer and model
tokenizer = BertTokenizer.from_pretrained('huawei-noah/TinyBERT_General_4L_312D')
model = BertForSequenceClassification.from_pretrained('huawei-noah/TinyBERT_General_4L_312D', num_labels=2)

# Load dataset
df_actual = pd.read_csv("udemy_dataset_binary.csv")
df = pd.concat([df_actual.head(), df_actual.tail()])
texts = df['content'].tolist()
labels_text = df['title'].tolist()

# Convert textual labels to numerical labels
unique_labels = list(set(labels_text))
label_to_id = {label: i for i, label in enumerate(unique_labels)}
labels = [label_to_id[label] for label in labels_text]

# Split the data
train_texts, val_texts, train_labels, val_labels = train_test_split(
    texts, labels, test_size=0.2, stratify=labels, random_state=42
)

# Tokenize
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=256)
val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=256)

# Define custom dataset
class TextDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = TextDataset(train_encodings, train_labels)
val_dataset = TextDataset(val_encodings, val_labels)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    evaluation_strategy="steps",
    save_strategy="steps",
    logging_dir='./logs',
    logging_steps=10,
    do_train=True,
    do_eval=True,
    no_cuda=False,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    push_to_hub=False,
    logging_first_step=False,
    save_steps=500,
    eval_steps=100,
    save_total_limit=2,
    remove_unused_columns=True
)

# Train
from datasets import load_metric
import numpy as np

def compute_metrics(p):
    pred, labels = p
    pred = np.argmax(pred, axis=1)

    accuracy = (pred == labels).mean()
    return {"accuracy": accuracy}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics  # Add this line
)

trainer.train()

# Evaluate the model
results = trainer.evaluate()
print(results)

# Test
input_text = "Your sample text here for prediction"
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=256)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=-1)  # Get the predicted class index

id_to_label = {v: k for k, v in label_to_id.items()}
predicted_label = id_to_label[predictions.item()]
print(f"Predicted Label: {predicted_label}")

#Metrics
from datasets import load_metric

def compute_metrics(p):
    pred, labels = p
    pred = np.argmax(pred, axis=1)

    accuracy = (pred == labels).mean()
    return {"accuracy": accuracy}
