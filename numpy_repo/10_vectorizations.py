# Arithmetic Operations
import numpy as np

# Create two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Perform element-wise addition
c = a + b
print(c)  # Outputs: array([5, 7, 9])

# Perform element-wise multiplication
d = a * b
print(d)  # Outputs: array([ 4, 10, 18])

#============================================================

# Mathematical Functions

# Create an array
a = np.array([1, 2, 3])

# Compute the square root of each element
b = np.sqrt(a)
print(b)  # Outputs: array([1.        , 1.41421356, 1.73205081])

#============================================================

# Conditional Operations 

# Create an array
a = np.array([1, 2, 3])

# Check which elements are greater than 2
b = a > 2
print(b)  # Outputs: array([False, False,  True])

#============================================================

# Statistical Functions

# Create an array
a = np.array([1, 2, 3])

# Calculate the sum of all elements
b = np.sum(a)
print(b)  # Outputs: 6

# Calculate the mean of all elements
c = np.mean(a)
print(c)  # Outputs: 2.0

#============================================================

# Applying a Function to Each Element

# Create an array
a = np.array([1, 2, 3])

# Define a function
def square(x):
    return x ** 2

# Apply the function to each element of the array
b = np.vectorize(square)(a)
print(b)  # Outputs: array([1, 4, 9])

#============================================================


