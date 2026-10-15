import re

text = "My roll number is 51 and age is 21"
result = re.findall(r'\d', text)

print("Digits:", result)