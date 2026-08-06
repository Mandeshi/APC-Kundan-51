numbers = []

for i in range(3):
    n = int(input("Enter number: "))
    numbers.append(n)

total = sum(numbers)
avg = total / len(numbers)

print("Sum =", total)
print("Average =", avg)
