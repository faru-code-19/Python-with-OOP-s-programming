class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"Name id:{self.name}")
        print(f"Marks id:{self.marks}")

    def grade(self):
        if self.marks>=60:
            print("super class")
        elif self.marks>=50:
            print("sub class")
        else:
            print("fail class")

n=int(input("Enter the number of students: "))
for i in range(n):
    name=input("Enter the name of student: ")
    marks=int(input("Enter the marks of student: "))
    s=Student(name,marks) # Create an object of Student class
    s.display() # call the display instance method
    s.grade() # call the grade instance method
    print()  # For better readability between students