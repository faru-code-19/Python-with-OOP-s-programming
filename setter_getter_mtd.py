class Student:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setMarks(self, marks):
        self.marks = marks  
    
    def getMarks(self):
        return self.marks   
    
n=int(input("Enter the number of students: "))
Stud=[] # List to store Student objects 
for i in range(n):
    name=input("Enter the name of student: ")
    marks=int(input("Enter the marks of student: "))
    s=Student() # Create an object of Student class
    s.setName(name)  # Set the name using setter method
    s.setMarks(marks)  # Set the marks using setter method
    Stud.append(s)  # Append the object to the list
    print()
for j in  Stud:
    print("student name is:",j.getName())  # Get the name using getter method
    print("student marks is:",j.getMarks())  # Get the marks using getter method
    print()
