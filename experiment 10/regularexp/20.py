import re

text = "Files: photo.jpg notes.txt program.py data.csv"
result = re.findall(r'\.([A-Za-z0-9]+)\b', text)

print("Extensions:", result)