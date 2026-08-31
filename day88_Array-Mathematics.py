import numpy as np

n, m = map(int, input("Enter rows and columns: ").split())

array1 = []
array2 = []

# First array
for i in range(n):
    row = list(map(int, input(f"Enter array 1 row {i + 1}: ").split()))
    array1.append(row)

# Second array
for i in range(n):
    row = list(map(int, input(f"Enter array 2 row {i + 1}: ").split()))
    array2.append(row)

a = np.array(array1)
b = np.array(array2)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)