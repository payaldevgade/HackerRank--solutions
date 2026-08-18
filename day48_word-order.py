n = int(input("Enter number of words: "))

words = {}

for _ in range(n):
    word = input("Enter word: ")

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print("Number of distinct words:", len(words))
print("Occurrences:", *words.values())