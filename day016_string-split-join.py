def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)
    # write your code here

if __name__ == '__main__':
    line = input("Enter a string to split and join: ")
