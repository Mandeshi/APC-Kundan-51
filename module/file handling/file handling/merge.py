f1 = open("student.txt", "r")
f2 = open("students.txt", "r")

data1 = f1.read()
data2 = f2.read()

f1.close()
f2.close()

f3 = open("file3.txt", "w")

f3.write(data1)
f3.write("\n")
f3.write(data2)

f3.close()

print("Files merged")