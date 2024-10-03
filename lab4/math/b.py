#2. Calculate the area of a trapezoid
# Function to calculate the area of a trapezoid
def area_of_trapezoid(height, base1, base2):
    return (base1 + base2) / 2 * height

# Input values
height = 5
base1 = 5
base2 = 6

# Calculation
area = area_of_trapezoid(height, base1, base2)

# Output
print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {area}")
