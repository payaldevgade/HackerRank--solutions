import re

s = input("Enter the string: ")

match = re.search(r'([a-zA-Z0-9])\1', s)

if match:
    print("First repeating alphanumeric character:", match.group(1))
else:
    print("No repeating alphanumeric character:", -1)