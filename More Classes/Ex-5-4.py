#Using Dunder Methods: Implement the __str__ and __repr__ methods for the Book class.
#Create instances and print them to see the effect of these methods.
class Book:
    book_count = 0  # Class variable to keep track of the number of books

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.book_count += 1  # Increment the count when a new book is created

    def __str__(self):
        # The __str__ method is used for human-readable output
        return f"'{self.title}' by {self.author}, ISBN: {self.isbn}"

    def __repr__(self):
        # The __repr__ method should return a more detailed and unambiguous string representation of the object
        return f"Book(title={self.title!r}, author={self.author!r}, isbn={self.isbn!r})"

    @staticmethod
    def validate_isbn(isbn):
        # Basic validation: check if the ISBN is 13 digits long
        if len(isbn) == 13 and isbn.isdigit():
            return True
        return False

    @classmethod
    def get_book_count(cls):
        return cls.book_count  # Return the number of books created


# Creating instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book2 = Book("1984", "George Orwell", "9780451524935")

# Printing the instances to see the effect of __str__ and __repr__
print(book1)  # Uses __str__ method
print(book2)  # Uses __str__ method

# Printing the instances in a more developer-friendly way (shows __repr__ method)
print(repr(book1))  # Uses __repr__ method
print(repr(book2))  # Uses __repr__ method
