#3. Calculate the area of a regular polygon
import math

# Function to calculate the area of a regular polygon
def area_of_polygon(num_sides, side_length):
    return (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

# Input values
num_sides = 4
side_length = 25

# Calculation
area = area_of_polygon(num_sides, side_length)

# Output
print(f"Input number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.1f}")
