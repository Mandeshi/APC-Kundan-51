import re

text = "Kundan likes to play cricket and driving cars "
result = re.findall(r'\b\w+s\b', text, re.IGNORECASE)

print(result)