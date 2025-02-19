#Demonstrate inheritance by adding a method to manage subordinates.
class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def display_info(self):
        print("-----------------------------")
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print("-----------------------------")
    
    def update_name(self, new_name):
        self.name = new_name
    
    def update_position(self, new_position):
        self.position = new_position

class Manager(Employee):
    def __init__(self, name, emp_id, position, subordinates=None):
        super().__init__(name, emp_id, position)
        self.subordinates = subordinates if subordinates else []
    
    def add_subordinate(self, emp_id):
        self.subordinates.append(emp_id)
    
    def remove_subordinate(self, emp_id):
        if emp_id in self.subordinates:
            self.subordinates.remove(emp_id)
    
    def display_info(self):
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

# Managing subordinates
mgr1.add_subordinate(102)
mgr1.display_info()

mgr1.remove_subordinate(103)
mgr1.display_info()
