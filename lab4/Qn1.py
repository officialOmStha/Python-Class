# Class and Object

class Cat:
    species = 'chichi'
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def __str__(self):
        return (f"Name: {self.name} Age: {self.age} Species: {self.species}")
    
    def info(self):
        print("Cat's name is: ", self.name)

    def sound(self):
        print(self.name, "meow")


c=Cat("Tom", 3)
print(c.name)        
print(c.age)
print(c.species)
print(c)



        