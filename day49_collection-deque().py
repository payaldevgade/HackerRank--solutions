from collections import deque

d = deque()

n = int(input("Enter number of operations: "))

for _ in range(n):
    command = input("Enter operation: ").split()

    if command[0] == "append":
        d.append(command[1])

    elif command[0] == "appendleft":
        d.appendleft(command[1])

    elif command[0] == "pop":
        d.pop()

    elif command[0] == "popleft":
        d.popleft()

print("Final deque:", *d)