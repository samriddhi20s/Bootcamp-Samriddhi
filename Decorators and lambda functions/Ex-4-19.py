#functools.total_ordering for Classes: Use total_ordering to simplify class comparison.
#Create a class representing a simple 2D point (with x and y coordinates) and use functools.total_ordering to compare points based on their distance from the origin.
import functools
import math

@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define __eq__ for equality comparison (points are equal if they have the same distance)
    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    # Define __lt__ for less-than comparison (for sorting based on distance)
    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    # Method to calculate the distance from the origin
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    # String representation for easy display
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
point1 = Point(3, 4)
point2 = Point(1, 1)
point3 = Point(6, 8)

# Comparison examples
print(f"point1 < point2: {point1 < point2}")  # False, because point1 is farther from the origin
print(f"point2 == point3: {point2 == point3}")  # False, because point2 is closer to the origin than point3
print(f"Sorted points: {sorted([point1, point2, point3])}")  # Will sort based on distance from origin
