import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string = input(" enter a string:")
    max_width = int(input(" enter max width:"))

    result = wrap(string, max_width)
    print(result)
