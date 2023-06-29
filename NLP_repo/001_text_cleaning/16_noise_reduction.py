import re

# Sample text data with noise
text = "Th!s $%# is an e#xamp@le t%e#xt w&ith n*ois^e. 1234567.8.9.0"

# Remove special characters and symbols
text = re.sub(r'[^\w\s]', '', text)

# Remove numbers
text = re.sub(r'\d+', '', text)

# Remove extra white spaces
text = re.sub(r'\s+', ' ', text)

# Remove stop words
stopwords = ['the', 'and', 'is', 'an', 'with']
text = ' '.join([word for word in text.split() if word.lower() not in stopwords])

# Remove HTML tags and markup
text = re.sub(r'<[^>]*>', '', text)

# Remove URLs and email addresses
text = re.sub(r'\S+@\S+', '', text)
text = re.sub(r'http\S+', '', text)

# Expand abbreviations and acronyms
abbreviations = {'mr.': 'mister', 'dr.': 'doctor'}
text = ' '.join([abbreviations.get(word.lower(), word) for word in text.split()])

# Convert all text to lowercase
text = text.lower()

# Print the cleaned text
print(text)
