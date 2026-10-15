import numpy as np

a = np.arange(1, 28).reshape(3, 3, 3)

b = a.flatten()

print("Flattened array:", b)

print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))