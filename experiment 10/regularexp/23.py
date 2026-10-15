import re

text = """
# This is a comment
print("Hello")
x = 10  # This is another comment
"""

result = re.findall(r'#.*', text)

print("Comments:")
for comment in result:
    print(comment)