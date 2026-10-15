import re

text = "Kundan is a good boy and he is very kind and helpful"
result = re.findall(r'\b\w+\b', text)

print("Word count:", len(result))