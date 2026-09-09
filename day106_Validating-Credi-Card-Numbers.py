
import re

n = int(input("Enter number of credit cards: "))

for i in range(n):
    card = input(f"Enter credit card {i + 1}: ").strip()

    pattern = r'^[456]\d{15}$|^[456]\d{3}(-\d{4}){3}$'

    if re.match(pattern, card) and not re.search(
        r'(\d)\1{3,}', card.replace('-', '')
    ):
        print("Valid")
    else:
        print("Invalid")
