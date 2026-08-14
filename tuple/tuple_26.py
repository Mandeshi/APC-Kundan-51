tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

common = []
for item in tuple1:
    if item in tuple2:
        common.append(item)

print("Common elements:", tuple(common))