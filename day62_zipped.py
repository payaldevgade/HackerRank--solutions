n, x = map(int, input("Enter number of students and subjects: ").split())

marks = []

for _ in range(x):
    
    subject_marks = list(
        map(float, input("Enter marks for subject: ").split())
    )
    marks.append(subject_marks)

print("Average marks:")

for student_marks in zip(*marks):
    average = sum(student_marks) / x
    print(average)
    
