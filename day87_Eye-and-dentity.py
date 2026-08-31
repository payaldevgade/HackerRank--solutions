import numpy as np

np.set_printoptions(legacy='1.13')

n, m = map(int, input("Enter rows and columns: ").split())

print(np.eye(n, m))