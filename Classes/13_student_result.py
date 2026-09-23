class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        percent = self.percentage()
        if percent >= 90:
            return "A"
        elif percent >= 75:
            return "B"
        elif percent >= 60:
            return "C"
        else:
            return "D"

    def __del__(self):
        print(f"Result processing for {self.name} completed")


name = input("Enter student name: ")
marks = [float(x) for x in input("Enter marks for 5 subjects separated by spaces: ").split()]

result = StudentResult(name, marks)
print("Total:", result.total())
print("Percentage:", result.percentage())
print("Grade:", result.grade())

del result   
