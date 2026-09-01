import re
import email.utils

T = int(input("Enter number of emails: "))

for _ in range(T):
    name, email_text = input("Enter name and email: ").split()

    email_address = email.utils.parseaddr(email_text)[1]

    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

    if re.match(pattern, email_address):
        print(name, email_text)