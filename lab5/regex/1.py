#Program to match a string that has an 'a' followed by zero or more 'b''s:
import re

def match_ab(string):
    pattern = r'ab*'
    return re.fullmatch(pattern, string)

# Test cases
print(match_ab("a"))      # Match
print(match_ab("ab"))     # Match
print(match_ab("abb"))    # Match
print(match_ab("b"))      # No match
