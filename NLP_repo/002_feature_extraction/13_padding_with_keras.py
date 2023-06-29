# Sample input sequences
sequences = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

import keras 

# Import the pad_sequences function
from keras.preprocessing.sequence import pad_sequences

# Pad the sequences with zeros to a maximum length of 5
padded_sequences = pad_sequences(sequences, maxlen=5)

# Print the padded sequences
print(padded_sequences)
