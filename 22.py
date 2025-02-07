class Shape:
    def area(self):
        """Returns the default area, which is 0 for a generic shape."""
        return 0

class Square(Shape):
    def __init__(self, length):
        """Initializes the square with a given side length."""
        self.length = length

    def area(self):
        """Calculates and returns the area of the square."""
        return self.length ** 2

# Example usage:
shape = Shape()
print("Shape area:", shape.area())  # Output: 0

square = Square(5)
print("Square area:", square.area())  # Output: 25
