import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input("Enter the string to wrap: "), int(input("Enter the maximum width: "))
    result = wrap(string, max_width)
    print(result)