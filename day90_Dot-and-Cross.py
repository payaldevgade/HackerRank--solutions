import numpy as np

n = int(input("Enter the size of matrix: "))

A = []
B = []

# First matrix
for i in range(n):
    row = list(map(int, input(f"Enter A row {i + 1}: ").split()))
    A.append(row)

# Second matrix
for i in range(n):
    row = list(map(int, input(f"Enter B row {i + 1}: ").split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

result = np.dot(A, B)

print(result)