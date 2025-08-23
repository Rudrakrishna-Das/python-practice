# Create a base class Vehicle with:

# Attribute: brand

# Method: start()

# Create a class Electric with:

# Attribute: battery_life

# Method: charge()

# Create a class ElectricCar that inherits from both Vehicle and Electric:

# Add attribute: model

# Add method: info() to display brand, model, and battery life.

# Create an ElectricCar object and demonstrate all inherited behaviors.

from abc import ABC, abstractmethod

# parent class = skeleton
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
        
    @abstractmethod
    def start(self):
        pass
    
class Electric(ABC):
    def __init__(self, battery_life):
        self.battery_life = battery_life
        
    def charge(self):
        pass

class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, model, battery_life):
        Vehicle.__init__(self, brand)
        # Electric.__init__(self, battery_life)
        self.battery_life = battery_life
        self.model = model
        
    def start(self):
        return f"Trying out {self.brand}"
        
    def info(self):
        return f"Brancd: {self.brand}, Model: {self.model} and the battery life is {self.battery_life}"
    

e1 = ElectricCar('Tesla', 'Model Y', '436 miles')

print(e1.start())
print(e1.info())
