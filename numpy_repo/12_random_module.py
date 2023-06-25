# Generate Random Number from Uniform Distribution
import numpy as np

# Generate a single random number
random_num = np.random.rand()
print(random_num)

# Generate an array of random numbers
random_nums = np.random.rand(5)
print(random_nums)

# Generate a 2D array of random numbers
random_nums_2d = np.random.rand(3, 3)
print(random_nums_2d)
# =================================================================
# Generate Random Integer

# Generate a single random integer between 0 and 10
random_int = np.random.randint(0, 10)
print(random_int)

# Generate an array of 5 random integers between 0 and 10
random_ints = np.random.randint(0, 10, 5)
print(random_ints)

# ================================================================
# Generate Random Numbers from Normal Distribution 

# Generate a single random number from a normal distribution
random_num = np.random.randn()
print(random_num)

# Generate an array of random numbers from a normal distribution
random_nums = np.random.randn(5)
print(random_nums)

# Generate a 2D array of random numbers from a normal distribution
random_nums_2d = np.random.randn(3, 3)
print(random_nums_2d)

# ================================================================
# Randomly Shuffle a Sequence 

# Create an array of numbers
nums = np.array([1, 2, 3, 4, 5])

# Shuffle the numbers
np.random.shuffle(nums)
print(nums)

# ================================================================
# ================================================================

