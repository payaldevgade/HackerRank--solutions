import re

T = int(input("Enter number of test cases: "))

for _ in range(T):
    uid = input("Enter UID: ")

    if (
        len(uid) == 10
        and uid.isalnum()
        and len(set(uid)) == 10
        and len(re.findall(r'[A-Z]', uid)) >= 2
        and len(re.findall(r'[0-9]', uid)) >= 3
    ):
        print("Valid")
    else:
        print("Invalid")