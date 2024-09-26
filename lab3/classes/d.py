import math

class Point:
    # Initialize with coordinates (default is 0, 0)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Display the coordinates
    def show(self):
        print(f"Point({self.x}, {self.y})")

    # Move the point to new coordinates
    def move(self, x, y):
        self.x = x
        self.y = y

    # Calculate distance to another point
    def dist(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

# Example usage:
p1 = Point(0, 0)
p2 = Point(3, 4)
print("Distance between points:", p1.dist(p2))  # Output: 5.0
