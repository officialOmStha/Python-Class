# Hirarchical Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        self.display_info()
        print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")


class Intern(Person):
    def __init__(self, name, age, intern_id, duration):
        super().__init__(name, age)
        self.intern_id = intern_id
        self.duration = duration

    def display_intern(self):
        self.display_info()
        print(f"Intern ID: {self.intern_id}, Duration: {self.duration} months")


emp = Employee("Ram", 30, 101, 50000)
intern = Intern("Sita", 21, 201, 6)

emp.display_employee()
print()
intern.display_intern()
