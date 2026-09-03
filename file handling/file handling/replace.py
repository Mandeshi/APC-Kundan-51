old = input("Enter word to replace: ")
new = input("Enter new word: ")

f = open("student.txt", "r")
data = f.read()
f.close()

data = data.replace(old, new)

f = open("student.txt", "w")
f.write(data)
f.close()

print("Word replaced successfully")