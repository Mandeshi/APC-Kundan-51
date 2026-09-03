f = open("student.txt", "r")
data = f.read()
f.close()

f = open("uppercase.txt", "w")

f.write(data.upper())

f.close()

print("Uppercase file created")