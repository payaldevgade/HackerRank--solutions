import re

rows, cols = map(int, input("Enter rows and columns: ").split())

matrix = []

for _ in range(rows):
    matrix.append(input("Enter row: "))

decoded = ''

for col in range(cols):
    for row in range(rows):
        decoded += matrix[row][col]

decoded = re.sub(
    r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',
    ' ',
    decoded
)

print("Decoded script:", decoded)