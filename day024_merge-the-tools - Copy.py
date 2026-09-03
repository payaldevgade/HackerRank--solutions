def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        result = ""

        for ch in substring:
            if ch not in result:
                result += ch

        print(result)


# Main Program
string = input("Enter the string: ")
k = int(input("Enter the value of k: "))

merge_the_tools(string, k)
