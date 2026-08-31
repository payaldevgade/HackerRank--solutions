import numpy as np

n = int(input("Enter the size of matrix: "))

matrix = []

for i in range(n):
    row = list(map(float, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

determinant = np.linalg.det(matrix)

print(f"Determinant: {round(determinant, 2)}")