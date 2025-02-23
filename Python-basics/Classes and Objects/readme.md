Classes and Objects in Python

   This document covers key concepts of object-oriented programming in 
   Python. It starts with basic class creation and builds up to modeling a 
   complete company structure.

Basic Class Creation

  Defines an Employee class with attributes like:

  name

  id

  position

Adding Methods to Classes

  Enhancing the Employee class by adding methods to update and display 
  information:

  update_position to change an employee's role

  display_info to print employee details

Class Inheritance

  Defines a Manager class that inherits from Employee and includes:

   A subordinates attribute

   A method to manage subordinates

Composition: The Department Class

  A Department class is introduced to associate multiple employees:

  Employees are managed using a list or dictionary

Using Data Structures in Classes

  Manages employees efficiently using structured data

  Implements salary calculation and employee management

Special Methods in Classes

 Implements __str__ and __repr__ for better representation of objects

Aggregation: The Project Class

 A Project class is introduced to associate multiple employees and a 
 department.

Property Decorators

  Uses property decorators in Employee to manage attribute access and 
  modification.

  Bringing It All Together: The Company Class

  Defines a Company class managing departments, projects, and employees

  Implements methods for department addition, employee assignments, and 
  summaries

Conclusion

This project explores:

  Basic class creation and methods

  Inheritance and composition

  Data management using lists and dictionaries

  Special methods and property decorators

  Aggregation and real-world modeling

This structured approach provides clarity while working with Python classes, making it easier to manage complex relationships in an organized way.
