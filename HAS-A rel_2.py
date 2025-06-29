class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def car_info(self):
        print(f"Car {self.name} created with model {self.model} and color {self.color}")

class Employee:
    def __init__(self,ename,eno,car):# Employee has-a Car object
        self.ename = ename
        self.eno = eno
        self.car = car

    def emp_info(self):
        print(f"Employee {self.ename} with ID {self.eno} has a car:")
        self.car.car_info() # calling car_info method of Car class
    
c=Car("Toyota", "Camry", "Blue") # create a Car object
e=Employee("John Doe", 12345, c) # create an Employee object with a Car object
e.emp_info() # call emp_info method to display employee and car information