import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Example usage:
radius = 5
print(f"Volume of sphere with radius {radius} is {sphere_volume(radius)}.")
