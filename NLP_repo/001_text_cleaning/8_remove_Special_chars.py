import re

# Sample text data
text = "This is an example text with special characters like @, #, $, %, and ^."

# Remove special characters from the text using regular expressions
processed_text = re.sub(r'[^\w\s]', '', text)

# Print the processed text
print(processed_text)
