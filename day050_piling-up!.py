from collections import deque

T = int(input("Enter number of test cases: "))

for _ in range(T):
    n = int(input("Enter number of cubes: "))
    blocks = deque(map(int, input("Enter cube sizes: ").split()))

    top = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            cube = blocks.popleft()
        else:
            cube = blocks.pop()

        if cube > top:
            possible = False
            break

        top = cube

    if possible:
        print("Yes")
    else:
        print("No")
