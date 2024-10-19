from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Example usage:
numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(f"The product of all numbers: {result}")
