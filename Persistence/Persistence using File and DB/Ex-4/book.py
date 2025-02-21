import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)  # Serialize attributes to JSON

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)  # Deserialize JSON string to a dictionary
        return cls(**data)  # Create a Book instance using unpacked dictionary values

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"
