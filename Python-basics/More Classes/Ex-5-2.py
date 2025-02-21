#Static Method Usage: Add a static method to the Book class that validates ISBN numbers.
#Implement and demonstrate its usage without creating an instance of Book.
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author}, ISBN: {self.isbn}"

    @staticmethod
    def validate_isbn(isbn):
        if len(isbn) == 13 and isbn.isdigit():
            return True
        return False

# Demonstrating the static method usage without creating an instance
isbn1 = "9781234567890"
isbn2 = "12345abc67890"

print(f"Is ISBN {isbn1} valid? {Book.validate_isbn(isbn1)}")  # Should return True
print(f"Is ISBN {isbn2} valid? {Book.validate_isbn(isbn2)}")  # Should return False
