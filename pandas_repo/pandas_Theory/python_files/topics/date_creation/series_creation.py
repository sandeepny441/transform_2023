import pandas as pd

# Create series from list
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)

# Create series from numpy array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
s2 = pd.Series(arr)
print(s2)

# Create series from dictionary
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s3 = pd.Series(dict)
print(s3)
