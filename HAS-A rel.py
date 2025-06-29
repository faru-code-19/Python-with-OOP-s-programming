class Engine:

    def __init__(self):
        self.power = 100

    def m1(self): #instance method
        print("Engine m1() called")

class Car:
    def __init__(self):
        print("Car __init__() called")
        self.engine=Engine() # Car has-a Engine object
        print("Car object created with an Engine")

    def m2(self):
        print("Car m2() called")
        self.engine.m1()
        print(self.engine.power) # accessing Engine's power attribute

c=Car() # create a Car object
c.m2() # call Car's m2() method which calls Engine's m1()