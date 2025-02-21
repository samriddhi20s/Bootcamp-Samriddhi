#Operator Overloading: Overload comparison operators in a class.
#Implement __eq__, __lt__, etc., in a class to enable direct object comparisons.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Equality comparison (==)
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return NotImplemented

    # Less than comparison (<)
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return (self.width * self.height) < (other.width * other.height)
        return NotImplemented

    # Greater than comparison (>)
    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return (self.width * self.height) > (other.width * other.height)
        return NotImplemented

    # Less than or equal to (<=)
    def __le__(self, other):
        if isinstance(other, Rectangle):
            return (self.width * self.height) <= (other.width * other.height)
        return NotImplemented

    # Greater than or equal to (>=)
    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return (self.width * self.height) >= (other.width * other.height)
        return NotImplemented

    # String representation for easy printing
    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"

# Testing the class and comparison operators
rect1 = Rectangle(4, 5)
rect2 = Rectangle(6, 3)
rect3 = Rectangle(4, 5)

# Testing equality
print(rect1 == rect2)  # False
print(rect1 == rect3)  # True

# Testing less than and greater than comparisons
print(rect1 < rect2)  # True (20 < 18)
print(rect1 > rect2)  # False (20 > 18)

# Testing greater than or equal to and less than or equal to
print(rect1 <= rect2)  # True (20 <= 18)
print(rect1 >= rect2)  # False (20 >= 18)
