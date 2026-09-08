
n = int(input("Enter number of elements: "))

t = tuple(map(int, input("Enter the elements: ").split()))

print("Tuple:", t)
print("Hash:", hash(t))
