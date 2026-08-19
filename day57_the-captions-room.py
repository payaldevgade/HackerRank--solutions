from collections import Counter

K = int(input("Enter group size: "))

rooms = list(map(int, input("Enter room numbers: ").split()))

count = Counter(rooms)

for room, frequency in count.items():
    if frequency == 1:
        print("Captain's room:", room)
        break