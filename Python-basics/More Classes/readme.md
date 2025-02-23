# More Classes in Python

This guide covers advanced class features and techniques in Python, exploring various Object-Oriented Programming (OOP) concepts.

---

## 1. Basic Class Creation
- Define a `Book` class with attributes like `title` and `author`.
- Create instances of the `Book` class.

## 2. Static Method Usage
- Add a static method to `Book` that validates ISBN numbers.
- Demonstrate usage without creating an instance.

## 3. Class Method Implementation
- Implement a class method to track the number of `Book` instances created.
- Test and verify functionality.

## 4. Using Dunder Methods
- Implement `__str__` and `__repr__` in `Book` to enhance object representation.

## 5. Implementing an Abstract Base Class (ABC)
- Create an abstract base class `Shape` with an abstract method `area`.
- Implement subclasses like `Circle` and `Rectangle`.

## 6. Contracts with @property
- Create a `Temperature` class with controlled attribute access using `@property`.
- Enforce valid temperature ranges (-273.15 to 5000°C).

## 7. Using Dunder Methods for Arithmetic
- Implement `__add__`, `__sub__`, etc., in a `Vector` class.
- Demonstrate vector operations.

## 8. Abstract Properties
- Implement abstract properties in an abstract base class `Animal`.
- Define concrete implementations in subclasses.

## 9. Dynamic Class Creation
- Use `type` to create a new class dynamically at runtime.

## 10. Class Decorators
- Write a class decorator to add methods or attributes dynamically.
- Apply and test on an existing class.

## 11. Static Variables and Methods
- Explore the use of static variables and methods.
- Track the number of instances of a class.

## 12. Enforcing Interface Implementation
- Define an interface `Streamable` using ABC.
- Implement `stream()` in subclasses like `VideoStream` and `AudioStream`.

## 13. Class Mixins
- Use mixins to add common functionalities.
- Example: `JsonMixin` for JSON serialization/deserialization.

## 14. Operator Overloading
- Implement comparison operators (`__eq__`, `__lt__`, etc.).
- Enable direct object comparisons.

## 15. Immutable Class
- Create an immutable `Point` class.
- Prevent attribute modifications after instantiation.

## 16. Custom Context Managers
- Implement a class with `__enter__` and `__exit__`.
- Example: `FileOpen` class for safe file handling.

---

## Conclusion
This guide provides a structured exploration of advanced Python class concepts, reinforcing OOP principles and best practices.


