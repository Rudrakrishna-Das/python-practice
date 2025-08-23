# Create a base class Employee with:

# Attributes: name, salary

# Method: get_details() that returns name and salary.

# Create a derived class Manager that:

# Adds an attribute: department

# Overrides get_details() to include the department info.

# Create both Employee and Manager objects and print their details.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def get_details(self):
        return f"The salary of {self.name} is {self.salary}"
    

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"The salary of {self.name} from {self.department} department is {self.salary}"
    
    
p1 = Employee('John', 120000)
p2 = Manager('Mark', 200000, 'Product')

print(p1.get_details())
print(p2.get_details())
        