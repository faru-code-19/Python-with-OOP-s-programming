class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"name:{self.name} and age:{self.age}"
    
c1=Student('abc',20)
c2=Student('def',31)
print(c1)#<__main__.Student object at 0x000001FDF67C2290>
print(c2)#<__main__.Student object at 0x000001FDF67C23D0>