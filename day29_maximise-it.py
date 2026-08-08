from itertools import product

k, m = map(int, input("Enter K and M: ").split())

lists = []

for i in range(k):
    data = list(map(int, input(f"Enter list {i+1}: ").split()))
    lists.append(data[1:])   # Ignore the first number

maximum = 0

for values in product(*lists):
    total = sum(x**2 for x in values) % m
    maximum = max(maximum, total)

print("Maximum value:", maximum)