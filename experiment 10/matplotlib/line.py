
import matplotlib.pyplot as plt

students = ["Kundan", "Tanuja", "Sakshi", "Omkar", "Sanika"]
marks = [70, 85, 90, 65, 80]

plt.plot(students, marks, marker="o")

plt.title("Student Marks - Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)

plt.show()
