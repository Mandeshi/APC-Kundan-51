f = open("student.txt", "r")

data = f.read()

alphabet = 0
digit = 0
space = 0
special = 0

for ch in data:
    if ch.isalpha():
        alphabet += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
    else:
        special += 1

print("Alphabets:", alphabet)
print("Digits:", digit)
print("Spaces:", space)
print("Special characters:", special)

f.close()