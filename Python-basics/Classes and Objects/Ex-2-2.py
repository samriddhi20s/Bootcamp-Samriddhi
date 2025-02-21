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
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")

# Example usage
emp1 = Employee("Sam", 101, "Software Engineer")
emp1.display_info()
