import re

text = """
Name: Kundan, Roll: 101, Marks: 98
Name: Tanuja, Roll: 102, Marks: 95
"""

pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'

result = re.findall(pattern, text)

for name, roll, marks in result:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)
    print()