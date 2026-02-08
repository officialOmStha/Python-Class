# Encapsulation in Python - Complete Example

class Person:
    def __init__(self, name, age, salary):
        # Public variable
        self.name = name

        # Protected variable
        self._age = age

        # Private variable
        self.__salary = salary

    # Public method
    def display_public(self):
        print("Name (Public):", self.name)

    # Protected method
    def _display_protected(self):
        print("Age (Protected):", self._age)

    # Private method
    def __display_private(self):
        print("Salary (Private):", self.__salary)

    # Public method to access private data (Getter)
    def get_salary(self):
        return self.__salary

    # Public method to modify private data (Setter)
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

    # Method to call all members inside the class
    def show_all(self):
        self.display_public()
        self._display_protected()
        self.__display_private()


# Object creation
p = Person("Alex", 22, 50000)

print("---- Accessing Public Member ----")
print(p.name)           # Public access
p.display_public()

print("\n---- Accessing Protected Member ----")
print(p._age)            # Possible but not recommended
p._display_protected()

print("\n---- Accessing Private Member ----")
# print(p.__salary)      # ❌ Error
print("Salary using getter:", p.get_salary())

print("\n---- Modifying Private Member ----")
p.set_salary(60000)
print("Updated Salary:", p.get_salary())

print("\n---- Accessing All Inside Class ----")
p.show_all()
