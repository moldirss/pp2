#Program to split a string at uppercase letters:
import re

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

# Test cases
print(split_at_uppercase("HelloWorldPython")) # ['Hello', 'World', 'Python']
