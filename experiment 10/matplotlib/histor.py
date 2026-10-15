
import matplotlib.pyplot as plt

marks = [70, 85, 90, 65, 80, 75, 85, 60, 95, 70]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
