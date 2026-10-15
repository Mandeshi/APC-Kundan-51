import numpy as np

a = np.array([10, 60, 30, 80, 45, 90, 20, 70, 40, 55])

a[a > 50] = 0

print(a)