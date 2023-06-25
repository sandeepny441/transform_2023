# CuPy
import cupy as cp

# Create a 2D array on the GPU
x_gpu = cp.array([[1, 2, 3], [4, 5, 6]])

# Perform computations on this array
y_gpu = cp.exp(x_gpu)

# You can convert the result back to a NumPy array on the CPU if needed
y_cpu = cp.asnumpy(y_gpu)

# Numba 
from numba import cuda
import numpy as np

@cuda.jit
def add_kernel(x, y, out):
    tx = cuda.threadIdx.x  # this is the unique thread ID within a 1D block
    ty = cuda.blockIdx.x   # Similarly, this is the unique block ID within the 1D grid

    block_size = cuda.blockDim.x  # number of threads per block
    grid_size = cuda.gridDim.x    # number of blocks in the grid

    start = tx + ty * block_size
    stride = block_size * grid_size

    # Assuming x and y inputs are same length
    for i in range(start, x.shape[0], stride):
        out[i] = x[i] + y[i]

# Now we can use this function
n = 100000
x = np.arange(n).astype(np.float32)
y = 2 * x
out = np.empty_like(x)

# Move the data to the GPU
x_device = cuda.to_device(x)
y_device = cuda.to_device(y)
out_device = cuda.to_device(out)

# Set up enough threads for kernel
threads_per_block = 128
blocks_per_grid = 30

# Launch kernel (device arrays are automatically converted to pointers)
add_kernel[blocks_per_grid, threads_per_block](x_device, y_device, out_device)

# Copy the result back to the CPU (this is synchronous and will wait for kernel to complete)
out = out_device.copy_to_host()



