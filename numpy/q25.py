import numpy as np

a = np.random.randint(1, 101, (3, 4, 5))

b = a.flatten()

average = np.mean(b)

print("Array:")
print(a)

print("Greater than 50:")
print(b[b > 50])

print("Even numbers:")
print(b[b % 2 == 0])

print("Less than average:")
print(b[b < average])