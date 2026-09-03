f = open("employee.txt", "r")

employees = []

for line in f:
    id, name, dept, salary = line.strip().split(",")
    employees.append([id, name, dept, int(salary)])

f.close()

print("All Employees")

for e in employees:
    print(e)

highest = max(employees, key=lambda x: x[3])

print("Highest Paid:", highest)

total = 0

for e in employees:
    total += e[3]

print("Average Salary:", total / len(employees))

amount = int(input("Enter salary: "))

print("Employees above salary:")

for e in employees:
    if e[3] > amount:
        print(e)