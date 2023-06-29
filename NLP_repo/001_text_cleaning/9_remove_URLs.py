import re

# Sample text data
text = "This is an example text with a URL like https://example.com and an email address like john@example.com."

# Remove URLs and email addresses from the text using regular expressions
processed_text = re.sub(r'http\S+|www.\S+|[\w\.-]+@[\w\.-]+', '', text)

# Print the processed text
print(processed_text)
