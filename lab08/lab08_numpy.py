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

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()    # чтобы исходный массив hours не изменился
changed_hours[2:5] = 99
print(changed_hours, hours, sep='\n')

changed_matrix = matrix.copy()
changed_matrix[1] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print(matrix, changed_matrix, sep='\n')

#_______________________________________________________________________________

numbers = np.arange(12)
table = numbers.reshape(3, 4) # reshape(5, 3) выведет ошибку, так как 5*3 > 12
transposed = table.T

print(numbers.shape, table.shape, transposed.shape)
