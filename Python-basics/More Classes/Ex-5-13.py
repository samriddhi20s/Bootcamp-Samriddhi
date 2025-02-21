#Class Mixins: Implement and use mixins to add common functionalities to classes.
#Example: A JsonMixin that adds JSON serialization/deserialization to classes.
import json

# Mixin class for JSON functionality
class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)  # Convert the object's attributes to a dictionary

    @classmethod
    def from_json(cls, json_string):
        """Deserialize a JSON string to an object."""
        data = json.loads(json_string)
        return cls(**data)  # Create a new instance of the class using the deserialized data

class Person(JsonMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Product(JsonMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Create instances of Person and Product
person = Person("Alice", 30)
product = Product("Laptop", 999.99)

# Convert objects to JSON
person_json = person.to_json()
product_json = product.to_json()

print("Person as JSON:", person_json)
print("Product as JSON:", product_json)

# Deserialize JSON back to objects
person_from_json = Person.from_json(person_json)
product_from_json = Product.from_json(product_json)

print(f"Person from JSON: {person_from_json.name}, {person_from_json.age}")
print(f"Product from JSON: {product_from_json.name}, {product_from_json.price}")
