class Calculator:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod       
    def sub(a,b):
        print(a-b)

    @staticmethod
    def mul(a,b):
        print(a*b)
    @staticmethod
    def div(a,b):
        if b != 0:
            print(a/b)
        else:
            print("Division by zero is not allowed")

Calculator.add(10, 5)  # Calling the static method to add two numbers
Calculator.sub(10, 5)  # Calling the static method to subtract two numbers          
Calculator.mul(10, 5)  # Calling the static method to multiply two numbers
Calculator.div(10, 5)  # Calling the static method to divide two numbers
