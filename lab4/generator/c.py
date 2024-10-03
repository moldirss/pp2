#3. Function with a generator for numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    # Iterate from 0 to n
    for i in range(n + 1):
        # Check if the number is divisible by both 3 and 4
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
n = 50
for number in divisible_by_3_and_4(n):
    print(number)  # Prints numbers divisible by both 3 and 4
