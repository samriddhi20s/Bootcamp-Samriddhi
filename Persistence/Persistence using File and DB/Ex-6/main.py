from car import Car

# Step 1: Create a Car object and serialize it to YAML
car1 = Car("Tesla", "Model S", 2023)
yaml_representation = car1.to_yaml()
print("Serialized YAML:\n", yaml_representation)

# Step 2: Deserialize YAML back into a Car object
deserialized_car = Car.from_yaml(yaml_representation)
print("\nDeserialized Car Object:", deserialized_car)
