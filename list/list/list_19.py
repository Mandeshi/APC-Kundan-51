students = ["varad", "Namo", "Shivratna", "Pravin"]

print("Total students =", len(students))

search = input("Enter student name to search: ")
if search in students:
    print(search, "is present")
else:
    print(search, "not found")

students.append("Anuj")

students.remove("Namo")

print("Updated list:", students)