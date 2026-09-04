from collections import namedtuple

n = int(input(" enter number of students:"))
Student = namedtuple('Student', input(" enter field names:").split())

print(f"{sum(int(Student(*input(" enter student details:").split()).MARKS) for _ in range(n)) / n:.2f}")
