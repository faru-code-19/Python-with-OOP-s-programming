class Person:
    def __init__(self,name,height,weeight,age):
        self.name=name
        self.height=height
        self.weight=weeight
        self.age=age

    def display(self):
        print(self.name)
        print(self.height)
        print(self.weight)
        print(self.age)

class Student(Person):
    def __init__(self,name,height,weeight,age,roll):
        super().__init__(name, height, weeight, age)
        self.roll=roll

    def dis(self):
        super().display()
        print("roll:",self.roll)

c=Student('ac',2,4,12,2412)
c.dis()