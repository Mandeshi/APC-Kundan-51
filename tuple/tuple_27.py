tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)

merged = tuple1 + tuple2
result = []

for item in merged:
    if item not in result:
        result.append(item)

print("Merged tuple without duplicates:", tuple(result))