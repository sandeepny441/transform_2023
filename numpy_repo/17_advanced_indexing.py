import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
idx = np.array([1, 3, 5])
print(x[idx])  # Outputs: [1 3 5]


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
mask = x > 5  # creates a boolean array
print(x[mask])  # Outputs: [6 7 8 9]


x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
row_idx = np.array([0, 1, 2])
col_idx = np.array([2, 1, 0])
print(x[row_idx, col_idx])  # Outputs: [2 4 6]


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
mask = x % 2 == 0  # selects all even numbers
x[mask] = -1  # all even numbers are replaced by -1
print(x)  # Outputs: [-1  1 -1  3 -1  5 -1  7 -1  9]
