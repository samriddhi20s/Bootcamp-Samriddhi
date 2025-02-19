#Dynamic Class Creation: Dynamically create a class at runtime.
#Use type to create a new class with dynamically specified properties.
# Dynamically creating a class with `type`
def create_class(class_name, properties):
    # Dynamically create a class with specified properties
    return type(class_name, (object,), properties)

# Define properties and methods for the class
properties = {
    'greet': lambda self: f"Hello, my name is {self.name}",
    'name': 'John Doe',
    'age': 30
}

# Create a new class called "Person"
Person = create_class("Person", properties)

# Create an instance of the dynamically created class
person_instance = Person()

# Accessing the dynamically added properties
print(person_instance.name)  # Should print 'John Doe'
print(person_instance.age)   # Should print 30
print(person_instance.greet())  # Should print "Hello, my name is John Doe"
