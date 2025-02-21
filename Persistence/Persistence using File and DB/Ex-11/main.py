from collection import MyCollection
from book import Book

# Step 1: Create a Collection and Add Books
my_collection = MyCollection()
my_collection.add(Book("1984", "George Orwell", 1949))
my_collection.add(Book("The Catcher in the Rye", "J.D. Salinger", 1951))

# Step 2: Save Collection to a File
my_collection.save_to_file()

# Step 3: Load Collection from File
loaded_collection = MyCollection.load_from_file()
print("\nRestored Collection:", loaded_collection)
