class Car:
    def car_info(self):
        print("this is the car")

"""class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename 
        self.eno=eno
        self.car=car
    def eminfo(self):
        print(self.ename)
        print(self.eno)
        self.car.car_info()
car=Car()
e=Employee("abc",12,car)
e.eminfo()"""

class Employee:
    def __init__(self,name,eno):
        self.name=name
        self.eno=eno
        self.car=Car()

    def eminfo(self):
        print(self.name)
        print(self.eno)
        self.car.car_info()

e=Employee("abd",12)
e.eminfo()