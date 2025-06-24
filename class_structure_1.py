class Student:
    "this is a student class which conatins 2 methods and 3 variables"
    def __init__(self):
        self.name="farhan"
        self.roll=53
        self.marks=81   
    
    def talk(self):
        print("Hello i am",self.name)
        print("my roll number is",self.roll)
        print("my marks are",self.marks)


s=Student() #creating an object of class Student
print(s.name)
print(s.roll)
print(s.marks)

s.talk() #calling the method talk of class Student
