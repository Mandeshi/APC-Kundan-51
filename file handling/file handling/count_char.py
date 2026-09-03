f = open("student.txt", "r")

data = f.read()

print("Total characters:", len(data))

f.close()