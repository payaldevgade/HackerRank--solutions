
def score_words(words):
    score = 0

    for word in words:
        num_vowels = 0

        for letter in word:
            if letter in 'aeiouy':
                num_vowels += 1

        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1

    return score


n = int(input("Enter number of words: "))
words = input("Enter the words: ").split()

result = score_words(words)

print("Score:", result)

