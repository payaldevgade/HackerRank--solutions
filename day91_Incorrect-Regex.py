import re

T = int(input("Enter number of test cases: "))

for _ in range(T):
    s = input("Enter regex: ")

    try:
        re.compile(s)

        if re.search(r'(\*|\+|\?|\{.*\})[\*\+\?]', s):
            print("False")
        else:
            print("True")

    except re.error:
        print("False")