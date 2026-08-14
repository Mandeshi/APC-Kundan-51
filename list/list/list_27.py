salaries = []
n = int(input("Enter number of employees: "))

for i in range(n):
    s = int(input("Enter salary: "))
    salaries.append(s)

highest = max(salaries)
lowest = min(salaries)
average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for s in salaries:
    if s > 50000:
        above_50000 = above_50000 + 1
    if s < 30000:
        below_30000 = below_30000 + 1

print("Highest salary =", highest)
print("Lowest salary =", lowest)
print("Average salary =", average)
print("Employees above 50000 =", above_50000)
print("Employees below 30000 =", below_30000)