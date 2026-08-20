import re

def replace_symbols(match):
    if match.group(0) == '&&':
        return 'and'
    else:
        return 'or'

n = int(input("Enter number of lines: "))

for _ in range(n):
    line = input("Enter line: ")
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', replace_symbols, line))