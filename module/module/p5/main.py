import salary

basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))

gross = salary.gross_salary(basic, allowance)
deduction = salary.deductions(gross)
net = salary.net_salary(gross, deduction)

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)