# Multi-level inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employ(Person):
    def __init__(self, name, role):
        Person.__init__(self,name)
        self.role = role

class Salary(Employ):
    def __init__(self, name, role, salary):
        Employ.__init__(self,name, role)
        self.salary = salary

    def info(self):
        print(f"{self.name} is an {self.role} with salary Rs {self.salary}")

obj1 = Salary("Ram", "Intern", 15000)
obj1.info()






