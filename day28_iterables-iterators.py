from itertools import combinations

n = int(input("Enter the number of letters: "))
letters = input("Enter the letters separated by spaces: ").split()
k = int(input("Enter the value of k: "))

all_combinations = list(combinations(range(n), k))

count = 0

for combo in all_combinations:
    for index in combo:
        if letters[index] == 'a':
            count += 1
            break

print(count / len(all_combinations))