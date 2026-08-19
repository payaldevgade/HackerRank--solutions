n, m = map(int, input("Enter number of athletes and attributes: ").split())

data = []

for _ in range(n):
    row = list(map(int, input("Enter athlete details: ").split()))
    data.append(row)

k = int(input("Enter attribute index to sort by: "))

data.sort(key=lambda row: row[k])

print("Sorted data:")

for row in data:
    print(*row)