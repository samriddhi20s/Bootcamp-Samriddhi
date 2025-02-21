#Class Method Implementation: Add a class method in the Book class for tracking the number of books created.
#Implement and test this method.
class Book:
    book_count = 0  # Class variable to keep track of the number of books

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Book.book_count += 1  # Increment the count when a new book is created

    def __str__(self):
        return f"'{self.title}' by {self.author}, ISBN: {self.isbn}"

    @staticmethod
    def validate_isbn(isbn):
        if len(isbn) == 13 and isbn.isdigit():
            return True
        return False

    @classmethod
    def get_book_count(cls):
        return cls.book_count  # Return the number of books created


# Creating instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")

# Testing the class method
print(f"Total books created: {Book.get_book_count()}")  # Should return 3
