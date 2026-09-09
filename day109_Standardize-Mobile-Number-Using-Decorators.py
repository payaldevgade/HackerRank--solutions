
def wrapper(f):
    def fun(l):
        formatted = []

        for number in l:
            number = number[-10:]
            number = "+91 " + number[:5] + " " + number[5:]
            formatted.append(number)

        return f(formatted)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

n = int(input("Enter number of mobile numbers: "))

l = []

for i in range(n):
    l.append(input(f"Enter mobile number {i + 1}: "))

sort_phone(l)

