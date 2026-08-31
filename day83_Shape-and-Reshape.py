import numpy as np

numbers = list(map(int, input("Enter 9 integers: ").split()))

array = np.array(numbers)

reshaped_array = np.reshape(array, (3, 3))

print(reshaped_array)