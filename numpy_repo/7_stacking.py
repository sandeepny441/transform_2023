# vertical stack 

import numpy as np

# Create two 1-dimensional arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical stack
result = np.vstack((a, b))

print(result)  
# Outputs: 
# array([[1, 2, 3],
#        [4, 5, 6]])

# Horizontal stack 

# Create two 1-dimensional arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Horizontal stack
result = np.hstack((a, b))

print(result)  # Outputs: array([1, 2, 3, 4, 5, 6])

# Depth stack 

# Create two 2-dimensional arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Depth stack
result = np.dstack((a, b))

print(result)  
# Outputs: 
# array([[[1, 5],
#         [2, 6]],
#        [[3, 7],
#         [4, 8]]])

# General Stack 

# Create two 1-dimensional arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack along a new axis
result = np.stack((a, b), axis=-1)

print(result)  # Outputs: array([[1, 4], [2, 5], [3, 6]])
