import re

number = input("Enter vehicle number: ").upper()

pattern = r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}'

if re.fullmatch(pattern, number):
    print("Valid vehicle number format")
else:
    print("Invalid vehicle number format")