f = open("students.txt", "r")

students = []

for line in f:
    roll, name, marks = line.strip().split(",")
    students.append([roll, name, int(marks)])

f.close()

print("All Students:")
for s in students:
    print(s)

highest = max(students, key=lambda x: x[2])
print("Highest Marks:", highest)

total = 0

for s in students:
    total += s[2]

average = total / len(students)

print("Average:", average)

print("Students above 80:")

for s in students:
    if s[2] > 80:
        print(s)