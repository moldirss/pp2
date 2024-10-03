#5. Generator that counts down from n to 0
def countdown(n):
    # Loop from n down to 0
    while n >= 0:
        yield n  # Yield the current value of n
        n -= 1  # Decrement n by 1

# Example usage
n = 10
for number in countdown(n):
    print(number)  # Prints numbers from n down to 0
