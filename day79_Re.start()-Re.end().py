import re

string = input("Enter the string: ")
sub_string = input("Enter the substring: ")

matches = re.finditer(f'(?={sub_string})', string)

found = False

for match in matches:
    print((match.start(), match.start() + len(sub_string) - 1))
    found = True

if not found:
    print((-1, -1))