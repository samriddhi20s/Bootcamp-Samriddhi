import pickle
import os

FILE_PATH = "data/person.pkl"

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

def serialize_object(obj, file_path=FILE_PATH):
    """Serialize and save a Python object to a file."""
    with open(file_path, "wb") as file:
        pickle.dump(obj, file)
    print(f"Object serialized successfully to {file_path}")

def deserialize_object(file_path=FILE_PATH):
    """Deserialize a Python object from a file."""
    if not os.path.exists(file_path):
        print("No file found to deserialize.")
        return None
    with open(file_path, "rb") as file:
        obj = pickle.load(file)
    print("Object deserialized successfully.")
    return obj
