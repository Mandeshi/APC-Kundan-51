marks = []
for i in range(20):
    m = int(input("Enter marks: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_average = 0
below_average = 0

for m in marks:
    if m > average:
        above_average = above_average + 1
    elif m < average:
        below_average = below_average + 1

print("Highest marks =", highest)
print("Lowest marks =", lowest)
print("Average marks =", average)
print("Students above average =", above_average)
print("Students below average =", below_average)