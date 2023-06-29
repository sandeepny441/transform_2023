import enchant
from nltk.tokenize import word_tokenize

# Sample text data
text = "Thiss is an exampl of misspelled text."

# Tokenize the text
tokens = word_tokenize(text)

# Create a spell checker object
spell_checker = enchant.Dict("en_US")

# Check each token for spelling errors and suggest corrections
corrected_tokens = []
for token in tokens:
    if not spell_checker.check(token):
        suggestions = spell_checker.suggest(token)
        if suggestions:
            corrected_tokens.append(suggestions[0])
        else:
            corrected_tokens.append(token)
    else:
        corrected_tokens.append(token)

# Re-join the corrected tokens into a string
corrected_text = ' '.join(corrected_tokens)

# Print the corrected text
print(corrected_text)

