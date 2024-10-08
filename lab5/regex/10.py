#Program to convert a given camel case string to snake case:
import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
    return snake_str.lstrip('_')

# Test cases
print(camel_to_snake("thisIsCamelCase"))  # this_is_camel_case
