n = int(input("Enter number of elements in A: "))

A = set(map(int, input("Enter elements of A: ").split()))

N = int(input("Enter number of operations: "))

for _ in range(N):
    operation, size = input("Enter operation and size: ").split()

    other = set(map(int, input("Enter elements of other set: ").split()))

    if operation == "update":
        A.update(other)

    elif operation == "intersection_update":
        A.intersection_update(other)

    elif operation == "difference_update":
        A.difference_update(other)

    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other)

print("Sum:", sum(A))

