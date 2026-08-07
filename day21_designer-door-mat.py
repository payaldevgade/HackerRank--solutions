# Read input
N, M = map(int, input("Enter N and M: ").split())

# Top half
for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

# Middle line
print("WELCOME".center(M, "-"))

# Bottom half
for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))