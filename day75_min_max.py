import numpy as np

n, m = map(int, input("Enter rows and columns: ").split())

arr = []

for _ in range(n):
    row = list(map(int, input("Enter row: ").split()))
    arr.append(row)

arr = np.array(arr)

min_result = np.min(arr, axis=1)
max_result = np.max(min_result)

print("Minimum of each row:", min_result)
print("Maximum:", max_result)