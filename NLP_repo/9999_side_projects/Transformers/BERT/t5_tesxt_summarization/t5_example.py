data = [
    {
        "source": "My firm uses MyCase for practice management. MyCase does a good job with our invoicing and matter management. It has a document automation feature. I’ve tried to figure it out a number of times and either I’m a dummy or it is terrible. Both are possibilities.",
        "target": "My firm uses MyCase mainly for invoicing and matter management but struggles with its document automation feature."
    },
    {
        "source": "We've integrated the Salesforce platform for customer relationship management. It provides great analytics, but the interface is not intuitive. Several team members took additional training to get accustomed to it.",
        "target": "We use Salesforce for CRM which offers excellent analytics, but its interface requires getting used to."
    },
    {
        "source": "Our company has been trying out the new Zoom Rooms feature. The virtual background feature is innovative and adds a fun element. However, connectivity in large meetings tends to lag.",
        "target": "Our company tested Zoom Rooms and found its virtual background feature innovative, but it lags in large meetings."
    }
]


import torch
from torch.utils.data import DataLoader, Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration, AdamW

# Dataset
class SummaryDataset(Dataset):
    def __init__(self, tokenizer, data, max_input_length=512, max_output_length=150):
        self.tokenizer = tokenizer
        self.data = data
        self.max_input_length = max_input_length
        self.max_output_length = max_output_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        item = self.data[index]
        source = item["source"]
        target = item["target"]

        source_tokens = self.tokenizer.encode_plus(source, max_length=self.max_input_length, truncation=True, padding='max_length', return_tensors="pt")
        target_tokens = self.tokenizer.encode_plus(target, max_length=self.max_output_length, truncation=True, padding='max_length', return_tensors="pt")

        return {"source_ids": source_tokens["input_ids"].squeeze(),
                "source_mask": source_tokens["attention_mask"].squeeze(),
                "target_ids": target_tokens["input_ids"].squeeze(),
                "target_mask": target_tokens["attention_mask"].squeeze()}

# Configurations
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Sample dataset (you would normally split it into train/valid/test)
data = [
    {
        "source": "My firm uses MyCase for practice management. MyCase does a good job with our invoicing and matter management. It has a document automation feature. I’ve tried to figure it out a number of times and either I’m a dummy or it is terrible. Both are possibilities.",
        "target": "My firm uses MyCase mainly for invoicing and matter management but struggles with its document automation feature."
    }
]

dataset = SummaryDataset(tokenizer, data)
dataloader = DataLoader(dataset, batch_size=1)

# Training loop
optimizer = AdamW(model.parameters(), lr=1e-4)
model.train()

for epoch in range(3):  # Use more epochs for actual fine-tuning
    for batch in dataloader:
        optimizer.zero_grad()

        source_ids = batch["source_ids"].to('cuda')
        source_mask = batch["source_mask"].to('cuda')
        target_ids = batch["target_ids"].to('cuda')

        outputs = model(input_ids=source_ids, attention_mask=source_mask, labels=target_ids)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

# Save the model
model.save_pretrained("fine_tuned_t5")
tokenizer.save_pretrained("fine_tuned_t5")
