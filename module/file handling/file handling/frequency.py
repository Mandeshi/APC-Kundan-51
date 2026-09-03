f = open("student.txt", "r")

words = f.read().split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

f.close()