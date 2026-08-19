T = int(input("Enter number of test cases: "))

for _ in range(T):
    n = int(input("Enter number of elements in A: "))
    A = set(map(int, input("Enter elements of A: ").split()))

    m = int(input("Enter number of elements in B: "))
    B = set(map(int, input("Enter elements of B: ").split()))

    print("Is A a subset of B?", A.issubset(B))