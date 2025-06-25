class Test:
    def __init__(self):
        self.a=10
        self.b=20
    
    def info(self):
        print(self.a) #accessing instance variable inside class
        print(self.b)

t=Test()
t.info()
print(t.a)
print(t.b) #accessing instance variable outside class