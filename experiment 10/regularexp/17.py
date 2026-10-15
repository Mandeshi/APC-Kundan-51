import re

text = "Kundan is a good boy and he is very kind and helpful"
result = re.findall(
    r'\b(\w+)\s+\1\b', text, re.IGNORECASE
)

print("Repeated words:", result)