import numpy as np


n, m = map(int, input("Enter rows and columns: ").split())

arr = []

for _ in range(n):
    row = list(map(int, input("Enter row: ").split()))
    arr.append(row)

arr = np.array(arr)

sum_result = np.sum(arr, axis=0)
product_result = np.prod(sum_result)

print("Sum along axis 0:", sum_result)
print("Product:", product_result)
