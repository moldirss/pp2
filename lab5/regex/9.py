#Program to insert spaces between words starting with capital letters:
import re

def insert_spaces(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

# Test cases
print(insert_spaces("HelloWorldPython"))  # Hello World Python
