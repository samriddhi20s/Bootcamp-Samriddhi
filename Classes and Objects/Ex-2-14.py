#Special Methods for Classes: Implement Python's special methods in your classes (like __str__, __repr__).
class Employee:
    def __init__(self, name, emp_id, position, salary):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"
    
    def __repr__(self):
        return f"Employee('{self.name}', {self.emp_id}, '{self.position}', {self.salary})"
    
    def display_info(self):
        print(self)
    
    def update_name(self, new_name):
        self.name = new_name
    
    def update_position(self, new_position):
        self.position = new_position
    
    def update_salary(self, new_salary):
        self.salary = new_salary

class Manager(Employee):
    def __init__(self, name, emp_id, position, salary, subordinates=None):
        super().__init__(name, emp_id, position, salary)
        self.subordinates = subordinates if subordinates else []
    
    def __str__(self):
        return super().__str__() + f", Subordinates: {', '.join(map(str, self.subordinates)) if self.subordinates else 'None'}"
    
    def __repr__(self):
        return f"Manager('{self.name}', {self.emp_id}, '{self.position}', {self.salary}, {self.subordinates})"
    
    def add_subordinate(self, emp_id):
        self.subordinates.append(emp_id)
    
    def remove_subordinate(self, emp_id):
        if emp_id in self.subordinates:
            self.subordinates.remove(emp_id)

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}
    
    def __str__(self):
        return f"Department: {self.name}, Total Employees: {self.count_employees()}"
    
    def __repr__(self):
        return f"Department('{self.name}')"
    
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
    
    def calculate_total_salary(self):
        return sum(emp.salary for emp in self.employees.values())
    
    def display_department_info(self):
        print(self)
        for emp in self.employees.values():
            emp.display_info()
        print(f"Total Salary: ${self.calculate_total_salary()}\n")

# Example usage
emp1 = Employee("John Doe", 101, "Software Engineer", 80000)
emp2 = Employee("Jane Smith", 102, "Project Manager", 90000)
emp3 = Employee("Alice Johnson", 103, "Data Analyst", 75000)
emp1.update_name("Johnathan Doe")
emp1.update_position("Senior Software Engineer")
emp1.update_salary(90000)

mgr1 = Manager("Robert Brown", 200, "Engineering Manager", 120000, [101, 103])
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

