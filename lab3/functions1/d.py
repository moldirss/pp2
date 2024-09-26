def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
numbers = [2, 3, 4, 5, 6, 7, 11]
print(filter_prime(numbers))  # Output: [2, 3, 5, 7, 11]
