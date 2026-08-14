t = (10, 20, 30, 40)
temp_list = list(t)

temp_list[1] = 99

t = tuple(temp_list)
print("Modified tuple:", t)