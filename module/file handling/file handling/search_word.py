word = input("Enter word to search: ")

f = open("student.txt", "r")

lines = f.readlines()
count = 0

for i in range(len(lines)):
    if word in lines[i]:
        print("Found on line:", i + 1)
        count += lines[i].count(word)

print("Total occurrences:", count)

f.close()