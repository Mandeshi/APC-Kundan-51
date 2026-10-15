import re

text = """
Research paper published in 2024.
DOI: 10.1234/abcd.5678
Email: author@gmail.com
URL: https://example.com/paper
"""

doi = re.findall(r'\b10\.\d{4,9}/[^\s,]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    text
)
urls = re.findall(r'https?://[^\s]+', text)

print("DOI:", doi)
print("Years:", years)
print("Emails:", emails)
print("URLs:", urls)