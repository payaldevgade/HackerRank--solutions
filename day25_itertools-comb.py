from itertools import combinations

s, k = input("Enter the string and k (e.g., HACK 2): ").split()
k = int(k)

s = "".join(sorted(s))

for i in range(1, k + 1):
    for j in combinations(s, i):
        print("".join(j))