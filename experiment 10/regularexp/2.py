import re

text = "Apple is an amazing and attractive, alive fruit"
result = re.findall(r'\b[Aa]\w*', text)

print(result)