# Single inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name is: ", self.name)

class Cat(Animal):
    def sound(self):
        print(self.name, "makes sound: 'meow'")


c = Cat("Tom")
c.info()
c.sound()