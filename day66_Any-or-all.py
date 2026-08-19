n = int(input("Enter number of integers: "))
numbers = input("Enter integers: ").split()

result = all(int(x) > 0 for x in numbers) and any(x == x[::-1] for x in numbers)

print("Result:", result)