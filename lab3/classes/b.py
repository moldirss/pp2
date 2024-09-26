class Shape:
    # Default area method returns 0
    def area(self):
        return 0

class Square(Shape):
    # Initialize square with a side length
    def __init__(self, length):
        self.length = length

    # Area of the square (side^2)
    def area(self):
        return self.length ** 2

# Example usage:
square = Square(4)
print("Area of the square:", square.area())  # Output: 16
