students = ["Amit", "Ravi", "Priya"]

print("Total Students:", len(students))

name = input("Enter name to search: ")

if name in students:
    print("Present")
else:
    print("Not Present")

students.append("Neha")
students.remove("Ravi")

print("Total Students:", len(students))