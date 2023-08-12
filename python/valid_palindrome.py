# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
import re

def valid_palindrome(str):
    new_str = re.compile('[^a-zA-Z]').sub('', str).lower()
    reversed_string = new_str[::-1]
    return new_str == reversed_string

print(valid_palindrome(' '))


