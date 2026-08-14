numbers = [10, 20, 20, 30, 40, 40, 50]
result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)