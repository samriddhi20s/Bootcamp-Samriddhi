class Employee:
    """
    A class representing an Employee.
    Attributes:
        name (str): The name of the employee.
        emp_id (int): The unique ID of the employee.
        position (str): The job position of the employee.
    """
    def __init__(self, name, emp_id, position):
        """
        Initializes an Employee object with name, emp_id, and position.
        """
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def display_info(self):
        """
        Displays the employee's information.
        """
        print("-----------------------------")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print("-----------------------------")
    
    def update_name(self, new_name):
        """
        Updates the employee's name.
        """
        self.name = new_name
    
    def update_position(self, new_position):
        """
        Updates the employee's position.
        """
        self.position = new_position

class Manager(Employee):
    """
    A class representing a Manager, inheriting from Employee.
    Attributes:
        subordinates (list): A list of employee IDs managed by the manager.
    """
    def __init__(self, name, emp_id, position, subordinates=None):
        """
        Initializes a Manager object with name, emp_id, position, and subordinates.
        """
        super().__init__(name, emp_id, position)
        self.subordinates = subordinates if subordinates else []
    
    def add_subordinate(self, emp_id):
        """
        Adds an employee ID to the manager's list of subordinates.
        """
        self.subordinates.append(emp_id)
    
    def display_info(self):
        """
        Displays the manager's information along with subordinates.
        """
        super().display_info()
        print(f"Subordinates: {', '.join(map(str, self.subordinates)) if self.subordinates else 'None'}")
        print("-----------------------------")

# Example usage
emp1 = Employee("John Doe", 101, "Software Engineer")
emp2 = Employee("Jane Smith", 102, "Project Manager")
emp3 = Employee("Alice Johnson", 103, "Data Analyst")

emp1.display_info()
emp2.display_info()
emp3.display_info()

# Updating employee information
emp1.update_name("Johnathan Doe")
emp1.update_position("Senior Software Engineer")
emp1.display_info()

# Creating and displaying a manager
mgr1 = Manager("Robert Brown", 200, "Engineering Manager", [101, 103])
mgr1.display_info()

# Adding a subordinate
mgr1.add_subordinate(102)
mgr1.display_info()
