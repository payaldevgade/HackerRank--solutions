from collections import OrderedDict

n = int(input(" enter number of items:"))
items = OrderedDict()

for _ in range(n):
    name, price = input(" enter item name and price:").rsplit(" ", 1)
    items[name] = items.get(name, 0) + int(price)

for name, price in items.items():
    print(name, price)