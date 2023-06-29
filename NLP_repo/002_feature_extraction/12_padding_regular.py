# Sample input sequences
sequences = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

# Find the maximum length of the input sequences
max_len = max([len(seq) for seq in sequences])

# Pad the sequences with zeros to a maximum length
padded_sequences = [seq + [0] * (max_len - len(seq)) for seq in sequences]

# Print the padded sequences
print(padded_sequences)
