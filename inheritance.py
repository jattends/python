"""#inheritance
class Person:
    course="Python"
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    course = "java"
    def __init__(self,salary,n):
        self.salary = salary
        super().__init__(n)#super key word uses is upper class calling the super key word is not using time the chid class only display//(n) is using name stored
        print(super().course)

emp=Employee(100,"arun")
print(emp.salary,emp.name)"""

class father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self    ):
        print(self.name,self.age)
class mother(father):
    def __init__(self,name,age,job):
        super().__init__(name,age)
        self.job = job
    def dispaly(self):
        print(self.name,self.age,self.job)
class child(mother)                                        