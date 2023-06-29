import langid

# Sample text data
text = "Esta es una frase en español. This is an English sentence."

# Detect code switching in the text
results = langid.classify(text)

# Print the detected language and probability
print(results[0]) # Detected language
print(results[1]) # Probability score
