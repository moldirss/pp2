def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Example usage:
string = "Hello World!"
upper, lower = count_case(string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
