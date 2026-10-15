import re

text = "Revenue Department Government of Maharashtra"
result = re.findall(r'[aeiouAEIOU]', text)

print("Vowel count:", len(result))