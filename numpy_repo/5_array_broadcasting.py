import numpy as np
# Addition of Array and Scalar
# Create an array
a = np.array([1, 2, 3])

# Add a scalar (which is a 0-dimensional array)
result = a + 5

print(result)  # Outputs: array([6, 7, 8])

# Addition of Array and Scalar
# Create a 2-dimensional array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 1-dimensional array
b = np.array([1, 2, 3])

# Add the two arrays
result = a + b

print(result)  # Outputs: array([[2, 4, 6], [5, 7, 9]])


# Addition of Array and Scalar

# Create a 3x1 dimensional array
a = np.array([[1], [2], [3]])

# Create a 1x3 dimensional array
b = np.array([1, 2, 3])

# Multiply the two arrays
result = a * b

print(result)  # Outputs: array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
