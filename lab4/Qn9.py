from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Concrete class
class Car(Vehicle):

    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")


# Another concrete class
class Bike(Vehicle):

    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")


# Object creation
car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()
