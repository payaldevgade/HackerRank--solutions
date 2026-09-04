n = int(input("Enter number of test cases: "))

for _ in range(n):
    a, b = input("Enter two values: ").split()

    try:
        result = int(a) // int(b)
        print(result)

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)
