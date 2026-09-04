m = int(input("Enter the size of set A: "))
a = set(map(int, input("Enter the elements of set A: ").split()))

n = int(input("Enter the size of set B: "))
b = set(map(int, input("Enter the elements of set B: ").split()))

result = a.symmetric_difference(b)

print("Symmetric difference:")
for i in sorted(result):
    print(i)
