from collections import Counter

n = int(input(" enter number of shoes:"))

shoes = list(map(int, input(" enter shoe sizes:").split()))

shoe_count = Counter(shoes)

customers = int(input(" enter number of customers:"))

money = 0

for _ in range(customers):
    size, price = map(int, input(" enter customer request (size price):").split())

    if shoe_count[size] > 0:
        money += price
        shoe_count[size] -= 1

print(money)
