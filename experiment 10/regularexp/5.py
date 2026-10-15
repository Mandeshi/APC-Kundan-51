import re

text = "Hello World\nPython\tProgramming"
result = re.findall(r'[ \t\n]', text)

print("Whitespace characters:", result)
print("Total:", len(result))