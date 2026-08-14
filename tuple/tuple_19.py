numbers = []
for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)

t = tuple(numbers)
even = 0
odd = 0

for num in t:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)