import re

T = int(input("Enter number of inputs: "))

for _ in range(T):
    s = input("Enter mobile number: ")
    
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")