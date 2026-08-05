import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))

prime = True

if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

print("Square root =", root)

if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
