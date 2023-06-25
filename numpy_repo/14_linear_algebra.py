import numpy as np

a = np.array([[1., 2.], [3., 4.]])
inv_a = np.linalg.inv(a)
print(inv_a)  # Outputs: [[-2. ,  1. ], [ 1.5, -0.5]]


a = np.array([[1, 2], [3, 4]])
det_a = np.linalg.det(a)
print(det_a)  # Outputs: -2.0


a = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)  # Outputs: [-0.37228132  5.37228132]
print(eigenvectors)  # Outputs: [[-0.82456484 -0.41597356]
#                                    [ 0.56576746 -0.90937671]]


# Solving the system of equations:
# 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8
a = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)
print(x)  # Outputs: [2. 3.]


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank_a = np.linalg.matrix_rank(a)
print(rank_a)  # Outputs: 2


