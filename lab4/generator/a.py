#1.Generator that generates the squares of numbers up to some number N:
def square_generator(N):
    # Iterate from 0 to N
    for i in range(N + 1):
        # Yield the square of i
        yield i * i

# Example usage
N = 5
for square in square_generator(N):
    print(square)  # Prints the squares of numbers from 0 to N