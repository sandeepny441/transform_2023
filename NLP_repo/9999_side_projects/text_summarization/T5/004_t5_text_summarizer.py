import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_text_t5(
    text: str,
    model,
    tokenizer,
    max_input_length: int = 512,
    max_output_length: int = 150
):
    """
    Function to summarize the input text using a pre-trained T5 model.

    Parameters:
    text (str): The text to summarize.
    model: The T5 model.
    tokenizer: The tokenizer compatible with the T5 model.
    max_input_length (int, optional): Maximum length of input text. Defaults to 512.
    max_output_length (int, optional): Maximum length of summarized text. Defaults to 150.
    
    Returns:
    str: The summarized text.
    """
    
    # Encode the input text
    inputs = tokenizer.encode(
        "summarize: " + text,
        return_tensors="pt",
        max_length=max_input_length,
        truncation=True
    )

    # Generate summary IDs
    summary_ids = model.generate(
        inputs,
        max_length=max_output_length,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )

    # Decode and return the summarized text
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Load the pre-trained T5 model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Define the text to be summarized
text = """
The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by 
the National Aeronautics and Space Administration (NASA), which succeeded in landing the first humans on the Moon from 1969 to 1972.
It was first conceived during Dwight D. Eisenhower's administration as a three-person spacecraft to follow the one-person Project Mercury,
which put the first Americans in space. Apollo was later dedicated to President John F. Kennedy's national goal for the 1960s of "landing a man on the Moon
and returning him safely to the Earth" in an address to Congress on May 25, 1961.
"""

# Get and print the summarized text
summary = summarize_text_t5(text, model, tokenizer)
print("Summary:", summary)
