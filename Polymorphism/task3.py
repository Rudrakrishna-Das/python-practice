# Create a parent class Employee with method get_role().

# Create subclasses:

# Manager

# Developer

# Designer

# Each should override get_role() with different return messages.

# Task:

# Write a function print_role(emp) that accepts any employee object and prints the role.

class Employee:
    def get_role(self):
        return "Welcome Employee!"

class Manager(Employee):
    def get_role(self):
        return "Welcome Manager"

class Developer(Employee):
    def get_role(self):
        return super().get_role()
    
class Designer(Employee):
    def get_role(self):
        return "Welcome Designer"
    
def print_role(emp):
    print(emp.get_role())
    
print_role(Developer())