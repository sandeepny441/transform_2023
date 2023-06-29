import re

# Sample text data
text = "This is an example text with numbers like 123 and 4567."

# Remove numbers from the text using regular expressions
processed_text = re.sub(r'\d+', '', text)

# Print the processed text
print(processed_text)
