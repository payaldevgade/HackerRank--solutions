def average(arr):
    distinct = set(arr)
    return round(sum(distinct) / len(distinct), 3)

if __name__ == '__main__':
    n = int(input(" enter a number"))
    arr = list(map(int, input(" enter a number").split()))
    result = average(arr)
    print(result)