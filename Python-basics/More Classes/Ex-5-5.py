#Implementing an Abstract Base Class (ABC): Create an abstract base class Shape with an abstract method area.
#Derive subclasses like Circle and Rectangle, implementing area in each.

from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of the circle: {circle.area()}")        #  area of the circle
print(f"Area of the rectangle: {rectangle.area()}")  #  area of the rectangle
