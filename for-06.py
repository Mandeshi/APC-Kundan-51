x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 1

for i in range(1, n + 1):
    fact = 1
    power = 2 * i

    for j in range(1, power + 1):
        fact *= j

    term = (x ** power) / fact

    if i % 2 == 1:
        sum -= term
    else:
        sum += term

print("cos(x) =", sum)
