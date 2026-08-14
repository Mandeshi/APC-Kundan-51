numbers = [21, 45, 12, 65, 50]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest =", largest)
print("Smallest =", smallest)