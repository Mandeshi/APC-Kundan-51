import re

number = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")