import numpy as np

n, m = map(int, input("Enter rows and columns: ").split())

arr = np.array([
    list(map(int, input("Enter row: ").split()))
    for _ in range(n)
])

mean = np.mean(arr, axis=1)
var = np.var(arr, axis=0)
std = np.std(arr)

print(mean)
print(var)
print(np.round(std, 11))