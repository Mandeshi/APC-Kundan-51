f = open("attendance.txt", "r")

for line in f:

    name, present, total = line.strip().split(",")

    percentage = int(present) / int(total) * 100

    print(name, ":", percentage, "%")

    if percentage < 75:
        print(name, "has attendance below 75%")

f.close()