class Test():
    a=10  # static variable

    def __init__(self):
        self.b=20 # instance variable
        Test.c=30  # declaring static variable c from within the constructor

    #instance method
    def m(self):
        Test.d=40  # declaring static variable d from within a instance method

    @classmethod
    def n(cls):
        cls.e=50
        Test.f=60  # declaring static variables e and f from within a class method
    
    @staticmethod
    def o():
        Test.g=70 # declaring static variable g from within a static method


print(Test.a) # accessing static variable a
t=Test()
t.m()  # call instance method to declare static variable d
Test.n() #call class method to declare static variables e and f
Test.o()  # call static method to declare static variable g
Test.h=80  # declaring static variable h from outside the class
print(Test.__dict__)  # print the class dictionary to see static variables

