import numpy as np

# Create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5, 6])

# Split the array into three equally sized sub-arrays
result = np.split(a, 3)

print(result)  # Outputs: [array([1, 2]), array([3, 4]), array([5, 6])]

#=======================================================================

# h split 

# Create a 2-dimensional array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Horizontally split the array into three equally sized sub-arrays
result = np.hsplit(a, 3)

print(result)  # Outputs: [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]

#=======================================================================

# v split 

# Create a 2-dimensional array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Vertically split the array into two equally sized sub-arrays
result = np.vsplit(a, 2)

print(result)  # Outputs: [array([[1, 2, 3]]), array([[4, 5, 6]])]

#=======================================================================
# split at specific indices 

# Create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5, 6])

# Split the array at indices 1 and 4
result = np.split(a, [1, 4])

print(result)  # Outputs: [array([1]), array([2, 3, 4]), array([5, 6])]

#=======================================================================
