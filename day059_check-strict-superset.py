A = set(map(int, input("Enter elements of A: ").split()))

n = int(input("Enter number of other sets: "))

result = True

for _ in range(n):
    B = set(map(int, input("Enter elements of B: ").split()))

    if not (A > B):
        result = False

print("Is A a strict superset of all sets?", result)
