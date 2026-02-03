# Polymorphism

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


# Using polymorphism
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()  # same method name, different behavior
