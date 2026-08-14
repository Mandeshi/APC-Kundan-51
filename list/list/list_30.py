names = ["Shivratna", "Varad", "Anuj"]
ages = [45, 30, 55]

names.append("Pravin")
ages.append(28)

del names[1]
del ages[1]

search = input("Enter patient name to search: ")
if search in names:
    index = names.index(search)
    print("Patient found. Age =", ages[index])
else:
    print("Patient not found")

print("All patients:")
for i in range(len(names)):
    print(names[i], "-", ages[i])

print("Total patients =", len(names))