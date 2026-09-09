
import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]


arr = input("Enter numbers: ").strip().split()

result = arrays(arr)

print("Reversed array:")
print(result)
