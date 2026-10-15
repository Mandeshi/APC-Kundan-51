import re

text = "My birthday is 27-12-2005 and today is 15-10-2026"
result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

print(result)