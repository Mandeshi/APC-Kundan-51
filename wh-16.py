n = int(input("Enter how many numbers: "))

smallest = float('inf')

for i in range(n):
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num

print("Smallest number =", smallest)