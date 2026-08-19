import math


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __sub__(self, other):
        return Complex(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imaginary)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2

        real = (
            self.real * other.real +
            self.imaginary * other.imaginary
        ) / denominator

        imaginary = (
            self.imaginary * other.real -
            self.real * other.imaginary
        ) / denominator

        return Complex(real, imaginary)

    def mod(self):
        return Complex(
            math.sqrt(self.real ** 2 + self.imaginary ** 2),
            0
        )

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            return f"{self.real:.2f}{self.imaginary:.2f}i"


a, b = 2, 1
c, d = 5, 6

x = Complex(a, b)
y = Complex(c, d)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x.mod())
print(y.mod())
