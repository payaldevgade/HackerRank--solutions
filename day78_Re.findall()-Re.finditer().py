import re

s = input("Enter the string: ")

pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

matches = re.findall(pattern, s)

if matches:
    print('\n'.join(matches))
else:
    print(-1)