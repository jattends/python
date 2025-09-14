from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

    def stop_engine(self):
        return "Car engine stopped."

class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started."

    def stop_engine(self):
        return "Bike engine stopped."

# Usage:
car = Car()
print(car.start_engine(), car.stop_engine())  # Car engine started. Car engine stopped.

bike = Bike()
print(bike.start_engine(), bike.stop_engine())  # Bike engine started. Bike engine stopped.
