import numpy as np

a = np.random.randint(1, 101, (2, 3, 4))

print("Original:")
print(a)

a[a > 50] = 0

print("After replacement:")
print(a)