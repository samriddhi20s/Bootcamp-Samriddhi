import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)  # Convert object attributes to JSON

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"
