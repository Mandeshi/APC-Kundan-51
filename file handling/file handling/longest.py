f = open("student.txt", "r")

words = f.read().split()

longest = max(words, key=len)

print("Longest word:", longest)

f.close()