import nltk
from nltk.tokenize import sent_tokenize

# Sample text data
text = "This is an example text. It contains multiple sentences. Each sentence ends with a period."

# Perform sentence segmentation on the text
sentences = sent_tokenize(text)

# Print the segmented sentences
for sentence in sentences:
    print(sentence)
