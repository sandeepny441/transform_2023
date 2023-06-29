import nltk
from nltk.tokenize import word_tokenize

# Sample text data
text = """
    The quik browne Fox, wasnt very goood at jummping, but he was a gud runner. <br> Check out my website: www.example.com!
""" 

# Tokenize the text
tokens = word_tokenize(text)