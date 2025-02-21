from car import Car

# Create a Car object
car1 = Car("Tesla", "Model S", 2023)

# Convert to YAML
yaml_representation = car1.to_yaml()
print("Serialized YAML:\n", yaml_representation)
