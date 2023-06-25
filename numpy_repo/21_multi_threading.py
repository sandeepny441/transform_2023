import numpy as np
import concurrent.futures
import time

# a function that performs some heavy computation on a NumPy array
def heavy_computation(data, start, end):
    time.sleep(0.1)  # simulate a heavy computation
    return data[start:end].sum()

# create a large array
data = np.random.rand(1000)

# create a ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # split the data into chunks and submit computations
    futures = [executor.submit(heavy_computation, data, i, i+100) for i in range(0, len(data), 100)]
    # collect the results as they become available
    results = [f.result() for f in concurrent.futures.as_completed(futures)]

# print the sum of the results
print(sum(results))
