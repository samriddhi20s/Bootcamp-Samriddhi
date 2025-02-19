#Using Dunder Methods for Arithmetic: Implement __add__, __sub__, and other arithmetic dunder methods in a Vector class.
#Test the class with vector addition, subtraction, etc.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Addition
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Subtraction
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    # Multiplication (scalar)
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    # Division (scalar)
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented

    # Equality comparison
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Representation for debugging
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

# Testing the Vector class
v1 = Vector(3, 4)
v2 = Vector(1, 2)

# Vector addition
v3 = v1 + v2
print(f"v1 + v2 = {v3}")

# Vector subtraction
v4 = v1 - v2
print(f"v1 - v2 = {v4}")

# Scalar multiplication
v5 = v1 * 2
print(f"v1 * 2 = {v5}")

# Scalar division
v6 = v1 / 2
print(f"v1 / 2 = {v6}")

# Equality comparison
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
