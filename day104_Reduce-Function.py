
from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


n = int(input("Enter number of rational numbers: "))

fracs = []

for i in range(n):
    numerator, denominator = map(
        int,
        input(f"Enter numerator and denominator for fraction {i + 1}: ").split()
    )
    fracs.append(Fraction(numerator, denominator))

result = product(fracs)

print("Product:", result[0], result[1])

