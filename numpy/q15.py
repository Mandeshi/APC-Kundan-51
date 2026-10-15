import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Horizontal:")
print(np.hstack((a, b)))

print("Vertical:")
print(np.vstack((a, b)))