class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Percentage: {self.percentage():.2f}")


n = 2
students = []

for i in range(2):
    print(f"\nEnter details for student {i+1}")
    roll_no = input("Roll No: ")
    name = input("Name: ")
    marks = [float(x) for x in input("Enter marks separated by spaces: ").split()]
    students.append(Student(roll_no, name, marks))

print()
for s in students:
    s.display()
