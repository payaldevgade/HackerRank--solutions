n = int(input("Enter number of English subscribers: "))

english = set(map(int, input("Enter English roll numbers: ").split()))

m = int(input("Enter number of French subscribers: "))

french = set(map(int, input("Enter French roll numbers: ").split()))

result = english.union(french)

print("Total students with at least one subscription:", len(result))
