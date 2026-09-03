f = open("student.txt", "r")

data = f.read().lower()

vowels = 0
consonants = 0

for ch in data:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

f.close()