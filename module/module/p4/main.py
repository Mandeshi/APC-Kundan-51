import string

text = input("Enter a string: ")

print("Vowels:", string.count_vowels(text))
print("Reverse:", string.reverse_string(text))
print("Palindrome:", string.palindrome(text))
print("Words:", string.count_words(text))
print("Without spaces:", string.remove_spaces(text))
