import re

# Sample text data
text = "This is   an    example   text     with   extra   white spaces."

# Remove extra white spaces from the text using regular expressions
processed_text = re.sub(r'\s+', ' ', text).strip()

# Print the processed text
print(processed_text)
