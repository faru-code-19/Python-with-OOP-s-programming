class Math:

    def m1(self):
        def calc(a,b):
            print(f"Sum: {a + b}")
            print(f"Difference: {a - b}")
            print(f"Product: {a * b}")
            
        calc(10, 5)
        calc(20, 10)
        calc(30, 15)
t=Math() 
t.m1()