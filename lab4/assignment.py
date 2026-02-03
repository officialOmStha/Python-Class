class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")  # overrides parent method

a = Animal()
d = Dog()

a.speak()  # Animal makes a sound
d.speak()  # Dog barks


class Calculator:
    def add(self, a, b=0, c=0):  # default parameters
        return a + b + c

calc = Calculator()
print(calc.add(5, 3))     # 8
print(calc.add(5, 3, 2))  # 10
print(calc.add(5))        # 5
