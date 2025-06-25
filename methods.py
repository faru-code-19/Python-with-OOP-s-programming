class Student:
    sch_name = "KV"  # static variable
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    def info(self): 
        print(f"Name: {self.name}, Age: {self.age}, School: {self.sch_name}") #instance method

    @classmethod
    def sc_info(cls):
        print(f"School Name: {cls.sch_name}")   # class method

    @staticmethod   
    def sum(a,b):
        sum=a+b
        print(f"sum is: {sum}")  # static method