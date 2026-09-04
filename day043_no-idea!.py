n, m = map(int, input("Enter n and m: ").split())

arr = list(map(int, input("Enter array elements: ").split()))

A = set(map(int, input("Enter elements of set A: ").split()))

B = set(map(int, input("Enter elements of set B: ").split()))

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print("Final happiness:", happiness)
