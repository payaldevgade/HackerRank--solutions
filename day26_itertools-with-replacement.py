from itertools import combinations_with_replacement

# Input
s, k = input("Enter the string and value of k (e.g., HACK 2): ").split()
k = int(k)

# Sort the string
s = "".join(sorted(s))

# Generate and print combinations with replacement
for i in combinations_with_replacement(s, k):
    print("".join(i))