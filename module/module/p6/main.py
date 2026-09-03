import recursive

n = int(input("Enter number: "))

print("Factorial:", recursive.factorial(n))

print("Fibonacci series:")

for i in range(n):
    print(recursive.fibonacci(i), end=" ")

print()

print("Sum of digits:", recursive.sum_digits(n))

print("Binary:", recursive.binary(n))