# Hybrid Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Employee(Person):
    def __init__(self, name, emp_id):
        Person.__init__(self, name)
        self.emp_id = emp_id

    def show_employee(self):
        print("Employee ID:", self.emp_id)


class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

    def show_student(self):
        print("Roll No:", self.roll_no)


class Intern(Employee, Student):
    def __init__(self, name, emp_id, roll_no, duration):
        Employee.__init__(self, name, emp_id)
        Student.__init__(self, name, roll_no)
        self.duration = duration

    def show_intern(self):
        self.show_name()
        self.show_employee()
        self.show_student()
        print("Internship Duration:", self.duration, "months")


intern = Intern("Amit", 101, 55, 6)
intern.show_intern()


