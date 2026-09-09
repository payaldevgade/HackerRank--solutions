
import numpy

A = numpy.array(input("Enter array A: ").split(), int)
B = numpy.array(input("Enter array B: ").split(), int)

print("Inner product:")
print(numpy.inner(A, B))

print("Outer product:")
print(numpy.outer(A, B))
