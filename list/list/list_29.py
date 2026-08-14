temperatures = []
for i in range(30):
    t = float(input("Enter temperature: "))
    temperatures.append(t)

hottest = max(temperatures)
coldest = min(temperatures)
average = sum(temperatures) / len(temperatures)

above_average = 0
below_average = 0

for t in temperatures:
    if t > average:
        above_average = above_average + 1
    elif t < average:
        below_average = below_average + 1

print("Hottest day =", hottest)
print("Coldest day =", coldest)
print("Average temperature =", average)
print("Days above average =", above_average)
print("Days below average =", below_average)