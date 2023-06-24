import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = a + b
print(c)  # Prints: array([5, 7, 9])


c = a - b
print(c)  # Prints: array([-3, -3, -3])


c = a * b
print(c)  # Prints: array([ 4, 10, 18])


c = a / b
print(c)  # Prints: array([0.25, 0.4 , 0.5 ])
 

c = np.sqrt(a)
print(c)  # Prints: array([1.        , 1.41421356, 1.73205081])
 

c = np.power(a, 2)
print(c)  # Prints: array([1, 4, 9])
 

c = np.sin(a)
print(c)  # Prints: array([0.84147098, 0.90929743, 0.14112001])


c = np.log(a)
print(c)  # Prints: array([0.        , 0.69314718, 1.09861229])
 

c = np.sum(a)
print(c)  # Prints: 6
 

print(np.min(a))  # Prints: 1
print(np.max(a))  # Prints: 3



