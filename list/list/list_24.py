numbers = [10, 20, 30, 40, 50]

left_rotate = numbers[1:] + numbers[0:1]
right_rotate = numbers[-1:] + numbers[:-1]

print("Left rotated:", left_rotate)
print("Right rotated:", right_rotate)