# Task: Create a class called Dog with:

# Attributes: name, breed, age

# Method: bark() that prints: "{name} says woof!"

# Practice:

# Create 2 instances of the Dog class

# Call bark() on both

class Dog():
    def __init__(self, name, breed, age):
        self.breed = breed
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says woof!")
        
dog1 = Dog('Coco', 'Boxer', 3)
dog2 = Dog('B', 'GS', 4)
dog1.bark()
dog2.bark()

