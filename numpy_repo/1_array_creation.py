import numpy as np

arr = np.array([1, 2, 3, 4, 5])  # A 1-dimensional array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # A 2-dimensional array

print(arr.shape)  # Prints: (5,)
print(arr2.shape)  # Prints: (2, 3)

print(arr.dtype)  # Could print: int64

print(arr.size)  # Prints: 5
print(arr2.size)  # Prints: 6

reshaped_arr = arr.reshape((5, 1))  # Reshapes arr to 5 rows and 1 column

seq_arr = np.arange(0, 10, 2)  # Creates an array with numbers from 0 to 10 with step size 2

lin_arr = np.linspace(0, 10, 5)  # Creates an array with 5 numbers, evenly spaced from 0 to 10

zeros_matrix = np.zeros((2, 2))  # Creates a 2x2 matrix filled with zeroes
ones_matrix = np.ones((2, 2))  # Creates a 2x2 matrix filled with ones

identity_matrix = np.eye(3)  # Creates a 3x3 identity matrix

random_array = np.random.random((2, 2))  # Creates a 2x2 array filled with random values
