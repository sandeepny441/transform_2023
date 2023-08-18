import torch
import numpy as np
import time

# Create two random matrices of size 5000 x 5000
mat1 = torch.randn(150001, 150001)
mat2 = torch.randn(150001, 150001)

# CPU matrix multiplication
start_time = time.time()
result_cpu = torch.mm(mat1, mat2)
end_time = time.time()
cpu_time = end_time - start_time
print(f"CPU matrix multiplication time: {cpu_time:.4f} seconds")

# Move matrices to GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
mat1 = mat1.to(device)
mat2 = mat2.to(device)

# GPU matrix multiplication
start_time = time.time()
result_gpu = torch.mm(mat1, mat2)
torch.cuda.synchronize()  # Ensure computation is done
end_time = time.time()
gpu_time = end_time - start_time
print(f"GPU matrix multiplication time: {gpu_time:.4f} seconds")

print(f"GPU is {cpu_time / gpu_time:.2f} times faster for this operation!")
