import torch
from transformers import BertTokenizer, EncoderDecoderModel

def extractive_summarization_bertsum(
    text: str,
    model,
    tokenizer,
    max_input_length: int = 512,
    max_output_length: int = 150
):
    """
    Function to perform extractive summarization on the input text using a pre-trained BERTSUM model.

    Parameters:
    text (str): The text to summarize.
    model: The BERTSUM model.
    tokenizer: The tokenizer compatible with the BERTSUM model.
    max_input_length (int, optional): Maximum length of input text. Defaults to 512.
    max_output_length (int, optional): Maximum length of summarized text. Defaults to 150.
    
    Returns:
    str: The extracted summary.
    """

    # Encode the input text
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=max_input_length,
        truncation=True
    )

    # Generate summary by extracting sentences
    # BERTSUM's EncoderDecoderModel can be used to predict the sentences to keep
    summary_ids = model.generate(
        input_ids=inputs['input_ids'],
        attention_mask=inputs['attention_mask'],
        max_length=max_output_length,
        decoder_start_token_id=model.config.pad_token_id
    )

    # Decode and return the summarized text
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Load the pre-trained BERTSUM model and tokenizer
# Make sure you have a BERTSUM model fine-tuned on a summarization task
model_name = "path/to/your/bertsum/model"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = EncoderDecoderModel.from_pretrained(model_name)

# Define the text to be summarized
text = """
The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by 
the National Aeronautics and Space Administration (NASA), which succeeded in landing the first humans on the Moon from 1969 to 1972.
It was first conceived during Dwight D. Eisenhower's administration as a three-person spacecraft to follow the one-person Project Mercury,
which put the first Americans in space. Apollo was later dedicated to President John F. Kennedy's national goal for the 1960s of "landing a man on the Moon
and returning him safely to the Earth" in an address to Congress on May 25, 1961.
"""

# Get and print the summarized text
summary = extractive_summarization_bertsum(text, model, tokenizer)
print("Summary:", summary)
