class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.sal}")
    
class Manager:
    def update_salary(e):
        e.sal += 1000
        e.display()


e= Employee("John", 5000)
Manager.update_salary(e)