import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)
print("Array:\n", a)
print("Total sum:", np.sum(a))

print("Layer sum:")
print(np.sum(a, axis=(1, 2)))

print("Row sum:")
print(np.sum(a, axis=2))

print("Column sum:")
print(np.sum(a, axis=1))