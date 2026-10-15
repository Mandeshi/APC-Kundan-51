import re

text = "Kundan2005@#"
result = re.sub(r'[^A-Za-z0-9 ]', '', text)

print(result)