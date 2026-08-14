numbers = [10, 20, 10, 30, 20, 10]
freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1

for num in freq:
    print(num, "=", freq[num])