n = int(input("Enter number of English subscribers: "))

english = set(map(int, input("Enter English roll numbers: ").split()))

m = int(input("Enter number of French subscribers: "))

french = set(map(int, input("Enter French roll numbers: ").split()))

result = english.symmetric_difference(french)

print("Students with only one subscription:", len(result))
