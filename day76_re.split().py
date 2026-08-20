import re

regex_pattern = r'[,\.]'

text = input("Enter the string: ")

result = re.split(regex_pattern, text)

print("\n".join(result))