import numpy as np

n, m, p = map(int, input("Enter N, M and P: ").split())

array1 = []
array2 = []

# First array
for i in range(n):
    row = list(map(int, input(f"Enter array 1 row {i + 1}: ").split()))
    array1.append(row)

# Second array
for i in range(m):
    row = list(map(int, input(f"Enter array 2 row {i + 1}: ").split()))
    array2.append(row)

array1 = np.array(array1)
array2 = np.array(array2)

result = np.concatenate((array1, array2), axis=0)

print(result)