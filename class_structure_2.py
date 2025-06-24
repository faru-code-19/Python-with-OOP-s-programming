class Student:
    "this ia a student class with multiple objects"
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks

    def talk(self):
        print("Hello i am",self.name)
        print("my roll number is",self.roll)
        print("my marks are",self.marks)

s1=Student("farhan",53,81)
s2=Student("luffy",23,88)
s1.talk()
s2.talk()