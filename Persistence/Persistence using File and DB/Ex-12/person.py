import pickle
import dill  # Handles cyclic references better

class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None 

    def __repr__(self):
        return f"Person(name={self.name}, pet={self.pet.name if self.pet else None})"

class Pet:
    def __init__(self, name):
        self.name = name
        self.owner = None 

    def __repr__(self):
        return f"Pet(name={self.name}, owner={self.owner.name if self.owner else None})"

def save_objects(obj, filename="cyclic_data.pkl"):
    """Serialize object with cyclic references."""
    with open(filename, "wb") as file:
        dill.dump(obj, file)
    print(f"Data saved to {filename}")

def load_objects(filename="cyclic_data.pkl"):
    """Deserialize object with cyclic references."""
    try:
        with open(filename, "rb") as file:
            obj = dill.load(file)
        print(f"Data loaded from {filename}")
        return obj
    except FileNotFoundError:
        print("No saved data found.")
        return None
