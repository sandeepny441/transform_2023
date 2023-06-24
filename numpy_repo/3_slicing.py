#slicing
import numpy as np

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])

# Slice from index 1 to index 4
print(arr[1:4])  # Output: [2, 3, 4]

# Slice from the beginning to index 2
print(arr[:2])  # Output: [1, 2]

# Slice from index 3 to the end
print(arr[3:])  # Output: [4, 5]

# Create a 2-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slice the first 2 rows
print(arr2d[:2])  # Output: [[1, 2, 3], [4, 5, 6]]

# Slice the last 2 columns
print(arr2d[:, -2:])  # Output: [[2, 3], [5, 6], [8, 9]]

# Slice the middle row and column
print(arr2d[1:2, 1:2])  # Output: [[5]]