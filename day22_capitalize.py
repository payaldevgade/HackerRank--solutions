def solve(s):
    words = s.split(" ")
    result = []

    for word in words:
        result.append(word.capitalize())

    return " ".join(result)

# Main program
s = input("Enter full name: ")
print(solve(s))