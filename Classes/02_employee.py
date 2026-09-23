class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print(f"Emp ID: {self.emp_id}, Name: {self.name}")
        print(f"HRA: {self.calculate_hra()}, DA: {self.calculate_da()}, Gross Salary: {self.gross_salary()}")


emp_id = input("Enter employee ID: ")
name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

e1 = Employee(emp_id, name, basic_salary)
e1.display()
