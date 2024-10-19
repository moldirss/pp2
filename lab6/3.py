def is_palindrome(s):
    return s == s[::-1]

# Example usage:
string = "madam"
result = is_palindrome(string)
print(f"Is '{string}' a palindrome? {result}")
