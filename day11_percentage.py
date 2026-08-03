if __name__ == '__main__':
    n = int(input("Enter the number of students: "))
    student_marks = {}

    for _ in range(n):
        name, *scores = input("Enter the student's name and scores separated by space: ").split()
        scores = list(map(float, scores))
        student_marks[name] = scores

    query_name = input("Enter the student's name to query: ")

    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
