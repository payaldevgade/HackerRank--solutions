import string

def print_rangoli(size):
    alpha = string.ascii_lowercase

    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        row = "-".join(left + right)
        lines.append(row.center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input("Enter the size of the rangoli: "))
    print_rangoli(n)