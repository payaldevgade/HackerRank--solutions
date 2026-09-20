from itertools import combinations_with_replacement

s, k = input("Enter the string and value of k (e.g., HACK 2): ").split()
k = int(k)

s = "".join(sorted(s))

# Generate and print 
for i in combinations_with_replacement(s, k):
    print("".join(i))
