scores = []
for i in range(10):
    s = int(input("Enter score: "))
    scores.append(s)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for s in scores:
    if s >= 100:
        centuries = centuries + 1
    elif s >= 50:
        half_centuries = half_centuries + 1

print("Highest score =", highest)
print("Lowest score =", lowest)
print("Total runs =", total)
print("Average runs =", average)
print("Centuries =", centuries)
print("Half-centuries =", half_centuries)