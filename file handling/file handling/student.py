import os
name = input("Enter name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
sem = input("Enter semester: ")

f = open("student.txt", "w")

f.write("Name: " + name + "\n")
f.write("Roll No: " + roll + "\n")
f.write("Branch: " + branch + "\n")
f.write("semester:"+ sem+"\n")
f.close()
print("Data written successfully")

print(os.getcwd())