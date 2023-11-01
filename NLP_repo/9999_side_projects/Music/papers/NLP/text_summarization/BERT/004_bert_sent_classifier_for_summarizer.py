import torch
from transformers import BertTokenizer, BertForSequenceClassification

def summarize_text_bert(
    text: str,
    model,
    tokenizer,
    threshold: float = 0.5
):
    """
    Function to perform extractive summarization on the input text using a pre-trained BERT model.

    Parameters:
    text (str): The text to summarize.
    model: The BERT model.
    tokenizer: The tokenizer compatible with the BERT model.
    threshold (float, optional): Threshold for sentence inclusion in the summary. Defaults to 0.5.
    
    Returns:
    str: The summarized text.
    """
    
    # Split the text into sentences
    sentences = text.split('.')
    
    # Classify each sentence
    summaries = []
    for sentence in sentences:
        # Encoding sentences and getting attention masks
        inputs = tokenizer(
            sentence,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )
        
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        
        # Getting model outputs
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        probs = torch.sigmoid(outputs.logits)
        
        # Include the sentence in the summary if the probability of the positive class is above the threshold
        if probs[0, 1] > threshold:
            summaries.append(sentence)
    
    # Join sentences to get the final summary
    summary = '. '.join(summaries)
    
    return summary


# Load the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"  # You might want to use a model fine-tuned for summarization
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Define the text to be summarized
text = """
The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by 
the National Aeronautics and Space Administration (NASA), which succeeded in landing the first humans on the Moon from 1969 to 1972.
"""

# Get and print the summarized text
summary = summarize_text_bert(text, model, tokenizer)
print("Summary:", summary)
