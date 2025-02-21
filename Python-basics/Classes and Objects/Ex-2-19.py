#In the Employee class, add property decorators to manage how an employee’s position or salary is set or retrieved.
class Employee:
    def __init__(self, name, emp_id, position, salary):
        self._name = name
        self._emp_id = emp_id
        self._position = position
        self._salary = salary
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
    
    @property
    def emp_id(self):
        return self._emp_id
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, new_position):
        if isinstance(new_position, str) and new_position.strip():
            self._position = new_position
        else:
            raise ValueError("Position must be a non-empty string.")
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, (int, float)) and new_salary > 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary must be a positive number.")
    
    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"
    
    def __repr__(self):
        return f"Employee('{self.name}', {self.emp_id}, '{self.position}', {self.salary})"

class Manager(Employee):
    def __init__(self, name, emp_id, position, salary, subordinates=None):
        super().__init__(name, emp_id, position, salary)
        self._subordinates = subordinates if subordinates else []
    
    @property
    def subordinates(self):
        return self._subordinates
    
    def add_subordinate(self, employee):
        if employee not in self._subordinates:
            self._subordinates.append(employee)
    
    def remove_subordinate(self, employee):
        if employee in self._subordinates:
            self._subordinates.remove(employee)
    
    def __str__(self):
        return super().__str__() + f", Subordinates: {', '.join(map(str, self.subordinates)) if self.subordinates else 'None'}"

class Department:
    def __init__(self, name, manager):
        self._name = name
        self._manager = manager
        self._employees = {}
    
    @property
    def name(self):
        return self._name
    
    @property
    def manager(self):
        return self._manager
    
    @property
    def employees(self):
        return self._employees
    
    def add_employee(self, employee):
        self._employees[employee.emp_id] = employee
    
    def remove_employee(self, emp_id):
        self._employees.pop(emp_id, None)
    
    def calculate_total_salary(self):
        return sum(emp.salary for emp in self._employees.values())
    
    def __str__(self):
        return f"Department: {self.name}, Manager: {self.manager.name if self.manager else 'None'}, Total Employees: {len(self._employees)}"

class Project:
    def __init__(self, name, department, employees=None):
        self._name = name
        self._department = department
        self._employees = employees if employees else []
    
    @property
    def name(self):
        return self._name
    
    @property
    def department(self):
        return self._department
    
    @property
    def employees(self):
        return self._employees
    
    def add_employee(self, employee):
        if employee not in self._employees:
            self._employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self._employees:
            self._employees.remove(employee)
    
    def __str__(self):
        return f"Project: {self.name}, Department: {self.department.name}, Employees: {len(self.employees)}"

# Example usage
emp1 = Employee("John Doe", 101, "Software Engineer", 80000)
emp2 = Employee("Jane Smith", 102, "Project Manager", 90000)
emp3 = Employee("Alice Johnson", 103, "Data Analyst", 75000)
emp1.name = "Johnathan Doe"
emp1.position = "Senior Software Engineer"
emp1.salary = 90000

mgr1 = Manager("Robert Brown", 200, "Engineering Manager", 120000, [emp1, emp3])
mgr1.add_subordinate(emp2)
mgr1.remove_subordinate(emp3)

department = Department("Engineering", mgr1)
department.add_employee(emp1)
department.add_employee(emp2)
department.add_employee(emp3)

project = Project("AI Development", department, [emp1, emp3])

print(department)
print(project)
print(f"Total number of employees: {len(department.employees)}")
