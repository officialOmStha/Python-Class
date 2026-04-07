class Animal():
    def __init__(self):
        self.living = True

    def is_animal(self):
        print("It is an animal")
    
class Cow(Animal):
    def __init__(self):
        self.legs = 4
        self.eat = "grass"

    def __str__(self):
        return f"It's cow and it has {self.legs} legs, and I eat {self.eat}"
    
coww = Cow()
print(coww)
coww.is_animal()