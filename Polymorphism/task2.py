# Create a base class Shape with method area().

# Then create subclasses:

# Circle (with radius)

# Rectangle (with width and height)

# Triangle (with base and height)

# Each subclass should override the area() method to compute its own.

import math

class Shape:
    def area():
        return "None"
    
class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad
        
    def area(self):
        return f"The area of the Circle is {math.pi*self.rad*self.rad}"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def area(self):
        return f"The area of the Rectangle is {self.w*self.h}"

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def area(self):
        return f"The area of the Triangle is {0.5*self.b*self.h}"

list1 = [Circle(2), Rectangle(2,3), Triangle(2,3)]

for i in list1:
    print(i.area())