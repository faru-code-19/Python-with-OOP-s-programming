class Test():
    a=10

    def __init__(self):
        Test.a = 20  # updating static variable using class name
    
    def instance_method(self):
        Test.a = 30
    
    @classmethod
    def class_method(cls):
        cls.a = 40
        Test.a = 50 
    
    @staticmethod   
    def static_method():
        Test.a = 60

print(Test.a)  # accessing static variable outside the class using class name
print()
t = Test()  # creating an instance of Test
print(Test.a)  # accessing static variable outside the class using class name after update
print()
t.instance_method()  # calling instance method to update static variable
print(Test.a)  # accessing static variable outside the class using class name after update
print()
Test.class_method()  # calling class method to update static variable
print(Test.a)  # accessing static variable outside the class using class name after update
print()
Test.static_method()  # calling static method to update static variable
print(Test.a)  # accessing static variable outside the class using class name after update
Test.a=80 # updating static variable using class name outside the class
print(Test.a)  # accessing static variable outside the class using class name after update