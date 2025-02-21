from person import Person, Pet, save_objects, load_objects

# Step 1: Create Cyclic References
person = Person("Alice")
pet = Pet("Buddy")

# Step 2: Link the Objects
person.pet = pet
pet.owner = person

print("Before Serialization:", person, pet)

# Step 3: Save to File
save_objects(person)

# Step 4: Load from File
loaded_person = load_objects()
print("\nAfter Deserialization:", loaded_person, loaded_person.pet)
