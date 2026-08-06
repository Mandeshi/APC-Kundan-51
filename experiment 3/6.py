numbers = [12, 45, 8, 67, 23]

largest = smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest =", largest)
print("Smallest =", smallest)