import numpy as np

marks = np.array([45, 67, 89, 32, 76, 90, 55, 82, 95, 61,
                  70, 48, 88, 91, 53, 79, 66, 84, 40, 72])

average = np.mean(marks)

print("Average:", average)
print("Above average:", marks[marks > average])