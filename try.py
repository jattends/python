"""class Car:
    vehicle = "Car"

    def __init__(self, model, color):
        self.model = model
        self.color = color
    def showDetails(self):
        print(self.model,self.color)
car1=Car("toyota","black")
car1.showDetails()"""

class Person:
    course="Python"
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    course = "java"
    def __init__(self,salary,n):
        self.salary = salary
        super().__init__(n)
        print(super().course)

emp=Employee(100,"arun")
print(emp.salary,emp.name)

