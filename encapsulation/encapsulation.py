# Private attributes: name, salary

# Methods:

# set_name(name)

# get_name()

# set_salary(amount)

# get_salary()
class Encapsulation:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        return f"Name is {self.__name}"
    
    def set_salary(self,amount):
        self.__salary = amount

    def get_salary(self):
        return f"Salary is {self.__salary}"
    

ram = Encapsulation('Ram',20000)

print(ram.get_name())
print(ram.get_salary())

ram.set_name('Ram Das')
ram.set_salary(3500)

print(ram.get_name())
print(ram.get_salary())

