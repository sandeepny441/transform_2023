import numpy as np

data = np.loadtxt('data.txt')  # 'data.txt' is the name of the file
print(data)


data = np.array([[1, 2, 3], [4, 5, 6]])
np.savetxt('data.txt', data)
 

data = np.genfromtxt('data.txt', delimiter=',') 
 # The delimiter specifies how the data is separated
print(data)


data = np.array([[1, 2, 3], [4, 5, 6]])
np.save('data.npy', data)  # Saving the array to a binary file

loaded_data = np.load('data.npy')  # Loading the array from a binary file
print(loaded_data)


data1 = np.array([1, 2, 3])
data2 = np.array([4, 5, 6])
np.savez('data.npz', data1=data1, data2=data2)

loaded_data = np.load('data.npz')  # Loading the array from a binary file
print(loaded_data['data1'])
print(loaded_data['data2'])

 
 

