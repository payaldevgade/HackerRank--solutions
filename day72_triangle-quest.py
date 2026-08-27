n = int(input("Enter height: "))


for i in range(1, n):
    print(i * (10**i - 1) // 9)
