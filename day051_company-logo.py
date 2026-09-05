from collections import Counter

s = input("Enter company name: ")

count = Counter(s)

result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

print("Top 3 characters:")

for char, frequency in result[:3]:
    print(char, frequency)
