class Test():
    def __init__(self):
        self.a = 10
        self.b = 20

t=Test()
t.a=100 # updating instance variable a
t.b=200 # updating instance variable b
print(t.__dict__)  # print the dictionary of instance variables to see the updates

t2=Test()  # create a new instance of Test
print(t2.__dict__)  # print the dictionary of instance variables for t2

