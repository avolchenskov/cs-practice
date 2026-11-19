import numpy as np
hours = np.array([i for i in range(0, 22, 3)])
line = np.linspace(0, 1, 5)
zeros = np.zeros(6)
unknown_table = np.array([
        [-1, -1, -1],
        [-1, -1, -1]
])
identity = np.ones((3, 3))

print(hours, hours.shape, hours.ndim, hours.size, hours.dtype, sep='\n')

#_______________________________________________________________________________
print()
print(hours[2], hours[-1], hours[2:6], hours[1::2], hours[::-1], sep='\n')

#_______________________________________________________________________________
print()
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape, temperatures.ndim, temperatures.size)
print(temperatures[0], temperatures[:, -1], temperatures[:2, 1:], temperatures[:2, 1:3], sep='\n')

#_______________________________________________________________________________
print()

matrix = np.arange(1, 26).reshape(5, 5)

print(matrix[:3], matrix[:3].shape, matrix[-2:], matrix[-2:].shape, matrix[1:4, 2:5], matrix[1:4, 2:5].shape, matrix[-2:, -2:], matrix[-2:, -2:].shape)

#_______________________________________________________________________________
