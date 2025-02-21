#Immutable Class: Create an immutable class where instances cannot be modified after creation.
#Example: A Point class representing a point in 2D space.
# Immutable Point class using dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

# Testing the immutable class
point = Point(3.0, 4.0)

print(f"Point: ({point.x}, {point.y})")

# Attempting to modify the attributes will raise an error
try:
    point.x = 5.0  # This will raise an error
except AttributeError as e:
    print(f"Error: {e}")

