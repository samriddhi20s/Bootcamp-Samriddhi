class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
    
    def update_name(self, new_name):
        self.name = new_name
    
    def update_position(self, new_position):
        self.position = new_position

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
