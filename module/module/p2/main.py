import student

name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = student.total_marks(marks)
per = student.percentage(marks)
g = student.grade(per)

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", per)
print("Grade:", g)