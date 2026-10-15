import re

text = "My Name is KUNDAN DHAVAN"
result = re.findall(r'[A-Z]', text)

print("Uppercase letters:", result)