import numpy as np

# Creating a 1D numpy array
x = np.array([1, 2, 3, 4, 5, 6], dtype=np.int32)

# Print the original strides
print(x.strides)  # Outputs: (4,)

# Reshape the array
y = x.reshape(2, 3)

# Print the strides after reshaping
print(y.strides)  # Outputs: (12, 4)
