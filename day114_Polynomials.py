
import numpy

coefficients = list(map(float, input("Enter polynomial coefficients: ").split()))
x = float(input("Enter value of x: "))

result = numpy.polyval(coefficients, x)

print("Result:", result)

