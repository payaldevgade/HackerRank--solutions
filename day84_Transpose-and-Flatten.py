import numpy as np

rows, columns = map(int, input("Enter rows and columns: ").split())

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

array = np.array(matrix)

print("\nTranspose:")
print(np.transpose(array))

print("\nFlatten:")
print(array.flatten())