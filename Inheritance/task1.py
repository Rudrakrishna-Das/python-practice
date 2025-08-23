# Create a base class Shape with:

# Attribute: color

# Method: describe() that prints the color.

# Create a derived class Circle that:

# Adds an attribute: radius

# Adds a method: area() that returns the area of the circle.

# Instantiate a Circle object and call both describe() and area()

import math

class Shape:
    def __init__(self, color):
        self.col = color
    
    def describe(self):
        return f"The color is {self.col}"
        
class Circle(Shape):
    def __init__(self,color, radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return f"The area is {round(math.pi*self.radius*self.radius, 2)}"
    

s1 = Circle('green', 3.2)

print(s1.area())
print(s1.describe())