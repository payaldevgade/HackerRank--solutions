from itertools import product

A = list(map(int, input(" enter elements of list A:").split("")))
B = list(map(int, input(" enter elements of list B:").split()))

print(*product(A, B))# Enter your code here. Read input from STDIN. Print output to STDOUT
