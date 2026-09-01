import re

n = int(input("Enter number of lines: "))
inside = False

for _ in range(n):
    line = input("Enter CSS line: ")

    if '{' in line:
        inside = True
        line = line.split('{', 1)[1]

    if inside:
        colors = re.findall(r'#[0-9a-fA-F]{3,6}\b', line)

        for color in colors:
            if len(color) == 4 or len(color) == 7:
                print(color)

    if '}' in line:
        inside = False