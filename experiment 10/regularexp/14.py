import re

text = "Visit https://google.com and http://karad.city.in"
result = re.findall(r'https?://[^\s]+', text)

print(result)