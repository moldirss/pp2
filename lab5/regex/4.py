#Program to find sequences of one upper case letter followed by lower case letters:
import re

def find_upper_followed_by_lower(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

# Test cases
print(find_upper_followed_by_lower("Hello World"))  # ['Hello', 'World']
print(find_upper_followed_by_lower("Python"))       # ['Python']
