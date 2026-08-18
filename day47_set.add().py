n = int(input("Enter number of stamps: "))

countries = set()

for _ in range(n):
    country = input("Enter country name: ")
    countries.add(country)

print("Total distinct countries:", len(countries))