s = input("Enter the string: ")


lower = sorted(c for c in s if c.islower())
upper = sorted(c for c in s if c.isupper())
odd = sorted(c for c in s if c.isdigit() and int(c) % 2 != 0)
even = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)

result = ''.join(lower + upper + odd + even)

print("Sorted string:", result)
