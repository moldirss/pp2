#Program to find sequences of lowercase letters joined with an underscore:
import re

def find_lowercase_with_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

# Test cases
print(find_lowercase_with_underscore("abc_def_ghi")) # ['abc_def']
print(find_lowercase_with_underscore("Abc_def"))     # ['def']
