
n = int(input("Enter number of elements: "))

s = set(map(int, input("Enter set elements: ").split()))

commands = int(input("Enter number of commands: "))

for _ in range(commands):
    command = input("Enter command: ").split()

    if command[0] == "pop":
        s.pop()

    elif command[0] == "remove":
        value = int(command[1])
        if value in s:
            s.remove(value)

    elif command[0] == "discard":
        value = int(command[1])
        s.discard(value)

print("Sum:", sum(s))

