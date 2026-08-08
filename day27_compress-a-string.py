from itertools import groupby

s = input("Enter the string: ")

for key, group in groupby(s):
    print((len(list(group)), int(key)), end=" ")