f1 = open("student.txt", "r")
f2 = open("students.txt", "r")

lines1 = f1.readlines()
lines2 = f2.readlines()

f1.close()
f2.close()

if lines1 == lines2:
    print("Files are identical")

else:

    print("Files are different")

    for i in range(min(len(lines1), len(lines2))):

        if lines1[i] != lines2[i]:
            print("First difference at line:", i + 1)
            break