# Create 3 classes: Dog, Cat, Cow. Each has a make_sound() method.

# Task: Write a function play_sound(animal) that accepts any of the three and calls make_sound().

class Dog:
    def make_sound():
        return "Bark!"

class Cat:
    def make_sound():
        return "Meow!"

class Cow:
    def make_sound():
        return "Moo!"

def play_sound(animal):
    return animal.make_sound()

print(play_sound(Cow))