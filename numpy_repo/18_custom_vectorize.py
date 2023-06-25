import numpy as np

# Let's say we have a function that works with individual numbers
def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b
    else:
        return a + b

# This function doesn't work with arrays
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])
try:
    print(myfunc(x, y))  # This raises an error
except ValueError as e:
    print(f"ValueError: {e}")

# Using np.vectorize, we can make it work with arrays
vfunc = np.vectorize(myfunc)
print(vfunc(x, y))  # This works: [6 6 6 2 4]
