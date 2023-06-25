# array filtering

import numpy as np

# Create an array
a = np.array([1, 2, 3, 4, 5, 6])

# Create a filter for elements greater than 2
filter = a > 2

# Apply the filter to the array
b = a[filter]

print(b)  # Outputs: array([3, 4, 5, 6])


# array masking 

import numpy as np

# Create an array
a = np.array([1, 2, 3, 4, 5, 6])

# Create a mask for elements that are even
mask = a % 2 == 0

# Apply the mask to the array
b = a[mask]

print(b)  # Outputs: array([2, 4, 6])
