class Rectangle(Shape):
    # Initialize with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate rectangle area (length * width)
    def area(self):
        return self.length * self.width

# Example usage:
rectangle = Rectangle(5, 3)
print("Area of the rectangle:", rectangle.area())  # Output: 15
