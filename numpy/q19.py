import numpy as np

a = np.arange(1, 25).reshape(2, 3, 4)

print("First element:", a[0, 0, 0])
print("Last element:", a[1, 2, 3])
print("Element [0,1,2]:", a[0, 1, 2])
print("Element [1,2,3]:", a[1, 2, 3])