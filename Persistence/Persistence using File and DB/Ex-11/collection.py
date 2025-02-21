import pickle

class MyCollection:
    def __init__(self):
        self.items = []  # List to store objects

    def add(self, item):
        """Add an object to the collection."""
        self.items.append(item)

    def save_to_file(self, filename="collection.pkl"):
        """Serialize the collection and save it to a file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        print(f"Collection saved to {filename}")

    @classmethod
    def load_from_file(cls, filename="collection.pkl"):
        """Deserialize the collection from a file."""
        try:
            with open(filename, "rb") as file:
                collection = pickle.load(file)
            print(f"Collection loaded from {filename}")
            return collection
        except FileNotFoundError:
            print("No saved collection found. Creating a new collection.")
            return cls()

    def __repr__(self):
        return f"MyCollection(items={self.items})"
