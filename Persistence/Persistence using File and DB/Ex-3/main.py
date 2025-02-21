from book import Book

# Create a Book object
book1 = Book("The Alchemist", "Paulo Coelho", 208)

# Convert to JSON
json_representation = book1.to_json()
print("Serialized JSON:\n", json_representation)
