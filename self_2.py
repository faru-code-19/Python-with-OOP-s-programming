class Test:
    def __init__(self):
        print("constructor")
    
    def m1(self,x): #instance method
        print("x val is:",x)

t=Test()
t.m1(10)