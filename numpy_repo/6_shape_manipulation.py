# Reshape 
import numpy as np

# Create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2-dimensional array
b = a.reshape((2, 3))

print(b)
# Outputs: 
# array([[1, 2, 3],
#        [4, 5, 6]])


#Flatten 

# Create a 2-dimensional array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
b = a.flatten()

print(b)  # Outputs: array([1, 2, 3, 4, 5, 6])

# Ravel

# Create a 2-dimensional array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Use ravel to flatten the array
b = a.ravel()

print(b)  # Outputs: array([1, 2, 3, 4, 5, 6])


# Transpose

# Create a 2-dimensional array
a = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose the array
b = a.T

print(b)
# Outputs: 
# array([[1, 4],
#        [2, 5],
#        [3, 6]])


# Expand Dimensions

# Create a 1-dimensional array
a = np.array([1, 2, 3])

# Add an axis
b = np.expand_dims(a, axis=0)

print(b)  # Outputs: array([[1, 2, 3]])



