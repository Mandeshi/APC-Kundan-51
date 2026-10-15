import re

text = "My PIN is 415110 and another PIN is 415508"
result = re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', text)

print("PIN codes:", result)