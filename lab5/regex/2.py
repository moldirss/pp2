#Program to match a string that has an 'a' followed by two to three 'b':
import re

def match_ab2to3(string):
    pattern = r'ab{2,3}'
    return re.fullmatch(pattern, string)

# Test cases
print(match_ab2to3("abb"))   # Match
print(match_ab2to3("abbb"))  # Match
print(match_ab2to3("abbbb")) # No match
