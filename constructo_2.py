class Student:
    def __init__(self,name,roll):
        self.name=name #instance variable declaration
        self.roll=roll #instance variable declaration

s1=Student("farhan",53) #creating objects of class Student
s2=Student("luffy",23) #creating objects of class Student
print(s1.name,s1.roll) #accessing instance variables of object s1
print(s2.name,s2.roll)  #accessing instance variables of object s2  