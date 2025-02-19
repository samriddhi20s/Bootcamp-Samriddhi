#Abstract Properties: Add abstract properties to an abstract base class and implement them in child classes.
#Example: abstract class Animal with an abstract property sound.
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        """An abstract property that must be implemented in the child classes."""
        pass

# Child Class Dog
class Dog(Animal):
    @property
    def sound(self):
        return "Bark"

# Child Class Cat
class Cat(Animal):
    @property
    def sound(self):
        return "Meow"

# Testing the classes
dog = Dog()
cat = Cat()

print(f"The dog says: {dog.sound}")  # Should print "Bark"
print(f"The cat says: {cat.sound}")  # Should print "Meow"
