import re

text = "#Govt #Maharashtra #Dream #Kundan2005"
result = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text)

print(result)