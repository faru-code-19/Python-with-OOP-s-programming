class Test:
    def __init__(self):
        self.a=10
        self.b=20   
        self.c=30
        self.d=40

    def m(self):
        del self.b  # deleting instance variable b from within the class

t=Test()
t.m()  # call method to delete instance variable b
print(t.__dict__)

t2=Test() # create a new instance of Test
del t2.d,t2.a  # delete instance variables d and a from the new instance
print(t2.__dict__)  # print the dictionary of instance variables for t2