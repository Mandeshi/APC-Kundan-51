f = open("student.txt", "a")

info = input("Enter additional information: ")

f.write("\n" + info)

f.close()

print("Data added successfully")