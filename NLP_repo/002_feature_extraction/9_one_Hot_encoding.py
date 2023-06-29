# Sample categorical data
data = ['red', 'blue', 'green', 'red', 'yellow', 'green']

# Create a LabelEncoder object
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# Fit the encoder to the data and transform the data into encoded labels
encoded_data = encoder.fit_transform(data)

# Create a OneHotEncoder object
from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder(sparse=False)

# Fit the encoder to the encoded data and transform the data into one-hot encoded vectors
onehot_data = onehot_encoder.fit_transform(encoded_data.reshape(-1, 1))

# Print the one-hot encoded data
print(onehot_data)
