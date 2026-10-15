import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Row sum:", np.sum(a, axis=1))
print("Column sum:", np.sum(a, axis=0))