from book import Book

# Step 1: Create a Book object and serialize it to JSON
book1 = Book("The Alchemist", "Paulo Coelho", 208)
json_representation = book1.to_json()
print("Serialized JSON:\n", json_representation)

# Step 2: Deserialize JSON back into a Book object
deserialized_book = Book.from_json(json_representation)
print("\nDeserialized Book Object:", deserialized_book)
