"""# Base Class
class Calculate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def division(self):
        print(self.a / self.b)


# Derived Class
class Add(Calculate):
    def __init__(self, a, b):
        Calculate.__init__(self, a, b)

    def add(self):
        print("Addition:", self.a + self.b)
        Add.division(self)


# Derived Class
class Subtract(Calculate):
    def __init__(self, a, b):
        Calculate.__init__(self, a, b)

    def subtract(self):
        print("Subtraction:", self.a - self.b)
        Subtract.division(self)


obj1 = Add(34, 98)
obj2 = Subtract(45, 67)
obj1.add()
obj2.subtract()"""


class calculate:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def division(self):
        print(self.a / self.b)

class add(calculate):
    def __init__(self,a,b):
        calculate.__init__(self,a,b)
    def add(self):
        print("Addition :",self.a + self.b)
        add.division(self)
class subtract(calculate):
    def __init__(self,a,b):
        calculate.__init__(self,a,b)
    def subtract(self):
        print("substraction :",self.a - self.b)
        subtract.division(self)
obj1 = add(34,98)
obj2 = subtract(5,9)
obj1.add()
obj2.subtract()
