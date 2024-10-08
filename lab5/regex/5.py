#Program to match a string that has an 'a' followed by anything, ending in 'b':
import re

def match_a_anything_b(string):
    pattern = r'a.*b$'
    return re.fullmatch(pattern, string)

# Test cases
print(match_a_anything_b("acb"))   # Match
print(match_a_anything_b("a123b")) # Match
print(match_a_anything_b("a123"))  # No match
