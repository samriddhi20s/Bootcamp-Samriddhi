#Basic Class Creation: Create a simple Book class with attributes like title and author.
#Implement the class and create instances of it.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Create instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")

# Print the instances
print(book1)
print(book2)
