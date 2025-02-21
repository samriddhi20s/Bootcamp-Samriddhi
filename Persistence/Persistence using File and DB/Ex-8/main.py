from user import User

# Step 1: Create a User object
user = User("John Doe", "john@example.com", "securepass123", "123-45-6789")

# Step 2: Serialize the User object (excluding sensitive data)
json_representation = user.to_json()
print("Serialized JSON (Sensitive Data Excluded):\n", json_representation)

# Step 3: Deserialize JSON back into a User object (adding sensitive data separately)
deserialized_user = User.from_json(json_representation, "securepass123", "123-45-6789")
print("\nDeserialized User Object:", deserialized_user)
