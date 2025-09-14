"""class laptop:
    def specs(self,m,c):
        self.model=m
        self.colour=c
obj1=laptop()
obj2=laptop()
obj2.specs("dell","black")
obj1.specs("HD","white")
print(obj1.model,obj1.colour)
print(obj2.model,obj2.colour)"""
class car:
    def __init__(self,brand,model,colour):
        self.brand=brand
        self.model=model
        self.colour=colour
obj1=car("toyota","corolla","black")
print(obj1.brand,obj1.model,obj1.colour)
