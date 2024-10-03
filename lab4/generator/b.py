#2. Generator to print even numbers between 0 and n in comma-separated form
def even_number_generator(n):
    # Iterate from 0 to n
    for i in range(n + 1):
        # Check if the number is even
        if i % 2 == 0:
            yield i

# Input from the user
n = int(input("Enter the value of n: "))

# Generate and print even numbers as a comma-separated string
print(", ".join(str(i) for i in even_number_generator(n)))
