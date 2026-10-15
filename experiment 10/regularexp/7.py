import re

text = "Profile Clerk Officer Magistrate District"
result = re.findall(r'\b[A-Za-z]{5}\b', text)

print(result)