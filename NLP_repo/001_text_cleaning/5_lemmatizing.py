import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Sample text data
text = "I am learning natural language processing and its various techniques like tokenization, stemming, and lemmatization."

# Tokenize the text
tokens = word_tokenize(text)

# Create a lemmatizer object
lemmatizer = WordNetLemmatizer()

# Perform lemmatization on the tokens
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Re-join the lemmatized tokens into a string
lemmatized_text = ' '.join(lemmatized_tokens)

# Print the lemmatized text
print(lemmatized_text)
