from datetime import datetime

t = int(input("Enter number of test cases: "))

for i in range(t):
    time1 = input("Enter first timestamp: ")
    time2 = input("Enter second timestamp: ")

    time1 = datetime.strptime(time1, "%a %d %b %Y %H:%M:%S %z")
    time2 = datetime.strptime(time2, "%a %d %b %Y %H:%M:%S %z")

    difference = abs((time1 - time2).total_seconds())

    print("Difference:", int(difference))