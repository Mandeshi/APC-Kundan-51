import re

text = "My     Name    Kundan   Dhavan "
result = re.sub(r' +', ' ', text)

print(result)