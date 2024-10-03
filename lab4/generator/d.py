#4. Generator squares to yield square of numbers from a to b
def squares(a, b):
    # Iterate from a to b
    for i in range(a, b + 1):
        # Yield the square of i
        yield i * i

# Example usage
a = 3
b = 7
for x in squares(a, b):
    print(x)  # Prints squares of numbers from a to b