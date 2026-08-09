from collections import defaultdict

n, m = map(int, input(" enter values for n and m:").split())

group_a = defaultdict(list)

# Read Group A
for i in range(1, n + 1):
    word = input(" enter word for group A:")
    group_a[word].append(i)

# Read Group B
for _ in range(m):
    word = input(" enter word for group B:")

    if word in group_a:
        print(*group_a[word])
    else:
        print(-1)