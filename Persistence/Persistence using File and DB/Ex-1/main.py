from person import Person
from serializer import serialize_object, deserialize_object

# Create a Person object
person1 = Person("Alice", ["Harvard", "MIT"])
person2 = Person("Bob", ["Stanford"])
person1.add_colleague(person2)

# Serialize to file
serialize_object(person1)

# Deserialize from file
loaded_person = deserialize_object()
print("Deserialized Object:", loaded_person)

