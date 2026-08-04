def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input("Enter the original string: ")
    i, c = input("Enter the position and character to replace (space-separated): ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)