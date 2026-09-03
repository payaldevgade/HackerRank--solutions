import re

T = int(input("Enter number of test cases: "))

for _ in range(T):
    card = input("Enter credit card number: ")

    pattern = r'^[456]\d{15}$|^[456]\d{3}(-\d{4}){3}$'

    if re.match(pattern, card) and not re.search(r'(\d)\1{3,}', card.replace('-', '')):
        print("Valid")
    else:
        print("Invalid")