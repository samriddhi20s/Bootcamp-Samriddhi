#Class Decorators: Write a class decorator that adds a new method or attribute to the class.
#Apply it to an existing class and demonstrate the added functionality.
# Class decorator to add a new method
def add_description_method(cls):
    # Adding a new method to the class
    def describe(self):
        return f"This is a {self.__class__.__name__} object with name {self.name} and age {self.age}."

    # Add the new method to the class
    setattr(cls, 'describe', describe)
    
    # Return the modified class
    return cls

# Original class
@add_description_method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the Person class
person = Person("Alice", 28)

# Use the newly added 'describe' method
print(person.describe())  # Should print a description of the object
