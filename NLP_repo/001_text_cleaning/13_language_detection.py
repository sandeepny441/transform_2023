from langdetect import detect

# Sample text data
text = "This is an example text. It is written in English."

# Detect the language of the text
lang = detect(text)

# Print the detected language
print(lang)
