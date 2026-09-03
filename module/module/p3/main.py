import numbers

n = int(input("Enter a number: "))

if numbers.prime(n):
    print("Prime number")
else:
    print("Not a prime number")

if numbers.palindrome(n):
    print("Palindrome")
else:
    print("Not palindrome")

if numbers.armstrong(n):
    print("Armstrong number")
else:
    print("Not Armstrong")

if numbers.perfect(n):
    print("Perfect number")
else:
    print("Not perfect")