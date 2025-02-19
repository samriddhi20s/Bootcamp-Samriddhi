#In the Department class, manage employees using a list or dictionary.
class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def display_info(self):
        print(f"Employee ID: {self.emp_id}\nName: {self.name}\nPosition: {self.position}\n")
    
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
        print(f"Subordinates: {', '.join(map(str, self.subordinates)) if self.subordinates else 'None'}\n")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}
    
    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee
    
    def remove_employee(self, emp_id):
        self.employees.pop(emp_id, None)
    
    def search_employee_by_name(self, name):
        return [emp for emp in self.employees.values() if emp.name.lower() == name.lower()]
    
    def list_employees_by_position(self, position):
        return [emp for emp in self.employees.values() if emp.position.lower() == position.lower()]
    
    def count_employees(self):
        return len(self.employees)
    
    def display_department_info(self):
        print(f"Department: {self.name}\nEmployees:")
        for emp in self.employees.values():
            emp.display_info()
        print(f"Total Employees: {self.count_employees()}\n")

# Example usage
emp1 = Employee("John Doe", 101, "Software Engineer")
emp2 = Employee("Jane Smith", 102, "Project Manager")
emp3 = Employee("Alice Johnson", 103, "Data Analyst")
emp1.update_name("Johnathan Doe")
emp1.update_position("Senior Software Engineer")

mgr1 = Manager("Robert Brown", 200, "Engineering Manager", [101, 103])
mgr1.add_subordinate(102)
mgr1.remove_subordinate(103)

department = Department("Engineering")
department.add_employee(emp1)
department.add_employee(emp2)
department.add_employee(emp3)
department.add_employee(mgr1)
department.display_department_info()

department.remove_employee(102)
department.display_department_info()

search_results = department.search_employee_by_name("Johnathan Doe")
for emp in search_results:
    emp.display_info()

software_engineers = department.list_employees_by_position("Software Engineer")
for emp in software_engineers:
    emp.display_info()

print(f"Total number of employees: {department.count_employees()}")
