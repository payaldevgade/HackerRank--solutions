n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

highest = max(arr)

while highest in arr:
    arr.remove(highest)

print(max(arr))