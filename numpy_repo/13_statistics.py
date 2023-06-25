import numpy as np

data = np.array([1, 2, 3, 4, 5])
print(np.mean(data))  # Outputs: 3.0

data = np.array([1, 2, 3, 4, 5])
print(np.median(data))  # Outputs: 3.0

data = np.array([1, 2, 3, 4, 5])
print(np.std(data))  # Outputs: 1.4142135623730951

data = np.array([1, 2, 3, 4, 5])
print(np.var(data))  # Outputs: 2.0

data = np.array([1, 2, 3, 4, 5])
print(np.min(data))  # Outputs: 1
print(np.max(data))  # Outputs: 5

data = np.array([1, 2, 3, 4, 5])
print(np.percentile(data, 50))  # Outputs: 3.0, which is the same as the median

data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
hist, bin_edges = np.histogram(data, bins=range(6))
print(hist)  # Outputs: [1 2 3 4 0], meaning 1 instance of 0, 2 instances of 1, etc.
print(bin_edges)  # Outputs: [0 1 2 3 4 5], the edges of the bins
