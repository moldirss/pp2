#1. Convert degree to radian
import math

# Function to convert degrees to radians
def degree_to_radian(degree):
    return degree * (math.pi / 180)
# Input
degree = 15

# Conversion
radian = degree_to_radian(degree)

# Output
print(f"Input degree:{degree}")
print(f"Output radian:{radian:.6f}")