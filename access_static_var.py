class Test():

    a=10  # static variable

    def __init__(self):
        print(self.a)  # accessing static variable inside class using self
        print(Test.a)  # accessing static variable inside class using class name

    #insatance method
    def info(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m(cls):
        print(cls.a)# accessing static variable inside class method using cls
        print(Test.a) # accessing static variable inside class method using class name  

    @staticmethod
    def b():
        print(Test.a) # accessing static variable inside static method using class name
t = Test()  # creating an instance of Test
t.info()  # calling the instance method to access static variables
Test.m()  # calling the class method to access static variables
print(Test.a)  # accessing static variable outside the class using class name
Test.b()  # calling the static method to access static variables
print(t.a)  # accessing static variable outside the class using object reference