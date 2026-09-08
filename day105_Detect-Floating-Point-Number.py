
import re

t = int(input("Enter number of test cases: "))

for i in range(t):
    s = input(f"Enter number {i + 1}: ")

    pattern = r'^[+-]?\d*\.\d+$'

    result = bool(re.match(pattern, s))

    print(result)

