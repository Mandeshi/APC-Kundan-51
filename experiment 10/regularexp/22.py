import re

text = """
Invoice No: INV-1234
Date: 15-10-2026
Amount: Rs. 2500.50
"""

invoice = re.findall(r'INV-\d+', text)
date = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amount = re.findall(r'Rs\.?\s*[\d,]+(?:\.\d{2})?', text)

print("Invoice number:", invoice)
print("Date:", date)
print("Amount:", amount)