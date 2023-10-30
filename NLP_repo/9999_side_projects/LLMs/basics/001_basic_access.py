import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def complete_prompt_with_gpt(prompt_text, model, tokenizer, max_length=100):
    """
    Complete the provided prompt using GPT.

    Parameters:
    - prompt_text (str): The input prompt.
    - model: The GPT model.
    - tokenizer: The tokenizer compatible with the GPT model.
    - max_length (int, optional): Maximum length of output. Defaults to 100.

    Returns:
    str: The completed text.
    """

    # Encode the input text and obtain tensor
    input_tensor = tokenizer.encode(prompt_text, return_tensors="pt")

    # Generate the completion tensor
    with torch.no_grad():
        output_tensor = model.generate(
            input_tensor, 
            max_length=max_length, 
            pad_token_id=tokenizer.eos_token_id
        )

    # Decode and return the completion
    return tokenizer.decode(output_tensor[0], skip_special_tokens=True)

def main():
    # Load pre-trained GPT-2 small model and tokenizer
    model_name = "gpt2" # This is the smallest GPT-2 model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Define the prompt for completion
    prompt = (
       "You're absolutely right, my previous example had a mistake in the matrix dimensions for multiplying a and b^T. Let me walk through a corrected example:"
    )

    # Obtain and display the completion
    completion = complete_prompt_with_gpt(prompt, model, tokenizer)
    print('Result================================')
    print(completion)

if __name__ == "__main__":
    main()
