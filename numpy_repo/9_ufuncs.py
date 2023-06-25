# arithmetic 

import numpy as np

# Create two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Perform element-wise addition
c = np.add(a, b)
print(c)  # Outputs: array([5, 7, 9])

# Perform element-wise multiplication
d = np.multiply(a, b)
print(d)  # Outputs: array([ 4, 10, 18])

#=======================================================================

# Trigonometric Functions

# Create an array
a = np.array([0, np.pi/2, np.pi])

# Calculate the sine of each element
b = np.sin(a)
print(b)  # Outputs: array([0., 1., 0.])

#=======================================================================

# Exponential and Logarithmic Functions

# Create an array
a = np.array([1, 2, 3])

# Calculate the exponential of each element
b = np.exp(a)
print(b)  # Outputs: array([ 2.71828183,  7.3890561 , 20.08553692])

# Calculate the natural logarithm of each element
c = np.log(a)
print(c)  # Outputs: array([0.        , 0.69314718, 1.09861229])

#=======================================================================

# Comparisons
# Create two arrays
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])

# Element-wise comparison
c = np.greater(a, b)
print(c)  # Outputs: array([False, False,  True])

#=======================================================================
#=======================================================================




