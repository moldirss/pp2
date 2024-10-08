#Program to replace all occurrences of space, comma, or dot with a colon:
import re

def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

# Test cases
print(replace_with_colon("Hello, world. How are you?")) # Hello:world:How:are:you?
