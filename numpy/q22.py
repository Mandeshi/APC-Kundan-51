import numpy as np

a = np.random.randint(1, 101, (3, 4, 5))

print("Array:")
print(a)

print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))